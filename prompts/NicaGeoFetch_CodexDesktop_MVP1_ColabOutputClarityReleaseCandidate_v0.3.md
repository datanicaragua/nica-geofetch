Continue work in the existing repository:

C:\Dev\nica-geofetch

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.3

PROMPT VERSION
0.3

STATUS
FINAL — READY FOR EXECUTION

TARGET AGENT
Codex Desktop

PROJECT
Nica-GeoFetch

REPOSITORY
https://github.com/datanicaragua/nica-geofetch

MILESTONE
MVP-1 — Final public-Colab clarity and output-packaging release candidate

SUPERSEDES

NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.2

GOVERNANCE MODEL

This repository follows a human-in-the-loop, AI-assisted engineering workflow:

1. Codex Desktop executes implementation and repository operations.
2. ChatGPT Project independently reviews the implementation, PR, evidence, and
   risks.
3. The human owner makes the final decision to:
   - approve;
   - request changes;
   - defer;
   - reject;
   - merge;
   - tag;
   - release.

Codex may autonomously perform reversible development actions:

- inspect the repository;
- create a task branch;
- edit files;
- run tests;
- create local commits;
- push the task branch;
- create a draft pull request;
- update the pull request;
- inspect GitHub Actions;
- correct CI failures;
- mark the PR ready for review;
- post an evidence summary to the PR.

Codex must not perform these actions without a separate explicit human
authorization:

- commit directly to main;
- merge a pull request;
- force push;
- rewrite Git history;
- delete the remote task branch;
- create a Git tag;
- create a GitHub release;
- publish to PyPI;
- change repository visibility;
- change branch-protection rules;
- alter repository secrets or environments;
- change software or data licensing;
- publish institutional datasets.

The PR must remain open for ChatGPT Project review and human decision.

PURPOSE

Apply a narrowly scoped beginner-UX and output-clarity correction before the
MVP-1 release candidate.

The existing implementation already provides:

- official INETER KML retrieval;
- source KML retention;
- structural and topology validation;
- explicit geometry repair;
- analytical conversion;
- provenance;
- manifests;
- checksums;
- CLI;
- public Colab installation;
- GitHub publication;
- CI;
- source-data exclusion controls.

Do not redesign or expand those components.

This task must improve only:

1. notebook step clarity;
2. removal of the duplicate automatic ZIP button;
3. explanation of raw and processed outputs;
4. interpretation of per-level analytical outputs;
5. manual-fallback presentation;
6. compact beginner-facing result summaries;
7. Spanish warning messages;
8. descriptive ZIP naming;
9. a concise results guide inside every ZIP;
10. code-cell presentation for beginner users;
11. the previously identified micro-fixes;
12. durable branch and pull-request governance for future work.

VERIFIED HUMAN EVIDENCE

A public Colab Run all execution selected:

- levels 4, 5, 6, and 7;
- GeoPackage;
- repair disabled;
- temporary Colab storage.

The final ZIP contained:

raw/
- ineter_pfafstetter_2025_level4.kml
- ineter_pfafstetter_2025_level5.kml
- ineter_pfafstetter_2025_level6.kml
- ineter_pfafstetter_2025_level7.kml

processed/
- pfaf_level4.gpkg

The independently inspected pfaf_level4.gpkg contains:

- layer: pfaf_n4;
- 12 features;
- MULTIPOLYGON geometry;
- EPSG:4326.

It does not contain levels 5, 6, or 7.

This is expected because repair was disabled and those levels contain known
topology warnings.

FIRST READ

Read in this order:

1. AGENTS.md
2. CONTRIBUTING.md
3. docs/index.md
4. docs/HANDOFF.md
5. docs/PROJECT_STATUS.md
6. docs/BEGINNER_GUIDE.es.md
7. docs/DATA_GOVERNANCE.md
8. docs/PUBLICATION_CHECKLIST.md
9. notebooks/NicaGeoFetch_Colab.ipynb
10. notebooks/NicaGeoFetch_Developer.ipynb
11. src/nica_geofetch/workflows.py
12. src/nica_geofetch/packaging.py
13. src/nica_geofetch/manifests.py
14. src/nica_geofetch/models.py
15. existing relevant tests
16. prompts/PROMPT_REGISTRY.md

Then inspect:

- git status;
- current branch;
- local branches;
- remote branches;
- git remote -v;
- recent commits;
- open pull requests;
- latest GitHub Actions runs;
- repository visibility;
- existing branch-protection status when readable.

Do not change branch-protection settings in this task.

Report their current status and any recommendation separately.

REPOSITORY SAFETY PREFLIGHT

The expected origin is:

https://github.com/datanicaragua/nica-geofetch.git

Run checks equivalent to:

git status --short --branch
git remote -v
git fetch --prune origin
git branch -vv
gh auth status
gh repo view datanicaragua/nica-geofetch
gh pr list --repo datanicaragua/nica-geofetch

Stop and report before editing if:

- origin does not point to the expected repository;
- the working tree contains unexplained changes;
- local main has commits not present on origin/main;
- origin/main has diverged from local main;
- another open PR already implements the same prompt;
- institutional source data is unexpectedly tracked;
- credentials or secrets are detected.

Do not discard or overwrite unexplained work.

BRANCH STRATEGY

Do not work directly on main.

Synchronize main using fast-forward-only operations:

git switch main
git pull --ff-only origin main

Preferred branch:

fix/mvp1-colab-output-clarity-v0.3

Create it from the synchronized origin/main state.

If that branch already exists:

1. inspect the local and remote branch;
2. determine whether it belongs to this exact prompt;
3. reuse it only if:
   - it has the expected scope;
   - it is clean;
   - it has no unexplained changes;
   - it has not already been merged.

If the preferred branch exists but is unrelated or stale, create:

fix/mvp1-colab-output-clarity-v0.3-r1

Document the reason.

Do not delete, reset, or overwrite an existing branch.

GENERAL BRANCH NAMING POLICY

Update CONTRIBUTING.md, and add only a concise reference in AGENTS.md, so future
work follows:

- fix/<milestone>-<short-purpose>
- feat/<milestone-or-domain>-<short-purpose>
- docs/<short-purpose>
- chore/<short-purpose>
- release/<version>

Use one branch per coherent unit of work or milestone.

Do not create one branch for every trivial typo.

Do not combine unrelated features in one branch.

PULL REQUEST STRATEGY

Create a draft pull request after the first stable pushed commit.

Base:

main

Head:

fix/mvp1-colab-output-clarity-v0.3

Preferred PR title:

fix: clarify Colab outputs before MVP-1 release

The PR body must include:

## Context

Explain the successful public Colab test and the remaining beginner-facing
ambiguities.

## Prompt traceability

Prompt tag:

NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.3

Link to:

prompts/NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.3.md

## Scope

List the intended UX and packaging corrections.

## Explicit non-scope

State that the PR does not change:

- provider selection;
- official URLs;
- topology semantics;
- repair semantics;
- source provenance;
- institutional licensing;
- CLI behavior;
- developer notebook;
- repository visibility;
- release status.

## Human evidence

Record the observed all-level Colab result:

- four retained KML files;
- only level-4 GeoPackage without repair;
- duplicated ZIP controls;
- manual fallback ambiguity.

## Validation

Include:

- installation;
- ruff;
- mypy;
- pytest;
- pre-commit;
- notebook validation;
- publication audit;
- GitHub Actions links.

## Data safety

Confirm that no real institutional dataset is added to Git.

## Manual review gates

Include unchecked items for:

- ChatGPT Project audit;
- human public-Colab Run all;
- human all-level output inspection;
- human second-run state validation;
- human approval to merge;
- human approval to create v0.1.0.

Create the PR initially with:

gh pr create --draft

Do not mark it ready until:

- implementation is complete;
- local quality gates pass;
- branch is pushed;
- GitHub Actions are green;
- the PR body is current.

When those conditions are met, Codex may execute:

gh pr ready

Codex must not merge the PR.

NOTEBOOK STRUCTURE

Use this static Markdown sequence:

1. Instalar Nica-GeoFetch
2. Elegir los datos y formatos
3. Descargar, preparar y guardar los resultados
4. ¿No funcionó la descarga automática?
5. Cómo interpretar los resultados

Do not generate numbered headings dynamically through widgets.HTML.

STEP 3: SINGLE AUTOMATIC DOWNLOAD CONTROL

Step 3 must contain:

