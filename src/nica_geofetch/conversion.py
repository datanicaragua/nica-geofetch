"""Verified conversion of normalized polygon features to supported formats."""

from __future__ import annotations

import csv
import hashlib
import re
import tempfile
import unicodedata
import zipfile
from collections.abc import Iterable
from pathlib import Path

import geopandas as gpd

from nica_geofetch.exceptions import ConversionError
from nica_geofetch.models import ConversionResult, OutputFormat, ValidationReport

REQUIRED_SHAPEFILE_SUFFIXES = {".shp", ".shx", ".dbf", ".prj", ".cpg"}
FIXED_ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def _safe_field_base(field_name: str) -> str:
    normalized = unicodedata.normalize("NFKD", field_name)
    ascii_name = normalized.encode("ascii", "ignore").decode("ascii").lower()
    safe = re.sub(r"[^a-z0-9_]+", "_", ascii_name).strip("_")
    return safe or "field"


def shapefile_field_mapping(field_names: Iterable[str]) -> dict[str, str]:
    """Create deterministic, collision-resistant DBF field names of at most 10 chars."""

    mapping: dict[str, str] = {}
    used: set[str] = set()
    for original in field_names:
        base = _safe_field_base(original)
        candidate = base[:10]
        if len(base) > 10 or candidate in used:
            digest = hashlib.sha1(original.encode("utf-8")).hexdigest()
            for offset in range(len(digest) - 2):
                candidate = f"{base[:7]}{digest[offset : offset + 3]}"[:10]
                if candidate not in used:
                    break
            else:
                raise ConversionError(f"Cannot create a unique Shapefile field for {original}")
        mapping[original] = candidate
        used.add(candidate)
    return mapping


def _geodataframe(report: ValidationReport) -> gpd.GeoDataFrame:
    if not report.features:
        raise ConversionError("No normalized polygon features are available for conversion")
    records = [dict(feature.attributes) for feature in report.features]
    geometries = [feature.geometry for feature in report.features]
    frame = gpd.GeoDataFrame(records, geometry=geometries, crs="EPSG:4326")
    if frame.empty:
        raise ConversionError("Normalized feature table is empty")
    return frame


def _verify_frame(
    frame: gpd.GeoDataFrame,
    *,
    expected_count: int,
    description: str,
) -> None:
    if len(frame) != expected_count:
        raise ConversionError(
            f"{description} reopened with {len(frame)} features; expected {expected_count}"
        )
    if frame.crs is None:
        raise ConversionError(f"{description} reopened without a CRS")
    if frame.geometry.is_empty.any() or frame.geometry.isna().any():
        raise ConversionError(f"{description} reopened with null or empty geometries")
    unexpected = set(frame.geometry.geom_type) - {"Polygon", "MultiPolygon"}
    if unexpected:
        raise ConversionError(f"{description} contains non-polygon geometry: {unexpected}")


def _write_mapping_csv(path: Path, mapping: dict[str, str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["original_field_name", "shapefile_field_name"])
        writer.writerows(mapping.items())


def _zip_files(archive: Path, files: list[Path]) -> None:
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(files, key=lambda value: value.name.lower()):
            info = zipfile.ZipInfo(path.name, FIXED_ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, path.read_bytes())


def _write_shapefile_zip(
    frame: gpd.GeoDataFrame,
    *,
    level: int,
    archive: Path,
    mapping_output: Path,
) -> dict[str, str]:
    mapping = shapefile_field_mapping(
        column for column in frame.columns if column != frame.geometry.name
    )
    renamed = frame.rename(columns=mapping)
    archive.parent.mkdir(parents=True, exist_ok=True)
    mapping_output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"pfaf_n{level}_", dir=archive.parent) as temp_name:
        temp_directory = Path(temp_name)
        shapefile_path = temp_directory / f"pfaf_n{level}.shp"
        renamed.to_file(
            shapefile_path,
            driver="ESRI Shapefile",
            engine="pyogrio",
            encoding="UTF-8",
        )
        _write_mapping_csv(temp_directory / "field_name_mapping.csv", mapping)
        _write_mapping_csv(mapping_output, mapping)
        available_suffixes = {
            path.suffix.lower() for path in temp_directory.glob(f"pfaf_n{level}.*")
        }
        missing = REQUIRED_SHAPEFILE_SUFFIXES - available_suffixes
        if missing:
            raise ConversionError(f"Shapefile is missing required components: {sorted(missing)}")
        reopened = gpd.read_file(shapefile_path, engine="pyogrio")
        _verify_frame(reopened, expected_count=len(frame), description="Shapefile")
        files = [
            *temp_directory.glob(f"pfaf_n{level}.*"),
            temp_directory / "field_name_mapping.csv",
        ]
        _zip_files(archive, files)

    with zipfile.ZipFile(archive) as bundle:
        names = set(bundle.namelist())
        if "field_name_mapping.csv" not in names:
            raise ConversionError("Shapefile ZIP does not include field_name_mapping.csv")
        for suffix in REQUIRED_SHAPEFILE_SUFFIXES:
            if not any(name.lower().endswith(suffix) for name in names):
                raise ConversionError(f"Shapefile ZIP does not include a {suffix} component")
    reopened_zip = gpd.read_file(f"zip://{archive}", engine="pyogrio")
    _verify_frame(reopened_zip, expected_count=len(frame), description="Shapefile ZIP")
    return mapping


def convert_report(
    report: ValidationReport,
    formats: Iterable[OutputFormat],
    output_directory: Path,
) -> ConversionResult:
    """Convert one valid validation result and reopen every generated dataset."""

    if not report.valid:
        raise ConversionError("Cannot convert a source that failed validation")
    selected = set(formats)
    processed = output_directory / "processed"
    mappings = output_directory / "field_mappings"
    processed.mkdir(parents=True, exist_ok=True)
    mappings.mkdir(parents=True, exist_ok=True)
    frame = _geodataframe(report)
    result = ConversionResult(level=report.level, outputs={})

    if OutputFormat.KML in selected:
        result.outputs[OutputFormat.KML.value] = report.source_path

    if OutputFormat.GPKG in selected:
        gpkg = processed / f"pfaf_level{report.level}.gpkg"
        layer = f"pfaf_n{report.level}"
        if gpkg.exists():
            gpkg.unlink()
        frame.to_file(gpkg, layer=layer, driver="GPKG", engine="pyogrio")
        reopened = gpd.read_file(gpkg, layer=layer, engine="pyogrio")
        _verify_frame(reopened, expected_count=len(frame), description="GeoPackage")
        result.outputs[OutputFormat.GPKG.value] = gpkg

    if OutputFormat.GEOJSON in selected:
        geojson = processed / f"pfaf_level{report.level}.geojson"
        if geojson.exists():
            geojson.unlink()
        frame.to_file(geojson, driver="GeoJSON", engine="pyogrio")
        reopened = gpd.read_file(geojson, engine="pyogrio")
        _verify_frame(reopened, expected_count=len(frame), description="GeoJSON")
        result.outputs[OutputFormat.GEOJSON.value] = geojson

    if OutputFormat.SHAPEFILE in selected:
        archive = processed / f"pfaf_level{report.level}_shapefile.zip"
        mapping_output = mappings / f"pfaf_n{report.level}_field_name_mapping.csv"
        if archive.exists():
            archive.unlink()
        result.field_mapping = _write_shapefile_zip(
            frame,
            level=report.level,
            archive=archive,
            mapping_output=mapping_output,
        )
        result.outputs[OutputFormat.SHAPEFILE.value] = archive

    return result
