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

Source URL, retrieval time, original SHA-256, provider ID, dataset ID, level,
and transformation outputs are recorded. Raw feature values are retained in
converted outputs, while committed audit summaries include only counts,
schemas, sizes, and checksums.

## Extension seam

A future provider implements the small base interface and receives its own
configuration, validation rules, synthetic fixtures, and governance record.
Generic code should be extended only when a second real provider demonstrates
a shared need.
