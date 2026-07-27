# Project status

- **Current milestone:** MVP-1 and the software-only v0.1.0 release are
  complete; the project is in post-release observation.
- **Released `main` commit:**
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- **Release closeout branch:** `chore/v0.1.0-post-release-closeout`.
- **last_updated_utc:** `2026-07-27T22:01:23Z`.

## v0.1.0 release record

- Release-preparation PR
  [#3](https://github.com/datanicaragua/nica-geofetch/pull/3) merged with a
  merge commit at
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- The annotated tag `v0.1.0` has tag object
  `37ccc3b6f37cc5a49d23af1ff5f467303c49b034` and peels to
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- The public
  [GitHub Release](https://github.com/datanicaragua/nica-geofetch/releases/tag/v0.1.0)
  was published at `2026-07-27T20:59:24Z`.
- The Release is public, non-draft, and not a prerelease. It has zero manually
  uploaded assets; only GitHub-generated source archives are available.
- Fresh tag-pinned Colab validation passed with installed version `0.1.0`,
  levels N4-N7, GeoPackage, and repair disabled. All original KML files were
  retained; the N4 analytical GeoPackage was generated; N5-N7 analytical
  outputs were omitted with the expected 2, 1, and 2 topology findings.
- The repository description, eight approved topics, and public-Colab website
  are configured. GitHub Private Vulnerability Reporting is enabled.
- No PyPI package or institutional dataset was published.

The `v0.1.0` tag and its Release are immutable by project policy. They must not
be moved, replaced, or republished. A corrective software release requires a
new version, such as `v0.1.1`. This policy does not claim that a GitHub release
immutability feature retroactively protects v0.1.0.

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

## Verification status

- Post-merge GitHub Actions run
  [`30301899149`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30301899149)
  passed every required job on Python 3.11 and 3.12.
- Ruff passed.
- Mypy passed for 17 source files.
- The offline suite passed with 72 tests.
- CLI help passed.
- All six pre-commit hooks passed.
- The final publication audit inspected 80 candidates and found no prohibited
  institutional data, sensitive filename, or supported secret signature.
- The post-release closeout audit inspected 81 candidates, including the new
  Dependabot configuration, with the same clean result.

## Post-release branch hygiene

The historical branches `release/v0.1.0`,
`docs/mvp1-pr1-merge-continuity`, and
`fix/mvp1-colab-output-clarity-v0.3` were verified locally and remotely at
their expected heads. Each was an ancestor of `main`, had zero commits ahead,
and was associated only with a merged PR. Their local and remote branch refs
were then deleted normally. PR history, merge commits, the tag, and the Release
remain available.

## Known limitations and deferred work

- Levels 5, 6, and 7 contain 2, 1, and 2 known invalid source geometries.
- Original KML is retained. Without repair, analytical derivatives for an
  affected level are omitted; repair is explicit, affects only an analytical
  copy, and is audited.
- No explicit open-data license has been identified for the 2025 institutional
  layers. License and redistribution clarification with INETER remains a
  priority.
- MVP-2 source clarification, drift checks, diagnostics, and schema hardening
  remain deferred.
- New providers and larger platform components remain subject to the component
  value gate.

## Next recommended action

Review the draft post-release closeout PR from
`chore/v0.1.0-post-release-closeout` and its CI. Do not merge it
automatically.
