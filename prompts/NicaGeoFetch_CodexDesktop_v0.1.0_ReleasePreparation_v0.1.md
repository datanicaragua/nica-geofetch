# NicaGeoFetch_CodexDesktop_v0.1.0_ReleasePreparation_v0.1

## ROLE

Act as the Open Source Release Architect, GeoAI Tech Lead, data-governance reviewer, technical documentation specialist, and release engineer for DataNicaTools / Nica-GeoFetch.

Repository:

https://github.com/datanicaragua/nica-geofetch

Your task is to prepare the software-only release candidate for v0.1.0 on a dedicated branch and open a release pull request.

You are not authorized to merge the pull request, create or push a tag, create a GitHub Release, publish to PyPI, publish institutional data, alter repository visibility, change repository protection or rulesets, delete branches, force push, or commit directly to `main`.

The human owner retains all merge, tag, release, repository-setting, and data-publication decisions.

---

## VERIFIED BASELINE

The required starting point is:

```text
repository: datanicaragua/nica-geofetch
branch: main
exact HEAD: 483ecb4836126109f90de1796d4bd6c5c5ec01ba
PR #1 merge commit: 141915416606abd47831775e677d89c6877643fb
PR #2 source HEAD: 7d08a244f16bdae704c620ee35fae19b02392390
PR #2 merge commit: 483ecb4836126109f90de1796d4bd6c5c5ec01ba
target release: v0.1.0
release branch: release/v0.1.0
```

No `v0.1.0` tag or GitHub Release should exist.

PyPI publication is out of scope.

Institutional-data publication is prohibited.

---

## GOVERNANCE MODEL

* Codex implements on `release/v0.1.0`.
* Codex tests, commits, pushes, and opens the release PR.
* ChatGPT Project audits the PR and evidence.
* The human owner decides whether to merge.
* A separate explicit human authorization is required before any tag.
* A further explicit human authorization is required before publishing the GitHub Release.

Do not bypass this model.

---

## SCOPE FREEZE

Accept only:

* release blockers;
* security or publication problems;
* legal-distribution risks;
* version inconsistencies;
* the stable notebook pin;
* broken links;
* small, verifiable, high-value adoption documentation;
* release notes and release evidence.

Do not add:

* providers;
* institutional sources;
* APIs;
* web applications;
* databases;
* cloud services;
* new output formats;
* public mirrors;
* generalized plugin architecture;
* cognitive architecture;
* automatic catalogs;
* major manifest changes;
* broad refactors.

If an unexpected improvement is not necessary for v0.1.0, record it as deferred and do not implement it.

---

## PHASE 1 — READ-ONLY PREFLIGHT

Before changing any file:

1. Read:

```text
AGENTS.md
CONTRIBUTING.md
README.md
README.es.md
pyproject.toml
CHANGELOG.md
CITATION.cff
LICENSE
DATA_TERMS.md
SECURITY.md
CODE_OF_CONDUCT.md
docs/index.md
docs/ARCHITECTURE.md
docs/ROADMAP.md
docs/LEGAL_AND_ATTRIBUTION.md
docs/PUBLICATION_CHECKLIST.md
docs/PROJECT_STATUS.md
docs/HANDOFF.md
docs/BEGINNER_GUIDE.es.md
notebooks/NicaGeoFetch_Colab.ipynb
.github/workflows/ci.yml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/bug_report.yml
prompts/PROMPT_REGISTRY.md
```

2. Inspect Git and GitHub:

```bash
git status --short --branch
git remote -v
git branch --show-current
git fetch origin --prune
git switch main
git pull --ff-only origin main
git rev-parse HEAD
git log --oneline --decorate -10
git tag --list "v0.1.0"
gh repo view datanicaragua/nica-geofetch
gh pr view 2 --repo datanicaragua/nica-geofetch
gh release view v0.1.0 --repo datanicaragua/nica-geofetch
```

3. Require all of the following:

