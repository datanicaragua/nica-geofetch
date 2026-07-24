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
| CI status | **Pending / blocker** | Workflow is configured for Python 3.11 and 3.12, but no public remote exists and GitHub Actions has not run. |
| Live download evidence | Passed locally | On 2026-07-24, the opt-in script downloaded only level 4, validated 12 polygon features, and removed its temporary output. |
| Fresh Colab execution | **Partially passed / blocker** | Automated bootstrap simulation passes from a directory without `pyproject.toml`. A real fresh-Colab run from the public URL remains impossible until the repository is visible. |
| README review | Passed locally | English and Spanish READMEs contain the required Colab badge, public/developer distinction, and data-term warning. |
| Legal notice review | Passed locally with limitation | Apache-2.0/software and third-party data terms are separated. No explicit open-data license was identified; institutional clarification remains recommended before redistributing data. |
| Public visibility gate | **Pending / blocker** | A human owner must review this checklist and explicitly authorize repository creation/visibility. This task did not do so. |
| v0.1.0 release gate | **Pending / blocker** | Requires passing GitHub CI, a real fresh-Colab run, stable-tag pin review, public visibility approval, and final release-note/legal review. |

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

## Public Colab gate

Before changing repository visibility:

1. Open the README badge in an incognito browser.
2. Start a new Colab runtime with no repository checkout.
3. Confirm the default `main` bootstrap completes from
   `https://github.com/datanicaragua/nica-geofetch`.
4. Run the diagnosis and a level 4 workflow.
5. Test the package-ZIP fallback separately.
6. Before v0.1.0, change the release-facing notebook ref from `main` to the
   stable tag and repeat the run.

Record the date, Git ref, Python version, result, and any warning here before
marking the fresh-Colab or v0.1.0 gates complete.
