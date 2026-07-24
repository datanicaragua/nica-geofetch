"""Field mapping and verified end-to-end local conversion tests."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

import geopandas as gpd

from nica_geofetch.conversion import shapefile_field_mapping
from nica_geofetch.models import OutputFormat
from nica_geofetch.validation import sha256_file
from nica_geofetch.workflows import import_local_workflow


def test_shapefile_field_mapping_is_short_unique_and_deterministic() -> None:
    fields = ["source_provider", "source-providér", "pfaf_code", "very_long_attribute_name"]
    first = shapefile_field_mapping(fields)
    second = shapefile_field_mapping(fields)
    assert first == second
    assert all(len(value) <= 10 for value in first.values())
    assert len(set(first.values())) == len(fields)


def test_checksum() -> None:
    assert sha256_file(Path(__file__)) == sha256_file(Path(__file__))
    assert len(sha256_file(Path(__file__))) == 64


def test_local_import_all_conversions_reopen_and_package(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    output = tmp_path / "workflow"
    result = import_local_workflow(
        input_path=fixtures_directory / "vector_level4.kml",
        level=4,
        formats=list(OutputFormat),
        output_directory=output,
    )
    assert result.valid
    conversion = result.conversions[0]
    assert set(conversion.outputs) == {"kml", "gpkg", "geojson", "shapefile"}
    gpkg = conversion.outputs["gpkg"]
    assert len(gpd.read_file(gpkg, layer="pfaf_n4", engine="pyogrio")) == 2
    assert len(gpd.read_file(conversion.outputs["geojson"], engine="pyogrio")) == 2
    assert len(gpd.read_file(f"zip://{conversion.outputs['shapefile']}", engine="pyogrio")) == 2
    with zipfile.ZipFile(conversion.outputs["shapefile"]) as bundle:
        assert "field_name_mapping.csv" in bundle.namelist()
    with zipfile.ZipFile(result.archive_path) as bundle:
        names = set(bundle.namelist())
        assert "audit_report.json" in names
        assert "source_manifest.json" in names
        assert "checksums_sha256.json" in names
        assert any(name.startswith("raw/") for name in names)
        assert any(name.startswith("processed/") for name in names)
        assert any(name.startswith("field_mappings/") for name in names)
    checksums = json.loads((output / "checksums_sha256.json").read_text(encoding="utf-8"))
    assert checksums["files"]["raw/ineter_pfafstetter_2025_level4.kml"]
    assert result.archive_path.exists()
