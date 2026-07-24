"""Logging helpers used by CLI and notebook interfaces."""

from __future__ import annotations

import logging


def configure_logging(verbose: bool = False) -> None:
    """Configure concise, understandable progress logs once."""

    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
        force=True,
    )