```text
working tree clean
current branch main
origin/main synchronized
HEAD exactly 483ecb4836126109f90de1796d4bd6c5c5ec01ba
PR #2 merged
no v0.1.0 tag
no v0.1.0 GitHub Release
```

The absence commands may return a non-zero status because the tag or release does not exist. Handle that as expected evidence, not as permission to create either.

If the HEAD differs, the working tree is dirty, the repository is not the expected repository, or a tag/release already exists, stop without making changes and report the discrepancy.

4. Read-only repository-metadata audit:

```bash
gh repo view datanicaragua/nica-geofetch \
  --json nameWithOwner,description,homepageUrl,repositoryTopics,defaultBranchRef
```

Record whether description, website, and topics are present.

Do not change repository settings.

If fields are empty, record this recommended metadata in the PR:

```text
Description:
Reproducible acquisition, validation, provenance, and preparation of INETER Pfafstetter hydrographic units for Nicaragua.

Suggested topics:
nicaragua
geospatial
hydrology
pfafstetter
ineter
data-provenance
data-engineering
python

Suggested website:
the public NicaGeoFetch Colab notebook
```

These are human-owner settings actions and must not be applied by this task.

---

## PHASE 2 — CREATE THE RELEASE BRANCH

Create the release branch only from the verified baseline:

```bash
git switch -c release/v0.1.0
```

Do not reuse an old branch.

Do not commit directly to `main`.

Do not force push.

---

## PHASE 3 — STABLE NOTEBOOK PIN

Update only the public beginner notebook:

```text
notebooks/NicaGeoFetch_Colab.ipynb
```

Required committed default:

```python
GIT_REF = "v0.1.0"
```

Update the adjacent beginner-facing markdown so it no longer says that the default is `main` before the first release.

The notebook must explain that:

* v0.1.0 is the stable default;
* advanced users may deliberately change `GIT_REF`;
* the software is installed from the stable Git tag;
* no GitHub credentials should be entered;
* the data licensing warning remains unchanged.

Do not change:

* provider logic;
* download behavior;
* validation semantics;
* geometry repair semantics;
* manifest schemas;
* archive structure;
* output formats;
* developer notebook behavior;
* CLI behavior.

Add or update focused notebook tests to assert:

* the committed default is exactly `v0.1.0`;
* the printed Git reference is still visible;
* no `main` default remains in release-facing notebook instructions;
* the bootstrap requirement still uses the selected `GIT_REF`;
* the notebook remains valid nbformat v4.

### Pre-tag validation

Because `v0.1.0` does not yet exist, do not weaken the committed stable pin.

For pre-merge execution only, use one of these temporary, untracked methods:

* create a temporary copy of the notebook and replace `v0.1.0` with the exact release-branch HEAD;
* use the existing package ZIP bootstrap;
* install directly from the exact release-branch commit in an isolated smoke environment.

Do not commit the temporary override.

Document that the final fresh-Colab stable-tag validation can occur only after the separately authorized tag is created.

---

## PHASE 4 — ADOPTION DOCUMENTATION

Update both:

```text
README.md
README.es.md
```

Keep the existing Colab badge.

Reorder the landing experience so that the sequence is:

1. one-sentence value proposition;
2. software-versus-data warning;
3. recommended Colab beginner path;
4. three numbered beginner actions;
5. stable-tag local installation;
6. technical CLI quickstart;
7. fallback and advanced information;
8. limitations, documentation, support, citation, authorship, and scope.

The three beginner actions should be equivalent to:

```text
1. Open the Colab notebook.
2. Run the numbered cells and select levels/formats.
3. Review the audit summary and download the final ZIP.
```

Do not claim that Nica-GeoFetch performs thematic analyses.

Add two or three carefully bounded downstream examples, such as:

* preparing traceable hydrographic units for watershed-based climate or agricultural analysis;
* supplying auditable basin geometries to risk or water-resource workflows;
* creating reproducible inputs for GIS analysis.

State explicitly that Nica-GeoFetch prepares foundational data and does not perform those downstream analyses.

### Stable installation

