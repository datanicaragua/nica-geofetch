"""Streaming validation and normalization of untrusted provider KML."""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from pathlib import Path
from typing import Any

from lxml import etree, html
from shapely import make_valid
from shapely.geometry import GeometryCollection, MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry

from nica_geofetch.diagnostics import utc_now
from nica_geofetch.models import (
    KMLFeature,
    RetrievalMode,
    ValidationIssue,
    ValidationReport,
)

KML_NAMESPACE = "http://www.opengis.net/kml/2.2"
KML = f"{{{KML_NAMESPACE}}}"
OGC_ERROR_ROOTS = {"ServiceExceptionReport", "ExceptionReport"}
HTML_ROOTS = {"html"}
NUMBER_WITH_ZERO_DECIMALS = re.compile(r"^([0-9]+)\.0+$")


def sha256_file(path: Path) -> str:
    """Calculate SHA-256 without loading the file into memory."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _local_name(tag: Any) -> str:
    if not isinstance(tag, str):
        return ""
    return tag.rsplit("}", 1)[-1]


def _normalize_attribute_name(value: str) -> str:
    return re.sub(r"\s+", "_", value.strip().lower())


def _description_attributes(description: str) -> dict[str, str]:
    """Extract GeoServer HTML list/table attributes while preserving raw values."""

    if not description.strip():
        return {}
    try:
        fragment = html.fragment_fromstring(description, create_parent="div")
    except (etree.ParserError, ValueError):
        return {}

    attributes: dict[str, str] = {}
    for row in fragment.xpath(".//li | .//tr"):
        names = row.xpath(
            './/*[contains(concat(" ", normalize-space(@class), " "), " atr-name ")]//text()'
        )
        values = row.xpath(
            './/*[contains(concat(" ", normalize-space(@class), " "), " atr-value ")]//text()'
        )
        if not names:
            names = row.xpath("./th[1]//text() | ./td[1]//text()")
        if not values:
            values = row.xpath("./td[last()]//text()")
        if names and values:
            key = _normalize_attribute_name("".join(str(value) for value in names))
            raw_value = "".join(str(value) for value in values).strip()
            if key:
                attributes[key] = raw_value
    return attributes


def _extended_data_attributes(placemark: etree._Element) -> dict[str, str]:
    attributes: dict[str, str] = {}
    for element in placemark.xpath('.//*[local-name()="Data" or local-name()="SimpleData"]'):
        name = element.get("name")
        if not name:
            continue
        values = element.xpath('./*[local-name()="value"]//text() | ./text()')
        value = "".join(str(item) for item in values).strip()
        attributes[_normalize_attribute_name(name)] = value
    return attributes


def _normalize_code(value: str) -> str:
    stripped = value.strip()
    match = NUMBER_WITH_ZERO_DECIMALS.fullmatch(stripped)
    return match.group(1) if match else stripped


def _extract_code(
    name: str,
    attributes: dict[str, str],
    aliases: tuple[str, ...],
    level: int,
) -> tuple[str | None, str | None]:
    for alias in aliases:
        raw_value = attributes.get(_normalize_attribute_name(alias))
        if raw_value:
            return _normalize_code(raw_value), alias
    normalized_name = _normalize_code(name)
    if normalized_name.isdigit() and len(normalized_name) == level:
        return normalized_name, "name"
    return None, None


def _parse_coordinates(text: str | None) -> list[tuple[float, float]]:
    if not text:
        return []
    points: list[tuple[float, float]] = []
    for token in text.split():
        components = token.split(",")
        if len(components) < 2:
            continue
        points.append((float(components[0]), float(components[1])))
    if points and points[0] != points[-1]:
        points.append(points[0])
    return points


def _polygon_from_element(element: etree._Element) -> Polygon | None:
    outer_nodes = element.xpath(
        './*[local-name()="outerBoundaryIs"]'
        '/*[local-name()="LinearRing"]/*[local-name()="coordinates"]/text()'
    )
    if not outer_nodes:
        return None
    outer = _parse_coordinates(str(outer_nodes[0]))
    if len(outer) < 4:
        return None
    holes = [
        ring
        for value in element.xpath(
            './*[local-name()="innerBoundaryIs"]'
            '/*[local-name()="LinearRing"]/*[local-name()="coordinates"]/text()'
        )
        if len(ring := _parse_coordinates(str(value))) >= 4
    ]
    return Polygon(outer, holes)


def _polygonal_only(geometry: BaseGeometry) -> BaseGeometry:
    if isinstance(geometry, Polygon | MultiPolygon):
        return geometry
    if isinstance(geometry, GeometryCollection):
        polygons: list[Polygon] = []
        for child in geometry.geoms:
            if isinstance(child, Polygon):
                polygons.append(child)
            elif isinstance(child, MultiPolygon):
                polygons.extend(child.geoms)
        if len(polygons) == 1:
            return polygons[0]
        if polygons:
            return MultiPolygon(polygons)
    return GeometryCollection()


def _placemark_geometry(placemark: etree._Element) -> BaseGeometry:
    polygons: list[Polygon] = []
    for element in placemark.xpath('.//*[local-name()="Polygon"]'):
        try:
            polygon = _polygon_from_element(element)
        except (TypeError, ValueError):
            polygon = None
        if polygon is not None and not polygon.is_empty:
            polygons.append(polygon)
    if len(polygons) == 1:
        return polygons[0]
    if polygons:
        return MultiPolygon(polygons)
    return GeometryCollection()


def _within_plausible_bounds(
    geometry: BaseGeometry,
    bounds: tuple[float, float, float, float],
) -> tuple[bool, bool]:
    min_x, min_y, max_x, max_y = geometry.bounds
    expected_min_x, expected_min_y, expected_max_x, expected_max_y = bounds
    intersects = not (
        max_x < expected_min_x
        or min_x > expected_max_x
        or max_y < expected_min_y
        or min_y > expected_max_y
    )
    contained = (
        min_x >= expected_min_x
        and min_y >= expected_min_y
        and max_x <= expected_max_x
        and max_y <= expected_max_y
    )
    return intersects, contained


def _content_error_report(
    report: ValidationReport,
    *,
    code: str,
    message: str,
) -> ValidationReport:
    report.issues.append(ValidationIssue("error", code, message))
    return report


def _metadata_basis(
    retrieval_mode: RetrievalMode,
    *,
    source_url: str | None,
    response_content_type: str | None,
) -> dict[str, list[str]]:
    """Describe how compact manifest metadata was obtained."""

    source_declared = ["source_institution", "source_layer"]
    if response_content_type:
        source_declared.append("response_content_type")
    user_supplied = ["selected_level"]
    if retrieval_mode in {RetrievalMode.MANUAL_IMPORT, RetrievalMode.SEED_INPUT}:
        user_supplied.append("source_file")
    derived = [
        "provider_id",
        "dataset_id",
        "source_relationship",
        "source_byte_size",
        "original_sha256",
        "feature_count",
        "geometry_count",
        "validation_status",
        "warnings",
        "crs.normalized",
        "generated_artifacts",
        "transformation_steps",
    ]
    if source_url:
        derived.append("source_url")
    return {
        "source_declared": source_declared,
        "detected": [
            "original_source_format",
            "geometry_types",
            "software_version",
            "provider_configuration_version",
        ],
        "inferred": ["dataset_year", "crs.source"],
        "derived": derived,
        "user_supplied": user_supplied,
        "unknown": [],
        "uncertainties": [
            "license_status",
            "redistribution_status",
            "institutional_metadata_completeness",
        ],
    }


def validate_kml(
    path: Path,
    *,
    level: int,
    code_aliases: tuple[str, ...],
    plausible_bounds: tuple[float, float, float, float],
    provider_id: str = "ineter-pfafstetter",
    provider_configuration_version: str = "1",
    dataset_id: str = "ineter-pfafstetter-2025",
    source_institution: str = "Instituto Nicaragüense de Estudios Territoriales (INETER)",
    source_relationship: str = "authoritative",
    source_url: str | None = None,
    source_layer: str = "",
    retrieval_mode: RetrievalMode = RetrievalMode.MANUAL_IMPORT,
    retrieved_at_utc: str | None = None,
    response_content_type: str | None = None,
    byte_size: int | None = None,
    repair: bool = False,
) -> ValidationReport:
    """Validate a KML and return normalized polygon features plus audit findings."""

    if level not in {4, 5, 6, 7}:
        raise ValueError("Pfafstetter level must be 4, 5, 6, or 7")
    checked_utc = utc_now()
    report = ValidationReport(
        source_path=path,
        source_url=source_url,
        source_layer=source_layer,
        retrieval_mode=retrieval_mode,
        level=level,
        sha256=sha256_file(path),
        checked_utc=checked_utc,
        retrieved_at_utc=retrieved_at_utc or checked_utc,
        response_content_type=response_content_type,
        byte_size=byte_size if byte_size is not None else path.stat().st_size,
        source_institution=source_institution,
        provider_id=provider_id,
        dataset_id=dataset_id,
        source_relationship=source_relationship,
        provider_configuration_version=provider_configuration_version,
        metadata_basis=_metadata_basis(
            retrieval_mode,
            source_url=source_url,
            response_content_type=response_content_type,
        ),
    )
    if path.stat().st_size == 0:
        return _content_error_report(report, code="empty_kml", message="The KML file is empty.")

    root_checked = False
    try:
        context = etree.iterparse(
            str(path),
            events=("start", "end"),
            resolve_entities=False,
            no_network=True,
            huge_tree=True,
        )
        for event, element in context:
            local_name = _local_name(element.tag)
            if not root_checked and event == "start":
                root_checked = True
                if local_name in OGC_ERROR_ROOTS:
                    return _content_error_report(
                        report,
                        code="ogc_error",
                        message="The document is an OGC exception response, not KML.",
                    )
                if local_name.lower() in HTML_ROOTS:
                    return _content_error_report(
                        report,
                        code="unexpected_html",
                        message="The document is HTML, not KML.",
                    )
                if local_name != "kml":
                    return _content_error_report(
                        report,
                        code="malformed_kml",
                        message=f"Unexpected XML root element: {local_name or '<unknown>'}.",
                    )
            if event != "end":
                continue
            if local_name == "GroundOverlay":
                report.ground_overlay_count += 1
            elif local_name == "NetworkLink":
                report.network_link_count += 1
            elif local_name == "Placemark":
                report.placemark_count += 1
                name_nodes = element.xpath('./*[local-name()="name"]/text()')
                name = "".join(str(value) for value in name_nodes).strip()
                description_nodes = element.xpath('./*[local-name()="description"]/text()')
                description = "".join(str(value) for value in description_nodes)
                attributes = _description_attributes(description)
                attributes.update(_extended_data_attributes(element))
                pfaf_code, code_source = _extract_code(name, attributes, code_aliases, level)
                geometry = _placemark_geometry(element)

                if geometry.is_empty:
                    report.issues.append(
                        ValidationIssue(
                            "error",
                            "empty_geometry",
                            "Placemark has no usable polygon geometry.",
                            name or None,
                        )
                    )
                else:
                    if not geometry.is_valid:
                        if repair:
                            repaired = _polygonal_only(make_valid(geometry))
                            if repaired.is_empty or not repaired.is_valid:
                                report.issues.append(
                                    ValidationIssue(
                                        "error",
                                        "invalid_geometry",
                                        "Geometry remains invalid after explicit repair.",
                                        name or None,
                                    )
                                )
                            else:
                                geometry = repaired
                                report.repaired_geometry_count += 1
                                report.issues.append(
                                    ValidationIssue(
                                        "warning",
                                        "geometry_repaired",
                                        "Invalid geometry was repaired by explicit request.",
                                        name or None,
                                    )
                                )
                        else:
                            report.issues.append(
                                ValidationIssue(
                                    "error",
                                    "invalid_geometry",
                                    "Polygon geometry is invalid; use repair only after review.",
                                    name or None,
                                )
                            )
                    intersects, contained = _within_plausible_bounds(geometry, plausible_bounds)
                    if not intersects:
                        report.issues.append(
                            ValidationIssue(
                                "error",
                                "implausible_bounds",
                                "Geometry is outside the configured Nicaragua bounds.",
                                name or None,
                            )
                        )
                    elif not contained:
                        report.issues.append(
                            ValidationIssue(
                                "warning",
                                "partial_bounds",
                                "Geometry extends beyond the broad configured Nicaragua bounds.",
                                name or None,
                            )
                        )

                if pfaf_code is None:
                    report.issues.append(
                        ValidationIssue(
                            "error",
                            "missing_pfaf_code",
                            "No Pfafstetter code was found through configured aliases or name.",
                            name or None,
                        )
                    )
                elif not pfaf_code.isdigit():
                    report.issues.append(
                        ValidationIssue(
                            "error",
                            "invalid_pfaf_code",
                            "Pfafstetter code must contain digits only.",
                            name or None,
                        )
                    )
                elif len(pfaf_code) != level:
                    report.issues.append(
                        ValidationIssue(
                            "warning",
                            "pfaf_code_length_mismatch",
                            f"Pfafstetter code has {len(pfaf_code)} digits; "
                            f"the configured level is {level}. The raw value was preserved.",
                            name or None,
                        )
                    )

                if not geometry.is_empty:
                    normalized_attributes = dict(attributes)
                    normalized_attributes.update(
                        {
                            "source_name": name,
                            "pfaf_code": pfaf_code or "",
                            "pfaf_level": str(level),
                            "pfaf_code_source": code_source or "",
                            "source_provider": provider_id,
                            "source_dataset": dataset_id,
                            "source_relationship": source_relationship,
                            "source_url": source_url or "",
                            "source_layer": source_layer,
                            "retrieval_mode": retrieval_mode.value,
                            "source_sha256": report.sha256,
                            "retrieved_at_utc": report.retrieved_at_utc,
                            "response_content_type": response_content_type or "",
                            "source_byte_size": str(report.byte_size),
                            "provider_configuration_version": provider_configuration_version,
                        }
                    )
                    report.features.append(
                        KMLFeature(
                            name=name,
                            pfaf_code=pfaf_code,
                            level=level,
                            attributes=normalized_attributes,
                            geometry=geometry,
                        )
                    )
                    report.polygon_feature_count += 1

                element.clear()
                parent = element.getparent()
                if parent is not None:
                    while element.getprevious() is not None:
                        del parent[0]
    except (etree.XMLSyntaxError, OSError, ValueError) as exc:
        return _content_error_report(
            report,
            code="malformed_kml",
            message=f"KML XML could not be parsed: {exc}",
        )

    if report.placemark_count == 0:
        code = "empty_kml"
        message = "KML contains no Placemark."
        if report.ground_overlay_count:
            code = "raster_only_kml"
            message = "KML contains GroundOverlay content but no vector Placemark."
        elif report.network_link_count:
            code = "network_link_only_kml"
            message = "KML contains NetworkLink content but no local vector Placemark."
        report.issues.append(ValidationIssue("error", code, message))
    elif report.polygon_feature_count == 0:
        report.issues.append(
            ValidationIssue(
                "error",
                "raster_only_kml",
                "No polygonal feature was found in the KML placemarks.",
            )
        )

    codes = [feature.pfaf_code for feature in report.features if feature.pfaf_code]
    duplicates = {code for code, count in Counter(codes).items() if count > 1}
    for duplicate in sorted(duplicates):
        report.issues.append(
            ValidationIssue(
                "warning",
                "duplicate_pfaf_code",
                f"Pfafstetter code {duplicate} occurs more than once.",
            )
        )
    return report
