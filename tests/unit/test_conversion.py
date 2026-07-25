"""Field mapping and verified end-to-end local conversion tests."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

import geopandas as gpd
import responses

from nica_geofetch.conversion import shapefile_field_mapping
from nica_geofetch.models import (
    METADATA_ORIGIN_VALUES,
    SOURCE_RELATIONSHIP_VALUES,
    OutputFormat,
    RetrievalMode,
)
from nica_geofetch.providers.ineter_pfafstetter import IneterPfafstetterProvider
from nica_geofetch.validation import sha256_file
from nica_geofetch.workflows import download_workflow, import_local_workflow


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
    manifest = json.loads((output / "source_manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 3
    assert set(manifest["metadata_origin_vocabulary"]) == METADATA_ORIGIN_VALUES
    assert set(manifest["source_relationship_vocabulary"]) == SOURCE_RELATIONSHIP_VALUES
    source = manifest["sources"][0]
    legacy_v2_fields = {
        "source_url",
        "source_layer",
        "retrieval_mode",
        "retrieved_at_utc",
        "response_content_type",
        "byte_size",
        "sha256",
        "validation_status",
        "placemark_count",
        "geometry_count",
    }
    assert legacy_v2_fields <= set(source)
    assert source["retrieval_mode"] == "manual_import"
    assert source["source_url"] is None
    assert source["source_layer"].endswith("nivel4_2025")
    assert source["byte_size"] > 0
    assert source["source_relationship"] == "authoritative"
    assert source["original_sha256"] == source["sha256"]
    assert source["source_byte_size"] == source["byte_size"]
    assert source["original_source_format"] == "KML"
    assert source["crs"] == {"source": "EPSG:4326", "normalized": "EPSG:4326"}
    assert set(source["metadata_basis"]) == METADATA_ORIGIN_VALUES | {"uncertainties"}
    assert "source_file" in source["metadata_basis"]["user_supplied"]
    artifacts = source["generated_artifacts"]
    assert {artifact["format"] for artifact in artifacts} == {
        "kml",
        "gpkg",
        "geojson",
        "shapefile",
    }
    assert all(len(artifact["sha256"]) == 64 for artifact in artifacts)
    assert (
        next(item for item in artifacts if item["format"] == "kml")["artifact_role"]
        == "preserved_source"
    )
    assert {item["artifact_role"] for item in artifacts if item["format"] != "kml"} == {
        "derived_output"
    }
    assert "convert_requested_formats" in source["transformation_steps"]
    assert result.archive_path.exists()


@responses.activate
def test_remote_download_manifest_contains_complete_http_provenance(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    provider = IneterPfafstetterProvider()
    url = provider.build_url(4)
    body = (fixtures_directory / "vector_level4.kml").read_bytes()
    content_type = "application/vnd.google-earth.kml+xml"
    responses.add(
        responses.GET,
        url,
        status=200,
        body=body,
        content_type=content_type,
    )
    output = tmp_path / "remote-workflow"
    result = download_workflow(
        levels=[4],
        formats=[OutputFormat.KML],
        output_directory=output,
        provider=provider,
    )
    assert result.reports[0].retrieval_mode is RetrievalMode.REMOTE_DOWNLOAD
    manifest = json.loads((output / "source_manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 3
    source = manifest["sources"][0]
    required = {
        "source_url",
        "source_layer",
        "retrieval_mode",
        "retrieved_at_utc",
        "response_content_type",
        "byte_size",
        "sha256",
        "validation_status",
        "placemark_count",
        "geometry_count",
    }
    assert required <= set(source)
    assert source["source_url"] == url
    assert source["source_layer"] == provider.config.layers[4]
    assert source["retrieval_mode"] == "remote_download"
    assert source["retrieved_at_utc"].endswith("Z")
    assert source["response_content_type"] == content_type
    assert source["byte_size"] == len(body)
    assert source["validation_status"] == "valid"
    assert source["placemark_count"] == 2
    assert source["geometry_count"] == 2
    assert source["source_relationship"] == "authoritative"
    assert "source_file" not in source["metadata_basis"]["user_supplied"]
    assert "source_url" in source["metadata_basis"]["derived"]
    assert "source_url" not in source["metadata_basis"]["source_declared"]
