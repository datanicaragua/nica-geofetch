"""Emit a non-sensitive structural audit of local seed inputs.

The script never copies source data and never prints coordinates, complete
attributes, feature names, or full Pfafstetter codes.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any

KML_NS = "{http://www.opengis.net/kml/2.2}"
ATTRIBUTE_PATTERN = re.compile(
    r'class=["\']atr-name["\'][^>]*>(.*?)</span>.*?'
    r'class=["\']atr-value["\'][^>]*>(.*?)</span>',
    re.IGNORECASE | re.DOTALL,
)
LEVEL_PATTERN = re.compile(r"nivel([4-7])", re.IGNORECASE)


def sha256_file(path: Path) -> str:
    """Calculate a source checksum without exposing source data."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def audit_kml(path: Path) -> dict[str, Any]:
    """Stream one KML and retain only schema/count information."""

    level_match = LEVEL_PATTERN.search(path.name)
    level = int(level_match.group(1)) if level_match else None
    attribute_names: Counter[str] = Counter()
    placemarks = polygons = multi_geometries = 0
    name_length_counts: Counter[int] = Counter()

    for _event, element in ET.iterparse(path, events=("end",)):
        local_name = element.tag.rsplit("}", 1)[-1]
        if local_name == "Polygon":
            polygons += 1
        elif local_name == "MultiGeometry":
            multi_geometries += 1
        elif local_name == "Placemark":
            placemarks += 1
            name = element.findtext(f"{KML_NS}name", default="").strip()
            if name.isdigit():
                name_length_counts[len(name)] += 1
            description = html.unescape(element.findtext(f"{KML_NS}description", default=""))
            for raw_name, _raw_value in ATTRIBUTE_PATTERN.findall(description):
                clean_name = re.sub(r"<[^>]+>", "", raw_name).strip().lower()
                if clean_name:
                    attribute_names[clean_name] += 1
            element.clear()

    return {
        "file_name": path.name,
        "level": level,
        "size_bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "placemark_count": placemarks,
        "polygon_element_count": polygons,
        "multi_geometry_count": multi_geometries,
        "attribute_names": dict(sorted(attribute_names.items())),
        "numeric_name_length_counts": dict(sorted(name_length_counts.items())),
    }


def main() -> int:
    """Run the audit and optionally save only its non-sensitive summary."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("seed_inputs"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = {
        "policy": "Schema, counts, sizes, and checksums only; no source features copied.",
        "kml_files": [audit_kml(path) for path in sorted(args.input.glob("*.kml"))],
        "pdf_files": [
            {
                "file_name": path.name,
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
            for path in sorted(args.input.glob("*.pdf"))
        ],
    }
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
