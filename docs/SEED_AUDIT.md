# Seed-input audit summary

Audit date: 2026-07-24. Source files remain ignored under `seed_inputs/`.
No feature coordinates or bulk attribute values are recorded here.

| Level | Bytes | Placemarks | Polygon elements | Observed attribute names |
|---:|---:|---:|---:|---|
| 4 | 5,235,971 | 12 | 111 | `objectid`, `n4`, `area_km2`, `codigo` |
| 5 | 8,247,241 | 68 | 170 | `n5`, `area_km2`, `code`, `perimetro` |
| 6 | 16,581,879 | 491 | 604 | `area_km2`, `codigo`, `n6_`, `objectid` |
| 7 | 35,391,314 | 2,337 | 2,451 | `n3`-`n7`, `phca`, `code_pfafs`, `cuencas`, `area` |

Level 4 and 5 each include one Pfaf code shorter than the configured level.
The raw values are preserved and reported as warnings rather than silently
padded. Level 6 and 7 placemark names are generally generated identifiers.
Therefore the validator prioritizes configured description attributes and
uses names only as a controlled fallback.

Full offline validation found 2 invalid geometries at level 5, 1 at level 6,
and 2 at level 7. The default workflow correctly blocks their conversion.
With explicit geometry repair, all three inputs validate and record 2, 1, and
2 repairs respectively. Level 6 produced 12 duplicate-code warnings; level 7
produced 87 code-length and 25 duplicate-code warnings. These are source
quality observations, not modifications to the institutional values.

Level 4 processed successfully without repair into KML, GeoPackage, GeoJSON,
and Shapefile ZIP; each generated dataset was reopened before packaging.

The PDF album is 36 pages and 9,806,511 bytes. Page 4 was text-extracted and
visually inspected. It contains the publication, commercial-use, and
educational/divulgative reproduction statement summarized in
`LEGAL_AND_ATTRIBUTION.md`.

Reproduce the KML audit locally:

```powershell
python scripts\audit_seed_inputs.py
```

The script emits only file names, sizes, SHA-256 checksums, element counts,
attribute-name counts, and numeric-name-length counts.
