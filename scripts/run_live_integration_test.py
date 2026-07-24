"""Opt-in, single-level live INETER smoke test with automatic cleanup."""

from __future__ import annotations

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
        print(
            f"Live test passed: {result.reports[0].polygon_feature_count} level 4 polygon features."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
