# Handoff

- **last_updated_utc:** `2026-07-27T19:11:05Z`

## What is being done

Prepare the software-only Nica-GeoFetch v0.1.0 release candidate on
`release/v0.1.0`, push it normally, and open an unmerged draft pull request for
independent audit. The governing prompt is
`NicaGeoFetch_CodexDesktop_v0.1.0_ReleasePreparation_v0.1`.

## Verified starting state

- Repository: `datanicaragua/nica-geofetch`.
- Starting branch: clean synchronized `main`.
- Starting and `origin/main` SHA:
  `483ecb4836126109f90de1796d4bd6c5c5ec01ba`.
- PR #2: merged.
- PR #2 source HEAD:
  `7d08a244f16bdae704c620ee35fae19b02392390`.
- PR #2 merge commit:
  `483ecb4836126109f90de1796d4bd6c5c5ec01ba`.
- Independently verified post-merge CI:
  [`30292686085`](https://github.com/datanicaragua/nica-geofetch/actions/runs/30292686085).
- No local or fetched `v0.1.0` tag and no GitHub Release existed.
- Repository description, website, and topics were empty.
- GitHub Private Vulnerability Reporting was disabled.

## Completed on the release branch

- Created `release/v0.1.0` only from the verified baseline.
- Pinned the public notebook default to `GIT_REF = "v0.1.0"` with stable-tag,
  advanced-user, anonymous-installation, and no-credential guidance.
- Added focused notebook release-pin assertions while preserving nbformat v4,
  selected-ref installation, and visible ref output.
- Reordered both READMEs for beginner adoption and stable-tag installation.
- Added bounded downstream examples while explicitly retaining the
  foundational-data-only scope.
- Aligned citation and package author metadata without inventing contact data.
- Added changelog, security-reporting, PR-template, and software-only asset
  policy updates.
- Archived the exact 855-line governing prompt with identical normalized text.
- Preserved provider, validation, repair, manifest, archive, format, CLI, and
  developer-notebook behavior.

## Local verification completed

- Editable installation passed.
- Ruff passed.
- Mypy passed for 17 source files.
- Pytest passed with 72 offline tests, including both nbformat-v4 notebook
  validations and focused stable-pin assertions.
- CLI help passed.
- Publication audit passed before and after build cleanup with 80 candidates
  and no forbidden institutional data, sensitive filename, or supported secret
  signature.
- All six pre-commit hooks passed.
- Wheel and sdist built successfully and passed Twine checks.
- The wheel contained only package modules, package metadata, `LICENSE`, and
  `NOTICE`.
- The sdist contained the software tree, documentation, tests, and clearly
  synthetic fixtures; it contained no institutional data, runtime output,
  cache, credential, private path, or Colab-generated archive.
- A clean temporary environment installed the wheel, imported version `0.1.0`,
  and passed CLI help.
- The temporary environment and `dist/` were removed, then the publication
  audit passed again.

## Verification still to complete

- Final diff review.
- Implementation commit and normal push.
- Draft release-preparation PR and GitHub CI.

The committed stable pin must not be weakened for pre-tag validation. Local
execution may use a temporary untracked override or the built wheel. Final
fresh-Colab validation of `v0.1.0` can occur only after a separately authorized
tag is created.

## Release governance

Release readiness is not yet declared. ChatGPT Project audit remains pending.
Merge remains pending human authorization. The tag remains pending separate
human authorization. A GitHub Release remains pending further separate human
authorization. No data publication is authorized.

No merge, tag, GitHub Release, PyPI publication, institutional-data
publication, repository-setting change, force push, or branch deletion is
authorized by this task.

## NEXT_ACTION

NEXT_ACTION:
Review the final diff, commit and push the release branch, open the draft
release-preparation PR, wait for green CI, and submit the open PR and evidence
to ChatGPT Project for independent audit. Do not merge, tag, or publish.

## Resume commands

```powershell
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
git status --short --branch
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
python scripts\publication_audit.py
pre-commit run --all-files
```

## Known risks and deferred items

- INETER endpoint availability, source schema, and institutional terms may
  change.
- No explicit open-data license has been identified.
- Levels 5-7 have 2, 1, and 2 known invalid source geometries.
- Enabling GitHub Private Vulnerability Reporting is a human-owner settings
  recommendation.
- Repository description, topics, and public-Colab website remain
  human-owner settings recommendations.
- Fresh-Colab validation from `v0.1.0` is deferred until the tag exists.
- Providers, services, APIs, web apps, mirrors, new formats, generalized
  plugin architecture, broad refactors, and other non-blocking improvements
  remain out of v0.1.0 scope.

## Working tree expectation

Before the implementation commit, only the intended release-preparation files
may be modified. After each commit and final push, the working tree must be
clean on `release/v0.1.0`.
