# Publication checklist

This checklist is the human-controlled gate for remaining public release
actions. It records completed GitHub publication steps but does not authorize a
push, tag, release, visibility/protection change, or data publication.

## Current gate status

| Gate | Status | Evidence or required action |
|---|---|---|
| Tracked-file audit | Passed on release branch | `python scripts/publication_audit.py` inspected 80 tracked and untracked/non-ignored candidates after build cleanup. |
| Institutional-data exclusion | Passed locally | Only synthetic KML under `tests/fixtures/` is eligible; real KML and converted formats remain ignored. |
| Secret scan | Passed locally | The publication audit found no supported private-key, GitHub, AWS, Google, or Slack token signature and no sensitive filename. A host-side scanner may be added before visibility changes. |
| Remote identity | Passed | Existing `origin` is exactly `https://github.com/datanicaragua/nica-geofetch.git`; it was not replaced. |
| GitHub authorization | Passed | Authenticated account `gustavoemc` has `ADMIN` permission; the prompt authorized the completed conditional visibility change. |
| CI baseline | Passed on merged `main` | Independently verified post-PR-#2 run [`30292686085`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30292686085) passed for merge commit `483ecb4836126109f90de1796d4bd6c5c5ec01ba`. |
| Live download evidence | Passed locally | On 2026-07-25 at `17:18:29Z`, the opt-in script downloaded only level 4, validated 12 Placemarks and 12 polygon geometries, recorded `validation_status=valid`, and removed its temporary output. |
| Fresh Colab execution | Passed / human approved | Human validation completed and approved the N4-N7 source-retention flow, corrected beginner messages, final-status ordering, separate warning categories, and latest-only second-run behavior. |
| Source retention and delivery UX | Passed / human approved | Human evidence confirmed source retention, per-level analytical omission, one automatic ZIP, archive structure, `LEEME_RESULTADOS.md`, and the five focused presentation corrections. Seventy-one offline tests retain automated coverage. |
| Pull request history | Passed / merged | PR [#1](https://github.com/datanicaragua/nica-geofetch/pull/1) merged at `1419154`; PR [#2](https://github.com/datanicaragua/nica-geofetch/pull/2) merged from source HEAD `7d08a244f16bdae704c620ee35fae19b02392390` into `483ecb4836126109f90de1796d4bd6c5c5ec01ba`. |
| README review | Passed locally | Both READMEs contain the Colab badge, public/developer distinction, legal warning, professional authorship, and discreet AI-development link. |
| Public notebook credential review | Passed locally | No token, credential prompt, or private-access mechanism is present; private testing uses package ZIP/wheel upload. |
| Context and lineage review | Passed locally | Strategic role, component value gate, metadata origins, source relationships, registry status, and the indexed INETER case study are documented; manifest schema v3 is covered by offline tests. |
| Legal notice review | Passed locally with limitation | Apache-2.0/software and third-party data terms are separated. No explicit open-data license was identified; institutional clarification remains recommended before redistributing data. |
| Public URL verification | Passed | Repository, raw public notebook, and Colab badge each returned HTTP 200 anonymously. |
| Public visibility gate | Passed | Existing `datanicaragua/nica-geofetch` changed from private to public after every automated gate passed. |
| Security reporting | Actionable; owner recommendation pending | Private vulnerability reporting was verified disabled through the GitHub API. `SECURITY.md` instructs reporters to request a private channel without disclosing details; enabling the GitHub setting remains a human-owner recommendation. |
| Build and clean-wheel audit | Passed locally | Wheel and sdist built and passed Twine checks; contents were inspected; a clean temporary environment installed the wheel, printed `0.1.0`, and passed CLI help; generated artifacts were removed. |
| v0.1.0 release gate | **Pending — readiness not declared** | The stable notebook pin and software-only policy are prepared on `release/v0.1.0`. Independent PR audit, human merge authorization, separate tag authorization, post-tag fresh-Colab validation, and separate GitHub Release authorization remain pending. |

## Release-preparation baseline

- Repository: `datanicaragua/nica-geofetch`.
- Verified starting branch: `main`.
- Verified starting and `origin/main` SHA:
  `483ecb4836126109f90de1796d4bd6c5c5ec01ba`.
- PR #2: merged.
- PR #2 source HEAD:
  `7d08a244f16bdae704c620ee35fae19b02392390`.
- PR #2 merge commit:
  `483ecb4836126109f90de1796d4bd6c5c5ec01ba`.
- Verified post-merge CI:
  [`30292686085`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30292686085).
- Release-preparation branch: `release/v0.1.0`.
- Release-preparation implementation commit:
  `52da0d7f9c36687f73b154b270072d8ecc2d696c`.
- Release-preparation PR: draft
  [#3](https://github.com/datanicaragua/nica-geofetch/pull/3), open and
  unmerged.
- No `v0.1.0` tag or GitHub Release existed at preflight.

## PR #1 merge evidence

- Authorized PR HEAD:
  `8a9b9a2e6f04e4ad5972f52383e291f4e3f997c1`.
- Merge commit: `141915416606abd47831775e677d89c6877643fb`.
- Merge method: merge commit; source commits `304b8a5`, `80c8015`, and
  `8a9b9a2` remain retained ancestors.
- Post-merge CI:
  [`30288177659`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30288177659),
  passed on Python 3.11 and 3.12.
- Human Colab validation completed and was approved.
- ChatGPT Project audit and merge recommendation completed and were approved.
- The source branch was retained. No tag, release, data publication, or
  repository protection/visibility change accompanied the merge.

## Remaining release gates

Release readiness is not yet declared. Before any release:

1. Complete the release-preparation PR and independent ChatGPT Project audit.
2. Obtain explicit human authorization to merge the PR.
3. Obtain separate explicit human authorization to create `v0.1.0`.
4. Repeat the fresh-Colab stable-tag validation after the tag exists.
5. Obtain further explicit human authorization before creating a GitHub
   Release.

No data publication is authorized.

## v0.1.0 release-asset policy

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
- institutional PDF or image material;
- Colab outputs containing institutional data;
- download caches;
- audit files containing feature coordinates or bulk attributes;
- credentials, proxy details, or private paths.

**Recommended v0.1.0 policy:** do not manually upload GitHub Release assets.
Use only GitHub-generated source archives. Apache-2.0 applies to the software,
not to institutional data.

## Reproduce the local publication audit

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
python scripts\publication_audit.py
git status --short --branch
git ls-files
```

Review every listed file. Do not waive a finding by adding institutional data
to an allowlist.

## Single-level live test

This test is opt-in, downloads only level 4, uses the provider's polite and
bounded network settings, and deletes temporary data:

```powershell
$env:RUN_INETER_LIVE_TEST = "1"
python scripts\run_live_integration_test.py
Remove-Item Env:RUN_INETER_LIVE_TEST
```

Never enable this variable in CI.

## Human-controlled four-level live workflow

The following command is documented for a human maintainer to run deliberately;
it must not be scheduled or placed in CI. Levels 5-7 have known invalid source
geometries, so `--repair` is explicit and every repair must be reviewed in
`audit_report.json` before any downstream use.

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
nica-geofetch diagnose --provider ineter-pfafstetter --level 4
nica-geofetch download `
  --provider ineter-pfafstetter `
  --levels 4 5 6 7 `
  --formats kml gpkg geojson shapefile `
  --output .\outputs\human-controlled-live `
  --repair
```

The output directory is intentionally ignored. Do not commit, upload, mirror,
or attach its institutional data to a public release.

## Historical post-visibility public Colab gate

After changing repository visibility:

1. Open the README badge in an incognito browser.
2. Start a new Colab runtime with no repository checkout.
3. Confirm the configured bootstrap completes from
   `https://github.com/datanicaragua/nica-geofetch`.
4. Confirm **Run all** does not open the manual KML chooser and that only one
   automatic **Descargar ZIP a mi computadora** button exists.
5. Select N4-N7, GeoPackage, repair disabled. Confirm four KML files in `raw/`,
   only `processed/pfaf_level4.gpkg`, and a clear explanation for omitted
   N5-N7 GeoPackages.
6. Confirm `LEEME_RESULTADOS.md` is accurate and the ZIP filename identifies
   levels, format, and UTC execution time.
7. Confirm the manual fallback is visually subordinate and its separate ZIP
   label cannot be confused with the automatic result.
8. Run a second automatic workflow and confirm it uses a distinct directory
   and only the latest archive remains downloadable.
9. Confirm implementation cells start collapsed/form-like but remain available
   for inspection.
10. Test explicit repair, manual import, Google Drive, and package-ZIP bootstrap
   separately as applicable.
11. The release-facing notebook is now committed with `GIT_REF = "v0.1.0"`.
    Repeat the fresh-Colab bootstrap after the separately authorized tag is
    created.

The earlier human fresh-Colab gate is complete. The stable pin is committed,
but its final fresh-Colab execution remains a post-tag gate and cannot be
completed during release preparation.

## Human evidence at `80c8015`

- Selection: N4-N7, GeoPackage, repair disabled, temporary Colab storage.
- Result: all four KML files retained; `processed/pfaf_level4.gpkg` generated;
  N5, N6, and N7 omitted with 2, 1, and 2 topology findings.
- Delivery: one automatic ZIP button downloaded
  `nica_geofetch_ineter_pfaf_n4-n7_gpkg_20260726T212025Z.zip`.
- Archive: `raw/`, `processed/`, `LEEME_RESULTADOS.md`, `audit_report.json`,
  `audit_report.md`, `source_manifest.json`, `provenance_summary.md`, and
  `checksums_sha256.json` confirmed.
- Presentation defects found: singular grammar, internal format tokens, INFO
  noise, premature final status, and combined warning categories.
- Correction status: all five were corrected with focused tests and final human
  confirmation completed and was approved.

## Completed final micro-fix confirmation

Human validation completed and approved all six points:

1. N6 uses singular and N5/N7 use plural in progress and the results guide.
2. Beginner progress says GeoPackage rather than `gpkg`.
3. Internal INFO record-count lines are absent.
4. Final success appears only after complete summary/archive delivery and the
   automatic ZIP button is enabled.
5. N4 attribute observations are separated from topology findings.
6. A second automatic workflow exposes only its latest downloadable archive.
