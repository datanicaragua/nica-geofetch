# Publication checklist

This checklist is the human-controlled gate between a locally hardened MVP and
any public GitHub action. It does not authorize remote creation, push,
visibility changes, or a release.

## Current gate status

| Gate | Status | Evidence or required action |
|---|---|---|
| Tracked-file audit | Passed locally | `python scripts/publication_audit.py` inspects tracked and untracked/non-ignored candidates. |
| Institutional-data exclusion | Passed locally | Only synthetic KML under `tests/fixtures/` is eligible; real KML and converted formats remain ignored. |
| Secret scan | Passed locally | The publication audit found no supported private-key, GitHub, AWS, Google, or Slack token signature and no sensitive filename. A host-side scanner may be added before visibility changes. |
| Remote identity | Passed | Existing `origin` is exactly `https://github.com/datanicaragua/nica-geofetch.git`; it was not replaced. |
| GitHub authorization | Passed | Authenticated account `gustavoemc` has `ADMIN` permission; the prompt authorized the completed conditional visibility change. |
| CI status | Passed | Run `30167669342` passed on source-retention implementation commit `0be8580` for Python 3.11 and 3.12, including installation, Ruff, mypy, 58 tests, CLI help, publication audit, and pre-commit. |
| Live download evidence | Passed locally | On 2026-07-25 at `17:18:29Z`, the opt-in script downloaded only level 4, validated 12 Placemarks and 12 polygon geometries, recorded `validation_status=valid`, and removed its temporary output. |
| Fresh Colab execution | **Partially passed / blocker** | Human public-Colab N4 reached remote download, 12 features, GeoPackage, and a final ZIP. Human N4+N5 exposed the former topology/retention defect. Automated bootstrap, warning-retention, all-level controls, ZIP visibility, and manual-picker tests pass; the corrected public notebook still requires a fresh human retest. |
| Source retention and delivery UX | **Automated pass / human retest pending** | Synthetic N5-like evidence confirms that two topology warnings preserve original bytes, skip derivatives without repair, convert after explicit repair, and do not stop the next level. N4 defaults on, all-level selection resolves to 4-7, `/content` guidance exists, and file upload/download calls are button-triggered. |
| README review | Passed locally | Both READMEs contain the Colab badge, public/developer distinction, legal warning, professional authorship, and discreet AI-development link. |
| Public notebook credential review | Passed locally | No token, credential prompt, or private-access mechanism is present; private testing uses package ZIP/wheel upload. |
| Context and lineage review | Passed locally | Strategic role, component value gate, metadata origins, source relationships, registry status, and the indexed INETER case study are documented; manifest schema v3 is covered by offline tests. |
| Legal notice review | Passed locally with limitation | Apache-2.0/software and third-party data terms are separated. No explicit open-data license was identified; institutional clarification remains recommended before redistributing data. |
| Public URL verification | Passed | Repository, raw public notebook, and Colab badge each returned HTTP 200 anonymously. |
| Public visibility gate | Passed | Existing `datanicaragua/nica-geofetch` changed from private to public after every automated gate passed. |
| v0.1.0 release gate | **Pending / blocker** | Requires green post-push CI, corrected human fresh-Colab retesting, stable-tag pin review, and final release-note/legal review. |

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
4. Run N4+N5 without repair and confirm both original KML files are retained,
   N5 analytical output is skipped, the final ZIP downloads from the primary
   button, and no raw traceback appears.
5. Select all levels and confirm sequential completion plus one summary table
   and one final ZIP.
6. Repeat with explicit repair and review original/repaired checksum and repair
   method evidence.
7. Run a second workflow and confirm it uses a distinct directory and the ZIP
   button points to the latest archive.
8. Test the optional manual-import button and package-ZIP bootstrap fallback
   separately; **Run all** must not open the KML chooser.
9. Before v0.1.0, change the release-facing notebook ref from `main` to the
   stable tag and repeat the run.

Record the date, Git ref, Python version, result, and any warning here before
marking the fresh-Colab or v0.1.0 gates complete.
