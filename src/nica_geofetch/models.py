"""Small data models shared by providers, validation, conversion, and interfaces."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

from shapely.geometry.base import BaseGeometry

METADATA_ORIGIN_VALUES = frozenset(
    {
        "source_declared",
        "detected",
        "inferred",
        "derived",
        "user_supplied",
        "unknown",
    }
)
SOURCE_RELATIONSHIP_VALUES = frozenset(
    {
        "authoritative",
        "official_mirror",
        "institutional_copy",
        "derived_from_authoritative",
        "comparable_not_equivalent",
        "fallback_non_equivalent",
        "unverified",
    }
)


class RetrievalMode(StrEnum):
    """How the exact source bytes entered a validation workflow."""

    REMOTE_DOWNLOAD = "remote_download"
    MANUAL_IMPORT = "manual_import"
    SEED_INPUT = "seed_input"


class OutputFormat(StrEnum):
    """Formats supported by MVP-1."""

    KML = "kml"
    GPKG = "gpkg"
    GEOJSON = "geojson"
    SHAPEFILE = "shapefile"


@dataclass(frozen=True)
class ProviderConfig:
    """Validated runtime configuration for the single MVP provider."""

    provider_id: str
    title: str
    endpoint: str
    allowed_hosts: tuple[str, ...]
    layers: dict[int, str]
    code_aliases: dict[int, tuple[str, ...]]
    plausible_bounds: tuple[float, float, float, float]
    configuration_version: str = "1"
    timeout_connect_seconds: float = 10.0
    timeout_read_seconds: float = 90.0
    max_response_bytes: int = 100_000_000
    retries: int = 2
    backoff_seconds: float = 1.0
    polite_delay_seconds: float = 1.0
    user_agent: str = "Nica-GeoFetch/0.1 (+https://github.com/datanicaragua/nica-geofetch)"


@dataclass(frozen=True)
class DownloadSettings:
    """Per-run network settings; TLS verification is never silently disabled."""

    timeout_connect_seconds: float
    timeout_read_seconds: float
    max_response_bytes: int
    retries: int
    backoff_seconds: float
    polite_delay_seconds: float
    user_agent: str
    ca_bundle: Path | None = None


@dataclass
class DiagnosticReport:
    """Normalized access diagnostic suitable for JSON output."""

    ok: bool
    category: str
    message: str
    official_url: str
    http_status: int | None = None
    content_type: str | None = None
    checked_utc: str | None = None
    manual_download_instructions: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation."""

        return asdict(self)


@dataclass(frozen=True)
class DownloadMetadata:
    """HTTP metadata captured after streaming and before source validation."""

    source_url: str
    retrieved_at_utc: str
    response_content_type: str | None
    byte_size: int