- diagnose button;
- download and prepare button;
- progress information;
- compact summary;
- dynamic explanation of generated outputs;
- one authoritative button:

  Descargar ZIP a mi computadora

Remove the independent section:

Descargar el ZIP final

Remove:

fallback_zip_button

and the button:

Descargar el último ZIP

There must be only one automatic ZIP download button.

The manual-import workflow may keep its separately labeled manual ZIP button.

OUTPUT LOCATION GUIDANCE

Explain inside Step 3:

- /content is temporary Colab storage;
- a generated ZIP is not yet on the user's computer;
- the user must click the blue download button;
- temporary files disappear when the runtime ends;
- Google Drive outputs remain at the exact displayed path.

After completion, display:

Proceso terminado.

1. Revise el resumen.
2. Pulse “Descargar ZIP a mi computadora”.
3. Guarde el archivo antes de cerrar Colab.

RAW AND PROCESSED GUIDANCE

Before execution and in Step 5, explain:

raw/

Contains original institutional KML files retained without geometry repair or
analytical modification.

processed/

Contains only analytical formats generated from valid geometries or from an
explicitly repaired analytical copy.

Clarify:

- selecting all levels downloads all selected original KML files;
- analytical outputs are created separately for each level;
- selecting all levels does not create one consolidated GeoPackage;
- pfaf_level4.gpkg contains only level 4;
- levels with topology warnings may have no analytical file when repair is off.

PER-LEVEL OUTPUT POLICY

Preserve one analytical file per level:

- pfaf_level4.gpkg
- pfaf_level5.gpkg
- pfaf_level6.gpkg
- pfaf_level7.gpkg

Do not create a combined GeoPackage in this milestone.

Document:

“Seleccionar todos los niveles” means one execution and one final ZIP, not one
single GeoPackage containing all hierarchical levels.

PREFLIGHT EXPECTATION

Before the workflow starts, dynamically display a concise expected-result
message based on:

- selected levels;
- requested formats;
- repair state;
- last verified audit warnings.

For levels 4–7, GeoPackage, repair=False, display an expectation equivalent to:

- Four original KML files are expected to be downloaded and retained.
- Level 4 is expected to generate a GeoPackage.
- Levels 5–7 may omit their GeoPackages because repair is disabled.
- Enable explicit repair only when analytical derivatives for those levels are
  required.

Clearly label this as an expectation based on the latest audit, not a permanent
guarantee.

COMPACT RESULT SUMMARY

Use a primary beginner-facing table containing:

- Nivel
- KML fuente conservado
- Estado geométrico
- Reparación
- Formatos generados
- Resultado

Replace:

KML oficial descargado

with:

KML fuente conservado

This wording must work for remote download and manual import.

Add “Modo de obtención” only if the resulting table remains readable.

Possible values:

- Descarga remota
- Importación manual
- Insumo de prueba

Keep detailed fields in:

- audit_report.json;
- audit_report.md;
- source_manifest.json;
- provenance_summary.md.

Do not remove technical audit information.

DYNAMIC RESULT EXPLANATION

After the summary, generate a concise explanation from WorkflowResult.

For each level, state:

- source KML retained;
- analytical files generated;
- analytical files skipped;
- invalid geometry count;
- repair state;
- reason for omission.

For the verified all-level repair-disabled case, the explanation should be
equivalent to:

Se descargaron y conservaron los KML originales de los niveles 4, 5, 6 y 7.

Se generó:
- processed/pfaf_level4.gpkg

No se generaron GeoPackages para:
- Nivel 5: 2 advertencias topológicas; reparación desactivada.
- Nivel 6: 1 advertencia topológica; reparación desactivada.
- Nivel 7: 2 advertencias topológicas; reparación desactivada.

Generate this dynamically.

Do not hard-code those exact levels as permanent results.

WARNING LOCALIZATION

Map expected warning codes to concise beginner-facing Spanish messages.

At minimum:

invalid_geometry:
Se detectaron geometrías con advertencias topológicas.

Pfafstetter code length mismatch:
El código Pfafstetter no coincide con la longitud esperada para este nivel.

duplicate code:
Se detectaron códigos repetidos en la fuente.

Keep original technical messages in audit files.

Do not alter source values or suppress findings.

ZIP NAMING

Replace the generic repeated archive name with a descriptive and unique name.

Use a pattern equivalent to:

nica_geofetch_ineter_pfaf_n4-n7_gpkg_20260726T112400Z.zip

Include, when practical:

- provider or dataset shorthand;
- selected levels;
- requested format or formats;
- UTC timestamp.

Keep filenames filesystem-safe and deterministic.

Do not rely on the browser adding “(1)” to distinguish executions.

ZIP CONTENTS GUIDE

Generate and include in every final archive:

LEEME_RESULTADOS.md

The UTF-8 Markdown guide must contain:

1. execution timestamp UTC;
2. provider;
3. selected levels;
4. requested formats;
5. repair requested;
6. explanation of raw/;
7. explanation of processed/;
8. compact per-level result table;
9. exact source files retained;
10. exact analytical files generated;
11. skipped outputs and reasons;
12. meaning of topology warnings;
13. audit and provenance file locations;
14. brief instructions for opening:
    - KML;
    - GeoPackage;
    - GeoJSON;
    - Shapefile ZIP;
15. distinction between software licensing and third-party institutional data.

Keep it concise.

Do not duplicate the complete audit report.

MANUAL FALLBACK

Rename Step 4:

¿No funcionó la descarga automática?

Use text equivalent to:

“Esta opción es un respaldo. Úsela solamente si INETER no responde, su red
bloquea el acceso o usted ya tiene un KML oficial que desea validar, convertir
o volver a procesar. No necesita utilizarla después de una descarga automática
correcta.”

Explain its concrete purposes:

- continuity during service outages;
- blocked-network fallback;
- offline conversion;
- reproducible reprocessing of a historical source file.

Keep:

- level selector;
- explicit repair checkbox;
- upload button;
- result summary;
- manual ZIP button.

Clarify that manual import uses the analytical format selected in Step 2, or
display that selected format clearly before processing.

Place the controls inside a collapsed or subordinate visual section when this
works reliably in Colab.

Run all must not open the file selector.

INTERPRETATION SECTION

Step 5 is informational only.

Explain:

Correcto:
The KML source was retained and requested analytical outputs were generated.

Correcto con advertencias:
The KML source was retained, but one or more analytical outputs were skipped.

Reparado:
The original KML remained unchanged and an analytical working copy was
explicitly repaired and validated.

Omitido:
The analytical format was not generated for that level, but the KML source may
still be available in raw/.

Do not place execution or ZIP buttons in Step 5.

CODE PRESENTATION

The public notebook currently exposes long implementation cells that may
overwhelm beginner users.

Where supported reliably by Colab:

- set implementation cells to appear collapsed or in form view by default;
- keep Markdown guidance and widgets visible;
- keep source code accessible for inspection;
- do not obfuscate or remove code;
- do not change developer-notebook presentation.

This is a presentation adjustment only.

MICRO-FIXES

Explicitly include:

1. Replace “KML oficial descargado” with “KML fuente conservado”.
2. Remove the redundant automatic ZIP button.
3. Use a static Markdown heading for Step 3.
4. Ensure the automatic ZIP button references the latest automatic run.
5. Preserve the separate manual ZIP button with an unambiguous label.
6. Ensure a second run cannot reference the previous archive.
7. Ensure automatic and manual LAST_RESULT state cannot become misleading.
8. Ensure failure disables stale download controls.

STATE MANAGEMENT

Confirm:

- one automatic ZIP button;
- latest-run archive only;
- descriptive unique archive name;
- buttons reset after failure;
- progress resets;
- unique output directories remain;
- manual and automatic results are not mixed;
- no stale ZIP remains downloadable.

DURABLE REPOSITORY WORKFLOW

Update CONTRIBUTING.md to document:

1. No nontrivial direct commits to main.
2. One coherent branch per change set.
3. Prompt tag recorded in the branch PR.
4. Local quality gates before push.
5. Draft PR before final review.
6. GitHub Actions required before ready-for-review status.
7. ChatGPT Project review.
8. Human approval before merge.
9. Separate approval for tags and releases.
10. No institutional datasets in Git.

Keep AGENTS.md concise.

Add a short rule equivalent to:

“Nontrivial changes must use a task branch and pull request. Read
CONTRIBUTING.md for the full workflow.”

Do not duplicate the full policy in AGENTS.md.

TESTS

Add only focused tests for:

1. one automatic ZIP download button exists;
2. fallback_zip_button no longer exists;
3. static step headings are ordered correctly;
4. “KML fuente conservado” is used;
5. raw and processed are explained;
6. per-level GeoPackage semantics are documented;
7. all-level selection is described as one ZIP, not one GPKG;
8. preflight expectation responds to levels, formats, and repair;
9. compact summary is produced;
10. common warnings are localized in Spanish;
11. dynamic generated/skipped explanation is correct;
12. LEEME_RESULTADOS.md is created;
13. LEEME_RESULTADOS.md is included in the final ZIP;
14. generated and skipped outputs are correctly listed;
15. archive filename includes level, format, and timestamp context;
16. manual fallback purpose is clearly documented;
17. Run all does not open the file picker;
18. manual import clearly displays or inherits the Step 2 format;
19. code cells carry intended Colab presentation metadata when supported;
20. bootstrap remains unchanged;
21. developer notebook remains unchanged;
22. validation, repair, manifests, and provenance remain unchanged in meaning;
23. CONTRIBUTING.md contains the branch-and-PR workflow;
24. AGENTS.md links concisely to the durable workflow.

Do not add tests merely to increase the test count.

DOCUMENTATION

Update only as needed:

- AGENTS.md
- CONTRIBUTING.md
- docs/BEGINNER_GUIDE.es.md
- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- docs/PUBLICATION_CHECKLIST.md
- CHANGELOG.md
- prompts/PROMPT_REGISTRY.md

Archive this complete prompt at:

prompts/NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.3.md

Record:

- prompt tag;
- task branch;
- PR number;
- PR URL;
- local commits;
- CI run;
- execution status.

QUALITY GATES

Run:

python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest -q
pre-commit run --all-files
python -m nica_geofetch.cli --help

Validate both notebooks.

Run the publication audit.

Do not perform another live N4–N7 download unless code changes affect source
download, validation, or remote behavior.

Use synthetic fixtures for:

- output guide;
- warning localization;
- ZIP naming;
- packaging;
- generated and skipped-output explanations.

COMMIT STRATEGY

Use one or two logical commits.

Suggested separation:

Commit 1:
fix: clarify Colab outputs and ZIP delivery

Commit 2:
docs: record PR governance and release-candidate handoff

Do not create empty or artificial commits.

Do not commit generated institutional outputs.

Before each commit:

- inspect git diff;
- inspect tracked files;
- confirm scope;
- run relevant tests.

PUSH STRATEGY

Push only the task branch:

git push -u origin fix/mvp1-colab-output-clarity-v0.3

Do not push directly to main.

Do not force push.

If corrections are required after CI:

- commit normally to the same task branch;
- push normally;
- allow the PR to update.

GITHUB ACTIONS

After pushing:

1. inspect the workflow run associated with the task-branch HEAD;
2. wait for completion;
3. inspect failed jobs and logs;
4. correct only failures related to this PR;
5. rerun local gates after corrections;
6. push corrected commits;
7. verify the final required jobs are green.

Use commands equivalent to:

gh run list --repo datanicaragua/nica-geofetch
gh run watch <run-id> --repo datanicaragua/nica-geofetch
gh run view <run-id> --repo datanicaragua/nica-geofetch

Do not mark the PR ready if required CI is failing.

PR FINALIZATION

When implementation and CI are complete:

1. update the PR body with:
   - final files changed;
   - test results;
   - CI links;
   - known limitations;
   - required human tests;
   - no-data-publication confirmation;

2. mark the PR ready for review;

3. add a final PR comment summarizing:
   - prompt tag;
   - final commit SHA;
   - quality gates;
   - GitHub Actions result;
   - remaining ChatGPT audit;
   - remaining human Colab validation.

Do not merge.

Do not enable auto-merge.

Do not delete the branch.

DECISION GATES

Gate A — Codex implementation

Codex may complete automatically:

- branch;
- implementation;
- tests;
- commits;
- branch push;
- draft PR;
- CI corrections;
- ready-for-review transition.

Gate B — ChatGPT Project audit

Pending after Codex completion.

The human owner will provide the PR URL, Codex output, and relevant evidence to
ChatGPT Project for independent review.

Codex must record this as pending.

Gate C — Human public-Colab validation

Pending after ChatGPT review.

Required human checks:

1. Run all does not open manual upload.
2. Only one automatic ZIP button exists.
3. N4–N7, GeoPackage, repair disabled:
   - four KML files in raw/;
   - only pfaf_level4.gpkg in processed/;
   - clear explanation of skipped outputs.
4. LEEME_RESULTADOS.md exists and is accurate.
5. ZIP filename is descriptive.
6. manual fallback is clearly subordinate.
7. second execution references only the latest archive.
8. code cells are less visually intrusive.

Gate D — Human merge decision

The human owner decides whether to:

- approve and merge;
- request changes;
- defer;
- close the PR.

Codex has no authority to merge in this prompt.

Gate E — Release decision

A separate explicit prompt and human authorization are required for:

- merge, if delegated;
- tag v0.1.0;
- GitHub release;
- notebook pinning to v0.1.0.

BRANCH-PROTECTION REVIEW

Inspect whether main currently has protection or repository rules requiring:

- pull requests;
- status checks;
- force-push restrictions;
- branch-deletion restrictions.

Do not alter those rules.

Report:

- current state;
- whether the new workflow is technically enforced or only documented;
- a concise recommendation for a future human-approved governance action.

Do not block this PR solely because protection is not yet configured.

CONTINUITY

Update:

- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- docs/PUBLICATION_CHECKLIST.md
- prompts/PROMPT_REGISTRY.md

PROJECT_STATUS.md must state:

- task branch;
- PR state;
- current HEAD;
- CI state;
- current blockers;
- next review gate.

HANDOFF.md must state:

NEXT_ACTION:
ChatGPT Project audit of the open pull request, followed by human public-Colab
validation.

Include:

- PR URL;
- branch;
- commits;
- CI run;
- exact human tests;
- unresolved risks;
- merge not authorized;
- release not authorized.

ACCEPTANCE CRITERIA

This task is complete only when:

1. work occurred on the task branch, not main;
2. one automatic ZIP button remains;
3. Steps 3 and 4 no longer duplicate ZIP retrieval;
4. manual import is clearly presented as fallback;
5. raw and processed folders are explained;
6. users understand that pfaf_level4.gpkg contains only level 4;
7. all-level selection is explained as one execution and one ZIP;
8. analytical outputs remain separate by level;
9. preflight expectations reduce output surprise;
10. the beginner-facing summary is compact;
11. warning messages are understandable in Spanish;
12. a descriptive unique ZIP filename is used;
13. LEEME_RESULTADOS.md exists inside the ZIP;
14. code cells are less visually intrusive where Colab supports it;
15. existing validation and provenance behavior is preserved;
16. CONTRIBUTING.md documents the branch and PR workflow;
17. AGENTS.md links to the workflow concisely;
18. all local quality gates pass;
19. publication audit passes;
20. task branch is pushed;
21. draft PR is created;
22. GitHub Actions are green;
23. PR is marked ready for review;
24. PR body and final evidence comment are current;
25. PR is not merged;
26. no tag or release is created;
27. main is unchanged by direct commits;
28. HANDOFF.md identifies ChatGPT audit and human Colab validation as the next
    gates;
29. working tree is clean.

FINAL RESPONSE

Report:

1. Prompt tag executed.
2. Repository preflight result.
3. Base branch and task branch.
4. Files changed.
5. Notebook step simplification.
6. ZIP button consolidation.
7. Manual-fallback presentation.
8. Raw and processed guidance.
9. Per-level GeoPackage clarification.
10. Preflight expectation.
11. Compact summary.
12. Warning localization.
13. ZIP naming.
14. LEEME_RESULTADOS.md contents.
15. Colab code-cell presentation.
16. CONTRIBUTING and AGENTS governance changes.
17. Tests added or updated.
18. Local quality gates.
19. Publication-audit result.
20. Commit hashes.
21. Branch push result.
22. Draft PR creation result.
23. PR URL and number.
24. GitHub Actions run and final status.
25. PR ready-for-review status.
26. Branch-protection observation.
27. Remaining ChatGPT audit.
28. Remaining human Colab tests.
29. Confirmation that merge was not performed.
30. Confirmation that no tag or release was created.
31. Git status.
32. HANDOFF.md location.

Do not claim MVP-1 release readiness.

Do not merge the PR.

Do not create v0.1.0.
