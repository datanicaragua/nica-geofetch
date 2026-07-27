# Publication checklist

This checklist is the human-controlled gate for remaining public release
actions. It records completed GitHub publication steps but does not authorize a
push, tag, release, visibility/protection change, or data publication.

## Current gate status

| Gate | Status | Evidence or required action |
|---|---|---|
| Tracked-file audit | Passed locally | `python scripts/publication_audit.py` inspects tracked and untracked/non-ignored candidates. |
| Institutional-data exclusion | Passed locally | Only synthetic KML under `tests/fixtures/` is eligible; real KML and converted formats remain ignored. |
| Secret scan | Passed locally | The publication audit found no supported private-key, GitHub, AWS, Google, or Slack token signature and no sensitive filename. A host-side scanner may be added before visibility changes. |
| Remote identity | Passed | Existing `origin` is exactly `https://github.com/datanicaragua/nica-geofetch.git`; it was not replaced. |
| GitHub authorization | Passed | Authenticated account `gustavoemc` has `ADMIN` permission; the prompt authorized the completed conditional visibility change. |
| CI status | Passed on merged `main` | Post-merge run [`30288177659`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30288177659) passed all gates on Python 3.11 and 3.12 for merge commit `141915416606abd47831775e677d89c6877643fb`. |
| Live download evidence | Passed locally | On 2026-07-25 at `17:18:29Z`, the opt-in script downloaded only level 4, validated 12 Placemarks and 12 polygon geometries, recorded `validation_status=valid`, and removed its temporary output. |
| Fresh Colab execution | Passed / human approved | Human validation completed and approved the N4-N7 source-retention flow, corrected beginner messages, final-status ordering, separate warning categories, and latest-only second-run behavior. |
| Source retention and delivery UX | Passed / human approved | Human evidence confirmed source retention, per-level analytical omission, one automatic ZIP, archive structure, `LEEME_RESULTADOS.md`, and the five focused presentation corrections. Seventy-one offline tests retain automated coverage. |
| Pull request review | Passed / merged | Public PR [#1](https://github.com/datanicaragua/nica-geofetch/pull/1) was merged by the authorized merge-commit method from exact HEAD `8a9b9a2` into merge commit `1419154`; ChatGPT Project audit and merge recommendation were completed and approved, and all preflight/post-merge CI checks passed. |
| README review | Passed locally | Both READMEs contain the Colab badge, public/developer distinction, legal warning, professional authorship, and discreet AI-development link. |
| Public notebook credential review | Passed locally | No token, credential prompt, or private-access mechanism is present; private testing uses package ZIP/wheel upload. |
| Context and lineage review | Passed locally | Strategic role, component value gate, metadata origins, source relationships, registry status, and the indexed INETER case study are documented; manifest schema v3 is covered by offline tests. |
| Legal notice review | Passed locally with limitation | Apache-2.0/software and third-party data terms are separated. No explicit open-data license was identified; institutional clarification remains recommended before redistributing data. |
| Public URL verification | Passed | Repository, raw public notebook, and Colab badge each returned HTTP 200 anonymously. |
| Public visibility gate | Passed | Existing `datanicaragua/nica-geofetch` changed from private to public after every automated gate passed. |
| v0.1.0 release gate | **Pending — readiness not declared** | Human Colab validation and merge review are complete. Remaining gates: stable notebook pin decision, software-only legal/distribution review, release audit, and explicit human tag/release authorization. |

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

Human Colab validation is complete and no longer blocks `v0.1.0`. Release
readiness is not yet declared. Before any tag or release:

1. Decide the stable notebook pin.
2. Complete a software-only legal and distribution review.
3. Complete the release audit.
4. Obtain explicit human authorization for the tag and release.

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

## Post-visibility public Colab gate

After changing repository visibility:

1. Open the README badge in an incognito browser.
2. Start a new Colab runtime with no repository checkout.
3. Confirm the default `main` bootstrap completes from
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
11. Before v0.1.0, change the release-facing notebook ref from `main` to the
   stable tag and repeat the run.

The human fresh-Colab gate is complete. Record the stable notebook pin decision
and repeat the applicable bootstrap check before marking the separate
`v0.1.0` release gate complete.

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
