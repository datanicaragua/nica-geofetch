# Handoff

- **last_updated_utc:** `2026-07-25T15:29:59Z`

## What was being done

Prompt `NicaGeoFetch_CodexDesktop_MVP1_PublicationAndColabFix_v0.1` is in
progress. Local implementation and quality gates are complete; the verified
commit, push, GitHub Actions gate, and conditional visibility change remain.

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
- Local installation, ruff, mypy, 49 tests, notebook validation, CLI help, and
  publication audit pass.

## Incomplete

The local change is not yet committed or pushed. GitHub Actions for the new
HEAD and the authorized conditional visibility change remain. A real
badge-launched fresh-Colab run and v0.1.0 release approval remain human gates.

## NEXT_ACTION

Create the verified local commit, push it to the existing `origin/main`, wait
for GitHub Actions, and apply the visibility authorization in the active prompt
only if every publication gate passes.

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
- HydroBASINS or another comparable source must never be substituted under the
  INETER dataset identifier.

## Relevant files

- `AGENTS.md`
- `docs/PROJECT_STATUS.md`
- `docs/ARCHITECTURE.md`
- `docs/CASE_STUDY_INETER_PFAFSTETTER.md`
- `docs/PUBLICATION_CHECKLIST.md`
- `configs/providers/ineter_pfafstetter_2025.yml`
- `registry/datasets.yml`
- `scripts/audit_seed_inputs.py`
- `pyproject.toml`

## Dirty working tree

Expected after the context/lineage closeout commit: clean tracked working tree.
`seed_inputs/`, `.venv/`, `.pytest_tmp/`, `.pre-commit-cache/`, and `tmp/` are
ignored local artifacts and must remain untracked.
