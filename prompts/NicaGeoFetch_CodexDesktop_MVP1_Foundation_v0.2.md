You are the founding software architect and implementation lead for a new
DataNicaTools open-source project.

PROMPT METADATA

Prompt Tag:
NicaGeoFetch_CodexDesktop_MVP1_Foundation_v0.2

Prompt Version:
0.2

Prompt Status:
AUDITED — READY FOR EXECUTION

Target Agent:
Codex Desktop

Project:
Nica-GeoFetch

Repository:
nica-geofetch

Milestone:
MVP-1 — Foundation and INETER Pfafstetter Provider

PURPOSE OF THIS PROMPT

Build the first focused, production-quality MVP of Nica-GeoFetch.

Nica-GeoFetch is not merely a downloader. Its long-term purpose is to become a
reproducible access and interoperability layer for trusted institutional
geospatial datasets relevant to Nicaragua.

The MVP must remain intentionally small:

- one implemented provider;
- one reference dataset family;
- one reusable Python package;
- one technical CLI;
- one beginner-friendly Google Colab notebook;
- strong validation, provenance, security, documentation, and project
  continuity.

Do not implement the future platform in this milestone. Document its strategic
direction and provide an architecture that can grow without rewriting the MVP.

PROJECT IDENTITY AND BRAND

Project name:

Nica-GeoFetch

Meaning:

- “Nica” identifies Nicaragua and its national context.
- “Geo” identifies geospatial information.
- “Fetch” communicates reproducible discovery and retrieval from trusted
  institutional sources.

English descriptor:

Reproducible access to trusted institutional geodata for Nicaragua.

Spanish descriptor:

Acceso reproducible a geodatos institucionales de Nicaragua.

Spanish tagline:

Descubre, descarga, valida y prepara datos geoespaciales confiables de
Nicaragua.

Brand hierarchy:

- Ecosystem: DataNicaTools
- Project: Nica-GeoFetch
- Repository: nica-geofetch
- Python package: nica_geofetch
- CLI command: nica-geofetch
- Colab notebook: NicaGeoFetch_Colab.ipynb

STRATEGIC VISION

Create docs/STRATEGIC_VISION.md.

The document must explain that Nica-GeoFetch will evolve through these stages:

Stage 1 — Reproducible downloader

Discover, download, validate, convert, and package institutional geospatial
datasets.

Stage 2 — Dataset registry

Maintain a structured catalog of sources, institutions, access protocols,
formats, licenses, provenance, availability, and quality status.

Stage 3 — Standardized national base layers

Provide reproducible workflows for foundational datasets used by technical
users, researchers, universities, municipalities, NGOs, and public-interest
projects.

Stage 4 — Interoperability layer

Expose normalized datasets through Python APIs, CLI workflows, catalogs,
metadata standards, and eventually lightweight services.

Stage 5 — DataNicaTools integration

Support domain applications and analyses in:

- hydrology;
- climate;
- drought;
- flooding;
- natural hazards;
- ecosystems;
- protected areas;
- agriculture and AgTech;
- population;
- economy;
- health;
- infrastructure;
- territorial planning.

Only Stage 1 is implemented in this MVP. The remaining stages are documented,
not built.

PRIMARY MVP USE CASE

Implement access to:

INETER Pfafstetter-adjusted national hydrographic units, 2025,
levels 4, 5, 6, and 7.

The layers are available through the INETER GeoServer WMS KML reflector.

Configured layers:

- wsINETER-RH:Unidad_Hidrológica_Nacional_nivel4_2025
- wsINETER-RH:Unidad_Hidrológica_Nacional_nivel5_2025
- wsINETER-RH:Unidad_Hidrológica_Nacional_nivel6_2025
- wsINETER-RH:Unidad_Hidrológica_Nacional_nivel7_2025

Official endpoint:

https://geoserveridefn.ineter.gob.ni/geoserver/wms/kml

Required parameters:

