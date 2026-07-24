"""Offline interface, notebook, live isolation, and resume-document checks."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import nbformat
import pytest
from nbformat.validator import validate

from nica_geofetch.cli import main

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def test_cli_help_smoke() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "nica_geofetch.cli", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "providers" in result.stdout
    assert "import-local" in result.stdout


def test_cli_provider_and_validation_smoke(
    fixtures_directory: Path,
    capsys: Any,
) -> None:
    assert main(["providers", "list"]) == 0
    assert (
        main(["validate", "--input", str(fixtures_directory / "vector_level4.kml"), "--level", "4"])
        == 0
    )
    captured = capsys.readouterr()
    assert "ineter-pfafstetter" in captured.out
    assert '"valid": true' in captured.out


@pytest.mark.parametrize(
    "notebook_name",
    ["NicaGeoFetch_Colab.ipynb", "NicaGeoFetch_Developer.ipynb"],
)
def test_both_notebooks_are_valid(notebook_name: str) -> None:
    path = REPOSITORY_ROOT / "notebooks" / notebook_name
    notebook = nbformat.read(path, as_version=4)
    validate(notebook)


def test_public_notebook_structure_and_safety() -> None:
    path = REPOSITORY_ROOT / "notebooks/NicaGeoFetch_Colab.ipynb"
    notebook = nbformat.read(path, as_version=4)
    source = "\n".join("".join(cell.source) for cell in notebook.cells)
    for expected in (
        "Proveedor",
        "for level in (4, 5, 6, 7)",
        "Diagnosticar acceso",
        "Descargar y validar",
        "Google Drive",
        "files.upload",
        "download_workflow",
        "import_local_workflow",
        "summary_rows",
        "files.download",
        "https://github.com/datanicaragua/nica-geofetch",
        'GIT_REF = "main"',
        'INSTALL_SOURCE = "github"',
        'INSTALL_SOURCE == "zip"',
        "etiqueta estable",
    ):
        assert expected in source
    assert "verify=False" not in source
    assert "pyproject.toml" not in source


def test_developer_notebook_is_repo_local_and_editable() -> None:
    path = REPOSITORY_ROOT / "notebooks/NicaGeoFetch_Developer.ipynb"
    notebook = nbformat.read(path, as_version=4)
    source = "\n".join("".join(cell.source) for cell in notebook.cells)
    assert "Solo para desarrollo" in source
    assert "pyproject.toml" in source
    assert '"-e", ".[dev,notebook]"' in source


def test_fresh_colab_bootstrap_does_not_require_pyproject(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    notebook = nbformat.read(
        REPOSITORY_ROOT / "notebooks/NicaGeoFetch_Colab.ipynb",
        as_version=4,
    )
    bootstrap = next(
        cell for cell in notebook.cells if "bootstrap" in cell.get("metadata", {}).get("tags", [])
    )
    calls: list[list[str]] = []

    def fake_check_call(command: list[str]) -> int:
        calls.append(command)
        return 0

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(subprocess, "check_call", fake_check_call)
    assert not (tmp_path / "pyproject.toml").exists()
    exec(compile(bootstrap.source, "public-colab-bootstrap", "exec"), {})
    assert calls
    requirement = calls[0][-1]
    assert "git+https://github.com/datanicaragua/nica-geofetch.git@main" in requirement


def test_live_script_is_opt_in_and_off_by_default() -> None:
    environment = os.environ.copy()
    environment.pop("RUN_INETER_LIVE_TEST", None)
    result = subprocess.run(
        [sys.executable, "scripts/run_live_integration_test.py"],
        cwd=REPOSITORY_ROOT,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Skipped" in result.stdout


def test_resume_document_consistency() -> None:
    agents = (REPOSITORY_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    status = (REPOSITORY_ROOT / "docs/PROJECT_STATUS.md").read_text(encoding="utf-8")
    handoff = (REPOSITORY_ROOT / "docs/HANDOFF.md").read_text(encoding="utf-8")
    index = (REPOSITORY_ROOT / "docs/index.md").read_text(encoding="utf-8")
    assert "Resume protocol" in agents
    assert "NEXT_ACTION" in handoff
    assert "Current milestone" in status
    assert "PROJECT_STATUS.md" in index and "HANDOFF.md" in index
    assert "git status" in agents


def test_no_real_institutional_data_is_tracked() -> None:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    tracked = result.stdout.splitlines()
    forbidden = [
        path
        for path in tracked
        if path.lower().endswith((".gpkg", ".shp", ".kmz"))
        or (path.lower().endswith(".kml") and not path.startswith("tests/fixtures/"))
    ]
    assert forbidden == []


def test_publication_audit_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/publication_audit.py"],
        cwd=REPOSITORY_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert '"passed": true' in result.stdout
