"""INETER 2025 Pfafstetter KML provider."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

from nica_geofetch.config import download_settings, load_provider_config
from nica_geofetch.download import SecureDownloader
from nica_geofetch.exceptions import ValidationError
from nica_geofetch.models import (
    DiagnosticReport,
    DownloadMetadata,
    ProviderConfig,
    RetrievalMode,
    ValidationReport,
)
from nica_geofetch.providers.base import Provider
from nica_geofetch.validation import validate_kml


class IneterPfafstetterProvider(Provider):
    """The only implemented MVP-1 provider."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        self.config = config or load_provider_config()

    @property
    def provider_id(self) -> str:
        """Return the stable provider ID."""

        return self.config.provider_id

    def _require_level(self, level: int) -> None:
        if level not in self.config.layers:
            raise ValueError("Level must be one of 4, 5, 6, or 7")

    def list_datasets(self) -> list[dict[str, Any]]:
        """Return the single configured dataset family."""

        return [
            {
                "dataset_id": "ineter-pfafstetter-2025",
                "title": self.config.title,
                "provider": self.provider_id,
                "levels": sorted(self.config.layers),
                "source_format": "KML",
                "recommended_format": "GeoPackage",
                "official_endpoint": self.config.endpoint,
            }
        ]

    def build_url(self, level: int) -> str:
        """Construct the exact official reflector URL with Unicode-safe encoding."""

        self._require_level(level)
        query = urlencode(
            {
                "layers": self.config.layers[level],
                "mode": "download",
                "kmattr": "true",
                "kmplacemark": "true",
            }
        )
        return f"{self.config.endpoint}?{query}"

    def _downloader(self, ca_bundle: Path | None = None) -> SecureDownloader:
        return SecureDownloader(
            allowed_hosts=self.config.allowed_hosts,
            settings=download_settings(self.config, ca_bundle),
        )

    def diagnose(self, level: int = 4, *, ca_bundle: Path | None = None) -> DiagnosticReport:
        """Probe one official level without retaining source bytes."""

        return self._downloader(ca_bundle).probe(self.build_url(level))

    def import_local(
        self,
        path: Path,
        level: int,
        *,
        repair: bool = False,
        source_url: str | None = None,
        retrieval_mode: RetrievalMode = RetrievalMode.MANUAL_IMPORT,
        retrieved_at_utc: str | None = None,
        response_content_type: str | None = None,
        byte_size: int | None = None,
    ) -> ValidationReport:
        """Validate a local KML using provider aliases and provenance."""

        self._require_level(level)
        if not path.is_file():
            raise FileNotFoundError(path)
        return validate_kml(
            path,
            level=level,
            code_aliases=self.config.code_aliases[level],
            plausible_bounds=self.config.plausible_bounds,
            provider_id=self.provider_id,
            source_url=source_url,
            source_layer=self.config.layers[level],
            retrieval_mode=retrieval_mode,
            retrieved_at_utc=retrieved_at_utc,
            response_content_type=response_content_type,
            byte_size=byte_size,
            repair=repair,
        )

    def download_level(
        self,
        level: int,
        raw_directory: Path,
        *,
        repair: bool = False,
        ca_bundle: Path | None = None,
        downloader: SecureDownloader | None = None,
    ) -> ValidationReport:
        """Download one level and atomically retain it only after validation."""

        self._require_level(level)
        url = self.build_url(level)
        destination = raw_directory / f"ineter_pfafstetter_2025_level{level}.kml"
        client = downloader or self._downloader(ca_bundle)

        def validator(part_path: Path, metadata: DownloadMetadata) -> ValidationReport:
            report = self.import_local(
                part_path,
                level,
                repair=repair,
                source_url=url,
                retrieval_mode=RetrievalMode.REMOTE_DOWNLOAD,
                retrieved_at_utc=metadata.retrieved_at_utc,
                response_content_type=metadata.response_content_type,
                byte_size=metadata.byte_size,
            )
            if not report.valid:
                errors = "; ".join(
                    issue.code for issue in report.issues if issue.severity == "error"
                )
                raise ValidationError(f"Downloaded KML failed validation: {errors}")
            return report

        report = client.download(url, destination, validator)
        report.source_path = destination
        return report

    def download_levels(
        self,
        levels: list[int],
        raw_directory: Path,
        *,
        repair: bool = False,
        ca_bundle: Path | None = None,
    ) -> list[ValidationReport]:
        """Download levels sequentially with a polite delay between requests."""

        unique_levels = list(dict.fromkeys(levels))
        for level in unique_levels:
            self._require_level(level)
        downloader = self._downloader(ca_bundle)
        reports: list[ValidationReport] = []
        for index, level in enumerate(unique_levels):
            if index and self.config.polite_delay_seconds > 0:
                time.sleep(self.config.polite_delay_seconds)
            reports.append(
                self.download_level(
                    level,
                    raw_directory,
                    repair=repair,
                    downloader=downloader,
                )
            )
        return reports
