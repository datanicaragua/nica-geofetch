# Project status

- **Current milestone:** MVP-1 public repository activation and Colab bootstrap
  correction (local changes complete; push/CI/visibility pending)
- **Current branch:** `main`
- **Latest stable commit:** `d4cd9d4` - `feat: close MVP-1 context and data lineage`
- **last_updated_utc:** `2026-07-25T15:29:59Z`

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

## Test status

- Editable installation: passed in the local Python 3.12 virtual environment.
- Seed audit: passed for four KML files and one PDF.
- Level 4 real offline workflow: passed all conversions and reopen checks.
- PDF rights statement: text-extracted and visually verified.
- `ruff check .`: passed.
- `mypy src`: passed (17 source files).
- `pytest -q`: passed (49 offline tests).
- `python -m nica_geofetch.cli --help`: passed.
- Both notebooks: valid nbformat v4 and smoke assertions passed.
- Fresh-Colab bootstrap simulation: passed without `pyproject.toml`.
- Four configured INETER URLs: semantically equivalent to manually verified URLs.
- Opt-in live level 4 test: passed with 12 polygon features; temporary data removed.
- Publication audit: passed with no forbidden institutional data or supported
  secret signature.
- Registry/source-relationship, metadata-origin, checksum-lineage, legacy
  manifest-field, documentation-link, and unchanged-notebook assertions passed.
- GitHub/private-access, authentication, missing-Git, pip-failure, post-install
  import, ZIP fallback, and public-notebook cell-order simulations passed.
- `pre-commit run --all-files`: passed all six hooks.

## Current limitations

Levels 5-7 contain 2, 1, and 2 invalid source geometries respectively and
require the user's explicit `--repair` decision for conversion. Python 3.12
was verified locally; Python 3.11 is configured in CI but was not available in
this desktop environment.

The expected `origin` is configured and `main` matched `origin/main` before
this task. GitHub reports the repository as private and the authenticated owner
as `ADMIN`. The previous CI run for `76141b6` passed, but the new publication
commit and its CI run are still pending.

## Blocked items

- GitHub Actions must pass for the new pushed HEAD.
- A real fresh-Colab run from the public badge is pending.
- Public visibility is authorized by the active prompt only after every
  automated gate passes.
- Institutional redistribution terms remain unclarified; no source data may be
  attached to a software release.

## Next recommended action

Commit and push only the verified publication/Colab changes to the existing
`origin/main`, wait for GitHub Actions on that HEAD, and change the existing
repository to public only if every gate in `docs/PUBLICATION_CHECKLIST.md`
passes. Do not tag or release `v0.1.0`; the interactive public-Colab test
remains a human gate.
