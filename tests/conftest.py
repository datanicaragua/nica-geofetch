"""Shared paths for synthetic, offline-only tests."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def fixtures_directory() -> Path:
    """Return the committed synthetic fixture directory."""

    return Path(__file__).parent / "fixtures"
