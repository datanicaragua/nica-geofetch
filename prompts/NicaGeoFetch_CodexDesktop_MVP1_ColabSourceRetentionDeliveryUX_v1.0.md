Continue work in the existing repository:

C:\Dev\nica-geofetch

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_ColabSourceRetentionDeliveryUX_v1.0

PROMPT VERSION
1.0

STATUS
FINAL — READY FOR EXECUTION

TARGET
Codex Desktop

PROJECT
Nica-GeoFetch

MILESTONE
MVP-1 — Final public Colab source-retention, delivery, and beginner-guidance fix

PURPOSE

Apply the final focused correction required before the MVP-1 release candidate
can be validated by a human in public Google Colab.

Do not redesign the package or expand the project.

This task must improve:

1. source KML retention;
2. distinction between source-file validity and geometry topology validity;
3. one-action download of levels 4, 5, 6, and 7;
4. explicit optional geometry repair;
5. final ZIP delivery to the user’s computer;
6. optional manual-import fallback;
7. beginner-facing guidance, status messages, progress feedback, and next-step
   explanations throughout the notebook.

Do not add new providers, APIs, databases, web applications, plugin systems,
generic workflow frameworks, or new provenance architectures.

VERIFIED HUMAN EVIDENCE

A public Colab test for level 4 completed successfully:

- retrieval_mode: remote_download
- valid: true
- features: 12
- GeoPackage generated
- ZIP generated at:
  /content/NicaGeoFetch_outputs/nica_geofetch_results.zip

A test selecting levels 4 and 5 produced:

ValidationError:
Downloaded KML failed validation: invalid_geometry; invalid_geometry

Known audit findings:

- Level 4: 12 Placemarks; no known topology warnings.
- Level 5: 68 Placemarks; 2 known invalid geometries.
- Level 6: 491 Placemarks; 1 known invalid geometry.
- Level 7: 2,337 Placemarks; 2 known invalid geometries.

The manually downloaded files for levels 4–7 are valid institutional KML
containers, open correctly, contain the expected vector content, and must not be
described as unusable files merely because a small number of polygon geometries
fail topology validation.

CORE USER PROMISE

The public notebook must communicate this promise clearly:

“Nica-GeoFetch downloads and preserves the original official KML files. It then
validates their geometry and, when requested, prepares analytical formats such
as GeoPackage, GeoJSON, and Shapefile. Geometry repair is optional, explicit,
and recorded.”

Spanish wording:

“Nica-GeoFetch descarga y conserva los KML oficiales originales. Después revisa
su geometría y, cuando se solicita, prepara formatos analíticos como GeoPackage,
GeoJSON y Shapefile. La reparación geométrica es opcional, explícita y queda
registrada.”

FIRST READ

Read:

1. AGENTS.md
2. docs/HANDOFF.md
3. docs/PROJECT_STATUS.md
4. docs/SEED_AUDIT.md
5. docs/DATA_GOVERNANCE.md
6. docs/BEGINNER_GUIDE.es.md
7. docs/PUBLICATION_CHECKLIST.md
8. notebooks/NicaGeoFetch_Colab.ipynb
9. notebooks/NicaGeoFetch_Developer.ipynb
10. src/nica_geofetch/download.py
11. src/nica_geofetch/validation.py
12. src/nica_geofetch/workflows.py
13. src/nica_geofetch/providers/ineter_pfafstetter.py
14. src/nica_geofetch/manifests.py
15. existing relevant tests
16. prompts/PROMPT_REGISTRY.md

Then inspect:

- git status;
- current branch;
- origin;
- recent commits;
- current CI status.

Preserve completed publication, authorship, branding, licensing, provenance, and
AI-transparency work.

Do not repeat or rewrite completed sections unless a small consistency update is
required.

VALIDATION MODEL

Implement or clarify the smallest possible distinction among:

A. acquisition_valid

The source KML may be retained when:

- HTTP response succeeded;
- response is not HTML;
- response is not an OGC error document;
- XML is parseable;
- at least one Placemark exists;
- polygonal vector geometry exists;
- the content is non-empty;
- the content is plausibly within the expected Nicaragua context.

B. geometry_valid

Whether all polygon geometries pass topology validation.

C. analytical_ready

Whether analytical derivatives may be generated without repair.

Do not introduce a large new validation framework.

Prefer extending current validation results or adding a few clearly named
fields.

SOURCE KML RETENTION

A source KML that is acquisition_valid must be preserved even if one or more
geometries have topology warnings.

