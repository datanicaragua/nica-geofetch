# Nica-GeoFetch

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/datanicaragua/nica-geofetch/blob/main/notebooks/NicaGeoFetch_Colab.ipynb)

**Adquiera, valide, documente y prepare de forma reproducible los datos
geoespaciales institucionales de Nicaragua para usos posteriores confiables.**

> La licencia Apache-2.0 cubre el software Nica-GeoFetch, no los datos
> institucionales. Los datos de INETER son material de terceros sin una
> licencia explícita de datos abiertos identificada. Lea
> [DATA_TERMS.md](DATA_TERMS.md) antes de usar o redistribuir datos.

## Ruta recomendada para principiantes: Colab

El cuaderno público
[NicaGeoFetch_Colab.ipynb](notebooks/NicaGeoFetch_Colab.ipynb) es el punto de
inicio recomendado. Usa de forma predeterminada la etiqueta estable de software
`v0.1.0`, guarda temporalmente en Colab salvo que se seleccione Google Drive de
forma explícita y no requiere credenciales de GitHub.

1. Abra el cuaderno de Colab.
2. Ejecute las celdas numeradas y seleccione niveles y formatos.
3. Revise el resumen de auditoría y descargue el ZIP final.

## Instalación local estable

Se admiten Python 3.11 y 3.12. Instale el software desde la etiqueta estable de
Git:

```bash
python -m pip install \
  "nica-geofetch @ git+https://github.com/datanicaragua/nica-geofetch.git@v0.1.0"
```

No se publica un paquete en PyPI para v0.1.0.

## Inicio rápido técnico con CLI

```bash
nica-geofetch providers list
nica-geofetch datasets list --provider ineter-pfafstetter
nica-geofetch diagnose --provider ineter-pfafstetter
nica-geofetch download --provider ineter-pfafstetter \
  --levels 4 5 6 7 --formats kml gpkg geojson shapefile --output outputs
```

## Respaldo y uso avanzado

Si no hay acceso institucional, use la URL oficial que muestra `diagnose` para
descargar un KML manualmente y continúe sin conexión:

```bash
nica-geofetch import-local --level 4 --input nivel4.kml \
  --formats gpkg geojson shapefile --output outputs
```

GeoPackage es el formato analítico recomendado. GeoJSON facilita el
intercambio y el ZIP de Shapefile ofrece compatibilidad. Los usuarios avanzados
del cuaderno pueden cambiar `GIT_REF` deliberadamente; quienes contribuyen al
repositorio deben usar
[NicaGeoFetch_Developer.ipynb](notebooks/NicaGeoFetch_Developer.ipynb) y la
instalación editable documentada en [CONTRIBUTING.md](CONTRIBUTING.md).

Los resultados preparados pueden aportar unidades hidrográficas trazables para
análisis climáticos o agrícolas por cuenca, geometrías auditables de cuencas
para flujos de riesgo o recursos hídricos e insumos reproducibles para análisis
SIG. Nica-GeoFetch prepara datos fundamentales; no realiza esos análisis
temáticos posteriores.

## Limitaciones y reproducibilidad

- El MVP-1 admite únicamente las unidades hidrográficas nacionales de INETER
  ajustadas a Pfafstetter en 2025, niveles 4-7.
- Los niveles 5, 6 y 7 tienen 2, 1 y 2 geometrías fuente inválidas conocidas.
- Se conserva el KML original. Sin reparación explícita, se omiten los
  derivados analíticos del nivel afectado; la reparación se aplica sólo a una
  copia analítica y queda auditada.
- La disponibilidad, el esquema y los términos de la fuente institucional
  pueden cambiar.
- La verificación HTTPS y los controles de host permanecen activos; las
  descargas son secuenciales, limitadas y registradas con procedencia y SHA-256.
- El Git y la versión de software excluyen KML institucionales reales y datos
  convertidos.

## Documentación

Comience en [docs/index.md](docs/index.md). El estado actual se registra en
[docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md) y la continuidad operativa en
[docs/HANDOFF.md](docs/HANDOFF.md). El
[caso de estudio de INETER Pfafstetter](docs/CASE_STUDY_INETER_PFAFSTETTER.md)
explica acceso, linaje y no equivalencia. La transparencia del proceso se
documenta en
[desarrollo asistido por IA](docs/AI_ASSISTED_DEVELOPMENT.md).

## Soporte

Reporte errores reproducibles en
[GitHub Issues](https://github.com/datanicaragua/nica-geofetch/issues) usando
únicamente datos sintéticos o redactados. No cargue datos institucionales,
credenciales, detalles de proxy ni rutas privadas. Reporte vulnerabilidades
según [SECURITY.md](SECURITY.md). Dirija las preguntas sobre derechos de los
datos de INETER a la institución fuente. No se garantizan tiempos de respuesta
de mantenimiento.

## Citación

Consulte [CITATION.cff](CITATION.cff). Cite por separado:

1. Nica-GeoFetch como software.
2. INETER como institución fuente de los datos hidrográficos.

No presente conversiones ni derivados de Nica-GeoFetch como productos
oficiales de INETER.

## Autoría y liderazgo del proyecto

**Gustavo Ernesto Martínez Cárdenas**

Científico de Datos Principal y Arquitecto de DataNicaTools

- [DataNicaTools](https://github.com/datanicaragua)
- [GitHub](https://github.com/gustavoemc)
- [LinkedIn](https://www.linkedin.com/in/gustavoernestom)

Desarrollado como parte del ecosistema DataNicaTools.

## Alcance

El MVP-1 no es una aplicación temática, aplicación web, espejo público,
servicio, base de datos ni plataforma generalizada de complementos. La
dirección de largo plazo está documentada en
[docs/STRATEGIC_VISION.md](docs/STRATEGIC_VISION.md).