- layers=<exact layer name>
- mode=download
- kmattr=true
- kmplacemark=true

Always construct query strings with urllib.parse.urlencode.

Do not depend on WFS for this provider. Previous verification demonstrated that
these layers are not currently exposed as WFS FeatureTypes.

SCOPE BOUNDARIES

This MVP must implement:

1. A reusable Python package.
2. One INETER Pfafstetter provider.
3. A command-line interface.
4. A beginner-friendly Google Colab notebook.
5. Manual KML import fallback.
6. KML validation and attribute extraction.
7. GeoPackage, GeoJSON, and Shapefile ZIP conversion.
8. Audit reports, provenance, and checksums.
9. Offline tests and an optional live test.
10. Strategic and continuity documentation.

This MVP must not implement:

- a web application;
- Streamlit;
- Gradio;
- a REST API;
- a database server;
- authentication;
- cloud deployment;
- a public data mirror;
- background scraping;
- parallel mass downloads;
- automatic publication;
- a generalized plugin marketplace.

OPERATING RULES

1. Work autonomously through the MVP.
2. Inspect the repository and seed_inputs/ before implementation.
3. Ask a question only when a missing decision would cause an irreversible,
   unsafe, or legally significant action.
4. Do not create a remote repository.
5. Do not push or publish anything.
6. Do not upload institutional data.
7. You may initialize local Git.
8. Create logical local commits after stable milestones.
9. Never report success unless acceptance criteria pass.
10. Keep the implementation understandable to future human and AI maintainers.
11. Do not over-engineer.
12. Target Python 3.11 and 3.12.

PROMPT VERSIONING

Create:

prompts/NicaGeoFetch_CodexDesktop_MVP1_Foundation_v0.2.md

Store this complete prompt there.

Create prompts/PROMPT_REGISTRY.md with:

- prompt tag;
- version;
- date;
- purpose;
- status;
- milestone;
- superseded prompt;
- execution status;
- resulting commits;
- notes.

Do not silently edit an executed prompt. New changes require a new version.

REPOSITORY CONTINUITY STRATEGY

Create these files:

- AGENTS.md
- docs/index.md
- docs/PROJECT_STATUS.md
- docs/PHASE_LOG.md
- docs/HANDOFF.md
- docs/ROADMAP.md
- docs/DECISION_LOG.md
- docs/STRATEGIC_VISION.md

AGENTS.md must remain concise. It must tell agents:

- what the project is;
- scope boundaries;
- required checks;
- where durable documentation lives;
- how to resume work;
- data licensing rules;
- prohibition against push and publication.

docs/index.md must describe and link all important project documentation.

PROJECT_STATUS.md must contain:

- current milestone;
- current branch;
- latest stable commit;
- implemented capabilities;
- tests status;
- current limitations;
- blocked items;
- next recommended action;
- last update timestamp.

PHASE_LOG.md must provide a chronological record of completed work.

HANDOFF.md must be an operational resume point containing:

- what was being done;
- what is complete;
- what is incomplete;
- exact next action;
- commands to verify the environment;
- commands to resume;
- known risks;
- relevant files;
- dirty working-tree files, if any.

ROADMAP.md must distinguish:

- current MVP;
- next milestone;
- medium-term capabilities;
- long-term vision;
- explicitly deferred features.

DECISION_LOG.md must document important decisions and their rationale, including:

- project name;
- KML instead of WFS;
- no public data mirroring in MVP;
- GeoPackage as recommended analytical format;
- separation between software and dataset licensing;
- no web UI before downloader stability.

RESUME PROTOCOL

Include this protocol in AGENTS.md:

Before continuing any future task:

1. Read AGENTS.md.
2. Read docs/index.md.
3. Read docs/PROJECT_STATUS.md.
4. Read docs/HANDOFF.md.
5. Review docs/ROADMAP.md.
6. Run git status.
7. Inspect the current branch and recent commits.
8. Run the documented smoke test.
9. Continue from NEXT_ACTION in HANDOFF.md.
10. Update PROJECT_STATUS.md, PHASE_LOG.md, and HANDOFF.md before stopping.

