# Handoff

- **last_updated_utc:** `2026-07-27T22:15:10Z`

## Post-release closeout record

[PR #4](https://github.com/datanicaragua/nica-geofetch/pull/4) is the
traceable review record for the v0.1.0 continuity updates and conservative
weekly Dependabot version-update proposals for pip and GitHub Actions. It
changes no software, provider, validation, repair, CLI, or notebook behavior.

This static document does not declare PR #4 open or merged. Use live GitHub PR
metadata and CI as the authoritative integration state.

## Verified released state

- Repository: `datanicaragua/nica-geofetch`.
- Released `main` baseline and PR #3 merge commit:
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- PR [#3](https://github.com/datanicaragua/nica-geofetch/pull/3):
  merged.
- PR #3 merge commit:
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- Annotated tag: `v0.1.0`.
- Tag object:
  `37ccc3b6f37cc5a49d23af1ff5f467303c49b034`.
- Peeled tag commit:
  `15edd9b7f181ec791c800f28fdbb48a14958cabc`.
- Public
  [GitHub Release](https://github.com/datanicaragua/nica-geofetch/releases/tag/v0.1.0):
  published at `2026-07-27T20:59:24Z`.
- Release assets: zero manual uploads; GitHub-generated source archives only.
- Fresh tag-pinned Colab validation: PASS.
- Repository metadata: approved description, topics, and public-Colab website
  applied.
- GitHub Private Vulnerability Reporting: enabled.
- PyPI publication: none.
- Institutional-data publication: none.
- Final release publication audit: 80 candidates, with no prohibited data,
  sensitive filename, or supported secret signature.

## Historical branch hygiene

The following local and remote branch heads were checked before deletion:

| Branch | Verified head | Ahead of `main` | Associated PR |
|---|---|---:|---|
| `release/v0.1.0` | `c75024f2db57856e4b60208584e919054e7ae015` | 0 | [#3](https://github.com/datanicaragua/nica-geofetch/pull/3), merged |
| `docs/mvp1-pr1-merge-continuity` | `7d08a244f16bdae704c620ee35fae19b02392390` | 0 | [#2](https://github.com/datanicaragua/nica-geofetch/pull/2), merged |
| `fix/mvp1-colab-output-clarity-v0.3` | `8a9b9a2e6f04e4ad5972f52383e291f4e3f997c1` | 0 | [#1](https://github.com/datanicaragua/nica-geofetch/pull/1), merged |

Every local and remote head was an ancestor of `main`, and no open PR
referenced any of them. All six branch refs were deleted normally. The merged
PRs and their commits remain in repository history.

## Closeout scope

- Update `PROJECT_STATUS.md`, `HANDOFF.md`, `PHASE_LOG.md`,
  `DECISION_LOG.md`, and `PUBLICATION_CHECKLIST.md`.
- Add `.github/dependabot.yml` using version 2 syntax.
- Configure weekly pip and GitHub Actions version-update checks from `/`.
- Limit each ecosystem to five open Dependabot PRs.
- Do not configure auto-merge, reviewers, assignees, or invented labels.

## Closeout validation

- Dependabot YAML syntax passed the pre-commit YAML hook.
- Ruff passed.
- Mypy passed for 17 source files.
- All 72 offline tests passed.
- CLI help passed.
- The publication audit passed with 81 candidates and no prohibited
  institutional data, sensitive filename, or supported secret signature.
- All six pre-commit hooks passed.

## Release immutability policy

Do not modify, move, delete, or replace `v0.1.0` or its GitHub Release. Future
corrections require a new version such as `v0.1.1`. This is a project
governance policy and does not claim retroactive protection from a GitHub
release immutability feature.

## NEXT_ACTION

NEXT_ACTION:
Query the live state of
[PR #4](https://github.com/datanicaragua/nica-geofetch/pull/4).

1. If it is open, verify its exact HEAD and green CI before submitting it for
   final audit or making a human merge decision.
2. If it is merged, verify post-merge CI, fast-forward local `main` to
   `origin/main`, and continue post-release observation.
3. Treat GitHub PR metadata as authoritative; do not infer current PR state
   from this static handoff.

## Resume commands

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
git status --short --branch
git fetch --prune origin
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
python scripts\publication_audit.py
pre-commit run --all-files
```

## Deferred work

- Obtain authoritative INETER licensing, redistribution, attribution, and
  update-cadence clarification.
- Continue MVP-2 hardening and source-drift observation.
- Use a new version for any corrective release.
- Keep providers, services, web applications, mirrors, new formats, and
  generalized architecture outside scope until they pass the component value
  gate.

## Working tree expectation

Start every continuation from a clean working tree and the branch appropriate
to the live PR state. While PR #4 is open, use its existing head branch for
authorized follow-ups. After it is merged, synchronize `main` using
fast-forward only. Any later correction requires a new focused task branch and
PR; do not reuse the closeout branch as a permanent working context.
