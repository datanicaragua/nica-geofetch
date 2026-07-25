# Handoff

- **last_updated_utc:** `2026-07-25T17:30:07Z`

## What was being done

Prompt
`NicaGeoFetch_CodexDesktop_MVP1_ColabSourceRetentionDeliveryUX_v1.0` is
implemented at `0be8580`. Local gates and the single-level N4 live test pass.
The implementation is pushed, GitHub Actions run `30167669342` passed on
Python 3.11 and 3.12, and the existing GitHub repository remains public.

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
- Local publication audit and 40 offline tests pass.
- Strategic positioning, component value gate, source-resolution method,
  metadata-origin groups, and controlled source relationships are documented.
- Manifest schema version 3 distinguishes original and generated artifact
  checksums while retaining version 2 source fields.
- The registry and indexed case study distinguish authoritative INETER from
  planned, non-equivalent HydroBASINS comparison; no new provider was added.
- Public Colab now catches and explains GitHub/private, authentication,
  missing-Git, pip, and post-install import failures in Spanish.
- A failed or skipped bootstrap blocks downstream package imports; ZIP/wheel
  fallback and package API use are preserved.
- README authorship, AI-assisted-development disclosure, and UTC/date policy
  are documented.
- Local installation, ruff, mypy, 58 tests, notebook validation, CLI help, and
  publication audit pass.
- Commit `c6d5829` was pushed normally to the existing `origin/main`.
- GitHub Actions run `30164223783` passed on Python 3.11 and 3.12.
- Repository visibility changed from private to public under the prompt's
  conditional authorization.
- Anonymous repository, raw-notebook, and Colab-badge requests returned HTTP
  200. A clean temporary environment installed the public Git requirement,
  resolved `c6d5829`, imported `nica_geofetch`, and printed `0.1.0`.
- Acquisition-valid KML is now retained independently of topology validity.
  N5-N7 warning levels keep the original source and skip only analytical
  derivatives when repair is off.
- Explicit repair affects only the analytical working copy and records original
  and repaired checksums, repair method, affected identifiers, and generated
  formats.
- The public notebook now supports N4-default/all-level selection, per-level
  progress, warning-aware summaries, unique repeated runs, immediate ZIP
  delivery, and optional click-triggered manual import. The developer notebook
  is unchanged.
- The offline suite has 58 passing tests; editable installation, Ruff, mypy,
  both notebooks, CLI help, publication audit, and all six pre-commit hooks
  pass.
- A new polite N4 live test passed at `2026-07-25T17:18:29Z` with 12
  Placemarks/geometries and automatic cleanup. Levels 5-7 were not downloaded
  for automated testing.
- Implementation commit `0be8580` was pushed normally to `origin/main`; CI run
  `30167669342` passed every required job on Python 3.11 and 3.12.

## Incomplete

The badge-launched human Colab retest remains. The human must exercise N4+N5
without repair, all levels, explicit repair, the primary ZIP button, repeated
execution, and optional manual import. No tag, GitHub release, PyPI package,
data release, or institutional-data archive was created.

## NEXT_ACTION

NEXT_ACTION:
Human public-Colab retesting from a fresh anonymous runtime.

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
- The automated public Git installation passes, but interactive Colab behavior
  still requires the human top-to-bottom retest of the corrected warning and
  delivery flows.
- HydroBASINS or another comparable source must never be substituted under the
  INETER dataset identifier.

## Relevant files

- `AGENTS.md`
- `docs/PROJECT_STATUS.md`
- `docs/ARCHITECTURE.md`
- `docs/CASE_STUDY_INETER_PFAFSTETTER.md`
- `docs/PUBLICATION_CHECKLIST.md`
- `notebooks/NicaGeoFetch_Colab.ipynb`
- `src/nica_geofetch/models.py`
- `src/nica_geofetch/workflows.py`
- `configs/providers/ineter_pfafstetter_2025.yml`
- `registry/datasets.yml`
- `scripts/audit_seed_inputs.py`
- `pyproject.toml`

## Dirty working tree

Expected after the source-retention/Colab closeout commit: clean tracked working
tree synchronized with `origin/main`.
`seed_inputs/`, `.venv/`, `.pytest_tmp/`, `.pre-commit-cache/`, and `tmp/` are
ignored local artifacts and must remain untracked.
