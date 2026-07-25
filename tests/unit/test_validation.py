"""Synthetic KML validation and Pfafstetter extraction tests."""

from __future__ import annotations

from pathlib import Path

from nica_geofetch.models import RetrievalMode
from nica_geofetch.providers.ineter_pfafstetter import IneterPfafstetterProvider


def test_vector_kml_and_code_extraction(
    fixtures_directory: Path,
) -> None:
    report = IneterPfafstetterProvider().import_local(
        fixtures_directory / "vector_level4.kml",
        4,
    )
    assert report.valid
    assert report.placemark_count == 2
    assert report.polygon_feature_count == 2
    assert [feature.pfaf_code for feature in report.features] == ["1234", "5678"]
    assert report.features[0].attributes["pfaf_code_source"] == "n4"
    assert report.features[1].attributes["pfaf_code_source"] == "name"
    assert report.features[0].attributes["label"] == "Área sintética uno"
    assert len(report.sha256) == 64


def test_raster_only_kml_rejected(fixtures_directory: Path) -> None:
    report = IneterPfafstetterProvider().import_local(
        fixtures_directory / "raster_only.kml",
        4,
    )
    assert not report.valid
    assert {issue.code for issue in report.issues} == {"raster_only_kml"}


def test_malformed_kml_rejected(fixtures_directory: Path) -> None:
    report = IneterPfafstetterProvider().import_local(
        fixtures_directory / "malformed.kml",
        4,
    )
    assert not report.valid
    assert report.issues[0].code == "malformed_kml"


def test_local_ogc_error_rejected(fixtures_directory: Path) -> None:
    report = IneterPfafstetterProvider().import_local(
        fixtures_directory / "ogc_error.kml",
        4,
    )
    assert not report.valid
    assert report.issues[0].code == "ogc_error"


def test_topology_warnings_are_distinct_from_acquisition_validity(
    fixtures_directory: Path,
) -> None:
    report = IneterPfafstetterProvider().import_local(
        fixtures_directory / "vector_level5_two_invalid.kml",
        5,
    )
    assert report.acquisition_valid
    assert not report.geometry_valid
    assert not report.analytical_ready
    assert report.invalid_geometry_count == 2
    assert report.invalid_geometry_feature_ids == [
        "synthetic-invalid-1",
        "synthetic-invalid-2",
    ]
    assert report.validation_status == "acquisition_valid_with_topology_warnings"


def test_explicit_repair_changes_only_the_analytical_working_copy(
    fixtures_directory: Path,
) -> None:
    source = fixtures_directory / "vector_level5_two_invalid.kml"
    original_bytes = source.read_bytes()
    report = IneterPfafstetterProvider().import_local(source, 5, repair=True)
    assert report.acquisition_valid
    assert not report.geometry_valid
    assert report.post_repair_geometry_valid
    assert report.analytical_ready
    assert report.repair_requested
    assert report.repair_applied
    assert report.repaired_geometry_count == 2
    assert report.repair_method == "shapely.make_valid"
    assert report.repaired_working_copy_sha256
    assert report.repaired_working_copy_sha256 != report.sha256
    assert source.read_bytes() == original_bytes


def test_seed_input_retrieval_mode(fixtures_directory: Path) -> None:
    report = IneterPfafstetterProvider().import_local(
        fixtures_directory / "vector_level4.kml",
        4,
        retrieval_mode=RetrievalMode.SEED_INPUT,
    )
    assert report.retrieval_mode is RetrievalMode.SEED_INPUT
    assert report.source_layer.endswith("nivel4_2025")
    assert report.byte_size == (fixtures_directory / "vector_level4.kml").stat().st_size


def test_level_code_length_validation(
    fixtures_directory: Path,
    tmp_path: Path,
) -> None:
    source = (fixtures_directory / "vector_level4.kml").read_text(encoding="utf-8")
    changed = source.replace(">1234<", ">123<").replace("<name>5678</name>", "<name>x</name>")
    path = tmp_path / "invalid-length.kml"
    path.write_text(changed, encoding="utf-8")
    report = IneterPfafstetterProvider().import_local(path, 4)
    assert not report.valid
    issues = {issue.code: issue.severity for issue in report.issues}
    assert issues["pfaf_code_length_mismatch"] == "warning"
    assert issues["missing_pfaf_code"] == "error"
