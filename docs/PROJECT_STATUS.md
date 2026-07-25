# Project status

- **Current milestone:** MVP-1 Colab source-retention, delivery, and beginner UX
  correction (implementation complete; human public-Colab retest pending)
- **Current branch:** `main`
- **Latest stable commit:** `0be8580` - `fix: retain source KML through topology warnings`
- **last_updated_utc:** `2026-07-25T17:30:07Z`

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

## Test status

- Editable installation: passed in the local Python 3.12 virtual environment.
- Seed audit: passed for four KML files and one PDF.
- Level 4 real offline workflow: passed all conversions and reopen checks.
- PDF rights statement: text-extracted and visually verified.
- `ruff check .`: passed.
- `mypy src`: passed (17 source files).
- `pytest -q`: passed (58 offline tests).
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
- `pre-commit run --all-files`: passed all six hooks.

## Current limitations

Levels 5-7 contain 2, 1, and 2 known invalid source geometries respectively.
Their original KML is now retained without repair, but their analytical
derivatives are skipped unless explicit repair succeeds. Python 3.12 was
verified locally; Python 3.11 is configured in CI but was not available in this
desktop environment.

The expected `origin` is configured. GitHub reports
`datanicaragua/nica-geofetch` as public and the authenticated owner as `ADMIN`.
CI run `30167669342` passed on implementation commit `0be8580` for Python 3.11
and 3.12, including every required project gate. Anonymous
HTTP access to the repository, raw notebook, and Colab badge returned 200.
A clean temporary Python environment installed the Colab Git requirement from
public `main`, resolved `c6d5829`, imported the package, and printed `0.1.0`.

## Blocked items

- Human public-Colab retesting of the new N4+N5 warning flow, all-level
  selection, explicit repair, immediate ZIP button, repeated execution, and
  optional manual import remains pending.
- Institutional redistribution terms remain unclarified; no source data may be
  attached to a software release.
- `v0.1.0` remains blocked until the human Colab workflow is accepted.

## Next recommended action

Open the public README badge in a fresh anonymous Colab runtime. Test N4+N5
without repair, all levels, explicit repair, the immediate ZIP button, a second
clean run, and the optional manual-import button. Record results in
`docs/PUBLICATION_CHECKLIST.md`. Do not tag or release `v0.1.0` until that human
gate passes.
