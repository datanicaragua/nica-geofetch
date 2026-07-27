# Decision log

## D001 - Project identity

**Decision:** Use ecosystem `DataNicaTools`, project `Nica-GeoFetch`, repository
`nica-geofetch`, package `nica_geofetch`, CLI `nica-geofetch`, and notebook
`NicaGeoFetch_Colab.ipynb`.

**Rationale:** The name clearly communicates national context, geospatial scope,
and reproducible retrieval while keeping ecosystem and implementation names
consistent.

## D002 - KML instead of WFS

**Decision:** Use the official WMS KML reflector with encoded `layers`,
`mode=download`, `kmattr=true`, and `kmplacemark=true`. Do not depend on WFS.

**Rationale:** Prior verification found that the target layers were not exposed
as WFS FeatureTypes. KML is the observed institutional access path.

## D003 - No public data mirroring in MVP-1

**Decision:** Publish software, URLs, metadata, checksums, audit summaries,
conversion tools, documentation, and synthetic fixtures only.

**Rationale:** A mirror expands operational and legal responsibility before
dataset redistribution rights and maintenance capacity are established.

## D004 - GeoPackage is the recommended analytical format

**Decision:** Preserve KML and support GeoJSON/Shapefile compatibility, but
recommend GeoPackage for analysis.

**Rationale:** GeoPackage supports Unicode, long field names, explicit CRS,
multiple geometry types and layers, and fewer sidecar-file hazards.

## D005 - Separate software and dataset licensing

**Decision:** License source code and synthetic fixtures under Apache-2.0.
Treat institutional datasets as third-party content under their own terms.

**Rationale:** A software license cannot grant rights in independently sourced
institutional data. No explicit open-data license has been identified here.

## D006 - No web UI before downloader stability

**Decision:** MVP-1 exposes a Python API, technical CLI, and beginner Colab
notebook only.

**Rationale:** Stable download, validation, provenance, and recovery semantics
are prerequisites for a responsible public UI or service.

## D007 - Small provider interface

**Decision:** Implement one concrete provider behind a minimal abstract
interface; do not build a plugin marketplace.

**Rationale:** A single provider cannot justify a generalized framework.
Extension seams exist without speculative complexity.

## D008 - Validate before atomic rename

**Decision:** Remote bytes stay in a `.part` file until provider-specific KML
validation passes, then move atomically to the final raw path.

**Rationale:** HTTP success does not prove usable vector KML; servers can return
OGC XML errors, HTML, raster overlays, or malformed content.

## D009 - Compact metadata-origin groups

**Decision:** Extend the existing validation report and source manifest with a
compact `metadata_basis` grouping instead of adding a provenance framework or
field-level ontology.

**Rationale:** MVP-1 must distinguish institutional statements from detected,
inferred, derived, user-supplied, and unknown metadata. Controlled groups meet
that need while keeping the manifest readable and backward-compatible with its
version 2 source fields.

## D010 - Explicit source relationship and component value gates

**Decision:** Record source relationships from a small controlled vocabulary,
prohibit silent substitution, and defer proposed components that cannot answer
the six questions in the architecture component value gate.

**Rationale:** Comparable data can be useful without being equivalent. Explicit
identity and value evidence prevent source ambiguity and speculative
architecture.

## D011 - Stable public-notebook release pin

**Decision:** Commit `GIT_REF = "v0.1.0"` as the public beginner notebook
default while retaining deliberate advanced-user override and package-ZIP
fallback.

**Rationale:** A stable Git tag gives beginner runs a reproducible software
reference. The tag does not exist during release preparation, so local
pre-tag verification uses the built wheel and final fresh-Colab validation
remains a post-tag human gate.

## D012 - Source-archive-only v0.1.0 release assets

**Decision:** If a separately authorized GitHub Release is later created, do
not manually upload assets for v0.1.0; use only GitHub-generated source
archives.

**Rationale:** The software tree contains source, documentation, configuration,
tests, and clearly synthetic fixtures. Excluding manually uploaded runtime
archives and institutional artifacts reduces legal-distribution and accidental
data-publication risk without broadening Apache-2.0 to third-party data.
