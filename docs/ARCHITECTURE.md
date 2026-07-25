# Architecture

## Design goals

The MVP separates institutional-source concerns from reusable workflow
mechanics without creating a plugin framework. Each layer is independently
testable with synthetic local data.

```text
CLI / Colab notebook
        |
        v
INETER provider ---- provider configuration / dataset registry
        |
        +---- URL construction and access diagnostics
        +---- secure sequential downloader
        |
        v
KML validator ---- XML / OGC / vector / attributes / geometry / bounds
        |
        v
normalized features (EPSG:4326 + provenance)
        |
        +---- GeoPackage
        +---- GeoJSON
        +---- Shapefile ZIP + field mapping
        |
        v
audit reports / manifest / checksums / deterministic final ZIP
```

## Modules

- `config.py` loads and validates provider YAML with safe built-in defaults.
- `providers/base.py` defines the small provider interface.
- `providers/ineter_pfafstetter.py` is the only MVP provider.
- `download.py` owns HTTPS, host/redirect validation, retries, size limits,
  `.part` files, and atomic finalization.
- `diagnostics.py` translates network failures into user-actionable categories.
- `validation.py` streams untrusted KML, parses provider attributes, and creates
  normalized polygon features.
- `conversion.py` writes and reopens each supported analytical output.
- `manifests.py` produces provenance, reports, and checksums.
- `packaging.py` assembles the final deterministic archive.
- `cli.py` and the notebook call provider/workflow functions; neither duplicates
  business rules.

## Data flow and trust boundaries

Remote bytes and manually supplied files are untrusted. A remote response stays
at a `.part` path until KML validation succeeds. Local imports are never
modified. Geometry repair is opt-in and recorded. Converted files are reopened
before a workflow reports success.

Source institution, provider and dataset IDs, source relationship, URL/layer,
retrieval mode/time, original format/size/SHA-256, level, validation results,
geometry/CRS facts, software/configuration versions, transformation steps, and
generated-artifact SHA-256 values are recorded. Raw feature values are retained
in converted outputs, while committed audit summaries include only counts,
schemas, sizes, and checksums.

Manifest schema version 3 retains the version 2 source fields and adds a compact
`metadata_basis` section. Its controlled origin categories are
`source_declared`, `detected`, `inferred`, `derived`, `user_supplied`, and
`unknown`, plus an `uncertainties` list. This field-level grouping is sufficient
to avoid presenting inference as institutional metadata without introducing a
metadata ontology. For example, the dataset year and source CRS are inferred,
geometry types are detected, counts and hashes are derived, and a local import
path is user-supplied.

The source-relationship policy is canonical in
[DATA_GOVERNANCE.md](DATA_GOVERNANCE.md).

## Extension seam

A future provider implements the small base interface and receives its own
configuration, validation rules, synthetic fixtures, and governance record.
Generic code should be extended only when a second real provider demonstrates
a shared need.

## Component value gate

Before a future component is implemented, its proposal must answer:

1. Which user or workflow needs it?
2. What concrete problem does it solve?
3. Why are existing components insufficient?
4. What acceptance test will demonstrate value?
5. What maintenance burden does it add?
6. Can it be deferred without breaking the core workflow?

A component without clear answers remains deferred. This gate applies before
new modules, services, schemas, provider abstractions, interfaces, or thematic
features are added.
