"""Audit, provenance, manifest, and checksum artifacts."""

from __future__ import annotations

import json
from collections.abc import Iterable
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

from nica_geofetch.models import (
    METADATA_ORIGIN_VALUES,
    SOURCE_RELATIONSHIP_VALUES,
    ConversionResult,
    ValidationReport,
)
from nica_geofetch.validation import sha256_file


def _write_json(path: Path, value: Any) -> Path:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def _software_version() -> str:
    try:
        return version("nica-geofetch")
    except PackageNotFoundError:
        return "0+unknown"


def _transformation_steps(
    report: ValidationReport,
    conversion: ConversionResult,
) -> list[str]:
    steps = [
        "preserve_original_source_bytes",
        "validate_acquisition_as_xml_vector_kml",
        "extract_provider_attributes",
        "inspect_polygon_topology",
    ]
    if not report.analytical_ready:
        steps.append("skip_analytical_formats_pending_explicit_repair_or_source_correction")
        return steps
    steps.append("normalize_polygon_features_to_epsg_4326")
    if report.repair_applied:
        steps.append("repair_analytical_working_copy_with_explicit_user_opt_in")
    if any(path.resolve() != report.source_path.resolve() for path in conversion.outputs.values()):
        steps.extend(["convert_requested_formats", "reopen_and_verify_generated_outputs"])
    return steps


def _generated_artifacts(
    output_directory: Path,
    report: ValidationReport,
    conversion: ConversionResult,
) -> list[dict[str, Any]]:
    artifacts: list[dict[str, Any]] = []
    for output_format, path in sorted(conversion.outputs.items()):
        preserved_source = path.resolve() == report.source_path.resolve()
        steps = (
            ["preserve_original_source_bytes"]
            if preserved_source
            else [
                "validate_source_kml",
                "normalize_polygon_features_to_epsg_4326",
                f"convert_to_{output_format}",
                "reopen_and_verify_output",
            ]
        )
        if report.repair_applied and not preserved_source:
            steps.insert(2, "repair_analytical_working_copy_with_explicit_user_opt_in")
        artifacts.append(
            {
                "format": output_format,
                "path": path.relative_to(output_directory).as_posix(),
                "artifact_role": "preserved_source" if preserved_source else "derived_output",
                "sha256": sha256_file(path),
                "transformation_steps": steps,
            }
        )
    return artifacts


def write_audit_reports(
    output_directory: Path,
    reports: list[ValidationReport],
    conversions: list[ConversionResult],
) -> tuple[Path, Path]:
    """Write equivalent machine-readable and human-readable validation reports."""

    audit_json = output_directory / "audit_report.json"
    audit_markdown = output_directory / "audit_report.md"
    _write_json(
        audit_json,
        {
            "project": "Nica-GeoFetch",
            "provider": "ineter-pfafstetter",
            "dataset_id": "ineter-pfafstetter-2025",
            "reports": [report.to_dict() for report in reports],
            "conversions": [conversion.to_dict() for conversion in conversions],
        },
    )
    lines = [
        "# Nica-GeoFetch audit report",
        "",
        "Institutional source data is third-party material and is not covered by "
        "the Apache-2.0 software license.",
        "",
        "| Level | Retrieval mode | Acquisition | Geometry | Analytical | Placemarks | Invalid geometries | Errors | Warnings | SHA-256 |",
        "|---:|---|:---:|:---:|:---:|---:|---:|---:|---:|---|",
    ]
    for report in reports:
        errors = sum(issue.severity == "error" for issue in report.issues)
        warnings = sum(issue.severity == "warning" for issue in report.issues)
        lines.append(
            f"| {report.level} | {report.retrieval_mode.value} | "
            f"{'valid' if report.acquisition_valid else 'invalid'} | "
            f"{'valid' if report.geometry_valid else 'warnings'} | "
            f"{'ready' if report.analytical_ready else 'skipped'} | "
            f"{report.placemark_count} | {report.invalid_geometry_count} | "
            f"{errors} | {warnings} | `{report.sha256}` |"
        )
    lines.extend(["", "## Findings", ""])
    for report in reports:
        lines.append(f"### Level {report.level}")
        if not report.issues:
            lines.append("")
            lines.append("No validation findings.")
        for issue in report.issues:
            suffix = f" ({issue.feature_name})" if issue.feature_name else ""
            lines.append(f"- **{issue.severity} / {issue.code}:** {issue.message}{suffix}")
        lines.append("")
    audit_markdown.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return audit_json, audit_markdown