@dataclass
class ValidationIssue:
    """One validation finding."""

    severity: str
    code: str
    message: str
    feature_name: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation."""

        return asdict(self)


@dataclass
class KMLFeature:
    """A normalized polygon feature and its source attributes."""

    name: str
    pfaf_code: str | None
    level: int
    attributes: dict[str, str]
    geometry: BaseGeometry


@dataclass
class ValidationReport:
    """Complete validation result for one source KML."""

    source_path: Path
    source_url: str | None
    source_layer: str
    retrieval_mode: RetrievalMode
    level: int
    sha256: str
    checked_utc: str
    retrieved_at_utc: str
    response_content_type: str | None
    byte_size: int
    source_institution: str = "Instituto Nicaragüense de Estudios Territoriales (INETER)"
    provider_id: str = "ineter-pfafstetter"
    dataset_id: str = "ineter-pfafstetter-2025"
    source_relationship: str = "authoritative"
    original_source_format: str = "KML"
    crs: str = "EPSG:4326"
    provider_configuration_version: str = "1"
    metadata_basis: dict[str, list[str]] = field(default_factory=dict)
    features: list[KMLFeature] = field(default_factory=list)
    issues: list[ValidationIssue] = field(default_factory=list)
    placemark_count: int = 0
    polygon_feature_count: int = 0
    ground_overlay_count: int = 0
    network_link_count: int = 0
    invalid_geometry_count: int = 0
    invalid_geometry_feature_ids: list[str] = field(default_factory=list)
    repair_requested: bool = False
    repaired_geometry_count: int = 0
    repair_method: str | None = None
    repaired_working_copy_sha256: str | None = None

    def __post_init__(self) -> None:
        """Reject provenance values outside the intentionally small vocabularies."""

        if self.source_relationship not in SOURCE_RELATIONSHIP_VALUES:
            raise ValueError(f"Unsupported source relationship: {self.source_relationship}")
        unsupported_origins = set(self.metadata_basis) - (
            METADATA_ORIGIN_VALUES | {"uncertainties"}
        )
        if unsupported_origins:
            raise ValueError(
                f"Unsupported metadata origin categories: {sorted(unsupported_origins)}"
            )

    @property
    def acquisition_valid(self) -> bool:
        """Whether the original bytes are a usable institutional vector KML."""

        acquisition_error_codes = {
            "empty_kml",
            "implausible_bounds",
            "malformed_kml",
            "network_link_only_kml",
            "ogc_error",
            "raster_only_kml",
            "unexpected_html",
        }
        return not any(
            issue.severity == "error" and issue.code in acquisition_error_codes
            for issue in self.issues
        )

    @property
    def geometry_valid(self) -> bool:
        """Whether every original polygon passed topology validation."""

        return self.invalid_geometry_count == 0

    @property
    def post_repair_geometry_valid(self) -> bool:
        """Whether the analytical working geometries are topologically valid."""

        return not any(
            issue.severity == "error" and issue.code in {"empty_geometry", "invalid_geometry"}
            for issue in self.issues
        )

    @property
    def analytical_ready(self) -> bool:
        """Whether analytical derivatives may be generated from the working copy."""

        return not any(issue.severity == "error" for issue in self.issues)

    @property
    def valid(self) -> bool:
        """Backward-compatible alias for analytical readiness."""

        return self.analytical_ready

    @property
    def repair_applied(self) -> bool:
        """Whether explicit repair changed at least one analytical geometry."""

        return self.repaired_geometry_count > 0

    @property
    def validation_status(self) -> str:
        """Return a status that does not mislabel a retained source as failed."""

        if not self.acquisition_valid:
            return "acquisition_invalid"
        if self.analytical_ready and self.geometry_valid:
            return "valid"
        if self.analytical_ready:
            return "valid_after_repair"
        if not self.geometry_valid:
            return "acquisition_valid_with_topology_warnings"
        return "acquisition_valid_not_analytical_ready"

    def to_dict(self, *, include_features: bool = False) -> dict[str, Any]:
        """Return a JSON-serializable audit summary."""

        result: dict[str, Any] = {
            "source_path": str(self.source_path),
            "source_institution": self.source_institution,
            "provider_id": self.provider_id,
            "dataset_id": self.dataset_id,
            "source_relationship": self.source_relationship,
            "source_url": self.source_url,
            "source_layer": self.source_layer,
            "retrieval_mode": self.retrieval_mode.value,
            "level": self.level,
            "original_source_format": self.original_source_format,
            "crs": self.crs,
            "sha256": self.sha256,
            "checked_utc": self.checked_utc,
            "retrieved_at_utc": self.retrieved_at_utc,
            "response_content_type": self.response_content_type,
            "byte_size": self.byte_size,
            "provider_configuration_version": self.provider_configuration_version,
            "metadata_basis": self.metadata_basis,
            "valid": self.valid,
            "acquisition_valid": self.acquisition_valid,
            "acquisition_status": "valid" if self.acquisition_valid else "invalid",
            "geometry_valid": self.geometry_valid,
            "geometry_validation_status": (
                "valid"
                if self.geometry_valid
                else "repaired"
                if self.repair_applied and self.post_repair_geometry_valid
                else "warnings"
            ),
            "post_repair_geometry_valid": self.post_repair_geometry_valid,
            "analytical_ready": self.analytical_ready,
            "validation_status": self.validation_status,
            "placemark_count": self.placemark_count,
            "polygon_feature_count": self.polygon_feature_count,
            "geometry_count": self.polygon_feature_count,
            "geometry_types": sorted({feature.geometry.geom_type for feature in self.features}),
            "ground_overlay_count": self.ground_overlay_count,
            "network_link_count": self.network_link_count,
            "invalid_geometry_count": self.invalid_geometry_count,
            "invalid_geometry_feature_ids": self.invalid_geometry_feature_ids,
            "repair_requested": self.repair_requested,
            "repair_applied": self.repair_applied,
            "repaired_geometry_count": self.repaired_geometry_count,
            "repair_method": self.repair_method,
            "original_sha256": self.sha256,
            "repaired_working_copy_sha256": self.repaired_working_copy_sha256,
            "issue_counts": {
                severity: sum(1 for item in self.issues if item.severity == severity)
                for severity in ("error", "warning", "info")
            },
            "issues": [issue.to_dict() for issue in self.issues],
        }
        if include_features:
            result["features"] = [
                {
                    "name": feature.name,
                    "pfaf_code": feature.pfaf_code,
                    "level": feature.level,
                    "attributes": feature.attributes,
                    "geometry_type": feature.geometry.geom_type,
                }
                for feature in self.features
            ]
        return result


@dataclass
class ConversionResult:
    """Verified files produced for one level."""

    level: int
    outputs: dict[str, Path]
    field_mapping: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation."""

        return {
            "level": self.level,
            "outputs": {key: str(value) for key, value in self.outputs.items()},
            "field_mapping": self.field_mapping,
        }


