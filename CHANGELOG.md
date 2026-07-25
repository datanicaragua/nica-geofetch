# Changelog

All notable changes are documented here.

## [Unreleased]

### Added

- MVP-1 foundation for the INETER Pfafstetter 2025 provider.
- Secure download, KML validation, offline import, conversion, provenance,
  deterministic packaging, CLI, Colab notebook, and offline tests.
- Self-bootstrapping public Colab notebook with configurable Git ref and package
  ZIP fallback.
- Repository-local developer notebook with editable installation.
- Publication checklist and tracked-file/institutional-data/secret audit.
- INETER Pfafstetter case study, controlled source relationships, metadata-origin
  groups, component value gate, and registry lineage status.

### Changed

- Validation reports and source manifests now distinguish `remote_download`,
  `manual_import`, and `seed_input`.
- Remote manifests now record source URL/layer, retrieval time/mode, response
  content type, byte size, SHA-256, validation status, and feature counts.
- Public repository metadata now targets
  `https://github.com/datanicaragua/nica-geofetch`.
- Source manifest schema version 3 retains version 2 fields while adding source
  institution/relationship, metadata basis, format/CRS/geometry facts,
  transformation steps, software/configuration versions, warnings, and
  source-versus-generated artifact SHA-256 values.
