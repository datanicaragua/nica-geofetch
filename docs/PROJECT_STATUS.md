# Project status

- **Current milestone:** MVP-1 context, provenance, and public-release closeout
  (locally complete; publication gated)
- **Current branch:** `main`
- **Latest stable commit:** `d4cd9d4` - `feat: close MVP-1 context and data lineage`
- **Last update:** 2026-07-25T14:09:20Z

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

## Test status

- Editable installation: passed in the local Python 3.12 virtual environment.
- Seed audit: passed for four KML files and one PDF.
- Level 4 real offline workflow: passed all conversions and reopen checks.
- PDF rights statement: text-extracted and visually verified.
- `ruff check .`: passed.
- `mypy src`: passed (17 source files).
- `pytest -q`: passed (40 offline tests).
- `python -m nica_geofetch.cli --help`: passed.
- Both notebooks: valid nbformat v4 and smoke assertions passed.
- Fresh-Colab bootstrap simulation: passed without `pyproject.toml`.
- Four configured INETER URLs: semantically equivalent to manually verified URLs.
- Opt-in live level 4 test: passed with 12 polygon features; temporary data removed.
- Publication audit: passed with no forbidden institutional data or supported
  secret signature.
- Registry/source-relationship, metadata-origin, checksum-lineage, legacy
  manifest-field, documentation-link, and unchanged-notebook assertions passed.
- `pre-commit run --all-files`: passed all six hooks.

## Current limitations

Levels 5-7 contain 2, 1, and 2 invalid source geometries respectively and
require the user's explicit `--repair` decision for conversion. Python 3.12
was verified locally; Python 3.11 is configured in CI but was not available in
this desktop environment.

The target GitHub repository is not configured as a remote or public here.
Therefore the real badge URL, GitHub CI, and end-to-end fresh-Colab install
cannot yet be verified. The public notebook no longer fails before bootstrap,
but its default GitHub installation depends on future repository visibility.

## Blocked items

- GitHub Actions has not run on a public remote.
- A real fresh-Colab run from the public badge is pending.
- Public visibility and v0.1.0 release require explicit human authorization.
- Institutional redistribution terms remain unclarified; no source data may be
  attached to a software release.

## Next recommended action

The next action is GitHub publication under explicit human control: review
`docs/PUBLICATION_CHECKLIST.md`, authorize repository creation/visibility and
the initial push separately, publish only the software tree to
`datanicaragua/nica-geofetch`, then run GitHub CI and the real fresh-Colab gate.
Do not tag or release `v0.1.0` until those gates and the legal review pass.
