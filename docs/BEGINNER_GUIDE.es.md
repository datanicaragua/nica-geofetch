# Guía para principiantes

Nica-GeoFetch permite obtener o importar unidades hidrográficas de INETER,
revisarlas y convertirlas a formatos de análisis sin esconder la procedencia.

Nica-GeoFetch descarga y conserva los KML oficiales originales. Después revisa
su geometría y, cuando se solicita, prepara formatos analíticos como
GeoPackage, GeoJSON y Shapefile. La reparación geométrica es opcional, explícita
y queda registrada.

## Opción recomendada: Google Colab

1. Abra `notebooks/NicaGeoFetch_Colab.ipynb` en Colab.
2. Ejecute la celda de instalación. La referencia predeterminada es la etiqueta
   estable `v0.1.0`; los usuarios avanzados pueden cambiar `GIT_REF`
   deliberadamente. Si GitHub no funciona, use `INSTALL_SOURCE = "zip"` y
   cargue el paquete. No pegue tokens de GitHub en el cuaderno.
3. El nivel 4 comienza seleccionado. Marque uno o más niveles o use
   **Seleccionar todos los niveles** para procesar 4, 5, 6 y 7 en una acción.
4. Elija KML, GeoPackage, GeoJSON, Shapefile ZIP o todos. GeoPackage es el
   formato recomendado para análisis.
5. Mantenga la reparación desactivada si sólo necesita los KML originales.
   Actívela explícitamente si necesita derivados analíticos de niveles con
   advertencias topológicas.
6. Use almacenamiento temporal. Monte Google Drive sólo si lo selecciona
   explícitamente y entiende dónde se guardarán los archivos.
7. Pulse **Diagnosticar acceso**.
8. Si el acceso funciona, pulse **Descargar y preparar**. Los niveles se
   descargan secuencialmente y el progreso se muestra por nivel.
9. Revise la tabla compacta y la explicación por nivel. **Correcto con
   advertencias** significa que el KML fuente fue conservado, aunque uno o más
   derivados analíticos se omitieron.
10. Pulse **Descargar ZIP a mi computadora** antes de cerrar Colab.

Los valores de la última auditoría son 12, 68, 491 y 2,337 unidades para niveles
4, 5, 6 y 7. Los niveles 5, 6 y 7 tuvieron 2, 1 y 2 geometrías con advertencias,
respectivamente. Son referencias y pueden cambiar si INETER actualiza la
fuente. Una advertencia topológica no impide descargar el KML.

Shapefile tiene nombres de campo limitados; el ZIP incluye
`field_name_mapping.csv`.

## Qué contiene el ZIP

`raw/` contiene los KML institucionales originales, conservados sin reparación
geométrica ni modificación analítica. `processed/` contiene únicamente los
formatos analíticos generados a partir de geometrías válidas o de una copia
analítica reparada explícitamente.

Cada nivel tiene su propio archivo analítico. Por ejemplo,
`processed/pfaf_level4.gpkg` contiene sólo el nivel 4. Seleccionar todos los
niveles significa una ejecución y un ZIP final, no un GeoPackage consolidado.
Con reparación desactivada, todos los KML seleccionados pueden quedar en
`raw/`, mientras los niveles con advertencias topológicas pueden no tener el
formato solicitado en `processed/`.

Cada ZIP incluye `LEEME_RESULTADOS.md`, con las rutas exactas de fuentes
conservadas y derivados generados u omitidos, además de los motivos de omisión
y las ubicaciones de auditoría y procedencia.

## Dónde quedan los archivos

`/content` es almacenamiento temporal dentro de la sesión de Colab. No se
guarda automáticamente en la computadora y desaparece al finalizar la sesión.
El ZIP generado tampoco está todavía en su computadora: pulse el único botón
azul **Descargar ZIP a mi computadora**. Si seleccionó Google Drive, el
notebook muestra la ruta exacta bajo
`MyDrive/NicaGeoFetch_outputs/`.

Cada ejecución usa una carpeta distinta y los botones quedan desactivados
mientras trabajan, de modo que una segunda ejecución no se mezcla con la
anterior.

## Alternativa opcional: importación manual

La sección **¿No funcionó la descarga automática?** es un respaldo para
continuidad durante una caída del servicio, una red bloqueada, conversión sin
conexión o reprocesamiento reproducible de una fuente histórica. No se necesita
después de una descarga automática correcta.

La sección muestra un selector de nivel, una opción de reparación y el botón
**Cargar KML manualmente**. Usa y muestra el formato analítico elegido en el
paso 2. Ejecutar todas las celdas no abre el selector de archivos; se abre
únicamente después de pulsar el botón. Su archivo final se obtiene con el botón
separado **Descargar ZIP de importación manual**.

Si la descarga automática falla, copie la URL oficial mostrada, ábrala en un
navegador normal, guarde el KML y cárguelo en esa sección. No evada controles
institucionales.

## Privacidad y permisos

El cuaderno no publica datos. Google Drive se monta únicamente tras una
selección explícita. No desactive la validación TLS. El acceso técnico a una
URL no equivale a permiso de redistribución.

`NicaGeoFetch_Developer.ipynb` no es para principiantes: requiere una copia
local del repositorio y usa instalación editable.
