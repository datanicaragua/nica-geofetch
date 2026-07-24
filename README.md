# Nica-GeoFetch

**Reproducible access to trusted institutional geodata for Nicaragua.**

Nica-GeoFetch is a focused Python package and technical CLI for discovering,
downloading, validating, converting, and packaging institutional geospatial
datasets with reproducible provenance. MVP-1 implements one dataset family:
INETER's 2025 Pfafstetter-adjusted national hydrographic units, levels 4-7.

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

Open [notebooks/NicaGeoFetch_Colab.ipynb](notebooks/NicaGeoFetch_Colab.ipynb)
in Google Colab. The notebook is in Spanish, uses package functions, defaults
to temporary Colab storage, and mounts Google Drive only after an explicit
choice.

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
point is [docs/HANDOFF.md](docs/HANDOFF.md).

## Scope

MVP-1 is deliberately not a web application, public mirror, service, database,
or generalized plugin platform. The documented long-term direction is in
[docs/STRATEGIC_VISION.md](docs/STRATEGIC_VISION.md).
