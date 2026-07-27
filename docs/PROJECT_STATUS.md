# Project status

- **Current milestone:** v0.1.0 software-only release preparation; release
  readiness is not yet declared
- **Verified starting branch:** `main`
- **Verified starting and `origin/main` SHA:**
  `483ecb4836126109f90de1796d4bd6c5c5ec01ba`
- **Release-preparation branch:** `release/v0.1.0`
- **Release-preparation implementation commit:**
  `52da0d7f9c36687f73b154b270072d8ecc2d696c`
- **Release-preparation pull request:** draft
  [#3](https://github.com/datanicaragua/nica-geofetch/pull/3), open and
  unmerged
- **PR #2:** merged
- **PR #2 source HEAD:**
  `7d08a244f16bdae704c620ee35fae19b02392390`
- **PR #2 merge commit:**
  `483ecb4836126109f90de1796d4bd6c5c5ec01ba`
- **Verified post-merge CI:** run
  [`30292686085`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30292686085)
  passed for the PR #2 merge commit
- **last_updated_utc:** `2026-07-27T19:18:47Z`

## Implemented MVP-1 capabilities

- One focused provider for INETER Pfafstetter 2025 levels 4-7.
- Secure diagnosis and sequential download with manual local-import fallback.
- Streaming KML validation, attribute and Pfaf-code checks, geometry warnings,
  opt-in repair, provenance, and SHA-256 checksums.
- Verified KML, GeoPackage, GeoJSON, and Shapefile ZIP workflows.
- Audit reports, schema-v3 source manifest, provenance summary, checksum map,
  deterministic packaging, CLI, and public/developer notebooks.
- Explicit separation between Apache-2.0 software and third-party
  institutional data.

## v0.1.0 release-preparation scope

- The public beginner notebook commits `GIT_REF = "v0.1.0"` as the stable
  default, prints the selected Git reference, retains anonymous installation
  and package-ZIP fallback, and contains no credential mechanism.
- English and Spanish landing pages lead with the software/data distinction,
  Colab beginner flow, three numbered actions, stable-tag installation, CLI
  quickstart, bounded downstream examples, limitations, support, and separate
  software/source-data citation guidance.
- `CITATION.cff` and package authorship identify Gustavo Ernesto Martínez
  Cárdenas with DataNicaTools affiliation and no invented contact, ORCID, DOI,
  or release date.
- `CHANGELOG.md` retains an empty `[Unreleased]` section and records the
  completed MVP under `[0.1.0]` without a release date or publication claim.
- Security reporting is actionable while GitHub Private Vulnerability
  Reporting remains disabled; enabling it is a human-owner recommendation.
- The v0.1.0 asset policy allows software materials and GitHub-generated source
  archives, prohibits institutional or runtime data artifacts, and recommends
  no manually uploaded GitHub Release assets.
- The governing 855-line prompt is archived with identical normalized text.

No provider logic, download behavior, validation semantics, repair semantics,
manifest schema, archive structure, output format, developer notebook, or CLI
behavior is changed by release preparation.

## Version and citation consistency

- Package version in `pyproject.toml`: `0.1.0`.
- Runtime version in `src/nica_geofetch/__init__.py`: `0.1.0`.
- Citation version in `CITATION.cff`: `0.1.0`.
- Stable installation and public notebook tag: `v0.1.0`.
- `CITATION.cff` has no premature `date-released`.
- Software and INETER source data require separate citations; generated
  derivatives are not represented as official INETER products.

## Verification status

The clean-baseline smoke test passed Ruff, mypy, 71 offline tests, CLI help,
and all six pre-commit hooks before changes. Release-branch verification then
passed:

- editable `.[dev]` installation;
- `ruff check .`;
- `mypy src` with 17 source files;
- `pytest -q` with 72 passing offline tests;
- both notebooks validated as nbformat v4 through the test suite;
- `python -m nica_geofetch.cli --help`;
- `python scripts/publication_audit.py` after implementation and after build
  cleanup, with 80 candidates and no institutional data, sensitive filename,
  or supported secret signature;
- `pre-commit run --all-files`, all six hooks;
- wheel and sdist build plus Twine checks;
- wheel inspection showing only the package, metadata, `LICENSE`, and `NOTICE`;
- sdist inspection showing the clean software tree, documentation, tests, and
  clearly synthetic fixtures, with no institutional or runtime data;
- clean temporary wheel installation, imported version `0.1.0`, and CLI help;
- removal of the temporary environment and `dist/` before commit.

The preflight independently confirmed:

- clean synchronized `main`;
- expected repository and remote;
- exact required baseline SHA;
- PR #2 merged;
- no `v0.1.0` tag;
- no `v0.1.0` GitHub Release;
- post-merge CI run `30292686085` successful;
- repository description, website, and topics empty;
- GitHub Private Vulnerability Reporting disabled.

## Known limitations

- Levels 5, 6, and 7 contain 2, 1, and 2 known invalid source geometries.
- Original KML is retained. Without repair, analytical derivatives for the
  affected level are omitted; repair is explicit, affects only an analytical
  copy, and is audited.
- No explicit open-data license has been identified for the 2025 institutional
  layers. No institutional data is included in the software release.
- No PyPI package is published for v0.1.0.
- The final fresh-Colab stable-tag validation cannot occur until a separately
  authorized `v0.1.0` tag exists.

## Governance state

Release readiness is not yet declared. Draft release-preparation PR #3 is
open and unmerged. Its GitHub Actions result and independent ChatGPT Project
audit remain pending. Human merge authorization, separate tag authorization,
post-tag fresh-Colab check, and further GitHub Release authorization remain
pending. No data publication is authorized.

This task does not authorize a merge, tag, GitHub Release, PyPI publication,
institutional-data publication, repository-setting change, force push, or
branch deletion.

## Repository metadata recommendations

The repository description, website, and topics were empty at preflight.
Recommended human-owner settings:

- Description: Reproducible acquisition, validation, provenance, and
  preparation of INETER Pfafstetter hydrographic units for Nicaragua.
- Topics: `nicaragua`, `geospatial`, `hydrology`, `pfafstetter`, `ineter`,
  `data-provenance`, `data-engineering`, `python`.
- Website: the public NicaGeoFetch Colab notebook.

These settings are recommendations only and were not applied.

## Next recommended action

Wait for green CI on draft PR #3, add final branch/CI evidence, and submit the
open PR and evidence to ChatGPT Project for independent audit. Do not merge,
tag, publish, or change repository settings under the current authorization.
