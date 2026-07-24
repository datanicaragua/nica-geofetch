# Nica-GeoFetch

**Acceso reproducible a geodatos institucionales de Nicaragua.**

Descubre, descarga, valida y prepara datos geoespaciales confiables de
Nicaragua. El MVP-1 implementa únicamente las unidades hidrográficas nacionales
ajustadas a Pfafstetter de INETER (2025), niveles 4, 5, 6 y 7.

## Instalación

```bash
python -m pip install -e ".[dev]"
```

## Uso rápido

```bash
nica-geofetch diagnose --provider ineter-pfafstetter
nica-geofetch download --provider ineter-pfafstetter \
  --levels 4 5 6 7 --formats kml gpkg geojson shapefile --output outputs
```

Si el acceso remoto falla, el diagnóstico muestra la URL oficial exacta. Se
puede descargar el KML manualmente con el navegador y continuar sin Internet:

```bash
nica-geofetch import-local --level 4 --input nivel4.kml \
  --formats gpkg geojson shapefile --output outputs
```

GeoPackage es el formato analítico recomendado. El cuaderno
[notebooks/NicaGeoFetch_Colab.ipynb](notebooks/NicaGeoFetch_Colab.ipynb)
ofrece un flujo introductorio en español.

## Términos de datos

Apache-2.0 cubre el software, no los datos institucionales de terceros. No se
afirma que los datos de INETER sean datos abiertos. Consulte
[DATA_TERMS.md](DATA_TERMS.md) y solicite aclaración institucional antes de
redistribuir copias completas.

La documentación central está enlazada desde [docs/index.md](docs/index.md).
