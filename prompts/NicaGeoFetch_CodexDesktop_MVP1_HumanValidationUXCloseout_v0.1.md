Continue work in:

C:\Dev\nica-geofetch

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_HumanValidationUXCloseout_v0.1

PROMPT VERSION
0.1

STATUS
FINAL — READY FOR EXECUTION

TARGET
Codex Desktop

PROJECT
Nica-GeoFetch

MILESTONE
MVP-1 — Human-validation UX closeout for open PR #1

FOLLOWS

NicaGeoFetch_CodexDesktop_MVP1_ColabOutputClarityReleaseCandidate_v0.3

REPOSITORY

https://github.com/datanicaragua/nica-geofetch

EXISTING BRANCH

fix/mvp1-colab-output-clarity-v0.3

EXISTING PULL REQUEST

https://github.com/datanicaragua/nica-geofetch/pull/1

GOVERNANCE

Continue on the existing task branch and update the existing PR.

Do not create another branch or another PR because these corrections are part of
the same coherent Colab output-clarity change set.

Codex may:

- inspect the human evidence;
- implement the focused corrections;
- run local gates;
- commit normally;
- push the existing task branch;
- update PR #1;
- inspect and correct CI failures;
- update the PR evidence comment.

Codex must not:

- merge PR #1;
- enable auto-merge;
- push directly to main;
- force push;
- delete the branch;
- create a tag or release;
- change protection, visibility, licensing, provider URLs, validation semantics,
  repair behavior, or source-data policy.

HUMAN VALIDATION EVIDENCE

A fresh public-Colab test executed the PR code at commit:

80c8015b26854e5e0d03c51c0444b6ffefacaf3e

Selected:

- levels 4, 5, 6, and 7;
- GeoPackage;
- repair disabled;
- temporary Colab storage.

Successful result:

- levels 4–7 KML retained;
- `processed/pfaf_level4.gpkg` generated;
- level 5 omitted with 2 topology warnings;
- level 6 omitted with 1 topology warning;
- level 7 omitted with 2 topology warnings;
- compact summary rendered;
- dynamic generated/skipped explanation rendered;
- no traceback;
- one automatic ZIP button enabled;
- archive downloaded as:
  `nica_geofetch_ineter_pfaf_n4-n7_gpkg_20260726T212025Z.zip`;
- archive root contained:
  - `raw/`
  - `processed/`
  - `LEEME_RESULTADOS.md`
  - `audit_report.json`
  - `audit_report.md`
  - `source_manifest.json`
  - `provenance_summary.md`
  - `checksums_sha256.json`.

OBSERVED MICRO-DEFECTS

1. Singular/plural grammar:

   `Se detectaron 1 advertencias topológicas.`

   and:

   `1 advertencias topológicas; reparación desactivada.`

2. Technical format identifiers appear in beginner progress:

   `Formato solicitado: gpkg.`

   `No se generará gpkg...`

3. An internal INFO message appears in the beginner log:

   `INFO | Created 12 records`

4. `Proceso terminado` is emitted by the workflow callback before the notebook
   finishes rendering the summary, explanation, archive path, and enabled
   download button.

5. User-facing output groups topology findings and attribute-quality warnings
   under the same heading, making valid N4 geometry appear potentially
   problematic.

PURPOSE

Apply only the focused corrections demonstrated by the human Colab test and
close the corresponding documentation and PR evidence.

Do not change:

- download behavior;
- provider configuration;
- code aliases;
- topology validation logic;
- warning severities;
- repair behavior;
- analytical conversion behavior;
- provenance or manifest meaning;
- per-level output policy;
- archive structure;
- CLI logging defaults;
- developer notebook.

FIRST READ

Read:

1. AGENTS.md
2. CONTRIBUTING.md
3. docs/HANDOFF.md
4. docs/PROJECT_STATUS.md
5. docs/PUBLICATION_CHECKLIST.md
6. notebooks/NicaGeoFetch_Colab.ipynb
7. src/nica_geofetch/logging_utils.py
8. src/nica_geofetch/manifests.py
9. src/nica_geofetch/models.py
10. src/nica_geofetch/validation.py
11. relevant tests
12. prompts/PROMPT_REGISTRY.md

Then confirm:

- current branch is `fix/mvp1-colab-output-clarity-v0.3`;
- HEAD matches the remote PR branch;
- PR #1 is open;
- working tree is clean;
- no unrelated work exists.

Stop if the branch, PR, or working tree is inconsistent.

CORRECTION 1 — SPANISH COUNT GRAMMAR

Implement correct singular and plural phrasing in every beginner-facing output,
including the generated results guide.

Required examples:

- 0 advertencias topológicas
- 1 advertencia topológica
- 2 advertencias topológicas

Use:

- `Se detectó 1 advertencia topológica.`
- `Se detectaron 2 advertencias topológicas.`

Ensure N6 output and `LEEME_RESULTADOS.md` use the singular form.

Keep numeric counts and technical audit content unchanged.

CORRECTION 2 — FRIENDLY FORMAT LABELS

Use existing user-facing labels consistently:

- KML
- GeoPackage
- GeoJSON
- Shapefile ZIP

Replace beginner-visible `gpkg`, `geojson`, or `shapefile` tokens in:

- initial selected-format message;
- skipped-conversion progress messages;
- human-readable completion guidance.

Do not change internal enum values, filenames, manifests, JSON schema, or CLI
arguments.

CORRECTION 3 — PUBLIC NOTEBOOK LOG NOISE

Suppress internal INFO logs in the public beginner notebook only.

The public progress callback already communicates the workflow state.

Do not change default CLI logging behavior.

