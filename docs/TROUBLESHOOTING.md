# Troubleshooting

## Access diagnostics

- `dns_failure`: confirm DNS and institutional hostname availability.
- `connection_timeout`: check firewall, route, proxy, and try later.
- `read_timeout`: the server accepted the connection but did not respond in time.
- `tls_failure`: update local trust roots or supply an approved custom CA bundle.
- `proxy_failure`: review standard Requests proxy environment variables.
- `http_failure`: preserve the status and official URL; do not bypass controls.

For any remote failure, use the exact URL printed by `diagnose` in a normal
browser. If the official file downloads, use `import-local`; validation and
conversion require no network.

## Content diagnostics

- `ogc_error`: HTTP succeeded but the body is an OGC exception document.
- `unexpected_html`: the endpoint returned a web/error page instead of KML.
- `malformed_kml`: XML is not well formed.
- `empty_kml`: no `Placemark` exists.
- `raster_only_kml`: only `GroundOverlay` content exists.
- `network_link_only_kml`: the response delegates to another resource.
- `invalid_geometry`: retry with `--repair` only when the transformation is
  acceptable and inspect the audit record.

## Filesystem diagnostics

- Confirm the output directory is writable.
- Ensure free space exceeds the response-size limit plus converted outputs.
- Stale `.part` files indicate an interrupted run and may be removed after
  confirming no process is active.
- Shapefile ZIPs must contain `.shp`, `.shx`, `.dbf`, `.prj`, `.cpg`, and
  `field_name_mapping.csv`.
