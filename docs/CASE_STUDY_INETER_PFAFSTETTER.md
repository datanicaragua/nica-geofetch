# Case study: INETER Pfafstetter 2025

This case study explains why the first Nica-GeoFetch provider targets one
specific national institutional dataset and how its lineage is preserved. It
does not claim that the source is openly licensed or that another basin product
is equivalent.

## Evidence boundaries

- **Verified repository evidence:** configured GeoServer URLs, WFS/KML access
  observations recorded by the project, synthetic tests, seed-audit counts,
  validation findings, and the successful 2026-07-24 level 4 live test.
- **Known institutional statements:** the configured layer names identify
  INETER, national hydrographic units, Pfafstetter adjustment, levels 4-7, and
  2025. The separate 2014 album rights statement is summarized in
  [LEGAL_AND_ATTRIBUTION.md](LEGAL_AND_ATTRIBUTION.md).
- **Inferred interpretation:** the year is inferred from layer names; the source
  CRS is inferred from KML semantics; analytical relevance is a project
  interpretation, not an institutional suitability statement.
- **Unresolved questions:** complete institutional metadata, production method,
  update cadence, explicit license, redistribution permission, and formal
  equivalence to other basin products.

## 1. Problem context

The national hydrographic units were visible through institutional mapping
services but were not straightforward to retrieve as vectors. Repository
verification found that WFS did not expose the target FeatureTypes. The INETER
GeoServer WMS KML reflector, with explicit layer and download parameters,
returned vector KML instead. Nica-GeoFetch makes that observed access path
deterministic and validates the response before accepting it as data.

## 2. Why this case matters

Hydrographic boundaries are foundational inputs for watershed analysis and may
support downstream drought, flooding, risk, and territorial-integration
workflows. This provider is therefore a useful reference case for institutional
data that exists but is difficult to acquire reproducibly. Nica-GeoFetch
prepares the boundary data; it does not perform those thematic analyses.

## 3. Why the INETER adjustment is preferred

This provider deliberately targets the national institutional reference
identified by INETER's configured 2025 layers. It is represented with the
relationship `authoritative` for this dataset identity. The layer names and
observed attributes indicate a Nicaragua-specific Pfafstetter adjustment.
Downstream work may require consistency with the national codes and
institutional cartography, so the provider preserves source values, layer
identity, checksums, and warnings rather than silently normalizing them to a
different product.

This preference is provider scope, not a claim that the project has verified
the source's complete production methodology or fitness for every use.

## 4. Relationship to HydroBASINS

HydroBASINS is a valid global standardized basin product and can be useful for
regional, continental, and cross-country analysis. It is not assumed to be
geometrically, hierarchically, or institutionally identical to the national
INETER adjustment.

A future HydroBASINS provider could be evaluated as
`comparable_not_equivalent` or `fallback_non_equivalent`. It would require a
distinct dataset identifier, explicit selection, its own provenance, and its
own acceptance evidence. It must never be silently substituted for INETER
under `ineter-pfafstetter-2025`. MVP-1 does not implement HydroBASINS.

## 5. Behavior when the source is unavailable

The downloader retries only failures classified as transient. Diagnostics
distinguish DNS, TLS, firewall/proxy, timeout, HTTP, and OGC response failures.
They show the exact official URL so a user can attempt controlled manual
retrieval, then import that local KML through the same validation and conversion
workflow.

The resulting provenance records `remote_download` or `manual_import` as
appropriate. The workflow does not disable TLS controls, bypass network policy,
search for replacements, or silently substitute another source.

## 6. Data limitations

Institutional source metadata is incomplete in the current evidence. Inferred,
detected, derived, and user-supplied metadata are labeled separately in manifest
schema version 3. Seed validation found invalid geometries in levels 5-7 and
duplicate or unexpected code patterns in some levels; repair is explicit and
recorded. These are repository observations, not corrections to institutional
values.

No explicit open-data license has been identified for the 2025 layers.
Redistribution rights remain unresolved, so real KML and converted
institutional data must not be committed or attached to a software release.

## 7. Lessons for future providers

- Data existence and access-protocol availability are different questions.
- HTTP 200 alone does not demonstrate successful vector-data retrieval.
- Lineage, validation, and non-equivalence are part of acquisition.
- Manual fallback should preserve the same validation and provenance semantics.
- Provider-specific URL and parsing logic should remain small and testable.
- A new component or provider must pass the
  [component value gate](ARCHITECTURE.md#component-value-gate) before
  implementation.