Replace the editable development installation in the user-facing README with the stable-tag installation:

```bash
python -m pip install \
  "nica-geofetch @ git+https://github.com/datanicaragua/nica-geofetch.git@v0.1.0"
```

Keep editable `.[dev]` installation only in contributor/developer documentation.

### Support section

Add a concise support section:

* reproducible bugs belong in GitHub Issues;
* reproductions must use synthetic or redacted data;
* do not upload institutional datasets, credentials, proxy details, or private paths;
* security vulnerabilities must follow `SECURITY.md`;
* questions about INETER data rights must be directed to the source institution;
* maintenance response times are not guaranteed.

Do not create a separate `SUPPORT.md` in this release.

### Citation section

Add a concise citation section linking to `CITATION.cff`.

State that users should cite:

1. Nica-GeoFetch as software; and
2. INETER as the source institution for the hydrographic data.

Do not represent Nica-GeoFetch derivatives as official INETER products.

---

## PHASE 5 — VERSION AND CITATION CONSISTENCY

Audit every release-facing version occurrence.

Required software version:

```text
0.1.0
```

Required tag:

```text
v0.1.0
```

At minimum, verify:

```text
pyproject.toml
src/nica_geofetch/__init__.py
CITATION.cff
CHANGELOG.md
notebooks/NicaGeoFetch_Colab.ipynb
README.md
README.es.md
docs/*
```

### CITATION.cff

Correct `CITATION.cff`:

* retain `cff-version: 1.2.0`;
* retain `type: software`;
* retain `version: 0.1.0`;
* remove the premature `date-released` field;
* do not invent a release date;
* identify the human project architect and author accurately;
* do not invent an ORCID or email;
* retain DataNicaTools affiliation;
* clarify in the message that software and institutional source data require separate citations.

Use this author structure unless a more authoritative existing repository record contradicts it:

```yaml
authors:
  - family-names: "Martínez Cárdenas"
    given-names: "Gustavo Ernesto"
    affiliation: "DataNicaTools"
```

Do not add an unverified DOI.

### pyproject.toml

Do not change the package version.

Evaluate whether the package author metadata can be aligned with the verified README/CITATION authorship using names only. Make the smallest consistent change; do not invent contact data.

---

## PHASE 6 — CHANGELOG AND RELEASE NOTES

Update `CHANGELOG.md` so that:

* a new empty `[Unreleased]` section remains at the top;
* the completed MVP content moves under `[0.1.0]`;
* no release date is invented;
* there are no claims of PyPI publication or data publication;
* known limitations remain visible.

Prepare the GitHub Release notes in the release PR body or a clearly identified PR evidence comment.

Use the approved structure:

```text
Nica-GeoFetch v0.1.0 — Initial Public Software Release
Highlights
Known data-quality limitations
Installation from stable Git tag
Verification
Software and data licensing
Scope
```

The notes must state:

* N5 has 2 known invalid geometries;
* N6 has 1;
* N7 has 2;
* original KML is retained;
* analytical derivatives are omitted without repair;
* repair is explicit and auditable;
* no PyPI package is published;
* no institutional data is included in the release.

Do not create a GitHub Release.

---

## PHASE 7 — SECURITY REPORTING

Retain the existing threat model.

Make `SECURITY.md` reporting instructions actionable.

First verify, read-only, whether GitHub private vulnerability reporting is enabled.

Do not enable or disable repository settings.

If private vulnerability reporting is enabled:

* link the policy to the repository’s private vulnerability-reporting workflow.

If it is not enabled:

* do not invent an email address;
* state that a reporter should open a public issue requesting a private contact channel without including vulnerability details;
* record enabling GitHub private vulnerability reporting as a human-owner recommendation.

If a concrete verified project security contact already exists in repository documentation, it may be used. Do not infer or invent one.

Optionally align the final two lines of `CODE_OF_CONDUCT.md` to the same verified private-contact process, but do not replace the current proportional code of conduct.

---

## PHASE 8 — PR TEMPLATE

Update:

