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
- Beginner-readable Colab bootstrap diagnostics, immediate package import
  verification, and guards that stop downstream imports after a failed install.
- Professional project authorship and proportionate AI-assisted-development
  disclosure.
- Public Colab controls for selecting all levels, explicit analytical repair,
  per-level progress, immediate ZIP delivery, and button-triggered manual KML
  import.
- Separate acquisition, original-geometry, and analytical-readiness statuses
  with retained-source and repair-checksum evidence.
- A concise `LEEME_RESULTADOS.md` in every final ZIP, listing retained source
  files, generated analytical files, skipped outputs, and audit/provenance
  locations.
- Dynamic Colab preflight expectations and per-level Spanish result
  explanations based on selected levels, formats, repair state, and the latest
  verified audit.

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
- Governance now records the ISO 8601/UTC update policy without adding
  manually maintained dates to the README files.
- The existing GitHub repository was activated publicly after local audit and
  Python 3.11/3.12 CI passed; no release or institutional data was published.
- Acquisition-valid source KML is now retained when topology warnings are
  present. Without repair, only analytical derivatives for the affected level
  are skipped; with explicit repair, the unchanged source and repaired
  analytical working-copy checksums are recorded separately.
- Every completed workflow includes retained original KML in the final ZIP,
  even when the selected analytical format cannot be generated for a warning
  level.
- The public Colab now has static five-step guidance, one authoritative
  automatic ZIP button, a subordinate manual fallback, compact result columns,
  localized common warnings, and collapsed implementation cells.
- Final archives use descriptive level/format/UTC names and preserve separate
  per-level analytical outputs; all-level selection still means one execution
  and one ZIP, not one consolidated GeoPackage.
- Nontrivial repository changes now use the documented task-branch, draft-PR,
  CI, independent-review, and human-approval workflow.
