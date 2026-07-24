"""Minimal provider interface for the focused MVP."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from nica_geofetch.models import DiagnosticReport, ValidationReport


class Provider(ABC):
    """The small contract required by technical and beginner interfaces."""

    @property
    @abstractmethod
    def provider_id(self) -> str:
        """Return the stable configured provider ID."""

    @abstractmethod
    def list_datasets(self) -> list[dict[str, Any]]:
        """Describe implemented datasets and levels."""

    @abstractmethod
    def build_url(self, level: int) -> str:
        """Construct the exact official source URL."""

    @abstractmethod
    def diagnose(self, level: int = 4, *, ca_bundle: Path | None = None) -> DiagnosticReport:
        """Diagnose official-source access without saving the dataset."""

    @abstractmethod
    def import_local(
        self,
        path: Path,
        level: int,
        *,
        repair: bool = False,
        source_url: str | None = None,
    ) -> ValidationReport:
        """Validate and normalize a manually supplied local file."""
