Continue work in the existing repository:

C:\Dev\nica-geofetch

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_PublicationAndColabFix_v0.1

PROMPT VERSION
0.1

STATUS
READY FOR EXECUTION

TARGET AGENT
Codex Desktop

PROJECT
Nica-GeoFetch

REPOSITORY
datanicaragua/nica-geofetch

MILESTONE
MVP-1 — Public repository activation and Colab bootstrap correction

PURPOSE

Perform the final focused corrections required before changing the existing
GitHub repository from private to public.

The repository already exists at:

https://github.com/datanicaragua/nica-geofetch

The local repository already has an origin remote and the main branch has
previously been pushed.

This task must:

1. improve the beginner Colab bootstrap failure handling;
2. add professional project authorship;
3. document AI-assisted development transparently but proportionately;
4. validate local and GitHub publication gates;
5. push the verified changes;
6. change repository visibility to public only if every automated gate passes;
7. leave the v0.1.0 release pending until a human completes the real public
   Colab test.

Do not create another repository.
Do not replace the existing origin remote.
Do not publish institutional data.
Do not create v0.1.0 in this task.

FIRST READ

Read in this order:

1. AGENTS.md
2. docs/index.md
3. docs/PROJECT_STATUS.md
4. docs/HANDOFF.md
5. docs/PUBLICATION_CHECKLIST.md
6. docs/DATA_GOVERNANCE.md
7. docs/LEGAL_AND_ATTRIBUTION.md
8. DATA_TERMS.md
9. README.md
10. README.es.md
11. notebooks/NicaGeoFetch_Colab.ipynb
12. notebooks/NicaGeoFetch_Developer.ipynb
13. prompts/PROMPT_REGISTRY.md

Then inspect:

- git status;
- current branch;
- git remote -v;
- recent commits;
- GitHub CLI authentication;
- repository visibility;
- user permissions;
- current GitHub Actions state.

EXPECTED REMOTE

The existing remote must be:

https://github.com/datanicaragua/nica-geofetch.git

If origin differs, stop and report the discrepancy. Do not rewrite the remote
without explicit human approval.

COLAB FAILURE CONTEXT

The public notebook currently installs with a requirement equivalent to:

nica-geofetch[notebook] @
git+https://github.com/datanicaragua/nica-geofetch.git@main

A real Colab test performed while the repository was private produced:

ModuleNotFoundError: No module named 'nica_geofetch'

This may occur because:

- an anonymous Colab runtime cannot install from the private GitHub repository;
- the bootstrap cell was skipped;
- the pip or Git installation failed and the next import cell still ran.

Improve this behavior without redesigning the notebook.

PUBLIC COLAB BOOTSTRAP REQUIREMENTS

Update notebooks/NicaGeoFetch_Colab.ipynb so that:

1. The bootstrap cell remains the first executable code cell.
2. Installation failure is caught explicitly.
3. The user receives a clear Spanish explanation.
4. The error distinguishes, where practical:
   - repository unavailable or private;
   - authentication failure;
   - Git not available;
   - pip installation failure;
   - package still unavailable after installation.
5. The notebook must not continue silently to package imports after a failed
   bootstrap.
6. The message must explain that:
   - anonymous installation requires a public repository;
   - private testing should use INSTALL_SOURCE = "zip";
   - no GitHub token should be pasted into the public notebook.
7. After installation, verify the package immediately with:

   import nica_geofetch

8. Print:
   - installed package version;
   - selected Git ref;
   - installation source.
9. If import verification fails, raise a beginner-readable RuntimeError rather
   than exposing only ModuleNotFoundError.
10. Preserve the existing ZIP or wheel fallback.
11. Preserve package API use and avoid business-logic duplication.
12. Preserve the developer notebook behavior.

Add or update tests for:

- failed GitHub bootstrap;
- successful bootstrap simulation;
- no import cell execution after bootstrap failure;
- private-repository guidance text;
- ZIP fallback;
- package import verification;
- public notebook cell order.

Do not add credentials, tokens, secrets, or interactive GitHub authentication
to the notebook.

AUTHORSHIP

Add a concise professional authorship section to both README files.

README.md:

## Author and project leadership

