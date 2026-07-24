# Phase log

## 2026-07-24 - Phase 0: inspect and establish baseline

- Inspected the empty repository and initialized local Git on `main`.
- Audited four ignored KML seed files without copying feature data.
- Found 12, 68, 491, and 2,337 placemarks for levels 4-7.
- Derived source aliases: `n4`, `n5`, `n6_`, and `code_pfafs` (level 7).
- Noted that level 6-7 placemark names are identifiers rather than codes, so
  HTML description attributes must take priority.
- Extracted and visually verified the rights statement on page 4 of the
  36-page 2014 reference album.
- Initial install exposed the expected ordering issue that `README.md` did not
  yet exist; governance scaffolding corrected it.

## 2026-07-24 - Phase 1: governance and continuity (in progress)

- Added bilingual project identity, contribution, security, software/data
  licensing separation, registry, provider configuration, strategic vision,
  architecture, roadmap, legal, governance, beginner, troubleshooting, and
  continuity documentation.
- Added a concise agent resume protocol and explicit no-push/no-publication rules.
- Relevant checks: seed audit passed; packaging checks pending.

## 2026-07-24 - Phase 2: core provider

- Implemented Unicode-safe official URL construction, HTTPS/host/redirect
  enforcement, bounded retries/backoff, timeouts, size and disk limits,
  Requests proxy support, custom CA support, `.part` files, and atomic rename.
- Implemented access diagnostics and manual browser-download guidance.
- Implemented streaming KML/XML/OGC/HTML/vector validation, GeoServer HTML
  attribute extraction, Pfaf alias normalization, provenance fields,
  code-length/bounds/duplicate checks, and opt-in geometry repair.
- Ruff and mypy passed after the phase.

## 2026-07-24 - Phase 3: conversion and packaging

- Implemented and reopened GeoPackage, GeoJSON, and Shapefile ZIP outputs.
- Added deterministic Shapefile field mapping, required-component checks,
  audit reports, source manifest, provenance summary, SHA-256 file map, and
  deterministic final ZIP.
- Processed the supplied level 4 KML offline into all four formats: 12 polygon
  features, no geometry repair, one preserved code-length warning.
- Validated levels 5-7 and recorded 2, 1, and 2 invalid source geometries.
  Explicit repair produced valid results while recording every repair.

## 2026-07-24 - Phase 4: interfaces

- Implemented all requested CLI commands.
- Added a Spanish Colab notebook with provider/level/format/output controls,
  access diagnosis, sequential download, manual upload fallback, simple-cell
  fallback, final summary, and ZIP download.

## 2026-07-24 - Phase 5: quality assurance (in progress)

- Added 27 offline tests covering the requested network, validation,
  conversion, interface, notebook, and continuity behaviors.
- Current evidence: 27 tests passed; ruff passed; mypy passed; CLI help passed.
- Final clean rerun and closeout metadata remain.