DATASET REGISTRY

Create:

registry/datasets.yml

Provide a small, documented schema with fields such as:

- dataset_id;
- title;
- institution;
- thematic_domain;
- geographic_scope;
- official_source_url;
- access_protocol;
- source_formats;
- supported_levels;
- expected_geometry;
- attribution;
- license_status;
- redistribution_status;
- provider_status;
- implementation_status;
- quality_status;
- last_checked_utc;
- update_frequency;
- contact;
- notes.

Register INETER Pfafstetter 2025 as implemented.

Register future datasets only as planned examples:

- rivers and water bodies;
- protected areas;
- ecosystems and land cover;
- municipalities and departments;
- elevation models;
- population;
- economic indicators;
- agricultural datasets;
- health facilities;
- infrastructure;
- climate and hydrometeorological data;
- natural-hazard and exposure datasets.

Do not implement future providers in MVP-1.

SOURCE DATA POLICY

License source code under Apache-2.0.

Institutional datasets are third-party data and are not covered by the software
license.

Do not describe INETER datasets as open data unless an explicit open-data
license is identified.

Do not commit real KML files or converted institutional datasets.

Publish only:

- downloader code;
- validation code;
- official source URLs;
- metadata;
- checksums;
- audit summaries;
- conversion tools;
- documentation;
- synthetic fixtures.

Document that the 2014 album:

- reserves publication rights;
- prohibits commercial reproduction and use;
- indicates that educational or divulgative reproduction requires prior INETER
  permission.

Do not provide legal advice. Explain the known statement and recommend
institutional clarification before public redistribution of complete data
copies.

INITIAL REPOSITORY STRUCTURE

Create approximately:

nica-geofetch/
├── AGENTS.md
├── README.md
├── README.es.md
├── LICENSE
├── NOTICE
├── DATA_TERMS.md
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── .gitignore
├── .editorconfig
├── .pre-commit-config.yaml
├── prompts/
│   ├── PROMPT_REGISTRY.md
│   └── NicaGeoFetch_CodexDesktop_MVP1_Foundation_v0.2.md
├── registry/
│   └── datasets.yml
├── configs/
│   └── providers/
│       └── ineter_pfafstetter_2025.yml
├── docs/
│   ├── index.md
│   ├── STRATEGIC_VISION.md
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   ├── PROJECT_STATUS.md
│   ├── PHASE_LOG.md
│   ├── HANDOFF.md
│   ├── DECISION_LOG.md
│   ├── DATA_GOVERNANCE.md
│   ├── LEGAL_AND_ATTRIBUTION.md
│   ├── PROVIDER_DEVELOPMENT.md
│   ├── BEGINNER_GUIDE.es.md
│   └── TROUBLESHOOTING.md
├── notebooks/
│   └── NicaGeoFetch_Colab.ipynb
├── src/
│   └── nica_geofetch/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── models.py
│       ├── exceptions.py
│       ├── diagnostics.py
│       ├── download.py
│       ├── validation.py
│       ├── conversion.py
│       ├── manifests.py
│       ├── packaging.py
│       ├── logging_utils.py
│       └── providers/
│           ├── __init__.py
│           ├── base.py
│           └── ineter_pfafstetter.py
├── tests/
│   ├── fixtures/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── scripts/
│   ├── audit_seed_inputs.py
│   └── run_live_integration_test.py
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── pull_request_template.md
    └── workflows/
        └── ci.yml

PROVIDER DESIGN

Use a small provider interface, not a complex plugin framework.

A provider must:

- identify available configured datasets;
- construct official source URLs;
- diagnose access;
- download selected resources;
- validate provider-specific content;
- return normalized results.

The INETER provider is the only implemented provider in MVP-1.

BEGINNER USER FLOW

The Colab notebook must provide:

1. Spanish introduction.
2. Provider selector.
3. Level checkboxes for 4, 5, 6, and 7.
4. Output format selector:
   - KML;
   - GeoPackage;
   - GeoJSON;
   - Shapefile ZIP;
   - all.
5. Output location:
   - Colab temporary storage;
   - Google Drive only after explicit selection.
6. Diagnosticar acceso action.
7. Descargar y validar action.
8. Progress and understandable logs.
9. Manual upload fallback.
10. Final summary table.
11. Final ZIP download.

Use package functions. Do not duplicate business logic in notebook cells.

Provide a plain configuration-cell fallback if widgets do not work.

TECHNICAL USER FLOW

Implement commands equivalent to:

nica-geofetch providers list

nica-geofetch datasets list --provider ineter-pfafstetter

nica-geofetch diagnose --provider ineter-pfafstetter

nica-geofetch download \
  --provider ineter-pfafstetter \
  --levels 4 5 6 7 \
  --formats kml gpkg geojson shapefile \
  --output ./outputs

nica-geofetch validate \
  --input ./level4.kml \
  --level 4

nica-geofetch import-local \
  --level 4 \
  --input ./level4.kml \
  --formats gpkg geojson shapefile \
  --output ./outputs

NETWORK AND SECURITY

Implement:

- HTTPS verification by default;
- allowed-host validation;
- redirect validation;
- Requests Session;
- sequential requests;
- bounded transient retries;
- exponential backoff;
- polite delay;
- identifiable User-Agent;
- response-size limits;
- configurable timeouts;
- temporary .part files;
- atomic rename after validation;
- proxy support through Requests environment variables;
- optional custom CA bundle;
- no SSL-disable control in the beginner notebook.

Classify:

- DNS failure;
- connection timeout;
- read timeout;
- TLS failure;
- proxy failure;
- HTTP failure;
- OGC XML error;
- unexpected HTML;
- malformed KML;
- empty KML;
- raster-only KML;
- invalid geometry;
- disk-space failure;
- permission failure.

Do not bypass firewalls, access controls, authentication, CAPTCHA, rate limits,
or administrative restrictions.

When remote access fails:

- produce a diagnostic report;
- provide the exact official URL;
- explain manual browser download;
- allow local upload;
- continue validation and conversion locally.

VALIDATION

For every KML:

1. Validate XML.
2. Detect OGC error documents.
3. Require Placemark.
4. Require Polygon or MultiGeometry.
5. Reject GroundOverlay-only and NetworkLink-only responses.
6. Parse Placemark names.
7. Parse HTML description tables.
8. Extract Pfafstetter codes using configured aliases.
9. Preserve raw values.
10. Add normalized provenance fields.
11. Validate code length against level.
12. Validate polygonal geometry.
13. Validate plausible Nicaragua bounds.
14. Report null, empty, duplicate, or invalid geometries.
15. Repair geometry only when explicitly requested.
16. Calculate SHA-256.

Inspect seed_inputs/ and derive actual field aliases and counts.

Do not commit real seed data. Commit only synthetic fixtures and non-sensitive
audit summaries.

CONVERSION

Support:

- original KML;
- GeoPackage;
- GeoJSON;
- Shapefile ZIP.

Use GeoPackage as the recommended analytical format.

Store one GeoPackage layer per level:

- pfaf_n4;
- pfaf_n5;
- pfaf_n6;
- pfaf_n7.

For Shapefile:

- deterministic names of at most 10 characters;
- collision prevention;
- field_name_mapping.csv;
- required components;
- UTF-8 where supported;
- reopen and verify the output.

Produce a final ZIP containing:

- raw files;
- processed files;
- audit_report.json;
- audit_report.md;
- source_manifest.json;
- checksums_sha256.json;
- provenance summary;
- field mappings.

TESTING

Use:

- pytest;
- pytest-cov;
- ruff;
- mypy where practical;
- pre-commit;
- nbformat;
- notebook smoke validation.