**Gustavo Ernesto Martínez Cárdenas**
Lead Data Scientist and Architect, DataNicaTools

- DataNicaTools: https://github.com/datanicaragua
- GitHub: https://github.com/gustavoemc
- LinkedIn: https://www.linkedin.com/in/gustavoernestom

Developed as part of the DataNicaTools ecosystem.

README.es.md:

## Autoría y liderazgo del proyecto

**Gustavo Ernesto Martínez Cárdenas**
Científico de Datos Principal y Arquitecto de DataNicaTools

- DataNicaTools: https://github.com/datanicaragua
- GitHub: https://github.com/gustavoemc
- LinkedIn: https://www.linkedin.com/in/gustavoernestom

Desarrollado como parte del ecosistema DataNicaTools.

Use normal Markdown hyperlinks.

Do not describe INETER as an author or contributor to the software. Identify it
only as the institutional source or producer of the referenced dataset.

AI-ASSISTED DEVELOPMENT

Create:

docs/AI_ASSISTED_DEVELOPMENT.md

Document that:

- development was human-led and AI-assisted;
- Codex and ChatGPT supported repository scaffolding, implementation, testing,
  documentation, and review;
- architecture, provider selection, legal interpretation, publication, and
  release approval remain human responsibilities;
- versioned prompts are preserved under prompts/;
- tests and Git history are the verification record;
- AI tools are not software authors or legal decision-makers.

Include a small historical execution record such as:

tool: Codex Desktop
model_at_execution: GPT-5.6 Sol
reasoning_effort: Extra High
human_lead: Gustavo Ernesto Martínez Cárdenas

Record this only as historical process metadata.

Do not make the exact model or reasoning level a prominent README badge,
product dependency, reproducibility claim, or marketing statement.

Add one discreet line in the README documentation section linking to
docs/AI_ASSISTED_DEVELOPMENT.md.

DATE AND UPDATE POLICY

Do not add a manually maintained “Last updated” date to README.md or
README.es.md.

Document the following policy in an appropriate existing governance or
continuity document:

1. Git commits, tags, and releases are the canonical software-history record.
2. PROJECT_STATUS.md and HANDOFF.md must include last_updated_utc.
3. Dataset registry entries should include last_checked_utc or
   last_live_verified_utc when applicable.
4. Manifests and audit reports must retain retrieval and generation timestamps.
5. Case studies or source-access documents may include “Last reviewed” when
   their factual status can become stale.
6. Use ISO 8601 dates and UTC for machine-readable timestamps.
7. Do not add static dates that require unnecessary manual maintenance.

PUBLICATION AUDIT

Before any push or visibility change, run and verify:

git status --short --branch
git remote -v
git ls-files
git status --ignored

Confirm that Git does not track real institutional data, including:

- seed_inputs real KML files;
- downloaded KML or KMZ files;
- GeoPackages;
- Shapefiles;
- institutional GeoJSON;
- output directories;
- credentials;
- tokens;
- temporary notebooks containing secrets.

Only the documented synthetic fixtures may be tracked.

Run the repository publication-audit script.

LOCAL QUALITY GATES

Run:

python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest -q
pre-commit run --all-files
python -m nica_geofetch.cli --help

Validate both notebooks using:

- nbformat;
- existing notebook smoke tests;
- fresh-directory bootstrap tests.

Do not proceed to push if any applicable check fails.

COMMIT AND PUSH

If all local gates pass:

1. Update:
   - CHANGELOG.md
   - docs/PROJECT_STATUS.md
   - docs/PHASE_LOG.md
   - docs/HANDOFF.md
   - docs/PUBLICATION_CHECKLIST.md
   - docs/index.md
   - prompts/PROMPT_REGISTRY.md

2. Archive this complete prompt at:

prompts/NicaGeoFetch_CodexDesktop_MVP1_PublicationAndColabFix_v0.1.md

3. Create one or two logical local commits.

4. Confirm that main is ahead of origin/main only by the expected commits.

5. Push main to the existing origin:

git push origin main

Do not force push.
Do not rewrite history.
Do not create another repository.

GITHUB ACTIONS GATE

After push:

1. Use GitHub CLI to inspect workflow runs for the pushed HEAD.
2. Wait for the applicable workflow to complete.
3. Inspect failed jobs and logs if any job fails.
4. Correct only relevant failures.
5. Re-run all local gates after corrections.
6. Push corrected commits.
7. Do not change visibility until all required GitHub Actions jobs are green.

Use commands equivalent to:

gh run list --repo datanicaragua/nica-geofetch
gh run watch <run-id> --repo datanicaragua/nica-geofetch
gh run view <run-id> --repo datanicaragua/nica-geofetch

PUBLIC VISIBILITY AUTHORIZATION

The human owner authorizes Codex, through this prompt, to change the existing
repository:

datanicaragua/nica-geofetch

from private to public only if all of these conditions are true:

1. local quality gates pass;
2. publication audit passes;
3. no real institutional data is tracked;
4. no secrets are detected;
5. origin points to the expected repository;
6. GitHub Actions for the pushed HEAD are green;
7. the working tree is clean;
8. local main matches origin/main;
9. README authorship and legal notices are correct;
10. the public Colab notebook contains no token or private-access mechanism.

Before changing visibility, print a concise gate summary.

Then execute:

gh repo edit datanicaragua/nica-geofetch \
  --visibility public \
  --accept-visibility-change-consequences

If GitHub or the organization rejects the change, do not attempt to bypass the
restriction. Report the exact error and leave the repository private.

POST-VISIBILITY VERIFICATION

After the visibility change:

1. Verify repository visibility with GitHub CLI.
2. Verify that the anonymous repository URL is reachable.
3. Verify that the raw public notebook file is reachable.
4. Test package installation from the public repository in a new temporary
   Python environment using the same Git requirement used by Colab.
5. Verify:

   import nica_geofetch
   print(nica_geofetch.__version__)

6. Verify that the Colab badge URL resolves to:

https://colab.research.google.com/github/datanicaragua/nica-geofetch/blob/main/notebooks/NicaGeoFetch_Colab.ipynb

7. Do not claim the interactive Colab gate is complete.

A human must still open the badge in a fresh anonymous Colab runtime and run
the notebook from top to bottom.

RELEASE RESTRICTION

Do not create:

- tag v0.1.0;
- GitHub release v0.1.0;
- PyPI package;
- data release;
- institutional-data archive.

The v0.1.0 release remains blocked until the human confirms:

- public badge execution;
- successful bootstrap;
- successful N4 diagnosis and download;
- final ZIP generation;
- fallback behavior;
- acceptable beginner experience.

CONTINUITY

After completion, update HANDOFF.md with one of these exact next states:

A. If the repository is public:

NEXT_ACTION:
Human public-Colab validation from a fresh anonymous runtime.

B. If visibility could not be changed:

NEXT_ACTION:
Resolve the documented GitHub permission or organization-policy blocker.

ACCEPTANCE CRITERIA

This task is complete only when:

1. Colab bootstrap failure handling is beginner-readable.
2. Failed installation cannot silently lead to raw package imports.
3. ZIP fallback remains functional.
4. Authorship and links are present in both READMEs.
5. AI-assisted development is documented proportionately.
6. Static README update dates are not added.
7. temporal metadata remains present where operationally useful.
8. all local quality gates pass.
9. publication audit passes.
10. changes are committed and pushed to the existing repository.
11. GitHub Actions are green.
12. repository visibility becomes public, or an exact external blocker is
    documented.
13. anonymous Git installation succeeds after publication.
14. no release is created.
15. HANDOFF.md identifies human public-Colab validation as the next action.
16. the working tree is clean.

FINAL RESPONSE

Report:

1. Prompt tag executed.
2. Initial and final repository visibility.
3. Files changed.
4. Colab bootstrap corrections.
5. Authorship additions.
6. AI-development transparency changes.
7. Date and update policy.
8. Local quality-gate results.
9. Publication-audit result.
10. GitHub Actions run and final status.
11. Push result.
12. Visibility-change command and result.
13. Anonymous installation verification.
14. Remaining manual Colab gate.
15. Git status.
16. Final commit hashes.
17. HANDOFF.md location.

Do not claim v0.1.0 release readiness until the human public-Colab test passes.
