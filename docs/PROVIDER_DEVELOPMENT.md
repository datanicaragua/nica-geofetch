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

The INETER provider uses KML because the target layers were not exposed as WFS
FeatureTypes during prior verification. Query parameters are `layers`,
`mode=download`, `kmattr=true`, and `kmplacemark=true`, encoded only with
`urllib.parse.urlencode`.
