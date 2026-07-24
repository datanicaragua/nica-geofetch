# Handoff

## What was being done

Prompt `NicaGeoFetch_CodexDesktop_MVP1_PublicReleaseHardening_v0.1` is complete.
The local hardening implementation is checkpointed at `a52e32d`.

## Complete

- Local Git initialized on `main`.
- Seed KML structure and counts audited without tracking source data.
- Album rights statement extracted and visually verified.
- Package metadata, project identity, scope, governance, registry, provider
  configuration, architecture, strategic direction, and continuity created.
- Secure provider, validation, conversion, packaging, CLI, notebook, live-test
  isolation, and 27-test offline suite implemented.
- Supplied level 4 KML converted offline to every requested format and reopened.
- MVP foundation and hardening acceptance checks and pre-commit hooks pass.
- Public notebook bootstraps from GitHub without requiring a repository checkout
  and supports package-ZIP upload; the developer notebook remains editable/local.
- Reports and manifests distinguish all retrieval modes and contain complete
  remote HTTP/source provenance.
- Live level 4 test passed with 12 features and automatic temporary cleanup.
- Local publication audit and 38 offline tests pass.

## Incomplete

Nothing remains inside the authorized local hardening task. GitHub CI, a real
badge-launched fresh-Colab run, visibility approval, and v0.1.0 release
approval are intentionally external human gates.

## NEXT_ACTION

A human owner must review `docs/PUBLICATION_CHECKLIST.md` and explicitly
authorize any remote, push, visibility change, or release. After visibility,
run GitHub CI and the real fresh-Colab gate before considering v0.1.0. No such
action is authorized by this handoff.

## Verify environment

```powershell
python --version
python -m pip install -e ".[dev]"
git status --short --branch
python scripts\publication_audit.py
```

## Resume

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
pre-commit run --all-files
```

## Known risks

- Institutional endpoint availability and schema may change.
- No explicit open-data license has been identified for the 2025 layers.
- Real level 7 input is large (about 35 MB and 2,337 placemarks), so parsing
  must remain bounded and conversions must be verified after writing.
- Shapefile field-name constraints require deterministic mappings.
- The public Colab GitHub bootstrap cannot complete until the target repository
  exists and is visible.

## Relevant files

- `AGENTS.md`
- `docs/PROJECT_STATUS.md`
- `docs/ARCHITECTURE.md`
- `docs/PUBLICATION_CHECKLIST.md`
- `configs/providers/ineter_pfafstetter_2025.yml`
- `registry/datasets.yml`
- `scripts/audit_seed_inputs.py`
- `pyproject.toml`

## Dirty working tree

Expected after the hardening closeout commit: clean tracked working tree.
`seed_inputs/`, `.venv/`, `.pytest_tmp/`, `.pre-commit-cache/`, and `tmp/` are
ignored local artifacts and must remain untracked.
