# Handoff

## What was being done

Prompt `NicaGeoFetch_CodexDesktop_MVP1_Foundation_v0.2` is complete. MVP-1 is
implemented, verified, and checkpointed at `aaba58b`.

## Complete

- Local Git initialized on `main`.
- Seed KML structure and counts audited without tracking source data.
- Album rights statement extracted and visually verified.
- Package metadata, project identity, scope, governance, registry, provider
  configuration, architecture, strategic direction, and continuity created.
- Secure provider, validation, conversion, packaging, CLI, notebook, live-test
  isolation, and 27-test offline suite implemented.
- Supplied level 4 KML converted offline to every requested format and reopened.
- All acceptance checks and pre-commit hooks pass.

## Incomplete

Nothing remains inside MVP-1. External source-license clarification and a
human-authorized live endpoint check belong to MVP-2.

## NEXT_ACTION

Begin MVP-2 by obtaining and recording an authoritative INETER statement for
licensing, redistribution, attribution, and update cadence. Before making any
change, run the resume checks below. Do not add a second provider yet.

## Verify environment

```powershell
python --version
python -m pip install -e ".[dev]"
git status --short --branch
python scripts\audit_seed_inputs.py
```

## Resume

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
```

## Known risks

- Institutional endpoint availability and schema may change.
- No explicit open-data license has been identified for the 2025 layers.
- Real level 7 input is large (about 35 MB and 2,337 placemarks), so parsing
  must remain bounded and conversions must be verified after writing.
- Shapefile field-name constraints require deterministic mappings.

## Relevant files

- `AGENTS.md`
- `docs/PROJECT_STATUS.md`
- `docs/ARCHITECTURE.md`
- `configs/providers/ineter_pfafstetter_2025.yml`
- `registry/datasets.yml`
- `scripts/audit_seed_inputs.py`
- `pyproject.toml`

## Dirty working tree

Expected after the closeout documentation commit: clean tracked working tree.
`seed_inputs/`, `.venv/`, `.pytest_tmp/`, `.pre-commit-cache/`, and `tmp/` are
ignored local artifacts and must remain untracked.