Do not remove technical logging from the package.

A simple notebook-scoped root logging level adjustment is acceptable if it does
not affect package tests or the developer notebook.

The beginner log must no longer display messages such as:

`INFO | Created 12 records`

Expected warnings and unexpected errors must remain visible through the
notebook’s own handling.

CORRECTION 4 — FINAL STATUS ORDER

Do not show the definitive status:

`Proceso terminado.`

until all of these have completed:

1. workflow returned successfully;
2. compact summary rendered;
3. dynamic explanation rendered;
4. archive path assigned;
5. location guidance rendered;
6. latest archive existence verified;
7. automatic ZIP button enabled.

The workflow-level completed callback may display:

`ZIP creado. Preparando el resumen…`

or an equivalent non-final message.

If summary or explanation rendering fails, the interface must not remain in a
false final-success state.

CORRECTION 5 — WARNING CATEGORIES

In beginner-facing output, distinguish:

A. Topology findings that affect analytical generation:

- `invalid_geometry`
- post-repair invalidity when applicable.

Use a heading equivalent to:

`Advertencias topológicas del nivel N`

B. Attribute or metadata observations that do not by themselves prevent
analytical conversion:

- `pfaf_code_length_mismatch`
- `duplicate_pfaf_code`

Use a heading equivalent to:

`Observaciones sobre los atributos del nivel N`

Do not alter issue codes, severity, validation rules, raw values, audit files,
or provider aliases.

Do not claim the source values are wrong.

Explain briefly that attribute observations are retained for review and do not
mean the geometry is invalid.

LEEME_RESULTADOS

Apply correct singular/plural grammar to skipped-output reasons.

Keep the existing content and archive placement.

Do not expand it into a full audit report.

Ensure it continues to list:

- retained sources;
- generated outputs;
- skipped outputs;
- reasons;
- audit and provenance locations;
- format-opening guidance;
- licensing distinction.

HUMAN-EVIDENCE DOCUMENTATION

Update:

- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- docs/PUBLICATION_CHECKLIST.md
- CHANGELOG.md
- prompts/PROMPT_REGISTRY.md

Record:

- successful human test against commit `80c8015`;
- test timestamp context `20260726T212025Z`;
- archive name;
- confirmed generated and skipped outputs;
- `LEEME_RESULTADOS.md` presence;
- discovered micro-defects;
- their correction status;
- final PR branch HEAD after this task;
- final CI run.

Do not mark merge or release as authorized.

After implementation, HANDOFF NEXT_ACTION must be:

Final human Colab confirmation of the micro-fixes and second-run latest-only
behavior, followed by ChatGPT Project merge recommendation.

PROMPT ARCHIVE

Archive this complete prompt at:

prompts/NicaGeoFetch_CodexDesktop_MVP1_HumanValidationUXCloseout_v0.1.md

Register it in:

prompts/PROMPT_REGISTRY.md

Do not modify the executed v0.3 prompt.

TESTS

Add or update only focused tests for:

1. singular topology-warning grammar;
2. plural topology-warning grammar;
3. singular grammar in `LEEME_RESULTADOS.md`;
4. friendly format labels in beginner progress;
5. absence of raw `gpkg` in beginner-facing messages;
6. public notebook suppression of internal INFO log noise;
7. final status is assigned only after summary, explanation, archive assignment,
   and button enablement;
8. topology warnings and attribute observations are displayed separately;
9. technical audit issue codes and messages remain unchanged;
10. bootstrap source remains unchanged;
11. developer notebook remains unchanged;
12. archive contents remain unchanged;
13. existing 66 tests continue passing.

Do not add tests merely to increase the count.

QUALITY GATES

Run:

python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest -q
pre-commit run --all-files
python -m nica_geofetch.cli --help
python scripts/publication_audit.py

Validate both notebooks.

Do not repeat the live N4–N7 download.

Use synthetic fixtures and the recorded human evidence.

COMMIT AND PR

Create one focused commit, unless documentation separation clearly requires two.

Suggested commit:

fix: polish Colab completion and warning messages

Push normally to:

fix/mvp1-colab-output-clarity-v0.3

Update PR #1.

Do not force push.

Wait for final GitHub Actions.

Update the PR body or evidence comment with:

- prompt tag;
- human evidence;
- micro-fixes;
- final commit SHA;
- local tests;
- final CI;
- remaining human confirmation.

Do not merge.

ACCEPTANCE CRITERIA

Complete only when:

1. singular/plural grammar is correct;
2. beginner messages use friendly format names;
3. internal INFO conversion logs do not clutter public Colab;
4. final-success status is emitted only after complete UI delivery;
5. topology and attribute observations are separated;
6. `LEEME_RESULTADOS.md` uses correct grammar;
7. no validation or repair semantics changed;
8. bootstrap remains unchanged;
9. developer notebook remains unchanged;
10. local gates pass;
11. publication audit passes;
12. branch is pushed normally;
13. PR #1 is updated;
14. final CI is green;
15. PR remains open and unmerged;
16. no tag or release is created;
17. working tree is clean.

FINAL RESPONSE

Report:

1. Prompt tag.
2. Repository preflight.
3. Branch and PR.
4. Files changed.
5. Grammar correction.
6. Friendly format labels.
7. Log-noise correction.
8. Final-status ordering.
9. Warning-category presentation.
10. `LEEME_RESULTADOS.md` correction.
11. Tests.
12. Local gates.
13. Publication audit.
14. Commit SHA.
15. Push result.
16. Final CI.
17. PR URL and state.
18. Remaining human test.
19. Confirmation of no merge, tag, or release.
20. Git status.
21. HANDOFF location.