```text
.github/pull_request_template.md
```

Add these checks:

```text
- [ ] `python scripts/publication_audit.py`
- [ ] `pre-commit run --all-files`
- [ ] wheel and sdist contents inspected
- [ ] clean-wheel installation smoke passed when release-facing packaging changed
- [ ] no tag, release, PyPI publication, repository-setting change, or institutional-data publication performed
```

Do not add a feature-request template.

Do not add `.github/release.yml`.

Do not add a new issue-template system.

---

## PHASE 9 — LEGAL AND RELEASE-ASSET POLICY

Update `docs/PUBLICATION_CHECKLIST.md` with an explicit v0.1.0 asset policy.

Allowed:

```text
source code
documentation
configuration
tests
clearly synthetic fixtures
LICENSE
CITATION.cff
CHANGELOG
GitHub-generated source archives
```

Prohibited:

```text
institutional KML or KMZ
institutional GeoPackage
institutional GeoJSON
institutional Shapefile components
runtime-generated ZIP files
institutional PDF or image material
Colab outputs containing institutional data
download caches
audit files containing feature coordinates or bulk attributes
credentials, proxy details, or private paths
```

Recommended release policy:

```text
No manually uploaded GitHub Release assets for v0.1.0.
Use only GitHub-generated source archives.
```

Do not broaden Apache-2.0 to cover institutional data.

Do not call INETER data open data.

Do not change the existing attribution wording unless required for consistency.

---

## PHASE 10 — CONTINUITY CORRECTION

Update:

```text
docs/PROJECT_STATUS.md
docs/HANDOFF.md
docs/PHASE_LOG.md
docs/PUBLICATION_CHECKLIST.md
prompts/PROMPT_REGISTRY.md
```

Correctly record:

```text
current verified baseline before release branch:
483ecb4836126109f90de1796d4bd6c5c5ec01ba

PR #2:
merged

PR #2 source HEAD:
7d08a244f16bdae704c620ee35fae19b02392390

PR #2 merge commit:
483ecb4836126109f90de1796d4bd6c5c5ec01ba
```

Independently verify and record the actual post-merge CI run for `483ecb483...`.

The owner-provided candidate run is:

```text
30292686085
```

Do not copy it blindly. Confirm it through GitHub or `gh`.

Record the publication-audit candidate count produced by this release branch rather than copying an older count.

At the end of the release-preparation task, continuity docs must say:

* release preparation PR is open;
* release readiness is not yet declared;
* ChatGPT Project audit remains pending;
* merge remains pending human authorization;
* tag remains pending separate human authorization;
* GitHub Release remains pending separate human authorization;
* no data publication is authorized.

Do not describe a future PR merge as already completed.

Do not leave self-stale language that becomes false immediately after the release PR is opened.

---

## PHASE 11 — ARCHIVE THIS PROMPT

Save this exact governing prompt as:

```text
prompts/NicaGeoFetch_CodexDesktop_v0.1.0_ReleasePreparation_v0.1.md
```

Update:

```text
prompts/PROMPT_REGISTRY.md
```

Record:

* prompt tag;
* purpose;
* branch;
* verified base SHA;
* scope;
* prohibitions;
* final implementation commit SHA when known;
* release PR number when known.

Preserve the prompt text faithfully.

---

## PHASE 12 — QUALITY AND RELEASE AUDIT

Use the existing environment when valid.

Run:

```bash
python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
python scripts/publication_audit.py
pre-commit run --all-files
```

Validate both notebooks with the existing notebook tests.

### Build audit

Install build tooling only for local audit if necessary:

```bash
python -m pip install build twine
python -m build
python -m twine check dist/*
```

Inspect wheel contents:

```bash
python -m zipfile -l dist/*.whl
```

Inspect sdist contents using the appropriate local archive command.

Confirm that wheel and sdist contain only software-package materials expected from the clean tracked tree.

They must not contain:

* institutional data;
* runtime outputs;
* seed inputs;
* temporary directories;
* credentials;
* local paths;
* Colab-generated archives.

