# Handoff

## What was being done

Executing prompt `NicaGeoFetch_CodexDesktop_MVP1_Foundation_v0.2`. The complete
MVP implementation exists and is in final QA/commit closeout.

## Complete

- Local Git initialized on `main`.
- Seed KML structure and counts audited without tracking source data.
- Album rights statement extracted and visually verified.
- Package metadata, project identity, scope, governance, registry, provider
  configuration, architecture, strategic direction, and continuity created.
- Secure provider, validation, conversion, packaging, CLI, notebook, live-test
  isolation, and 27-test offline suite implemented.
- Supplied level 4 KML converted offline to every requested format and reopened.

## Incomplete

- Final clean acceptance rerun.
- Local checkpoint commits and commit hashes in continuity files.
- Final status/registry update and clean-tree confirmation.

## NEXT_ACTION

Run the final acceptance commands from `.venv`, create logical local commits,
write their hashes to `PROJECT_STATUS.md` and `PROMPT_REGISTRY.md`, then verify
that `git status --short --branch` is clean.

## Verify environment

```powershell
python --version
python -m pip install -e ".[dev]"
git status --short --branch
python scripts\audit_seed_inputs.py
```

## Resume

```powershell
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
```

During initial implementation some commands are expected to fail until their
modules exist. Fix the smallest failing layer and rerun the focused check.

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

Implementation and documentation changes are currently uncommitted.
`seed_inputs/`, `.venv/`, `.pytest_tmp/`, and `tmp/` are ignored local artifacts.
