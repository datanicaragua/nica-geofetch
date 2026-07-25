# Nica-GeoFetch

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/datanicaragua/nica-geofetch/blob/main/notebooks/NicaGeoFetch_Colab.ipynb)

**A reproducible acquisition, validation, provenance, and preparation layer for
institutional datasets used across the DataNicaTools ecosystem.**

Nica-GeoFetch supplies trusted foundational datasets to downstream notebooks,
analyses, models, and applications. It is not itself an end-user risk, climate,
health, agriculture, hydrology, or other thematic application. MVP-1 implements
one reference family: INETER's 2025 Pfafstetter-adjusted national hydrographic
units, levels 4-7.

> The software is Apache-2.0 licensed. Institutional datasets are third-party
> material and are **not** covered by that license. See [DATA_TERMS.md](DATA_TERMS.md)
> before redistributing data.

## Install

Python 3.11 and 3.12 are supported.

```bash
python -m pip install -e ".[dev]"
```

## Technical quick start

```bash
nica-geofetch providers list
nica-geofetch datasets list --provider ineter-pfafstetter
nica-geofetch diagnose --provider ineter-pfafstetter
nica-geofetch download --provider ineter-pfafstetter \
  --levels 4 5 6 7 --formats kml gpkg geojson shapefile --output outputs
```

If institutional access is unavailable, download a KML manually using the
official URL emitted by `diagnose`, then continue completely offline:

```bash
nica-geofetch import-local --level 4 --input level4.kml \
  --formats gpkg geojson shapefile --output outputs
```

GeoPackage is the recommended analytical format. GeoJSON is convenient for
interchange, and the Shapefile ZIP exists for compatibility.

## Beginner flow

Open the public [NicaGeoFetch_Colab.ipynb](notebooks/NicaGeoFetch_Colab.ipynb)
by itself in a fresh Google Colab runtime. It installs from the configurable
Git ref at `https://github.com/datanicaragua/nica-geofetch`, also supports
manual package ZIP upload, uses package APIs, defaults to temporary storage,
and mounts Google Drive only after an explicit choice. Before the first release
the default ref is `main`; released workflows should pin a stable tag.

Repository contributors should instead use
[NicaGeoFetch_Developer.ipynb](notebooks/NicaGeoFetch_Developer.ipynb), which
requires the repository root and installs in editable mode.

## Security and reproducibility

- HTTPS certificate verification is enabled by default.
- Only configured INETER hosts are accepted, including redirects.
- Requests are sequential, bounded, retried only for transient failures, and
  identify this project through a User-Agent.
- Downloads use `.part` files and are renamed atomically only after validation.
- Every workflow writes validation findings, source provenance, and SHA-256
  checksums.
- Real KML files and converted institutional datasets are excluded from Git.

## Documentation

Start at [docs/index.md](docs/index.md). The current implementation state is in
[docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md), and the operational resume
point is [docs/HANDOFF.md](docs/HANDOFF.md). The first provider's access and
non-equivalence lessons are documented in the
[INETER Pfafstetter case study](docs/CASE_STUDY_INETER_PFAFSTETTER.md).

## Scope

MVP-1 is deliberately not a web application, public mirror, service, database,
or generalized plugin platform. The documented long-term direction is in
[docs/STRATEGIC_VISION.md](docs/STRATEGIC_VISION.md).
