"""Synthetic KML validation and Pfafstetter extraction tests."""

from __future__ import annotations

from pathlib import Path

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
