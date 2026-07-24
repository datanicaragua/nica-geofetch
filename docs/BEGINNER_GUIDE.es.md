# Guía para principiantes

Nica-GeoFetch permite obtener o importar unidades hidrográficas de INETER,
revisarlas y convertirlas a formatos de análisis sin esconder la procedencia.

## Opción recomendada: Google Colab

1. Abra `notebooks/NicaGeoFetch_Colab.ipynb` en Colab.
2. Ejecute la celda de instalación. Antes de la primera versión instala desde
   `main`; para una versión publicada use una etiqueta estable. Si GitHub no
   funciona, seleccione la instalación mediante ZIP del paquete.
3. Seleccione el proveedor INETER.
4. Marque uno o más niveles: 4, 5, 6 y 7.
5. Elija KML, GeoPackage, GeoJSON, Shapefile ZIP o todos.
6. Use almacenamiento temporal. Monte Google Drive solo si lo selecciona
   explícitamente y entiende dónde se guardarán los archivos.
7. Pulse **Diagnosticar acceso**.
8. Si el acceso funciona, pulse **Descargar y validar**.
9. Si falla, abra la URL oficial indicada en el navegador, descargue el KML y
   use la carga manual.
10. Revise la tabla final y descargue el ZIP.

GeoPackage es el formato recomendado para análisis. Shapefile tiene nombres de
campo limitados; el ZIP incluye `field_name_mapping.csv`.

## Privacidad y permisos

El cuaderno no publica datos. Google Drive se monta únicamente tras una
selección explícita. No desactive la validación TLS. El acceso técnico a una
URL no equivale a permiso de redistribución.

## Alternativa sin widgets

El cuaderno incluye una celda de configuración simple. Edite las variables
`LEVELS`, `FORMATS`, `OUTPUT_LOCATION` y `MANUAL_KML`, y ejecute el flujo
correspondiente.

`NicaGeoFetch_Developer.ipynb` no es para principiantes: requiere una copia
local del repositorio y usa instalación editable.
