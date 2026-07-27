# Project status

- **Current milestone:** MVP-1 post-merge release handoff; release readiness is
  not yet declared
- **MVP-1 implementation baseline from merged PR #1:**
  `141915416606abd47831775e677d89c6877643fb`
- **PR #2 continuity source branch:** `docs/mvp1-pr1-merge-continuity`
- **Merged pull request:** [#1](https://github.com/datanicaragua/nica-geofetch/pull/1)
  into `main` with merge commit `141915416606abd47831775e677d89c6877643fb`
- **Merged task HEAD:** `8a9b9a2e6f04e4ad5972f52383e291f4e3f997c1`
- **Previous task branch:** `fix/mvp1-colab-output-clarity-v0.3` remains
  available but is no longer the active project branch
- **Human Colab validation:** completed and approved
- **ChatGPT Project audit and merge recommendation:** completed and approved
- **last_updated_utc:** `2026-07-27T17:53:19Z`

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
- Human-tested beginner output now uses number-correct topology phrases,
  friendly format labels, notebook-scoped INFO suppression, final-success
  ordering after complete UI delivery, and separate topology/attribute
  sections without changing validation or repair semantics.

## Test status

- Editable installation: passed in the local Python 3.12 virtual environment.
- Seed audit: passed for four KML files and one PDF.
- Level 4 real offline workflow: passed all conversions and reopen checks.
- PDF rights statement: text-extracted and visually verified.
- `ruff check .`: passed.
- `mypy src`: passed (17 source files).
- `pytest -q`: passed (71 offline tests).
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
- GitHub Actions PR runs were green for the authorized task HEAD. Post-merge
  `main` run
  [`30288177659`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30288177659)
  passed every required gate on Python 3.11 and 3.12 for merge commit
  `141915416606abd47831775e677d89c6877643fb`.

## Human Colab evidence

A fresh public-Colab run executed PR code at `80c8015` for levels 4-7,
GeoPackage, repair disabled, and temporary storage. It retained all four source
KML files, generated only `processed/pfaf_level4.gpkg`, and omitted N5, N6, and
N7 with 2, 1, and 2 topology findings respectively. The summary and dynamic
explanation rendered without traceback; one automatic ZIP button downloaded
`nica_geofetch_ineter_pfaf_n4-n7_gpkg_20260726T212025Z.zip`.
The archive contained `raw/`, `processed/`, `LEEME_RESULTADOS.md`, both audit
reports, source manifest, provenance summary, and checksums.

The same run identified five presentation-only defects: singular grammar,
internal format tokens, INFO log noise, premature final status, and combined
topology/attribute headings. All five received focused corrections and
synthetic tests. Final human Colab validation of the corrected experience and
latest-only second-run behavior was completed and approved.

## Current limitations

Levels 5-7 contain 2, 1, and 2 known invalid source geometries respectively.
Their original KML is now retained without repair, but their analytical
derivatives are skipped unless explicit repair succeeds. Python 3.12 was
verified locally; Python 3.11 is configured in CI but was not available in this
desktop environment.

The expected `origin` is configured. GitHub reports
`datanicaragua/nica-geofetch` as public and the authenticated owner as `ADMIN`.
PR #1 was merged into `main` on 2026-07-27 using the authorized merge-commit
method after exact-HEAD, file-scope, mergeability, and CI verification. Local
`main` was synchronized by fast-forward only. The source branch remains
available locally and remotely but is no longer the active project branch. No
direct `main` commit, force push,
auto-merge, branch deletion, tag, or release was performed. Anonymous
HTTP access to the repository, raw notebook, and Colab badge returned 200.
A clean temporary Python environment installed the Colab Git requirement from
public `main`, resolved `c6d5829`, imported the package, and printed `0.1.0`.

## Remaining `v0.1.0` release gates

Human Colab validation and the ChatGPT Project audit/merge recommendation are
complete and no longer block `v0.1.0`. Release readiness is not yet declared.
The remaining gates are:

1. Stable notebook pin decision.
2. Software-only legal and distribution review; institutional data must not be
   included.
3. Release audit.
4. Explicit human authorization for the tag and release.

## Next recommended action

Complete the stable notebook pin decision, software-only legal/distribution
review, and release audit. Then request separate explicit human authorization
before creating any tag or release. Do not create a GitHub release, PyPI
publication, data release, or institutional-data archive under the current
authorization.
