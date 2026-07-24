# Roadmap

## Current MVP - MVP-1 foundation

- One provider: `ineter-pfafstetter`.
- One reference family: 2025 hydrographic units, levels 4-7.
- Secure sequential KML retrieval with manual fallback.
- XML, vector, attribute, Pfaf code, geometry, and bounds validation.
- KML, GeoPackage, GeoJSON, and Shapefile ZIP output.
- Audits, provenance, checksums, final ZIP, CLI, Colab notebook, and offline tests.

MVP-1 is complete. Every acceptance command and the offline real-seed level 4
workflow pass as recorded in `PROJECT_STATUS.md`.

## Next milestone - MVP-2 hardening and source clarification

1. Obtain and record an authoritative INETER statement for licensing,
   redistribution, attribution, and update cadence of the 2025 GeoServer layers.
2. Run scheduled human-supervised live checks and compare source schema/count
   drift without mirroring data.
3. Improve diagnostics from real field reports while keeping the provider
   interface small.
4. Publish a versioned schema contract for normalized Pfafstetter outputs.
5. Add Python 3.11 and 3.12 CI evidence on synthetic fixtures.

## Medium term

- Mature the dataset registry with availability and quality review workflows.
- Add a second provider only after a source/governance readiness review.
- Define standardized national base-layer conventions and cross-dataset metadata.
- Add richer provenance exchange and catalog export.

## Long term

- A lightweight interoperability layer for stable normalized datasets.
- DataNicaTools integration for hydrology, climate, hazards, ecosystems,
  agriculture, population, economy, health, infrastructure, and planning.

## Explicitly deferred

Web applications, Streamlit, Gradio, REST APIs, database servers,
authentication, cloud deployment, public data mirrors, background scraping,
parallel mass downloads, automatic publication, and a generalized plugin
marketplace are outside MVP-1.
