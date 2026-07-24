# Project status

- **Current milestone:** MVP-1 public-release hardening (locally complete; publication gated)
- **Current branch:** `main`
- **Latest stable baseline:** `154c25d` - `docs: close MVP-1 execution and handoff`
- **Hardening commit:** pending final quality gates
- **Last update:** 2026-07-24T22:52:48Z

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

## Test status

- Editable installation: passed in the local Python 3.12 virtual environment.
- Seed audit: passed for four KML files and one PDF.
- Level 4 real offline workflow: passed all conversions and reopen checks.
- PDF rights statement: text-extracted and visually verified.
- `ruff check .`: passed.
- `mypy src`: passed (17 source files).
- `pytest -q`: passed (38 offline tests during hardening; final gate rerun pending).
- `python -m nica_geofetch.cli --help`: passed.
- Both notebooks: valid nbformat v4 and smoke assertions passed.
- Fresh-Colab bootstrap simulation: passed without `pyproject.toml`.
- Four configured INETER URLs: semantically equivalent to manually verified URLs.
- Opt-in live level 4 test: passed with 12 polygon features; temporary data removed.
- Publication audit: passed with no forbidden institutional data or supported
  secret signature.
- `pre-commit run --all-files`: pending final staged-file run.

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

Complete the human gates in `docs/PUBLICATION_CHECKLIST.md`: review the staged
files, authorize visibility separately, run GitHub CI, execute the public
notebook in a truly fresh Colab runtime, then pin and verify `v0.1.0`. Do not
push, change visibility, or publish a release without that explicit authority.
