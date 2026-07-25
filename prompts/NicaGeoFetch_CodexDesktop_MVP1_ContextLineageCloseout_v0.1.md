Continue work in the existing repository:

C:\Dev\nica-geofetch

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_ContextLineageCloseout_v0.1

PROMPT VERSION
0.1

STATUS
READY FOR EXECUTION

TARGET
Codex Desktop

PROJECT
Nica-GeoFetch

MILESTONE
MVP-1 — Context, provenance, and public-release closeout

PURPOSE

Perform a final, narrowly scoped contextual and data-lineage closeout before
the repository is published to GitHub.

The software implementation and public-release hardening are already complete.
Do not redesign the package, add new providers, introduce a web UI, or expand
the MVP into a general data platform.

This task must clarify:

1. why Nica-GeoFetch exists;
2. its role as a foundational data-access layer in DataNicaTools;
3. how source provenance and derived metadata are represented;
4. how authoritative and alternative sources are distinguished;
5. why INETER Pfafstetter is the first reference case;
6. why global products such as HydroBASINS must not be treated as silently
   interchangeable with the national INETER adjustment;
7. how future components must justify their value before implementation.

FIRST READ

Read in this order:

1. AGENTS.md
2. docs/index.md
3. docs/PROJECT_STATUS.md
4. docs/HANDOFF.md
5. docs/STRATEGIC_VISION.md
6. docs/ARCHITECTURE.md
7. docs/DATA_GOVERNANCE.md
8. docs/PROVIDER_DEVELOPMENT.md
9. docs/LEGAL_AND_ATTRIBUTION.md
10. docs/ROADMAP.md
11. docs/PUBLICATION_CHECKLIST.md
12. docs/SEED_AUDIT.md
13. registry/datasets.yml
14. configs/providers/ineter_pfafstetter_2025.yml
15. current manifest and provenance models
16. prompts/PROMPT_REGISTRY.md

Then inspect:

- git status;
- current branch;
- recent commits;
- existing tests;
- current manifest fields;
- notebook output metadata.

Do not assume that a requested capability is missing until the repository has
been inspected.

SCOPE

This task may:

- improve existing documentation;
- create one focused case-study document;
- add minimal provenance fields when they are currently absent;
- add small tests for provenance semantics;
- update the dataset registry;
- update continuity and prompt records.

This task must not:

- implement another provider;
- add HydroBASINS support;
- add automated repository searching;
- add a crawler;
- add STAC;
- add PROV-O;
- add a database;
- add a web application;
- add an API;
- redesign the CLI;
- redesign the notebooks;
- add institutional datasets to Git;
- create a remote;
- push;
- publish;
- create a release.

STRATEGIC POSITIONING

Update docs/STRATEGIC_VISION.md and the main READMEs so that Nica-GeoFetch is
described consistently as:

“A reproducible acquisition, validation, provenance, and preparation layer for
institutional datasets used across the DataNicaTools ecosystem.”

Spanish:

“Una capa reproducible de adquisición, validación, procedencia y preparación
de datos institucionales para el ecosistema DataNicaTools.”

Explain that Nica-GeoFetch is not an end-user risk, climate, health, agriculture,
or hydrology application.

It supplies trusted foundational datasets to downstream notebooks, analyses,
models, and applications.

Mention future thematic domains only as roadmap areas:

- hydrology;
- climate;
- drought and flooding;
- ecosystems;
- protected areas;
- population;
- municipalities;
- economy;
- agriculture and AgTech;
- health;
- infrastructure;
- natural hazards;
- territorial planning.

Do not implement them.

COMPONENT VALUE RULE

Add a concise “component value gate” to AGENTS.md and an appropriate durable
architecture or governance document.

Before a future component is added, it must answer:

1. Which user or workflow needs it?
2. What concrete problem does it solve?
3. Why are existing components insufficient?
4. What acceptance test will demonstrate value?
5. What maintenance burden does it add?
6. Can it be deferred without breaking the core workflow?

State that components without a clear answer should remain deferred.

Keep AGENTS.md concise and link to the durable document for full guidance.

PROVENANCE AND LINEAGE

Audit the current source manifests, models, reports, and dataset registry.

Preserve the existing implementation when it already satisfies the requirements.

Ensure that generated provenance can distinguish at least:

- source institution;
- provider identifier;
- dataset identifier;
- source layer name;
- exact source URL;
- retrieval mode:
  - remote_download;
  - manual_import;
  - seed_input;
