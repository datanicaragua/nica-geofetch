"""Offline interface, notebook, live isolation, and resume-document checks."""

from __future__ import annotations

import ast
import builtins
import os
import re
import subprocess
import sys
import types
from pathlib import Path
from typing import Any

import nbformat
import pytest
import yaml
from nbformat.validator import validate

from nica_geofetch.cli import main

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def public_notebook() -> Any:
    """Load the public notebook used by bootstrap simulations."""

    return nbformat.read(
        REPOSITORY_ROOT / "notebooks/NicaGeoFetch_Colab.ipynb",
        as_version=4,
    )


def public_bootstrap_cell() -> Any:
    """Return the tagged public bootstrap cell."""

    return next(
        cell
        for cell in public_notebook().cells
        if "bootstrap" in cell.get("metadata", {}).get("tags", [])
    )


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
        "Seleccionar todos los niveles",
        "Seleccionar solo nivel 4",
        "Diagnosticar acceso",
        "Descargar y preparar",
        "Reparar geometrías inválidas para generar formatos analíticos",
        "Descargar ZIP a mi computadora",
        "Alternativa opcional: importar un KML descargado manualmente",
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
        "La instalación anónima desde GitHub requiere que el repositorio sea público",
        "No pegue tokens de GitHub",
        "import nica_geofetch",
        "BOOTSTRAP_OK",
    ):
        assert expected in source
    assert "verify=False" not in source
    assert "pyproject.toml" not in source


def test_public_notebook_defaults_and_all_level_selection() -> None:
    controls = next(cell for cell in public_notebook().cells if cell.get("id") == "controles")
    source = controls.source
    assert re.search(r"4:\s*widgets\.Checkbox\(\s*value=True", source)
    for level in (5, 6, 7):
        assert re.search(rf"{level}:\s*widgets\.Checkbox\(\s*value=False", source)
    assert "def select_all_levels" in source
    assert "control.value = True" in source
    assert "def select_only_level4" in source
    assert "control.value = level == 4" in source
    assert re.search(r"repair_checkbox\s*=\s*widgets\.Checkbox\(\s*value=False", source)
    assert re.search(r'layout=widgets\.Layout\(\s*display="none"', source)
    assert "disabled=True" in source


def test_manual_file_picker_runs_only_after_button_click() -> None:
    manual = next(
        cell for cell in public_notebook().cells if cell.get("id") == "configuracion-simple"
    )
    tree = ast.parse(manual.source)
    top_level_calls = [
        node
        for statement in tree.body
        for node in ast.walk(statement)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "upload"
        and not isinstance(statement, ast.FunctionDef)
    ]
    assert top_level_calls == []
    upload_function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "upload_manual_kml"
    )
    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "upload"
        for node in ast.walk(upload_function)
    )
    assert "manual_upload_button.on_click(upload_manual_kml)" in manual.source