@dataclass
class WorkflowResult:
    """End-to-end result shared by CLI and notebook."""

    output_directory: Path
    reports: list[ValidationReport]
    conversions: list[ConversionResult]
    archive_path: Path
    audit_json_path: Path
    audit_markdown_path: Path
    results_guide_path: Path
    requested_formats: list[OutputFormat]
    generated_at_utc: str

    @property
    def valid(self) -> bool:
        """Whether every retained source is ready for analytical conversion."""

        return all(report.valid for report in self.reports)

    @property
    def acquisition_valid(self) -> bool:
        """Whether every source in the completed workflow was retained safely."""

        return all(report.acquisition_valid for report in self.reports)

    def summary_rows(self) -> list[dict[str, Any]]:
        """Return compact rows for terminal or notebook display."""

        conversions_by_level = {item.level: item for item in self.conversions}
        requested_analytical = [
            item.value for item in self.requested_formats if item != OutputFormat.KML
        ]
        return [
            {
                "level": report.level,
                "retrieval_mode": report.retrieval_mode.value,
                "acquisition_valid": report.acquisition_valid,
                "acquisition_status": ("correct" if report.acquisition_valid else "failed"),
                "geometry_valid": report.geometry_valid,
                "geometry_status": (
                    "correct"
                    if report.geometry_valid
                    else "repaired"
                    if report.repair_applied and report.post_repair_geometry_valid
                    else "warnings"
                ),
                "invalid_geometry_count": report.invalid_geometry_count,
                "repair_requested": report.repair_requested,
                "repair_applied": report.repair_applied,
                "analytical_ready": report.analytical_ready,
                "valid": report.valid,
                "features": report.polygon_feature_count,
                "sha256": report.sha256,
                "outputs": sorted(conversions_by_level[report.level].outputs),
                "source_path": report.source_path.relative_to(self.output_directory).as_posix(),
                "analytical_outputs": sorted(
                    output
                    for output in conversions_by_level[report.level].outputs
                    if output != OutputFormat.KML.value
                ),
                "analytical_paths": sorted(
                    path.relative_to(self.output_directory).as_posix()
                    for output, path in conversions_by_level[report.level].outputs.items()
                    if output != OutputFormat.KML.value
                ),
                "skipped_analytical_outputs": [
                    output
                    for output in requested_analytical
                    if output not in conversions_by_level[report.level].outputs
                ],
                "skip_reason_code": (
                    "topology_warnings_repair_disabled"
                    if report.invalid_geometry_count and not report.repair_requested
                    else "post_repair_not_ready"
                    if report.repair_requested and not report.analytical_ready
                    else "analytical_not_generated"
                ),
                "warnings": [
                    issue.message
                    for issue in report.issues
                    if issue.severity == "warning" or issue.code == "invalid_geometry"
                ],
                "result": (
                    "correct"
                    if report.analytical_ready and report.geometry_valid
                    else "repaired"
                    if report.analytical_ready and report.repair_applied
                    else "correct_with_warnings"
                    if report.acquisition_valid
                    else "failed"
                ),
            }
            for report in self.reports
        ]