- retrieval timestamp UTC;
- original source format;
- source byte size;
- original SHA-256;
- generated artifact SHA-256;
- transformation steps;
- selected level;
- feature or Placemark count;
- geometry count and type;
- CRS;
- validation status;
- warnings;
- software version;
- provider configuration version.

METADATA ORIGIN

Nica-GeoFetch may derive or infer technical metadata, but it must never present
inferred information as metadata explicitly supplied by the institution.

Where practical within the current architecture, represent the origin of
important metadata using a small controlled vocabulary:

- source_declared;
- detected;
- inferred;
- derived;
- user_supplied;
- unknown.

Examples:

- dataset year inferred from a layer name;
- CRS detected by a geospatial driver;
- feature count derived during validation;
- title declared by the source;
- local file supplied by the user.

Do not build an elaborate metadata ontology.

If adding field-level origin tracking would substantially complicate the MVP,
use a compact provenance section such as:

metadata_basis:
  source_declared: [...]
  detected: [...]
  inferred: [...]
  derived: [...]
  user_supplied: [...]
  uncertainties: [...]

Document the design decision.

SOURCE RELATIONSHIP POLICY

Document a small controlled vocabulary for relationships between datasets and
sources:

- authoritative;
- official_mirror;
- institutional_copy;
- derived_from_authoritative;
- comparable_not_equivalent;
- fallback_non_equivalent;
- unverified.

Explain:

- no source is silently substituted;
- alternative use requires explicit selection;
- source relationship must be recorded in provenance;
- a global product must not inherit the identifier of a national official
  product;
- unavailable does not mean equivalent alternatives can be presented as the
  same dataset.

Do not implement automatic source discovery in this milestone.

SOURCE RESOLUTION GUIDANCE

Update docs/PROVIDER_DEVELOPMENT.md or docs/DATA_GOVERNANCE.md with a
lightweight source-resolution sequence:

1. official primary source;
2. another service from the same institution;
3. official or institutional mirror;
4. academic repository linked to the producer;
5. regional institutional repository;
6. comparable international product;
7. unverified source.

Document that this is a human-guided provider-development method, not an
automated search feature.

CASE STUDY

Create:

docs/CASE_STUDY_INETER_PFAFSTETTER.md

The document must be concise, evidence-aware, and understandable to technical
users, researchers, and future contributors.

Include:

1. Problem context
   - national hydrographic units were visible but not straightforward to
     retrieve as vectors;
   - WFS did not expose the target FeatureTypes;
   - the WMS KML reflector provided vector KML.

2. Why this case matters
   - foundational hydrological boundaries;
   - relevance for drought, flooding, watershed analysis, risk assessment, and
     territorial integration;
   - example of institutional data that exists but is difficult to access
     reproducibly.

3. Why the INETER adjustment is preferred for this provider
   - it is the national institutional reference being targeted;
   - it reflects a Nicaragua-specific implementation and adjustment;
   - downstream users may require consistency with national codes and
     institutional cartography.

4. Relationship to HydroBASINS
   - HydroBASINS is a valid global standardized product;
   - it is useful for regional, continental, and cross-country analysis;
   - it must not be assumed geometrically, hierarchically, or institutionally
     identical to the national INETER adjustment;
   - it may become a future provider classified as
     comparable_not_equivalent or fallback_non_equivalent;
   - it must never be silently substituted for INETER under the same dataset
     identifier.

5. Unavailability behavior
   - retry only transient failures;
   - diagnose DNS, TLS, firewall, timeout, HTTP, and OGC failures;
   - show the official URL for manual retrieval;
   - allow local import;
   - record the retrieval mode;
   - do not bypass controls;
   - do not silently substitute another source.

6. Data limitations
   - incomplete source metadata;
   - inferred metadata must be labeled;
   - possible invalid geometries;
   - duplicated or unexpected codes;
   - current legal and redistribution uncertainty.

7. Lessons for future providers
   - access protocol and data existence are different issues;
   - HTTP 200 does not prove successful data retrieval;
   - lineage and validation are part of acquisition;
   - provider-specific logic should remain small and testable.

Do not make unsupported historical, legal, cartographic-scale, or methodological
claims.

Clearly distinguish:

- verified repository evidence;
- known institutional statements;
- inferred interpretations;
- unresolved questions.

DATASET REGISTRY

Audit registry/datasets.yml.