def write_source_manifest(
    output_directory: Path,
    reports: list[ValidationReport],
    conversions: list[ConversionResult],
) -> Path:
    """Record reproducible source identities without granting data rights."""

    conversions_by_level = {item.level: item for item in conversions}
    sources = [
        {
            "source_institution": report.source_institution,
            "provider": report.provider_id,
            "provider_id": report.provider_id,
            "dataset_id": report.dataset_id,
            "source_relationship": report.source_relationship,
            "level": report.level,
            "selected_level": report.level,
            "source_url": report.source_url,
            "source_layer": report.source_layer,
            "retrieval_mode": report.retrieval_mode.value,
            "retrieved_at_utc": report.retrieved_at_utc,
            "original_source_format": report.original_source_format,
            "response_content_type": report.response_content_type,
            "byte_size": report.byte_size,
            "source_byte_size": report.byte_size,
            "local_raw_file": report.source_path.relative_to(output_directory).as_posix(),
            "sha256": report.sha256,
            "original_sha256": report.sha256,
            "repaired_working_copy_sha256": report.repaired_working_copy_sha256,
            "validation_status": report.validation_status,
            "acquisition_valid": report.acquisition_valid,
            "acquisition_status": "valid" if report.acquisition_valid else "invalid",
            "geometry_valid": report.geometry_valid,
            "geometry_validation_status": (
                "valid"
                if report.geometry_valid
                else "repaired"
                if report.repair_applied and report.post_repair_geometry_valid
                else "warnings"
            ),
            "post_repair_geometry_valid": report.post_repair_geometry_valid,
            "analytical_ready": report.analytical_ready,
            "invalid_geometry_count": report.invalid_geometry_count,
            "invalid_geometry_feature_ids": report.invalid_geometry_feature_ids,
            "repair_requested": report.repair_requested,
            "repair_applied": report.repair_applied,
            "repair_method": report.repair_method,
            "placemark_count": report.placemark_count,
            "feature_count": len(report.features),
            "geometry_count": report.polygon_feature_count,
            "geometry_types": sorted({feature.geometry.geom_type for feature in report.features}),
            "crs": {
                "source": report.crs,
                "normalized": "EPSG:4326",
            },
            "warnings": [
                issue.to_dict()
                for issue in report.issues
                if issue.severity == "warning" or issue.code == "invalid_geometry"
            ],
            "generated_analytical_formats": sorted(
                output_format
                for output_format in conversions_by_level[report.level].outputs
                if output_format != "kml"
            ),
            "software_version": _software_version(),
            "provider_configuration_version": report.provider_configuration_version,
            "transformation_steps": _transformation_steps(
                report,
                conversions_by_level[report.level],
            ),
            "generated_artifacts": _generated_artifacts(
                output_directory,
                report,
                conversions_by_level[report.level],
            ),
            "metadata_basis": report.metadata_basis,
            "dataset_year": 2025,
            "validated_at_utc": report.checked_utc,
            "attribution": (
                "Source: INETER, national hydrographic units adjusted to Pfafstetter, 2025."
            ),
            "license_status": "No explicit open-data license identified",
            "redistribution_status": (
                "Institutional clarification required before public redistribution"
            ),
        }
        for report in reports
    ]
    return _write_json(
        output_directory / "source_manifest.json",
        {
            "schema_version": 3,
            "software_license": "Apache-2.0",
            "software_license_scope": "Nica-GeoFetch software and synthetic fixtures only",
            "metadata_origin_vocabulary": sorted(METADATA_ORIGIN_VALUES),
            "source_relationship_vocabulary": sorted(SOURCE_RELATIONSHIP_VALUES),
            "sources": sources,
        },
    )


def write_provenance_summary(
    output_directory: Path,
    reports: list[ValidationReport],
    conversions: list[ConversionResult],
) -> Path:
    """Write a concise transformation and rights summary."""

    lines = [
        "# Provenance summary",
        "",
        "Generated by Nica-GeoFetch 0.1.0 using provider `ineter-pfafstetter`.",
        "Source files were validated as XML vector KML, normalized to EPSG:4326, "
        "and converted outputs were reopened before inclusion.",
        "",
        "The source institution is INETER. Converted files are not represented as "
        "official INETER products. No explicit open-data license was identified; "
        "obtain institutional clarification before redistributing complete copies.",
        "The configured source relationship is `authoritative`; technical metadata "
        "origins and generated-artifact checksums are recorded in source_manifest.json.",
        "",
        "## Levels and outputs",
        "",
    ]
    by_level = {item.level: item for item in conversions}
    for report in reports:
        outputs = ", ".join(sorted(by_level[report.level].outputs))
        analytical_note = (
            "analytical conversion ready"
            if report.analytical_ready
            else "analytical formats skipped; original KML retained"
        )
        lines.append(
            f"- Level {report.level} ({report.retrieval_mode.value}): "
            f"{report.polygon_feature_count} polygon features; "
            f"source SHA-256 `{report.sha256}`; {analytical_note}; outputs: {outputs}."
        )
    path = output_directory / "provenance_summary.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_checksums(
    output_directory: Path,
    paths: Iterable[Path] | None = None,
) -> Path:
    """Write SHA-256 values keyed by paths relative to the workflow directory."""

    checksum_path = output_directory / "checksums_sha256.json"
    if paths is None:
        candidates = [
            path
            for path in output_directory.rglob("*")
            if path.is_file()
            and path != checksum_path
            and path.name != "nica_geofetch_results.zip"
            and ".part" not in path.name
        ]
    else:
        candidates = list(paths)
    values = {
        path.relative_to(output_directory).as_posix(): sha256_file(path)
        for path in sorted(candidates, key=lambda item: item.as_posix())
    }
    return _write_json(checksum_path, {"algorithm": "SHA-256", "files": values})
