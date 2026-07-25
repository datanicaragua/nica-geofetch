# Provider development

MVP-1 uses a small provider interface, not a plugin framework. A provider must:

1. identify its configured datasets;
2. construct official source URLs deterministically;
3. diagnose access and emit manual fallback instructions;
4. download selected resources through the shared secure downloader;
5. apply provider-specific validation and normalization;
6. return shared workflow results.

For any future provider, first add a registry entry with institution, official
source, protocol, formats, attribution, license and redistribution status,
quality status, and contact. Add synthetic error/success fixtures and document
the source's rate limits and expected geometry.

Do not generalize the interface speculatively. A second implemented provider
should motivate only the abstractions it demonstrably shares with INETER.

## Human-guided source resolution

Provider research follows this sequence:

1. official primary source;
2. another service from the same institution;
3. official or institutional mirror;
4. academic repository linked to the producer;
5. regional institutional repository;
6. comparable international product;
7. unverified source.

This is a human-guided provider-development method, not an automated search,
crawler, or substitution feature. Each candidate retains a distinct dataset
identity and uses the controlled source relationship from
[DATA_GOVERNANCE.md](DATA_GOVERNANCE.md). Moving down the sequence requires
explicit evidence and user selection.

The INETER provider uses KML because the target layers were not exposed as WFS
FeatureTypes during prior verification. Query parameters are `layers`,
`mode=download`, `kmattr=true`, and `kmplacemark=true`, encoded only with
`urllib.parse.urlencode`.
