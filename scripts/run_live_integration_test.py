"""Opt-in, single-level live INETER smoke test with automatic cleanup."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from nica_geofetch.models import OutputFormat
from nica_geofetch.workflows import download_workflow


def main() -> int:
    """Download level 4 only when the explicit environment opt-in is present."""

    if os.environ.get("RUN_INETER_LIVE_TEST") != "1":
        print("Skipped: set RUN_INETER_LIVE_TEST=1 to run the single-level live test.")
        return 0
    with tempfile.TemporaryDirectory(prefix="nica_geofetch_live_") as directory:
        result = download_workflow(
            levels=[4],
            formats=[OutputFormat.KML],
            output_directory=Path(directory),
        )
        if not result.valid or result.reports[0].level != 4:
            raise RuntimeError("Live level 4 workflow did not validate")
        report = result.reports[0]
        print(
            json.dumps(
                {
                    "status": "passed",
                    "level": report.level,
                    "retrieval_mode": report.retrieval_mode.value,
                    "source_url": report.source_url,
                    "source_layer": report.source_layer,
                    "retrieved_at_utc": report.retrieved_at_utc,
                    "response_content_type": report.response_content_type,
                    "byte_size": report.byte_size,
                    "sha256": report.sha256,
                    "validation_status": "valid" if report.valid else "invalid",
                    "placemark_count": report.placemark_count,
                    "geometry_count": report.polygon_feature_count,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