def test_public_notebook_has_temporary_storage_and_warning_guidance() -> None:
    source = "\n".join("".join(cell.source) for cell in public_notebook().cells)
    for expected in (
        "/content",
        "almacenamiento temporal",
        "desaparece",
        "Correcto con advertencias",
        "El KML original se conservará",
        "No se generará",
        "Continuando con el siguiente nivel",
        "files.download(str(LATEST_ARCHIVE))",
        "zip_download_button.layout.display = (",
        '"inline-flex" if LATEST_ARCHIVE.exists() else "none"',
    ):
        assert expected in source
    controls = next(cell for cell in public_notebook().cells if cell.get("id") == "controles")
    assert controls.source.index("except (NicaGeoFetchError") < controls.source.index(
        "except Exception"
    )


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
    capsys: Any,
) -> None:
    bootstrap = public_bootstrap_cell()
    calls: list[list[str]] = []

    def fake_run(command: list[str], **_kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(subprocess, "run", fake_run)
    assert not (tmp_path / "pyproject.toml").exists()
    namespace: dict[str, Any] = {}
    exec(compile(bootstrap.source, "public-colab-bootstrap", "exec"), namespace)
    assert calls
    requirement = calls[0][-1]
    assert "git+https://github.com/datanicaragua/nica-geofetch.git@main" in requirement
    assert namespace["BOOTSTRAP_OK"] is True
    output = capsys.readouterr().out
    assert "Versión instalada:" in output
    assert "Referencia Git seleccionada: main" in output
    assert "Fuente de instalación: github" in output


@pytest.mark.parametrize(
    ("diagnostic", "expected"),
    [
        ("fatal: repository not found", "repositorio no está disponible"),
        ("fatal: authentication failed", "rechazó la autenticación"),
        ("ERROR: Cannot find command 'git'", "Git no está disponible"),
        ("ERROR: wheel build failed", "pip no pudo instalar"),
    ],
)
def test_failed_github_bootstrap_is_beginner_readable_and_stops_imports(
    monkeypatch: pytest.MonkeyPatch,
    diagnostic: str,
    expected: str,
) -> None:
    bootstrap = public_bootstrap_cell()

    def fake_run(command: list[str], **_kwargs: Any) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(command, 1, stdout="", stderr=diagnostic)

    monkeypatch.setattr(subprocess, "run", fake_run)
    namespace: dict[str, Any] = {}
    with pytest.raises(RuntimeError, match=expected):
        exec(compile(bootstrap.source, "public-colab-bootstrap", "exec"), namespace)
    assert namespace["BOOTSTRAP_OK"] is False

    controls = next(cell for cell in public_notebook().cells if cell.get("id") == "controles")
    with pytest.raises(RuntimeError, match="La instalación no se completó"):
        exec(compile(controls.source, "public-colab-controls", "exec"), namespace)
    assert "json" not in namespace


def test_private_repository_guidance_contains_no_token_mechanism() -> None:
    source = public_bootstrap_cell().source
    assert "Para probar un repositorio privado" in source
    assert "INSTALL_SOURCE" in source and "zip" in source
    assert "No pegue tokens de GitHub ni credenciales" in source
    assert "github_pat_" not in source
    assert "ghp_" not in source
    assert "getpass" not in source


def test_zip_bootstrap_fallback_and_package_verification(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bootstrap = public_bootstrap_cell()
    source = bootstrap.source.replace(
        'INSTALL_SOURCE = "github"',
        'INSTALL_SOURCE = "zip"',
        1,
    )
    calls: list[list[str]] = []

    def fake_run(command: list[str], **_kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    files_module = types.ModuleType("google.colab.files")
    files_module.upload = lambda: {"nica-geofetch-package.zip": b"synthetic"}  # type: ignore[attr-defined]
    colab_module = types.ModuleType("google.colab")
    colab_module.files = files_module  # type: ignore[attr-defined]
    google_module = types.ModuleType("google")
    google_module.colab = colab_module  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "google", google_module)
    monkeypatch.setitem(sys.modules, "google.colab", colab_module)
    monkeypatch.setitem(sys.modules, "google.colab.files", files_module)
    monkeypatch.setattr(subprocess, "run", fake_run)

    namespace: dict[str, Any] = {}
    exec(compile(source, "public-colab-zip-bootstrap", "exec"), namespace)
    assert namespace["BOOTSTRAP_OK"] is True
    assert calls[0][-1] == "nica-geofetch-package.zip"
    assert calls[1][-1] == "ipywidgets>=8.1,<9"
    assert namespace["installation_source"] == "zip: nica-geofetch-package.zip"


def test_post_install_import_failure_is_wrapped_for_beginners(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bootstrap = public_bootstrap_cell()

    def fake_run(command: list[str], **_kwargs: Any) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    original_import = builtins.__import__

    def fake_import(
        name: str,
        globals: dict[str, Any] | None = None,
        locals: dict[str, Any] | None = None,
        fromlist: tuple[str, ...] = (),
        level: int = 0,
    ) -> Any:
        if name == "nica_geofetch":
            raise ModuleNotFoundError(name)
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(builtins, "__import__", fake_import)
    with pytest.raises(RuntimeError, match="todavía no puede importarse"):
        exec(compile(bootstrap.source, "public-colab-bootstrap", "exec"), {})


def test_public_notebook_bootstrap_is_first_executable_cell() -> None:
    code_cells = [cell for cell in public_notebook().cells if cell.cell_type == "code"]
    assert "bootstrap" in code_cells[0].get("metadata", {}).get("tags", [])
    assert code_cells[0].get("id") == "bootstrap"
    controls_source = code_cells[1].source
    assert controls_source.index("BOOTSTRAP_OK") < controls_source.index("from nica_geofetch")


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


def test_documentation_index_local_links_resolve() -> None:
    index_path = REPOSITORY_ROOT / "docs/index.md"
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", index_path.read_text(encoding="utf-8"))
    local_links = [link.split("#", 1)[0] for link in links if not link.startswith(("http", "#"))]
    assert local_links
    assert all((index_path.parent / link).resolve().exists() for link in local_links)


def test_registry_source_relationships_are_explicit_and_non_substituting() -> None:
    registry = yaml.safe_load(
        (REPOSITORY_ROOT / "registry/datasets.yml").read_text(encoding="utf-8")
    )
    implemented = registry["datasets"][0]
    comparable = registry["planned_comparable_datasets"][0]
    assert implemented["dataset_id"] == "ineter-pfafstetter-2025"
    assert implemented["source_relationship"] == "authoritative"
    assert implemented["implementation_status"] == "implemented"
    assert comparable["dataset_id"] != implemented["dataset_id"]
    assert comparable["status"] == "planned"
    assert comparable["relationship"] == "comparable_not_equivalent"
    assert "provider_id" not in comparable
    assert "official_source_url" not in comparable


def test_authorship_ai_disclosure_and_update_policy() -> None:
    readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
    readme_es = (REPOSITORY_ROOT / "README.es.md").read_text(encoding="utf-8")
    ai_disclosure = (REPOSITORY_ROOT / "docs/AI_ASSISTED_DEVELOPMENT.md").read_text(
        encoding="utf-8"
    )
    governance = (REPOSITORY_ROOT / "docs/DATA_GOVERNANCE.md").read_text(encoding="utf-8")
    status = (REPOSITORY_ROOT / "docs/PROJECT_STATUS.md").read_text(encoding="utf-8")
    handoff = (REPOSITORY_ROOT / "docs/HANDOFF.md").read_text(encoding="utf-8")

    for content in (readme, readme_es):
        assert "Gustavo Ernesto Martínez Cárdenas" in content
        assert "https://github.com/datanicaragua" in content
        assert "https://github.com/gustavoemc" in content
        assert "https://www.linkedin.com/in/gustavoernestom" in content
        assert "AI_ASSISTED_DEVELOPMENT.md" in content
        assert "Last updated" not in content
        assert "Última actualización" not in content
    for expected in (
        "human-led and AI-assisted",
        "Codex and ChatGPT",
        "model_at_execution: GPT-5.6 Sol",
        "reasoning_effort: Extra High",
        "AI tools are not",
    ):
        assert expected in ai_disclosure
    assert "Date and update policy" in governance
    assert "last_updated_utc" in status
    assert "last_updated_utc" in handoff


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
