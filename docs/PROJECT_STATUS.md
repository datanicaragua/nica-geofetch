# Project status

- **Current milestone:** MVP-1 Colab output-clarity release candidate
  (Codex implementation complete; independent and human review pending)
- **Current branch:** `fix/mvp1-colab-output-clarity-v0.3`
- **Open pull request:** [#1](https://github.com/datanicaragua/nica-geofetch/pull/1)
  against `main`; created as draft and eligible for ready-for-review only after
  final branch CI is green
- **Implementation HEAD:** `304b8a5` -
  `fix: clarify Colab outputs and ZIP delivery`
- **Current HEAD:** the documentation closeout commit that follows `304b8a5`;
  its exact SHA is recorded in PR #1 evidence and the execution report
- **last_updated_utc:** `2026-07-26T19:57:07Z`

## Implemented capabilities

- Complete focused provider for INETER Pfafstetter 2025 levels 4-7.
- Secure diagnosis/download with manual local-import fallback.
- Streaming KML validation, attribute/code extraction, bounds and geometry
  checks, opt-in repair, provenance, and SHA-256.
- Verified KML, GeoPackage, GeoJSON, and Shapefile ZIP workflows.
- Audit reports, source manifest, checksum map, provenance summary, and final ZIP.
- Technical CLI, Spanish Colab notebook, governance, registry, architecture,
  strategic vision, and continuity documentation.
- Public fresh-Colab bootstrap from the configurable
  `datanicaragua/nica-geofetch` Git ref, with manual package-ZIP fallback.
- Separate repository-local developer notebook with editable installation.
- Retrieval modes (`remote_download`, `manual_import`, `seed_input`) and
  complete remote HTTP/source provenance in reports and manifests.
- Publication audit and human-controlled publication/release checklist.
- Consistent positioning as the acquisition, validation, provenance, and
  preparation layer for foundational DataNicaTools datasets.
- Manifest schema version 3 with source relationships, compact metadata-origin
  groups, source-versus-derived hashes, transformation steps, geometry/CRS
  facts, and software/provider-configuration versions.
- Component value gate, human-guided source-resolution policy, updated registry,
  and indexed INETER Pfafstetter case study.
- HydroBASINS recorded only as a planned `comparable_not_equivalent` dataset,
  with no provider or substitution behavior.
- Public Colab bootstrap failures are classified in Spanish, package import is
  verified immediately, and downstream package imports are guarded when
  bootstrap is skipped or fails.
- Professional authorship and proportionate human-led, AI-assisted development
  disclosure are documented.
- Acquisition validity, original geometry validity, and analytical readiness
  are explicit without introducing a new validation framework.
- Acquisition-valid original KML is preserved byte for byte through topology
  warnings; analytical derivatives remain strict and repair remains opt-in.
- Public Colab provides N4-default/all-level controls, sequential per-level
  status, explicit repair, a beginner summary, immediate click-to-download ZIP,
  and optional button-triggered manual import.
- Public Colab now uses five static beginner steps, one authoritative automatic
  ZIP control, a subordinate manual fallback, dynamic audit-based expectations,
  compact Spanish results, localized common warnings, and collapsed source
  presentation metadata.
- Each final archive has a descriptive level/format/UTC filename and includes
  `LEEME_RESULTADOS.md` with exact retained, generated, and skipped outputs.
- Nontrivial changes use the documented task-branch, draft-PR, CI,
  independent-review, and human-approval workflow.

## Test status

- Editable installation: passed in the local Python 3.12 virtual environment.
- Seed audit: passed for four KML files and one PDF.
- Level 4 real offline workflow: passed all conversions and reopen checks.
- PDF rights statement: text-extracted and visually verified.
- `ruff check .`: passed.
- `mypy src`: passed (17 source files).
- `pytest -q`: passed (66 offline tests).
- `python -m nica_geofetch.cli --help`: passed.
- Both notebooks: valid nbformat v4 and smoke assertions passed.
- Fresh-Colab bootstrap simulation: passed without `pyproject.toml`.
- Four configured INETER URLs: semantically equivalent to manually verified URLs.
- Opt-in live level 4 test: passed again on 2026-07-25 with 12 Placemarks,
  12 polygon geometries, `validation_status=valid`, and temporary data removed.
- Publication audit: passed with no forbidden institutional data or supported
  secret signature.
- Registry/source-relationship, metadata-origin, checksum-lineage, legacy
  manifest-field, documentation-link, and unchanged-notebook assertions passed.
- GitHub/private-access, authentication, missing-Git, pip-failure, post-install
  import, ZIP fallback, and public-notebook cell-order simulations passed.
- Synthetic N5-like topology evidence confirms two invalid geometries are
  retained without repair, derivatives are skipped, explicit repair enables
  conversion, source/working-copy checksums remain separate, and later selected
  levels continue.
- Focused notebook/package tests confirm one automatic ZIP button, static step
  order, raw/processed and per-level semantics, dynamic expectations and
  explanations, Spanish warning localization, descriptive names, results-guide
  content, manual fallback isolation, unchanged bootstrap source, unchanged
  developer notebook, and durable PR governance.
- `pre-commit run --all-files`: passed all six hooks.
- GitHub Actions PR run
  [`30217903826`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30217903826)
  passed every required gate on Python 3.11 and 3.12 for implementation commit
  `304b8a5`. A final run is required after the documentation closeout commit.

## Current limitations

Levels 5-7 contain 2, 1, and 2 known invalid source geometries respectively.
Their original KML is now retained without repair, but their analytical
derivatives are skipped unless explicit repair succeeds. Python 3.12 was
verified locally; Python 3.11 is configured in CI but was not available in this
desktop environment.

The expected `origin` is configured. GitHub reports
`datanicaragua/nica-geofetch` as public and the authenticated owner as `ADMIN`.
The task branch was pushed normally and public PR #1 is open against `main`.
No direct `main` commit, force push, merge, auto-merge, tag, or release was
performed. Anonymous
HTTP access to the repository, raw notebook, and Colab badge returned 200.
A clean temporary Python environment installed the Colab Git requirement from
public `main`, resolved `c6d5829`, imported the package, and printed `0.1.0`.

## Blocked items

- ChatGPT Project audit of open PR #1 remains pending.
- Human public-Colab validation remains pending: Run all without opening manual
  upload; one automatic ZIP button; N4-N7/GeoPackage/repair-off output
  inspection; accurate `LEEME_RESULTADOS.md`; descriptive ZIP name; subordinate
  fallback; latest-only second-run state; and collapsed code presentation.
- Institutional redistribution terms remain unclarified; no source data may be
  attached to a software release.
- Merge and `v0.1.0` remain unauthorized and blocked until independent review,
  human validation, and separate human decisions.

## Next recommended action

Submit open PR #1 and its evidence to ChatGPT Project for independent audit,
then perform the documented fresh public-Colab validation. Do not merge, tag,
or release until the applicable human gates are explicitly approved.