Topology warnings must not cause an otherwise valid source KML to be deleted.

For every retained source KML, record:

- level;
- official source URL;
- layer name;
- retrieval mode;
- retrieval timestamp;
- acquisition status;
- geometry validation status;
- invalid geometry count;
- affected feature identifiers when available;
- original feature count;
- source SHA-256;
- repair requested;
- repair applied;
- generated analytical formats;
- warnings.

Continue rejecting:

- malformed XML;
- OGC error XML;
- unexpected HTML;
- empty KML;
- GroundOverlay-only KML;
- NetworkLink-only KML;
- non-polygonal unexpected content;
- clearly implausible source responses.

ANALYTICAL FORMAT POLICY

For GeoPackage, GeoJSON, and Shapefile:

1. Valid geometries:
   - generate analytical formats normally.

2. Invalid geometries and repair=False:
   - preserve the original KML;
   - preserve validation reports and metadata;
   - skip analytical derivatives for that level;
   - continue processing the remaining selected levels;
   - explain the reason clearly.

3. Invalid geometries and repair=True:
   - preserve the original KML unchanged;
   - repair only an analytical working copy;
   - validate the repaired copy;
   - generate analytical formats only if post-repair validation passes;
   - record the repair method;
   - record original and repaired checksums separately;
   - preserve original institutional attributes and codes.

Never repair silently.

Keep repair=False as the package and CLI default.

ONE-ACTION MULTI-LEVEL DOWNLOAD

The public notebook must provide clear controls for:

- Nivel 4;
- Nivel 5;
- Nivel 6;
- Nivel 7;
- Seleccionar todos los niveles;
- Seleccionar solo nivel 4.

The user must be able to download levels 4–7 in one action.

Level 4 remains selected by default.

Levels 5–7 remain unselected by default.

The workflow must:

1. process selected levels sequentially;
2. preserve successful KML files;
3. continue when one level has topology warnings;
4. produce one final ZIP;
5. include all successfully retained original KML files;
6. include analytical formats successfully generated;
7. include validation reports, manifests, provenance, and checksums;
8. show one final summary by level.

Do not implement a generic workflow engine.

Adapt existing loops and result aggregation with the smallest maintainable
change.

PUBLIC NOTEBOOK LEVEL GUIDANCE

Replace the compressed horizontal selector with a clearly visible vertical or
two-column layout.

Display beginner-readable context:

- Nivel 4 — última auditoría: 12 unidades; sin advertencias topológicas conocidas.
- Nivel 5 — última auditoría: 68 unidades; 2 advertencias topológicas conocidas.
- Nivel 6 — última auditoría: 491 unidades; 1 advertencia topológica conocida.
- Nivel 7 — última auditoría: 2,337 unidades; 2 advertencias topológicas conocidas.

Clarify:

- these counts are reference values from the last verified audit;
- they may change if the institutional source is updated;
- topology warnings do not mean that the KML file cannot be downloaded;
- topology warnings affect analytical conversion unless repair is enabled.

EXPLICIT REPAIR CONTROL

Add a visible checkbox:

Reparar geometrías inválidas para generar formatos analíticos

Default:

False

Display help text:

“La reparación es opcional. El KML oficial original se conserva sin cambios.
La reparación se aplica únicamente a una copia destinada a formatos analíticos
y queda registrada en el manifiesto y la auditoría.”

Pass the value directly to the existing repair behavior.

Do not add unnecessary confirmation dialogs.

BEGINNER-FACING WORKFLOW GUIDANCE

The notebook must guide the user through a simple numbered flow.

Use descriptive headings similar to:

1. Instalar la herramienta
2. Elegir los datos y formatos
3. Descargar y preparar los archivos
4. Descargar el ZIP final
5. Alternativa opcional: importar un KML manual

At the beginning, include a concise explanation:

“Este notebook obtiene unidades hidrográficas oficiales de INETER. Usted puede
descargar el KML original o preparar formatos para análisis geoespacial. No
necesita conocer Python para usar los controles principales.”

STEP-BY-STEP STATUS MESSAGES

During execution, show clear progress messages.

Use messages equivalent to:

- “Preparando la descarga…”
- “Niveles seleccionados: 4, 5, 6, 7.”
- “Formato solicitado: GeoPackage.”
- “Reparación geométrica: desactivada.”
- “Conectando con el servicio oficial de INETER…”
- “Descargando nivel 4…”
- “Nivel 4 descargado correctamente.”
- “Validando estructura del KML…”
- “Revisando geometrías…”
- “Nivel 5 descargado. Se detectaron 2 advertencias topológicas.”
- “El KML original se conservará.”
- “No se generará GeoPackage para nivel 5 porque la reparación está
  desactivada.”
- “Continuando con el siguiente nivel…”
- “Generando manifiesto, auditoría y checksums…”
- “Creando ZIP final…”
- “Proceso completado.”

Do not expose raw internal implementation details unless the user opens an
optional technical-details output.

PROGRESS BY LEVEL

Show progress per level when practical:

- waiting;
- downloading;
- downloaded;
- validating;
- source preserved;
- analytical conversion completed;
- completed with warnings;
- failed.

Do not mislabel warnings as complete failure.

EXPECTED ERROR HANDLING

Catch expected validation and source-quality exceptions in public notebook
callbacks.

Do not show raw Python tracebacks for expected cases.

Show a concise message with:

- affected level;
- whether the official KML was retained;
- invalid geometry count;
- repair status;
- whether analytical formats were generated;
- next recommended action.

Example:

“Se descargó correctamente el KML del nivel 5, pero contiene 2 geometrías con
advertencias topológicas. El archivo original fue conservado. Active la opción
de reparación si necesita generar GeoPackage, GeoJSON o Shapefile para este
nivel.”

Unexpected programming errors may show:

- a short beginner-readable explanation;
- an expandable technical-details section.

OUTPUT LOCATION EXPLANATION

The notebook must clearly explain:

- `/content` is temporary storage inside the current Colab session;
- files stored there are not automatically saved to the user’s computer;
- the user must download the ZIP or choose Google Drive;
- temporary files disappear when the Colab session ends.

Display a message equivalent to:

“El archivo se creó temporalmente dentro de Colab. Use el botón ‘Descargar ZIP
a mi computadora’ antes de cerrar la sesión.”

FINAL ZIP DELIVERY

After a successful or partially successful run:

1. display the summary table;
2. display the final ZIP path;
3. explain whether the location is temporary Colab storage or Google Drive;
4. display a prominent button:

   Descargar ZIP a mi computadora

5. enable the button only when the archive exists;
6. ensure it points to the latest archive;
7. call the Colab file-download mechanism only after the user clicks;
8. if Google Drive was selected, show the exact Drive location.

Do not require the beginner to execute a separate hidden or distant code cell
to retrieve the ZIP.

The existing final-download cell may remain as a fallback, but the primary
workflow must provide the download control immediately after completion.

RESULT SUMMARY

Display a beginner-readable table with:

- Nivel
- KML oficial descargado
- Estado de adquisición
- Estado geométrico
- Geometrías con advertencias
- Reparación solicitada
- Reparación aplicada
- Registros encontrados
- Formatos analíticos generados
- Advertencias
- Resultado

Use values such as:

- Correcto
- Correcto con advertencias
- Omitido
- Reparado
- No solicitado
- Falló

Do not mark a retained source KML as failed solely because it contains topology
warnings.

MANUAL IMPORT FALLBACK

Keep the manual-upload capability because it provides resilience and
reproducibility.

Its purpose must be stated clearly:

- it is not the normal next step;
- it is used only when the official server is unavailable;
- it is useful when the user already has an official KML;
- it allows validation, conversion, and packaging without downloading again;
- it allows reprocessing the exact same historical source file.

Rename the section:

Alternativa opcional: importar un KML descargado manualmente

Add explanatory text:

“Use esta sección únicamente si la descarga automática falla o si ya dispone de
un KML oficial. No necesita usarla después de una descarga automática
correcta.”

Replace immediate execution of files.upload() with:

- level dropdown;
- optional repair checkbox;
- button: Cargar KML manualmente;
- status output;
- result summary;
- ZIP download button.

Running all notebook cells must not automatically open the file chooser.

Do not require the user to edit Python code such as:

MANUAL_LEVEL = 4

MANUAL DOWNLOAD GUIDANCE

When automatic access fails:

1. show the exact official URL;
2. explain that it may be opened in a normal browser;
3. explain how to save the KML;
4. direct the user to the optional manual-import section;
5. do not suggest bypassing institutional controls.

Do not display fallback guidance after a successful automatic run unless the
user opens or reads that optional section.

REPEATED EXECUTION AND STATE

Ensure:

- buttons are disabled while processing;
- buttons are re-enabled after success or failure;
- progress resets appropriately;
- previous outputs are not confused with the latest run;
- output directories are uniquely named or safely cleaned;
- LAST_RESULT represents the latest execution;
- the ZIP button references the latest archive;
- a second run does not mix files from the first run.

COMMENTS AND CODE READABILITY

Add concise comments in notebook code where they help future maintainers.

Comments should explain:

- why original KML is preserved;
- why topology validation is separate;
- why repair is explicit;
- why manual import is optional;
- why `/content` is temporary;
- why downloads are sequential.

Do not over-comment obvious Python syntax.

Avoid implementation comments that confuse beginner users.

Keep technical comments inside code and user guidance in Markdown cells.

SCOPE CONTROL

Do not:

- add new providers;
- redesign the CLI;
- redesign the developer notebook;
- add quarantine infrastructure;
- add a database;
- add an API;
- add a web application;
- add a generic results engine;
- add a provenance framework;
- repeat authorship work;
- repeat AI-transparency work;
- recreate the repository;
- change repository visibility;
- create a release;
- create a tag.

TESTS

Add only tests directly required by this correction.

Verify:

1. acquisition-valid KML with topology warnings is retained;
2. malformed KML remains rejected;
3. OGC error responses remain rejected;
4. HTML responses remain rejected;
5. N5-like source with two invalid geometries is preserved;
6. analytical derivatives are skipped when repair=False;
7. analytical derivatives are generated when repair=True and post-repair
   validation succeeds;
8. original and repaired checksums remain separate;
9. one level with warnings does not stop the remaining selected levels;
10. all-level selection resolves to levels 4, 5, 6, and 7;
11. level 4 remains selected by default;
12. manual file picker is not triggered by Run all;
13. manual upload occurs only after button click;
14. ZIP button appears only when a ZIP exists;
15. `/content` temporary-storage guidance exists;
16. expected topology warnings do not emit raw traceback;
17. notebook remains valid nbformat;
18. bootstrap remains functional;
19. developer notebook remains unchanged.

Do not add tests only to increase the count.

DOCUMENTATION

Update only when necessary:

- docs/BEGINNER_GUIDE.es.md
- docs/DATA_GOVERNANCE.md
- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- docs/PUBLICATION_CHECKLIST.md
- CHANGELOG.md
- prompts/PROMPT_REGISTRY.md

Archive this complete prompt at:

prompts/NicaGeoFetch_CodexDesktop_MVP1_ColabSourceRetentionDeliveryUX_v1.0.md

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

Run one polite live test for level 4.

Do not repeatedly download levels 5–7 solely for automated tests.

Use existing seed evidence and synthetic fixtures for topology-warning behavior.

GIT AND CI

After all local gates pass:

1. create one or two logical commits;
2. push normally to origin/main;
3. do not force push;
4. wait for GitHub Actions;
5. verify all required jobs are green;
6. do not create a tag;
7. do not create a release.

ACCEPTANCE CRITERIA

This task is complete only when:

1. original KML files for levels 4–7 can be obtained in one action;
2. topology warnings do not discard valid source KML files;
3. analytical outputs remain strict;
4. repair is explicit, optional, and audited;
5. level 4 remains selected by default;
6. all-level selection is available;
7. users understand what the tool is doing during execution;
8. progress is reported clearly by level and task;
9. users understand the difference between original KML and analytical formats;
10. users understand that /content is temporary;
11. the final ZIP can be downloaded from the primary workflow;
12. manual import is clearly optional and purposeful;
13. Run all does not open a file picker;
14. expected topology warnings do not expose raw tracebacks;
15. successful and warning states are distinguished;
16. all local quality gates pass;
17. GitHub Actions are green;
18. changes are pushed;
19. no release is created;
20. HANDOFF.md identifies human public-Colab retesting as NEXT_ACTION.

FINAL RESPONSE

Report:

1. Prompt tag executed.
2. Root cause and validation-policy decision.
3. Files changed.
4. Source-retention behavior.
5. N5–N7 behavior without repair.
6. N5–N7 behavior with repair.
7. All-level download behavior.
8. Beginner-guidance improvements.
9. Progress and status-message behavior.
10. ZIP delivery behavior.
11. Manual fallback behavior and purpose.
12. Tests added or updated.
13. Local quality gates.
14. Live N4 result.
15. GitHub Actions result.
16. Push result.
17. Remaining human Colab tests.
18. Commit hashes.
19. Git status.
20. HANDOFF.md location.
