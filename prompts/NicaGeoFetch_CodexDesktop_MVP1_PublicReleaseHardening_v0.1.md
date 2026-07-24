ejecuta prompt NicaGeoFetch_CodexDesktop_MVP1_PublicReleaseHardening_v0.1

Continue work in the existing C:\Dev\nica-geofetch repository.

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_PublicReleaseHardening_v0.1

PURPOSE

Prepare the completed MVP-1 for independent audit, GitHub publication, and
direct beginner use from Google Colab.

This is a focused hardening task. Do not add new providers, a web application,
an API, a database, or new domain datasets.

FIRST READ

Read in this order:

1. AGENTS.md
2. docs/index.md
3. docs/PROJECT_STATUS.md
4. docs/HANDOFF.md
5. docs/ROADMAP.md
6. docs/SEED_AUDIT.md
7. prompts/PROMPT_REGISTRY.md

Then inspect git status, the current branch, and recent commits.

REQUIRED CORRECTIONS

1. Split the current notebook workflow into:

   a. notebooks/NicaGeoFetch_Colab.ipynb
      - public beginner notebook;
      - must work when opened alone in a fresh Colab runtime;
      - must not require pyproject.toml to exist before bootstrap;
      - install the package from:
        https://github.com/datanicaragua/nica-geofetch
      - allow a configurable Git ref;
      - default to main before the first release;
      - document that releases should pin a stable tag;
      - include a manual package ZIP upload fallback;
      - provide Spanish beginner guidance;
      - use package APIs rather than duplicated business logic.

   b. notebooks/NicaGeoFetch_Developer.ipynb
      - repository-local development workflow;
      - may require pyproject.toml;
      - use editable installation;
      - clearly label it as developer-only.

2. Add a fresh-Colab bootstrap test that starts from a directory without
   pyproject.toml and verifies that the public notebook does not immediately
   raise FileNotFoundError.

3. Add an “Open in Colab” badge to README.md and README.es.md using:

   https://colab.research.google.com/github/datanicaragua/nica-geofetch/blob/main/notebooks/NicaGeoFetch_Colab.ipynb

4. Verify that provider configuration programmatically generates URLs
   semantically equivalent to the four manually verified INETER KML URLs.

5. Ensure every download report distinguishes:

   - remote_download;
   - manual_import;
   - seed_input.

6. Ensure remote-download manifests include:

   - source_url;
   - source_layer;
   - retrieval_mode;
   - retrieved_at_utc;
   - response content type;
   - byte size;
   - SHA-256;
   - validation status;
   - Placemark count;
   - geometry count.

7. Run a polite live download test for only one level when
   RUN_INETER_LIVE_TEST=1.

8. Provide a documented command for a human-controlled live download of
   levels 4, 5, 6, and 7.

9. Create docs/PUBLICATION_CHECKLIST.md containing:

   - tracked-file audit;
   - institutional-data exclusion;
   - secret scan;
   - CI status;
   - live download evidence;
   - fresh Colab execution;
   - README review;
   - legal notice review;
   - public visibility gate;
   - v0.1.0 release gate.

10. Do not create a remote, push, change repository visibility, or publish a
    release.

QUALITY GATES

Run:

python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest -q
pre-commit run --all-files

Validate both notebooks with nbformat and the existing notebook smoke
framework.

Update:

- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- prompts/PROMPT_REGISTRY.md
- CHANGELOG.md

Create a logical local commit only after all applicable checks pass.

FINAL REPORT

Report:

- exact files changed;
- public vs developer notebook behavior;
- fresh-Colab test result;
- URL-equivalence test result;
- live-test result or reason not run;
- all quality results;
- publication blockers;
- git status;
- resulting local commit hash.

Do not claim public-release readiness if a notebook opened alone in a fresh
Colab session still fails before bootstrapping the package.