Live INETER access must not be required in CI.

Include tests for:

1. Unicode URL encoding.
2. Host allowlisting.
3. Redirect rejection.
4. HTTP 200 containing OGC error XML.
5. Vector KML detection.
6. Raster-only KML rejection.
7. Malformed KML.
8. Pfaf code extraction from names.
9. Pfaf code extraction from HTML descriptions.
10. Level/code-length validation.
11. Response-size limits.
12. Atomic file handling.
13. Checksums.
14. Shapefile field mapping.
15. Shapefile write and reopen.
16. Local import.
17. DNS diagnostic.
18. Timeout diagnostic.
19. Notebook structure.
20. CLI smoke tests.
21. Resume-document consistency.

Provide an opt-in live test controlled by:

RUN_INETER_LIVE_TEST=1

It must download only one level, use a polite request, clean temporary data,
and never run automatically in CI.

IMPLEMENTATION PHASES

Phase 0 — Inspect and establish baseline

- inspect seed_inputs;
- inspect environment;
- create initial plan;
- initialize local Git if necessary;
- create prompt registry.

Phase 1 — Governance and continuity

- scaffold repository;
- create AGENTS.md;
- create strategic and continuity documents;
- create dataset registry;
- create provider configuration.

Phase 2 — Core provider

- implement URL generation;
- diagnostics;
- remote download;
- local import;
- KML validation.

Phase 3 — Conversion and packaging

- implement output formats;
- provenance;
- reports;
- checksums;
- final packaging.

Phase 4 — Interfaces

- implement CLI;
- implement Colab notebook.

Phase 5 — Quality assurance

- tests;
- lint;
- typing;
- notebook checks;
- offline end-to-end workflow.

Phase 6 — Closeout

- update PROJECT_STATUS.md;
- update PHASE_LOG.md;
- update HANDOFF.md;
- update ROADMAP.md;
- update PROMPT_REGISTRY.md;
- make logical local commits;
- leave a clean working tree or document remaining changes.

At the end of every phase:

1. Run relevant tests.
2. Record results in PHASE_LOG.md.
3. Update PROJECT_STATUS.md.
4. Update HANDOFF.md.
5. Create a local checkpoint commit when stable.

ACCEPTANCE CRITERIA

The MVP is complete only when:

1. Installation succeeds:

   python -m pip install -e ".[dev]"

2. These succeed:

   ruff check .
   mypy src
   pytest -q
   python -m nica_geofetch.cli --help

3. Unit tests require no internet.

4. A supplied local seed KML can be processed offline.

5. Conversion succeeds for GeoPackage, GeoJSON, and Shapefile ZIP.

6. Generated outputs are reopened and validated.

7. The notebook is valid JSON and passes its smoke validation.

8. The live test is isolated and optional.

9. No real institutional dataset is tracked by Git.

10. The Apache license applies only to software.

11. Strategic vision and roadmap are documented.

12. Dataset registry exists and is extensible.

13. PROJECT_STATUS.md accurately reflects reality.

14. HANDOFF.md contains an executable next-action state.

15. PROMPT_REGISTRY.md records this prompt and its execution.

16. The repository remains a focused MVP.

FINAL RESPONSE

Report:

1. Repository path.
2. Current branch.
3. Prompt tag executed.
4. Architecture created.
5. Seed-input audit findings.
6. Implemented commands.
7. Test, lint, typing, and notebook results.
8. Security controls.
9. Legal and licensing limitations.
10. Strategic documentation created.
11. Current project status.
12. Remaining risks.
13. Exact next recommended milestone.
14. Git status.
15. Local commit hashes.
16. Location of HANDOFF.md.

Do not report success unless all applicable acceptance criteria pass.

If interrupted before completion:

- preserve working code;
- update PROJECT_STATUS.md;
- update PHASE_LOG.md;
- update HANDOFF.md;
- identify the exact failed command;
- identify the smallest next corrective action;
- do not claim the phase is complete.
