"""High-level workflows used unchanged by CLI and Colab."""

from __future__ import annotations

import shutil
from collections.abc import Iterable
from pathlib import Path

from nica_geofetch.conversion import convert_report
from nica_geofetch.exceptions import ValidationError
from nica_geofetch.manifests import (
    write_audit_reports,
    write_checksums,
    write_provenance_summary,
    write_source_manifest,
)
from nica_geofetch.models import OutputFormat, ValidationReport, WorkflowResult
from nica_geofetch.packaging import create_final_archive
from nica_geofetch.providers.ineter_pfafstetter import IneterPfafstetterProvider


def normalize_formats(formats: Iterable[str | OutputFormat]) -> list[OutputFormat]:
    """Normalize format strings and preserve the user's order without duplicates."""

    result: list[OutputFormat] = []
    for value in formats:
        item = value if isinstance(value, OutputFormat) else OutputFormat(value.lower())
        if item not in result:
            result.append(item)
    return result


def _prepare_output(output_directory: Path) -> Path:
    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "raw").mkdir(exist_ok=True)
    (output_directory / "processed").mkdir(exist_ok=True)
    (output_directory / "field_mappings").mkdir(exist_ok=True)
    return output_directory


def _finalize(
    output_directory: Path,
    reports: list[ValidationReport],
    formats: list[OutputFormat],
) -> WorkflowResult:
    conversions = [
        convert_report(report, formats, output_directory) for report in reports if report.valid
    ]
    audit_json, audit_markdown = write_audit_reports(output_directory, reports, conversions)
    write_source_manifest(output_directory, reports)
    write_provenance_summary(output_directory, reports, conversions)
    write_checksums(output_directory)
    archive = create_final_archive(output_directory)
    return WorkflowResult(
        output_directory=output_directory,
        reports=reports,
        conversions=conversions,
        archive_path=archive,
        audit_json_path=audit_json,
        audit_markdown_path=audit_markdown,
    )


def import_local_workflow(
    *,
    input_path: Path,
    level: int,
    formats: Iterable[str | OutputFormat],
    output_directory: Path,
    repair: bool = False,
    provider: IneterPfafstetterProvider | None = None,
) -> WorkflowResult:
    """Copy, validate, convert, audit, and package one manually supplied KML."""

    active_provider = provider or IneterPfafstetterProvider()
    output = _prepare_output(output_directory)
    report = active_provider.import_local(input_path, level, repair=repair)
    raw_path = output / "raw" / f"ineter_pfafstetter_2025_level{level}.kml"
    if input_path.resolve() != raw_path.resolve():
        shutil.copy2(input_path, raw_path)
    report.source_path = raw_path
    selected_formats = normalize_formats(formats)
    if not report.valid:
        write_audit_reports(output, [report], [])
        raise ValidationError(f"Local KML failed validation; see {output / 'audit_report.json'}")
    return _finalize(output, [report], selected_formats)


def download_workflow(
    *,
    levels: list[int],
    formats: Iterable[str | OutputFormat],
    output_directory: Path,
    repair: bool = False,
    ca_bundle: Path | None = None,
    provider: IneterPfafstetterProvider | None = None,
) -> WorkflowResult:
    """Download sequentially, validate, convert, audit, and package selected levels."""

    active_provider = provider or IneterPfafstetterProvider()
    output = _prepare_output(output_directory)
    reports = active_provider.download_levels(
        levels,
        output / "raw",
        repair=repair,
        ca_bundle=ca_bundle,
    )
    return _finalize(output, reports, normalize_formats(formats))
