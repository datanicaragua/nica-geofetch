"""Field mapping and verified end-to-end local conversion tests."""

from __future__ import annotations

import json
import zipfile
from dataclasses import replace
from pathlib import Path

import geopandas as gpd
import responses

from nica_geofetch.conversion import shapefile_field_mapping
from nica_geofetch.manifests import write_checksums, write_results_guide
from nica_geofetch.models import (
    METADATA_ORIGIN_VALUES,
    SOURCE_RELATIONSHIP_VALUES,
    OutputFormat,
    RetrievalMode,
)
from nica_geofetch.packaging import build_archive_name, create_final_archive
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
        assert "LEEME_RESULTADOS.md" in names
        assert "audit_report.json" in names
        assert "source_manifest.json" in names
        assert "checksums_sha256.json" in names
        assert any(name.startswith("raw/") for name in names)
        assert any(name.startswith("processed/") for name in names)
        assert any(name.startswith("field_mappings/") for name in names)
    checksums = json.loads((output / "checksums_sha256.json").read_text(encoding="utf-8"))
    assert checksums["files"]["raw/ineter_pfafstetter_2025_level4.kml"]
    assert checksums["files"]["LEEME_RESULTADOS.md"]
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
    guide = result.results_guide_path.read_text(encoding="utf-8")
    for expected in (
        "Ejecución UTC",
        "INETER Pfafstetter 2025",
        "Niveles seleccionados",
        "Formatos solicitados",
        "Reparación solicitada",
        "`raw/`",
        "`processed/`",
        "raw/ineter_pfafstetter_2025_level4.kml",
        "processed/pfaf_level4.gpkg",
        "audit_report.json",
        "source_manifest.json",
        "provenance_summary.md",
        "KML",
        "GeoPackage",
        "GeoJSON",
        "Shapefile ZIP",
        "Apache-2.0",
        "material de terceros",
    ):
        assert expected in guide
    assert result.archive_path.name.startswith(
        "nica_geofetch_ineter_pfaf_n4_kml-gpkg-geojson-shapefile_"
    )
    assert result.archive_path.exists()


def test_archive_name_includes_level_format_and_utc_context() -> None:
    name = build_archive_name(
        levels=[7, 4, 5, 6],
        formats=[OutputFormat.GPKG],
        generated_at_utc="2026-07-26T11:24:00Z",
    )
    assert name == "nica_geofetch_ineter_pfaf_n4-n7_gpkg_20260726T112400Z.zip"


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


