# Data governance

## Classification

| Artifact | Repository policy |
|---|---|
| Source code and synthetic fixtures | May be tracked under Apache-2.0 |
| Official source URLs and public metadata | May be tracked with attribution |
| Checksums and non-sensitive audit counts | May be tracked |
| Real KML/KMZ and converted institutional data | Never track or publish here |
| User output directories | Local and ignored |
| Diagnostic reports | Review for proxy paths or sensitive environment details |

## Handling rules

1. Keep seed data under ignored `seed_inputs/`.
2. Never copy real features into tests, examples, screenshots, or notebooks.
3. Synthetic fixtures must be visibly artificial and geographically plausible.
4. Audit scripts may report schemas, counts, sizes, and hashes but not bulk
   attribute values or coordinates.
5. Preserve source bytes as raw output; do not imply the converted form is an
   official INETER product.
6. Record transformation software version, timestamp, source URL, checksum,
   level, validation findings, and any requested geometry repair.
7. Do not publish or upload outputs automatically.

## Source retention and analytical readiness

An institutional KML that passes acquisition validation is retained byte for
byte even when a small number of polygon geometries fail topology checks.
Acquisition validity covers the HTTP/content response, parseable XML, local
polygonal Placemarks, non-empty content, and plausible geographic context.
Malformed XML, OGC errors, HTML, empty/raster-only/network-link-only KML, and
clearly implausible responses remain rejected.

Geometry validity is recorded separately. Without explicit repair, topology
warnings prevent analytical conversion for that level but do not delete or
mislabel the original KML; other selected levels continue. With explicit
repair, only the normalized analytical working copy is changed. The original
source SHA-256, working-copy SHA-256, repair method, affected identifiers, and
generated formats are recorded separately. Repair remains off by default.

## Metadata origin

Nica-GeoFetch may detect, infer, or derive technical metadata, but does not
present those observations as values explicitly supplied by an institution.
Generated manifest metadata uses the compact origin categories documented in
[ARCHITECTURE.md](ARCHITECTURE.md). `metadata_basis.uncertainties` identifies
unresolved license, redistribution, or completeness questions.

## Source relationships and substitution

Every implemented or planned source relationship uses one of these values:

| Relationship | Meaning |
|---|---|
| `authoritative` | Primary institutional reference targeted by the provider. |
| `official_mirror` | Officially operated mirror of the same source. |
| `institutional_copy` | Copy held by another institution, with lineage recorded. |
| `derived_from_authoritative` | Product created from the authoritative source through explicit transformations. |
| `comparable_not_equivalent` | Useful for comparison but not assumed identical. |
| `fallback_non_equivalent` | Explicit fallback that changes the data basis. |
| `unverified` | Relationship or lineage has not been established. |

No source is silently substituted. Alternatives require explicit selection and
their relationship must be recorded in provenance. A global product does not
inherit the identifier of a national official product. Source unavailability
does not make a comparable dataset equivalent; local import of the same
official source remains the MVP fallback.

The INETER/HydroBASINS distinction is applied concretely in
[CASE_STUDY_INETER_PFAFSTETTER.md](CASE_STUDY_INETER_PFAFSTETTER.md).

## License status

No explicit open-data license has been identified for the implemented 2025
layers. `license_status` and `redistribution_status` remain explicit registry
fields. Absence of a technical access barrier is not a redistribution grant.

## Date and update policy

1. Git commits, tags, and releases are the canonical software-history record.
2. `PROJECT_STATUS.md` and `HANDOFF.md` record `last_updated_utc`.
3. Dataset registry entries use `last_checked_utc` or
   `last_live_verified_utc` when applicable.
4. Manifests and audit reports retain retrieval, validation, and generation
   timestamps.
5. Case studies or source-access documents may use `Last reviewed` when their
   factual status can become stale.
6. Machine-readable timestamps use ISO 8601 and UTC.
7. README files avoid static update dates that create unnecessary manual
   maintenance.
