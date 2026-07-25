# Guía para principiantes

Nica-GeoFetch permite obtener o importar unidades hidrográficas de INETER,
revisarlas y convertirlas a formatos de análisis sin esconder la procedencia.

Nica-GeoFetch descarga y conserva los KML oficiales originales. Después revisa
su geometría y, cuando se solicita, prepara formatos analíticos como
GeoPackage, GeoJSON y Shapefile. La reparación geométrica es opcional, explícita
y queda registrada.

## Opción recomendada: Google Colab

1. Abra `notebooks/NicaGeoFetch_Colab.ipynb` en Colab.
2. Ejecute la celda de instalación. Antes de la primera versión instala desde
   `main`; para una versión publicada use una etiqueta estable. Si GitHub no
   funciona o el repositorio aún es privado, use `INSTALL_SOURCE = "zip"` y
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
9. Revise la tabla final. **Correcto con advertencias** significa que el KML
   oficial fue conservado, aunque sus derivados analíticos se omitieron porque
   la reparación estaba desactivada.
10. Pulse **Descargar ZIP a mi computadora** antes de cerrar Colab.

Los valores de la última auditoría son 12, 68, 491 y 2,337 unidades para niveles
4, 5, 6 y 7. Los niveles 5, 6 y 7 tuvieron 2, 1 y 2 geometrías con advertencias,
respectivamente. Son referencias y pueden cambiar si INETER actualiza la
fuente. Una advertencia topológica no impide descargar el KML.

Shapefile tiene nombres de campo limitados; el ZIP incluye
`field_name_mapping.csv`.

## Dónde quedan los archivos

`/content` es almacenamiento temporal dentro de la sesión de Colab. No se
guarda automáticamente en la computadora y desaparece al finalizar la sesión.
Descargue el ZIP con el botón visible junto al resultado. Si seleccionó Google
Drive, el notebook muestra la ruta exacta bajo
`MyDrive/NicaGeoFetch_outputs/`.

Cada ejecución usa una carpeta distinta y los botones quedan desactivados
mientras trabajan, de modo que una segunda ejecución no se mezcla con la
anterior.

## Alternativa opcional: importación manual

Use la importación manual sólo cuando el servidor oficial no esté disponible o
cuando ya tenga un KML oficial que desea reprocesar. La sección muestra un
selector de nivel, una opción de reparación y el botón **Cargar KML
manualmente**. Ejecutar todas las celdas no abre el selector de archivos; se
abre únicamente después de pulsar el botón.

Si la descarga automática falla, copie la URL oficial mostrada, ábrala en un
navegador normal, guarde el KML y cárguelo en esa sección. No evada controles
institucionales.

## Privacidad y permisos

El cuaderno no publica datos. Google Drive se monta únicamente tras una
selección explícita. No desactive la validación TLS. El acceso técnico a una
URL no equivale a permiso de redistribución.

`NicaGeoFetch_Developer.ipynb` no es para principiantes: requiere una copia
local del repositorio y usa instalación editable.
