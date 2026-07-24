# Security policy

## Supported version

Security fixes target the latest `0.1.x` development version during MVP-1.

## Reporting

Do not open a public issue for a vulnerability that exposes credentials, local
paths, proxy configuration, or exploitable details. Contact the maintainers
privately and include a minimal reproduction with synthetic data.

## Threat model

Nica-GeoFetch treats remote responses and local KML files as untrusted:

- network access is HTTPS-only and host-allowlisted;
- redirects are validated before following;
- TLS verification remains enabled;
- response sizes and timeouts are bounded;
- XML parsing disables entity resolution and network access;
- files are written to temporary `.part` paths and moved atomically;
- archive names are controlled by the application;
- the tool does not bypass access controls, rate limits, firewalls, CAPTCHA, or
  authentication.

Proxy environment variables supported by Requests are honored. A custom CA
bundle may be supplied; no beginner-facing option disables TLS validation.
