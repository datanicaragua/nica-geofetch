"""Deterministic final workflow archive creation."""

from __future__ import annotations

import re
import zipfile
from collections.abc import Iterable
from pathlib import Path

from nica_geofetch.exceptions import ConversionError
from nica_geofetch.models import OutputFormat

FIXED_ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
REQUIRED_PACKAGE_FILES = {
    "audit_report.json",
    "audit_report.md",
    "source_manifest.json",
    "checksums_sha256.json",
    "provenance_summary.md",
    "LEEME_RESULTADOS.md",
}


def build_archive_name(
    *,
    levels: Iterable[int],
    formats: Iterable[OutputFormat],
    generated_at_utc: str,
) -> str:
    """Build a filesystem-safe archive name describing one workflow execution."""

    selected_levels = sorted(set(levels))
    if not selected_levels:
        raise ValueError("At least one level is required for the archive name")
    if len(selected_levels) == 1:
        level_token = f"n{selected_levels[0]}"
    elif selected_levels == list(range(selected_levels[0], selected_levels[-1] + 1)):
        level_token = f"n{selected_levels[0]}-n{selected_levels[-1]}"
    else:
        level_token = "_".join(f"n{level}" for level in selected_levels)

    format_values = list(dict.fromkeys(item.value for item in formats))
    format_token = "-".join(format_values) or "kml"
    timestamp_token = re.sub(r"[^0-9TZ]", "", generated_at_utc)
    if not re.fullmatch(r"\d{8}T\d{6}Z", timestamp_token):
        raise ValueError("generated_at_utc must be an ISO 8601 UTC timestamp")
    return f"nica_geofetch_ineter_pfaf_{level_token}_{format_token}_{timestamp_token}.zip"


def create_final_archive(output_directory: Path, *, archive_name: str) -> Path:
    """Create a deterministic ZIP containing raw, processed, and audit artifacts."""

    if Path(archive_name).name != archive_name or not archive_name.endswith(".zip"):
        raise ConversionError("Final archive name must be a safe ZIP basename")
    archive = output_directory / archive_name
    candidates = [
        path
        for path in output_directory.rglob("*")
        if path.is_file() and path != archive and ".part" not in path.name
    ]
    relative_names = {path.relative_to(output_directory).as_posix() for path in candidates}
    missing = REQUIRED_PACKAGE_FILES - relative_names
    if missing:
        raise ConversionError(f"Final package is missing required files: {sorted(missing)}")
    if not any(name.startswith("raw/") for name in relative_names):
        raise ConversionError("Final package does not contain a raw source file")

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(candidates, key=lambda value: value.as_posix()):
            relative = path.relative_to(output_directory).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, path.read_bytes())

    with zipfile.ZipFile(archive) as bundle:
        archived_names = set(bundle.namelist())
        if not REQUIRED_PACKAGE_FILES.issubset(archived_names):
            raise ConversionError("Final ZIP verification failed")
    return archive
