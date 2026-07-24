# Data governance

## Classification

| Artifact | Repository policy |
|---|---|
| Source code and synthetic fixtures | May be tracked under Apache-2.0 |
| Official source URLs and public metadata | May be tracked with attribution |
| Checksums and non-sensitive audit counts | May be tracked |
| Real KML/KMZ and converted institutional data | Never track or publish here |
| User output directories | Local and ignored |
| Diagnostic reports | Review for proxy paths or sensitive environment details |

## Handling rules

1. Keep seed data under ignored `seed_inputs/`.
2. Never copy real features into tests, examples, screenshots, or notebooks.
3. Synthetic fixtures must be visibly artificial and geographically plausible.
4. Audit scripts may report schemas, counts, sizes, and hashes but not bulk
   attribute values or coordinates.
5. Preserve source bytes as raw output; do not imply the converted form is an
   official INETER product.
6. Record transformation software version, timestamp, source URL, checksum,
   level, validation findings, and any requested geometry repair.
7. Do not publish or upload outputs automatically.

## License status

No explicit open-data license has been identified for the implemented 2025
layers. `license_status` and `redistribution_status` remain explicit registry
fields. Absence of a technical access barrier is not a redistribution grant.
