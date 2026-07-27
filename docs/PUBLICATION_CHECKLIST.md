# Publication checklist

This document records the completed software-only v0.1.0 publication and the
rules that remain in force after release. It does not authorize moving or
replacing the released tag, publishing institutional data, or publishing to
PyPI.

## v0.1.0 final gate status

| Gate | Status | Evidence |
|---|---|---|
| Release PR | Passed | [PR #3](https://github.com/datanicaragua/nica-geofetch/pull/3) merged at `15edd9b7f181ec791c800f28fdbb48a14958cabc`. |
| Post-merge CI | Passed | [Run 30301899149](https://github.com/datanicaragua/nica-geofetch/actions/runs/30301899149) passed Python 3.11 and 3.12. |
| Version and citation | Passed | Package, runtime, citation, stable installation, and notebook pin use `0.1.0` / `v0.1.0`. |
| Annotated tag | Passed | `v0.1.0` object `37ccc3b6f37cc5a49d23af1ff5f467303c49b034` peels to `15edd9b7f181ec791c800f28fdbb48a14958cabc`. |
| Fresh tag-pinned Colab | Passed / human approved | Installed `0.1.0`; N4-N7 GeoPackage repair-off behavior, archive structure, one automatic ZIP, and latest-only second run confirmed. |
| Publication audit | Passed | 80 candidates; no prohibited institutional data, sensitive filename, or supported secret signature. |
| Repository presentation | Passed | Approved description, eight topics, and public-Colab website applied; repository remains public with default branch `main`. |
| Security reporting | Passed | GitHub Private Vulnerability Reporting enabled. |
| GitHub Release | Passed | [v0.1.0](https://github.com/datanicaragua/nica-geofetch/releases/tag/v0.1.0) published at `2026-07-27T20:59:24Z`; public, non-draft, and not a prerelease. |
| Release assets | Passed | Zero manually uploaded assets; GitHub-generated source ZIP and TAR.GZ only. |
| PyPI exclusion | Passed | No PyPI package was published for v0.1.0. |
| Institutional-data exclusion | Passed | No institutional dataset or runtime/Colab output was published. |

## Released identifiers

- Repository: `datanicaragua/nica-geofetch`.
- Released `main` commit:
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- PR #3 source head:
  `c75024f2db57856e4b60208584e919054e7ae015`.
- Tag: `v0.1.0`.
- Annotated tag object:
  `37ccc3b6f37cc5a49d23af1ff5f467303c49b034`.
- Peeled commit:
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- Release:
  `https://github.com/datanicaragua/nica-geofetch/releases/tag/v0.1.0`.
- Tag-pinned Colab:
  `https://colab.research.google.com/github/datanicaragua/nica-geofetch/blob/v0.1.0/notebooks/NicaGeoFetch_Colab.ipynb`.

## Fresh-Colab result

The human-approved run used levels N4-N7, GeoPackage, temporary Colab storage,
and geometry repair disabled.

- All four original institutional KML files were retained in `raw/`.
- `processed/pfaf_level4.gpkg` was generated.
- N5, N6, and N7 analytical GeoPackages were omitted with 2, 1, and 2 known
  topology findings and clear repair-off explanations.
- The final ZIP contained `raw/`, `processed/`, `LEEME_RESULTADOS.md`, both
  audit reports, the source manifest, provenance summary, and checksum map.
- One automatic download was confirmed.
- A second execution exposed only its latest downloadable ZIP.
- No GitHub credential was requested and no unexpected error occurred.

The generated ZIP and institutional contents were validation evidence only.
They were not attached to the PR or Release.

## Release-asset policy

Allowed software-release content:

- source code;
- documentation;
- configuration;
- tests;
- clearly synthetic fixtures;
- `LICENSE`;
- `CITATION.cff`;
- `CHANGELOG.md`;
- GitHub-generated source archives.

Prohibited release content:

- institutional KML or KMZ;
- institutional GeoPackage;
- institutional GeoJSON;
- institutional Shapefile components;
- runtime-generated ZIP files;
- Colab outputs;
- institutional PDF or image material;
- download caches;
- audit files containing feature coordinates or bulk attributes;
- credentials, proxy details, or private paths;
- manually uploaded wheel or sdist files.

Apache-2.0 applies to the software and clearly synthetic fixtures, not to
institutional source data.

## Post-release immutability policy

The `v0.1.0` tag and its GitHub Release must not be moved, deleted, replaced,
or republished. Any corrective change requires a new version, such as
`v0.1.1`. This project policy does not claim that GitHub release immutability
retroactively protects v0.1.0.

## Future-release gates

Every future release must repeat:

1. focused task-branch and PR review;
2. local quality gates and publication audit;
3. green GitHub Actions;
4. explicit human merge authorization;
5. separate explicit tag and publication authorization;
6. source/data licensing and release-asset review;
7. tag-target verification;
8. applicable fresh-Colab validation;
9. final Release and source-archive verification.

Never move an existing released tag to satisfy a later gate.

## Reproduce the local publication audit

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
python scripts\publication_audit.py
git status --short --branch
git ls-files
```

Review every listed file. Do not waive a finding by adding institutional data
to an allowlist.

## Deferred work

- Obtain authoritative INETER licensing, redistribution, attribution, and
  update-cadence clarification.
- Continue MVP-2 hardening and source-drift observation.
- Apply the component value gate before adding providers, formats, services,
  interfaces, mirrors, or generalized architecture.
