"""Normalize network and content failures into actionable categories."""

from __future__ import annotations

import socket
from datetime import UTC, datetime

import requests

from nica_geofetch.models import DiagnosticReport


def utc_now() -> str:
    """Return a stable RFC 3339 UTC timestamp."""

    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def classify_request_exception(exc: requests.RequestException) -> tuple[str, str]:
    """Map Requests exceptions to stable public diagnostic categories."""

    if isinstance(exc, requests.exceptions.ProxyError):
        return "proxy_failure", "The configured proxy could not complete the request."
    if isinstance(exc, requests.exceptions.SSLError):
        return "tls_failure", "TLS certificate verification or negotiation failed."
    if isinstance(exc, requests.exceptions.ConnectTimeout):
        return "connection_timeout", "The connection to the institutional server timed out."
    if isinstance(exc, requests.exceptions.ReadTimeout):
        return "read_timeout", "The institutional server did not send data before the timeout."
    if isinstance(exc, requests.exceptions.Timeout):
        return "read_timeout", "The network operation timed out."
    if isinstance(exc, requests.exceptions.ConnectionError):
        message = str(exc).lower()
        cause = exc.__cause__
        if isinstance(cause, socket.gaierror) or any(
            token in message
            for token in ("name resolution", "getaddrinfo", "nodename nor servname", "11001")
        ):
            return "dns_failure", "The institutional hostname could not be resolved."
        return "connection_failure", "A connection to the institutional server could not be made."
    return "network_failure", "The network request failed."


def failure_report(
    *,
    official_url: str,
    category: str,
    message: str,
    http_status: int | None = None,
    content_type: str | None = None,
) -> DiagnosticReport:
    """Build a normalized failure with the standard manual fallback."""

    return DiagnosticReport(
        ok=False,
        category=category,
        message=message,
        official_url=official_url,
        http_status=http_status,
        content_type=content_type,
        checked_utc=utc_now(),
        manual_download_instructions=(
            "Open the exact official URL in a browser. If INETER returns a KML, "
            "save it locally and run `nica-geofetch import-local`; do not bypass "
            "firewalls, authentication, rate limits, or other access controls."
        ),
    )