def test_topology_warning_source_is_retained_and_derivatives_are_skipped(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    source_path = fixtures_directory / "vector_level5_two_invalid.kml"
    output = tmp_path / "warning-workflow"
    result = import_local_workflow(
        input_path=source_path,
        level=5,
        formats=[OutputFormat.GPKG, OutputFormat.GEOJSON],
        output_directory=output,
    )
    report = result.reports[0]
    conversion = result.conversions[0]
    retained = output / "raw/ineter_pfafstetter_2025_level5.kml"
    assert report.acquisition_valid
    assert not report.analytical_ready
    assert report.invalid_geometry_count == 2
    assert retained.read_bytes() == source_path.read_bytes()
    assert conversion.outputs == {"kml": retained}
    assert not list((output / "processed").iterdir())
    with zipfile.ZipFile(result.archive_path) as bundle:
        assert "raw/ineter_pfafstetter_2025_level5.kml" in bundle.namelist()
    manifest = json.loads((output / "source_manifest.json").read_text(encoding="utf-8"))
    manifest_source = manifest["sources"][0]
    assert manifest_source["acquisition_status"] == "valid"
    assert manifest_source["geometry_validation_status"] == "warnings"
    assert manifest_source["invalid_geometry_count"] == 2
    assert manifest_source["generated_analytical_formats"] == []
    assert not manifest_source["repair_requested"]
    assert not manifest_source["repair_applied"]
    guide = result.results_guide_path.read_text(encoding="utf-8")
    assert "Nivel 5: GeoPackage, GeoJSON" in guide
    assert "2 advertencias topológicas; reparación desactivada" in guide
    summary = result.summary_rows()[0]
    assert summary["source_path"] == "raw/ineter_pfafstetter_2025_level5.kml"
    assert summary["analytical_paths"] == []
    assert summary["skipped_analytical_outputs"] == ["gpkg", "geojson"]
    assert summary["skip_reason_code"] == "topology_warnings_repair_disabled"


def test_results_guide_uses_singular_topology_grammar_inside_archive(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    output = tmp_path / "singular-guide-workflow"
    result = import_local_workflow(
        input_path=fixtures_directory / "vector_level5_two_invalid.kml",
        level=5,
        formats=[OutputFormat.GPKG],
        output_directory=output,
    )
    result.reports[0].invalid_geometry_count = 1
    write_results_guide(
        output,
        result.reports,
        result.conversions,
        [OutputFormat.GPKG],
        generated_at_utc="2026-07-26T21:20:25Z",
    )
    write_checksums(output)
    archive = create_final_archive(output, archive_name="synthetic_singular_guide.zip")
    with zipfile.ZipFile(archive) as bundle:
        guide = bundle.read("LEEME_RESULTADOS.md").decode("utf-8")
        names = set(bundle.namelist())
    assert "1 advertencia topológica; reparación desactivada" in guide
    assert "1 advertencias topológicas" not in guide
    assert {
        "LEEME_RESULTADOS.md",
        "audit_report.json",
        "audit_report.md",
        "source_manifest.json",
        "provenance_summary.md",
        "checksums_sha256.json",
        "raw/ineter_pfafstetter_2025_level5.kml",
    } <= names


def test_explicit_repair_generates_derivatives_and_separate_checksums(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    source_path = fixtures_directory / "vector_level5_two_invalid.kml"
    output = tmp_path / "repair-workflow"
    result = import_local_workflow(
        input_path=source_path,
        level=5,
        formats=[OutputFormat.GPKG],
        output_directory=output,
        repair=True,
    )
    report = result.reports[0]
    assert report.analytical_ready
    assert report.repair_applied
    assert set(result.conversions[0].outputs) == {"kml", "gpkg"}
    assert (output / "raw/ineter_pfafstetter_2025_level5.kml").read_bytes() == (
        source_path.read_bytes()
    )
    manifest = json.loads((output / "source_manifest.json").read_text(encoding="utf-8"))
    manifest_source = manifest["sources"][0]
    assert manifest_source["original_sha256"] == report.sha256
    assert manifest_source["repaired_working_copy_sha256"]
    assert manifest_source["repaired_working_copy_sha256"] != report.sha256
    assert manifest_source["repair_method"] == "shapely.make_valid"
    assert manifest_source["generated_analytical_formats"] == ["gpkg"]


@responses.activate
def test_one_topology_warning_level_does_not_stop_later_selected_levels(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    base_provider = IneterPfafstetterProvider()
    provider = IneterPfafstetterProvider(replace(base_provider.config, polite_delay_seconds=0))
    responses.add(
        responses.GET,
        provider.build_url(5),
        status=200,
        body=(fixtures_directory / "vector_level5_two_invalid.kml").read_bytes(),
        content_type="application/vnd.google-earth.kml+xml",
    )
    responses.add(
        responses.GET,
        provider.build_url(4),
        status=200,
        body=(fixtures_directory / "vector_level4.kml").read_bytes(),
        content_type="application/vnd.google-earth.kml+xml",
    )
    output = tmp_path / "multi-level-workflow"
    result = download_workflow(
        levels=[5, 4],
        formats=[OutputFormat.GPKG],
        output_directory=output,
        provider=provider,
    )
    assert [report.level for report in result.reports] == [5, 4]
    assert result.reports[0].acquisition_valid
    assert result.reports[0].invalid_geometry_count == 2
    assert result.reports[1].analytical_ready
    retained_level5 = output / "raw/ineter_pfafstetter_2025_level5.kml"
    assert (
        retained_level5.read_bytes()
        == (fixtures_directory / "vector_level5_two_invalid.kml").read_bytes()
    )
    by_level = {conversion.level: conversion for conversion in result.conversions}
    assert set(by_level[5].outputs) == {"kml"}
    assert set(by_level[4].outputs) == {"kml", "gpkg"}
    guide = result.results_guide_path.read_text(encoding="utf-8")
    assert "processed/pfaf_level4.gpkg" in guide
    assert "Nivel 5: GeoPackage" in guide
    assert "2 advertencias topológicas; reparación desactivada" in guide
    with zipfile.ZipFile(result.archive_path) as bundle:
        assert "LEEME_RESULTADOS.md" in bundle.namelist()
    assert result.archive_path.exists()
