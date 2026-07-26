# Handoff

- **last_updated_utc:** `2026-07-26T19:57:07Z`

## What was being done

Prompt
`NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.3` is
implemented on `fix/mvp1-colab-output-clarity-v0.3`. Implementation commit
`304b8a5` is pushed, public PR
[#1](https://github.com/datanicaragua/nica-geofetch/pull/1) is open against
`main`, and GitHub Actions run
[`30217903826`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30217903826)
passed on Python 3.11 and 3.12. The documentation closeout is the following
commit; its exact SHA and final CI are recorded in PR evidence.

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
- The public notebook now has five static steps, one authoritative automatic
  ZIP button, a collapsed subordinate manual fallback, dynamic preflight and
  per-level explanations, compact Spanish results, localized warnings, and
  collapsed implementation cells.
- `raw/`, `processed/`, one-ZIP execution, and separate per-level GeoPackages
  are explained before and after execution.
- Every final ZIP uses a descriptive level/format/UTC filename and contains
  `LEEME_RESULTADOS.md` with retained, generated, skipped, audit, provenance,
  opening, and licensing guidance.
- The public bootstrap cell source and developer notebook remain unchanged.
- The complete v0.3 prompt is archived; the task-branch/PR workflow is durable
  in `CONTRIBUTING.md` and concisely referenced from `AGENTS.md`.
- Editable installation, Ruff, mypy, 66 tests, both notebooks, CLI help,
  publication audit, and all six pre-commit hooks pass locally.
- Only `fix/mvp1-colab-output-clarity-v0.3` was pushed. Draft PR #1 was created
  against `main`, and its first CI run passed every gate for Python 3.11 and
  3.12.

## Incomplete

ChatGPT Project has not yet audited open PR #1. Human public-Colab validation,
merge approval, and release approval remain pending. No merge, auto-merge,
direct `main` push, force push, branch deletion, tag, GitHub release, PyPI
package, data release, protection change, or institutional-data archive was
performed.

## NEXT_ACTION

NEXT_ACTION:
ChatGPT Project audit of the open pull request, followed by human public-Colab
validation.

## Open pull request

- **PR:** [#1](https://github.com/datanicaragua/nica-geofetch/pull/1)
- **Branch:** `fix/mvp1-colab-output-clarity-v0.3`
- **Base:** `main`
- **Commits:** `304b8a5` (implementation); documentation closeout is the
  following commit recorded in the PR evidence comment
- **First green CI:** [run
  `30217903826`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30217903826)
  on Python 3.11 and 3.12
- **Merge authorized:** no
- **Release authorized:** no

## Required human public-Colab tests

1. **Run all** does not open the manual upload picker.
2. Exactly one automatic **Descargar ZIP a mi computadora** button exists.
3. N4-N7, GeoPackage, repair disabled retains four KML files in `raw/`,
   generates only `processed/pfaf_level4.gpkg`, and clearly explains every
   skipped analytical output.
4. `LEEME_RESULTADOS.md` exists and accurately lists the result paths.
5. The archive filename describes levels, format, and UTC execution time.
6. Manual fallback is visually subordinate and unnecessary after success.
7. A second automatic execution exposes only its latest archive.
8. Public implementation cells are less intrusive but remain inspectable.

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
- Automated notebook/package tests pass, but interactive Colab rendering,
  browser download behavior, Google Drive paths, and latest-only second-run
  state still require human validation.
- GitHub reports `main` as unprotected and no repository rulesets were found.
  The new workflow is documented but not technically enforced. A future
  human-approved governance task should consider required PR/status checks and
  force-push/branch-deletion restrictions.
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

## Working tree

Expected after the output-clarity documentation closeout: clean tracked working
tree on `fix/mvp1-colab-output-clarity-v0.3`, synchronized with the remote task
branch.
`seed_inputs/`, `.venv/`, `.pytest_tmp/`, `.pre-commit-cache/`, and `tmp/` are
ignored local artifacts and must remain untracked.
