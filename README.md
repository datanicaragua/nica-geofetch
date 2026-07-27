# Nica-GeoFetch

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/datanicaragua/nica-geofetch/blob/main/notebooks/NicaGeoFetch_Colab.ipynb)

**Reproducibly acquire, validate, trace, and prepare Nicaragua's institutional
geodata for trustworthy downstream use.**

> The Apache-2.0 license covers the Nica-GeoFetch software, not institutional
> datasets. The INETER data is third-party material without an identified
> explicit open-data license. Read [DATA_TERMS.md](DATA_TERMS.md) before using
> or redistributing data.

## Recommended beginner path: Colab

The public [NicaGeoFetch_Colab.ipynb](notebooks/NicaGeoFetch_Colab.ipynb) is the
recommended starting point. It defaults to the stable `v0.1.0` software tag,
uses temporary Colab storage unless Google Drive is explicitly selected, and
does not require GitHub credentials.

1. Open the Colab notebook.
2. Run the numbered cells and select levels and formats.
3. Review the audit summary and download the final ZIP.

## Stable local installation

Python 3.11 and 3.12 are supported. Install the software from the stable Git
tag:

```bash
python -m pip install \
  "nica-geofetch @ git+https://github.com/datanicaragua/nica-geofetch.git@v0.1.0"
```

No PyPI package is published for v0.1.0.

## Technical CLI quickstart

```bash
nica-geofetch providers list
nica-geofetch datasets list --provider ineter-pfafstetter
nica-geofetch diagnose --provider ineter-pfafstetter
nica-geofetch download --provider ineter-pfafstetter \
  --levels 4 5 6 7 --formats kml gpkg geojson shapefile --output outputs
```

## Fallback and advanced use

If institutional access is unavailable, use the official URL emitted by
`diagnose` to download a KML manually, then continue offline:

```bash
nica-geofetch import-local --level 4 --input level4.kml \
  --formats gpkg geojson shapefile --output outputs
```

GeoPackage is the recommended analytical format. GeoJSON supports interchange,
and Shapefile ZIP supports compatibility. Advanced notebook users may
deliberately change `GIT_REF`; repository contributors should use
[NicaGeoFetch_Developer.ipynb](notebooks/NicaGeoFetch_Developer.ipynb) and the
editable setup documented in [CONTRIBUTING.md](CONTRIBUTING.md).

Prepared outputs can serve as traceable hydrographic units for
watershed-based climate or agricultural analysis, auditable basin geometries
for risk or water-resource workflows, and reproducible inputs for GIS
analysis. Nica-GeoFetch prepares foundational data; it does not perform those
downstream thematic analyses.

## Limitations and reproducibility

- MVP-1 supports only INETER's 2025 Pfafstetter-adjusted national hydrographic
  units, levels 4-7.
- Levels 5, 6, and 7 have 2, 1, and 2 known invalid source geometries.
- Original KML is retained. Without explicit repair, analytical derivatives
  for an affected level are omitted; repair applies only to an analytical copy
  and remains auditable.
- Institutional endpoint availability, schema, and terms may change.
- HTTPS verification and host checks remain enabled; downloads are sequential,
  bounded, and recorded with provenance and SHA-256 checksums.
- Real institutional KML and converted datasets are excluded from Git and the
  software release.

## Documentation

Start at [docs/index.md](docs/index.md). Current state is recorded in
[docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md), and operational continuity is
in [docs/HANDOFF.md](docs/HANDOFF.md). The
[INETER Pfafstetter case study](docs/CASE_STUDY_INETER_PFAFSTETTER.md) explains
source access, lineage, and non-equivalence. Development-process transparency
is documented in
[AI-assisted development](docs/AI_ASSISTED_DEVELOPMENT.md).

## Support

Report reproducible bugs in
[GitHub Issues](https://github.com/datanicaragua/nica-geofetch/issues) using
only synthetic or redacted data. Do not upload institutional datasets,
credentials, proxy details, or private paths. Report vulnerabilities through
[SECURITY.md](SECURITY.md). Direct questions about INETER data rights to the
source institution. Maintenance response times are not guaranteed.

## Citation

See [CITATION.cff](CITATION.cff). Cite both:

1. Nica-GeoFetch as software.
2. INETER as the source institution for the hydrographic data.

Do not represent Nica-GeoFetch conversions or derivatives as official INETER
products.

## Author and project leadership

**Gustavo Ernesto Martínez Cárdenas**

Lead Data Scientist and Architect, DataNicaTools

- [DataNicaTools](https://github.com/datanicaragua)
- [GitHub](https://github.com/gustavoemc)
- [LinkedIn](https://www.linkedin.com/in/gustavoernestom)

Developed as part of the DataNicaTools ecosystem.

## Scope

MVP-1 is deliberately not a thematic application, web application, public
mirror, service, database, or generalized plugin platform. The documented
long-term direction is in
[docs/STRATEGIC_VISION.md](docs/STRATEGIC_VISION.md).