Create a clean temporary environment and install the wheel:

```bash
python -m venv <temporary-clean-env>
<temporary-clean-env-python> -m pip install dist/*.whl
<temporary-clean-env-python> -c "import nica_geofetch; print(nica_geofetch.__version__)"
<temporary-clean-env-python> -m nica_geofetch.cli --help
```

Require the printed version to be:

```text
0.1.0
```

Do not upload the wheel or sdist.

Delete `dist/` and other generated build outputs before the final commit or ensure they remain ignored and untracked.

Run the publication audit again after cleanup.

Finally require:

```bash
git status --short
```

to show only the intended tracked release-preparation changes before commit, and a clean tree after commit.

Do not run unrestricted automated downloads of levels 5–7.

Do not add live institutional downloads to CI.

---

## PHASE 13 — REVIEW THE DIFF

Before committing, inspect:

```bash
git diff --check
git diff --stat
git diff
git status --short
```

Confirm the diff contains only:

* stable notebook pin and its focused tests;
* adoption/release documentation;
* version/citation consistency;
* security-reporting clarification;
* PR template gate additions;
* legal release-asset policy;
* continuity updates;
* prompt archive and registry entry.

If package business logic, provider logic, validation logic, repair behavior, manifest schema, or data handling changed unexpectedly, stop and revert those changes.

---

## PHASE 14 — COMMIT AND PUSH

Use one coherent release-preparation commit unless a second focused correction is necessary.

Suggested commit message:

```text
chore: prepare Nica-GeoFetch v0.1.0 release
```

Push normally:

```bash
git push -u origin release/v0.1.0
```

Do not force push.

Do not delete any retained branch.

Do not push a tag.

---

## PHASE 15 — OPEN THE RELEASE PR

Open a draft pull request:

```text
base: main
head: release/v0.1.0
title: chore: prepare Nica-GeoFetch v0.1.0 release
```

The PR body must include:

```text
## Purpose
## Scope freeze
## Stable notebook pin
## Adoption documentation
## Version and citation audit
## Software-only legal review
## Release-asset allowlist
## Release notes
## Automated verification
## Build and clean-wheel verification
## Publication audit
## Files changed
## Deferred items
## Human decisions still required
## Prohibited actions confirmed
## Governing prompt
```

Include exact evidence:

* base SHA;
* branch HEAD;
* test count;
* Ruff result;
* mypy result;
* pre-commit result;
* CLI smoke result;
* publication-audit candidate count;
* wheel/sdist inspection result;
* clean-wheel installed version;
* CI URLs once available.

Explicitly state:

```text
This PR does not authorize or perform its own merge.
This PR does not create or push v0.1.0.
This PR does not create a GitHub Release.
This PR does not publish to PyPI.
This PR does not publish institutional data.
This PR does not alter repository visibility, protection, rulesets, topics, description, or website.
```

Wait for GitHub Actions.

If CI fails, diagnose and correct only release-preparation defects on the same branch using normal follow-up commits.

Do not amend shared commits.

Do not force push.

When all checks are green, the PR may be marked ready for review, but it must remain unmerged.

Add a concise evidence comment containing the final branch HEAD and CI URLs.

---

## PHASE 16 — FINAL RESPONSE

Return a concise final report containing:

1. verified starting SHA;
2. release branch;
3. implementation commit SHA;
4. pull request URL and number;
5. files changed;
6. stable notebook pin;
7. version-consistency result;
8. build-audit result;
9. publication-audit candidate count;
10. test and CI results;
11. release notes location;
12. deferred items;
13. repository metadata recommendations;
14. explicit confirmation that no merge, tag, GitHub Release, PyPI publication, data publication, repository-setting change, force push, or branch deletion occurred.

End with exactly:

```text
NEXT HUMAN DECISION:
Submit the open release-preparation PR and its evidence to ChatGPT Project for independent audit. Do not merge, tag, or publish a GitHub Release until the corresponding separate human authorizations are given.
```
