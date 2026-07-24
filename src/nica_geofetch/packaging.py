"""Deterministic final workflow archive creation."""

from __future__ import annotations

import zipfile
from pathlib import Path

from nica_geofetch.exceptions import ConversionError

FIXED_ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
REQUIRED_PACKAGE_FILES = {
    "audit_report.json",
    "audit_report.md",
    "source_manifest.json",
    "checksums_sha256.json",
    "provenance_summary.md",
}


def create_final_archive(output_directory: Path) -> Path:
    """Create a deterministic ZIP containing raw, processed, and audit artifacts."""

    archive = output_directory / "nica_geofetch_results.zip"
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
