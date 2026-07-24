"""Small data models shared by providers, validation, conversion, and interfaces."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

from shapely.geometry.base import BaseGeometry


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
    timeout_connect_seconds: float = 10.0
    timeout_read_seconds: float = 90.0
    max_response_bytes: int = 100_000_000
    retries: int = 2
    backoff_seconds: float = 1.0
    polite_delay_seconds: float = 1.0
    user_agent: str = "Nica-GeoFetch/0.1 (+https://github.com/DataNicaTools/nica-geofetch)"


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
    level: int
    sha256: str
    checked_utc: str
    features: list[KMLFeature] = field(default_factory=list)
    issues: list[ValidationIssue] = field(default_factory=list)
    placemark_count: int = 0
    polygon_feature_count: int = 0
    ground_overlay_count: int = 0
    network_link_count: int = 0
    repaired_geometry_count: int = 0

    @property
    def valid(self) -> bool:
        """Whether no error-level finding was recorded."""

        return not any(issue.severity == "error" for issue in self.issues)

    def to_dict(self, *, include_features: bool = False) -> dict[str, Any]:
        """Return a JSON-serializable audit summary."""

        result: dict[str, Any] = {
            "source_path": str(self.source_path),
            "source_url": self.source_url,
            "level": self.level,
            "sha256": self.sha256,
            "checked_utc": self.checked_utc,
            "valid": self.valid,
            "placemark_count": self.placemark_count,
            "polygon_feature_count": self.polygon_feature_count,
            "ground_overlay_count": self.ground_overlay_count,
            "network_link_count": self.network_link_count,
            "repaired_geometry_count": self.repaired_geometry_count,
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

    @property
    def valid(self) -> bool:
        """Whether all source files passed validation."""

        return all(report.valid for report in self.reports)

    def summary_rows(self) -> list[dict[str, Any]]:
        """Return compact rows for terminal or notebook display."""

        conversions_by_level = {item.level: item for item in self.conversions}
        return [
            {
                "level": report.level,
                "valid": report.valid,
                "features": report.polygon_feature_count,
                "sha256": report.sha256,
                "outputs": sorted(conversions_by_level[report.level].outputs),
            }
            for report in self.reports
        ]
