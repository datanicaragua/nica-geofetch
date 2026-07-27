# Security policy

## Supported version

Security fixes target the latest `0.1.x` development version during MVP-1.

## Reporting

GitHub Private Vulnerability Reporting is not currently enabled for this
repository. Open a public
[GitHub issue](https://github.com/datanicaragua/nica-geofetch/issues/new)
requesting a private contact channel, but do **not** include vulnerability
details, credentials, local paths, proxy configuration, or exploitable
information in that issue.

After a maintainer provides a private channel, include a minimal reproduction
using only synthetic or redacted data. Enabling GitHub Private Vulnerability
Reporting remains a recommended human-owner repository-setting action.

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