Ensure the INETER Pfafstetter entry includes, when supported by the current
schema:

- thematic domain;
- source institution;
- source relationship: authoritative;
- access protocol;
- official endpoint;
- configured levels;
- source format;
- supported output formats;
- redistribution status;
- license status;
- provider implementation status;
- provenance status;
- last live verification date;
- quality warnings;
- metadata completeness status;
- comparable datasets note.

Do not register HydroBASINS as implemented.

It may appear only as a planned comparable dataset with status:

planned

and relationship:

comparable_not_equivalent

Do not add speculative provider URLs or unsupported metadata.

DOCUMENTATION CONSISTENCY

Update only the documents that need changes.

At minimum inspect and, when appropriate, update:

- README.md
- README.es.md
- AGENTS.md
- docs/STRATEGIC_VISION.md
- docs/ARCHITECTURE.md
- docs/DATA_GOVERNANCE.md
- docs/PROVIDER_DEVELOPMENT.md
- docs/ROADMAP.md
- docs/index.md
- docs/PUBLICATION_CHECKLIST.md
- registry/datasets.yml

Add the case study to docs/index.md.

Avoid duplicated long explanations across multiple files. Establish one
canonical document and link to it.

TESTING

Add or update tests only when code or manifest semantics change.

Tests should verify, where applicable:

1. retrieval_mode remains explicit;
2. source URL and layer are retained;
3. source and derived checksums remain distinguishable;
4. metadata origin values use the controlled vocabulary;
5. source relationship uses the controlled vocabulary;
6. a comparable source cannot silently replace an authoritative dataset;
7. existing manifests remain backward compatible when practical;
8. documentation links are valid;
9. registry entries are parseable;
10. the public notebook behavior remains unchanged.

Do not add tests solely to inflate test counts.

COMPLEXITY CONTROL

Before introducing any new Python module, class, schema file, or abstraction,
document why the existing implementation cannot support the requirement.

Prefer extending existing models and documents.

Do not add:

- a generic provenance framework;
- a plugin framework;
- an ontology library;
- a metadata database;
- a source search engine.

QUALITY GATES

Run:

python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest -q
pre-commit run --all-files

Validate both notebooks using the existing notebook checks.

Run the publication audit.

Do not require another live INETER download unless a code change affects remote
download behavior.

If no download code changes, preserve the previously recorded successful N4
live-test evidence.

CONTINUITY

Update:

- CHANGELOG.md
- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- docs/ROADMAP.md
- docs/PUBLICATION_CHECKLIST.md
- prompts/PROMPT_REGISTRY.md

Archive this prompt at:

prompts/NicaGeoFetch_CodexDesktop_MVP1_ContextLineageCloseout_v0.1.md

Record the resulting commit hash in PROMPT_REGISTRY.md.

COMMIT

Create one or two logical local commits only after all applicable quality gates
pass.

Do not create a remote.
Do not push.
Do not publish.
Do not create a GitHub release.
Do not change repository visibility.

ACCEPTANCE CRITERIA

This closeout is complete only when:

1. Nica-GeoFetch is consistently described as a foundational DataNicaTools
   data-acquisition and provenance layer.
2. The component value gate is documented.
3. The provenance model clearly distinguishes source, inferred, detected, and
   derived information.
4. Source relationships and non-equivalence are documented.
5. The INETER Pfafstetter case study exists and is indexed.
6. HydroBASINS is not implemented or presented as equivalent.
7. The dataset registry reflects current verified status.
8. No unnecessary architecture was added.
9. Existing CLI and notebook workflows remain functional.
10. All applicable quality gates pass.
11. No institutional data is tracked.
12. PROJECT_STATUS.md and HANDOFF.md identify GitHub publication as the next
    action.
13. The working tree is clean or all remaining changes are documented.

FINAL RESPONSE

Report:

1. Prompt tag executed.
2. Files changed.
3. Strategic positioning improvements.
4. Provenance and lineage changes.
5. Metadata-origin design.
6. Source relationship policy.
7. INETER case-study summary.
8. Any code changes and why they were necessary.
9. Tests added or changed.
10. All quality-gate results.
11. Publication audit result.
12. Remaining blockers.
13. Exact next action for GitHub publication.
14. Git status.
15. Local commit hashes.
16. HANDOFF.md location.

Do not claim that MVP-1 is publicly released.

Do not claim that INETER and HydroBASINS are equivalent.

Do not add new capabilities merely because they might be useful later.
