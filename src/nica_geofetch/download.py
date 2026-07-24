"""Secure, bounded, sequential HTTP retrieval for institutional source files."""

from __future__ import annotations

import logging
import os
import shutil
import time
from collections.abc import Callable
from pathlib import Path
from typing import TypeVar
from urllib.parse import urljoin, urlsplit

import requests

from nica_geofetch.diagnostics import (
    classify_request_exception,
    failure_report,
    utc_now,
)
from nica_geofetch.exceptions import DownloadError, SecurityError
from nica_geofetch.models import DiagnosticReport, DownloadSettings

LOGGER = logging.getLogger(__name__)
TRANSIENT_STATUSES = {429, 500, 502, 503, 504}
REDIRECT_STATUSES = {301, 302, 303, 307, 308}
T = TypeVar("T")


def validate_remote_url(url: str, allowed_hosts: tuple[str, ...]) -> None:
    """Require HTTPS and an exact allowlisted hostname."""

    parsed = urlsplit(url)
    if parsed.scheme.lower() != "https":
        raise SecurityError("Only HTTPS institutional source URLs are allowed")
    hostname = (parsed.hostname or "").lower().rstrip(".")
    normalized_hosts = {host.lower().rstrip(".") for host in allowed_hosts}
    if not hostname or hostname not in normalized_hosts:
        raise SecurityError(f"Host is not allowlisted: {hostname or '<missing>'}")
    if parsed.username or parsed.password:
        raise SecurityError("Credentials embedded in source URLs are not allowed")


def classify_content(prefix: bytes, content_type: str | None = None) -> tuple[str, str] | None:
    """Recognize common server-side bodies that are not vector KML."""

    lowered = prefix.lstrip().lower()
    content_type_lower = (content_type or "").lower()
    if (
        b"<serviceexceptionreport" in lowered
        or b"<ows:exceptionreport" in lowered
        or b"<exceptionreport" in lowered
    ):
        return "ogc_error", "The server returned an OGC exception document."
    if lowered.startswith((b"<!doctype html", b"<html")) or "text/html" in content_type_lower:
        return "unexpected_html", "The server returned HTML instead of KML."
    return None


class SecureDownloader:
    """Requests-based downloader with redirect, size, retry, and atomic-file controls."""

    def __init__(
        self,
        *,
        allowed_hosts: tuple[str, ...],
        settings: DownloadSettings,
        session: requests.Session | None = None,
    ) -> None:
        self.allowed_hosts = allowed_hosts
        self.settings = settings
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": settings.user_agent, "Accept": "*/*"})

    @property
    def verify(self) -> bool | str:
        """Requests verification value; false is intentionally impossible."""

        return str(self.settings.ca_bundle) if self.settings.ca_bundle else True

    def _request_once(self, url: str) -> requests.Response:
        current = url
        for _redirect_number in range(6):
            validate_remote_url(current, self.allowed_hosts)
            response = self.session.get(
                current,
                stream=True,
                allow_redirects=False,
                timeout=(
                    self.settings.timeout_connect_seconds,
                    self.settings.timeout_read_seconds,
                ),
                verify=self.verify,
            )
            if response.status_code not in REDIRECT_STATUSES:
                return response
            location = response.headers.get("Location")
            response.close()
            if not location:
                raise DownloadError(
                    "Redirect response did not include a Location header",
                    category="http_failure",
                )
            current = urljoin(current, location)
            validate_remote_url(current, self.allowed_hosts)
        raise DownloadError("Too many redirects", category="http_failure")

    def _request_with_retries(self, url: str) -> requests.Response:
        validate_remote_url(url, self.allowed_hosts)
        last_exception: requests.RequestException | None = None
        for attempt in range(self.settings.retries + 1):
            try:
                response = self._request_once(url)
            except requests.RequestException as exc:
                last_exception = exc
                if attempt >= self.settings.retries:
                    category, message = classify_request_exception(exc)
                    raise DownloadError(message, category=category) from exc
            else:
                if (
                    response.status_code not in TRANSIENT_STATUSES
                    or attempt >= self.settings.retries
                ):
                    return response
                response.close()
            delay = self.settings.backoff_seconds * (2**attempt)
            if delay > 0:
                time.sleep(delay)
        if last_exception:
            category, message = classify_request_exception(last_exception)
            raise DownloadError(message, category=category) from last_exception
        raise DownloadError("Network request did not complete", category="network_failure")

    def probe(self, url: str) -> DiagnosticReport:
        """Read only a small prefix to diagnose endpoint access and content type."""

        try:
            response = self._request_with_retries(url)
            with response:
                content_type = response.headers.get("Content-Type")
                if response.status_code >= 400:
                    return failure_report(
                        official_url=url,
                        category="http_failure",
                        message=f"The server returned HTTP {response.status_code}.",
                        http_status=response.status_code,
                        content_type=content_type,
                    )
                prefix = next(response.iter_content(chunk_size=8192), b"")
                content_problem = classify_content(prefix, content_type)
                if content_problem:
                    category, message = content_problem
                    return failure_report(
                        official_url=url,
                        category=category,
                        message=message,
                        http_status=response.status_code,
                        content_type=content_type,
                    )
                return DiagnosticReport(
                    ok=True,
                    category="ok",
                    message="The official endpoint returned a non-HTML response.",
                    official_url=url,
                    http_status=response.status_code,
                    content_type=content_type,
                    checked_utc=utc_now(),
                )
        except SecurityError:
            raise
        except DownloadError as exc:
            return failure_report(
                official_url=url,
                category=exc.category,
                message=str(exc),
            )
        except requests.RequestException as exc:
            category, message = classify_request_exception(exc)
            return failure_report(official_url=url, category=category, message=message)

    def download(self, url: str, destination: Path, validator: Callable[[Path], T]) -> T:
        """Stream to a `.part` file, validate, and atomically move on success."""

        validate_remote_url(url, self.allowed_hosts)
        destination.parent.mkdir(parents=True, exist_ok=True)
        part_path = destination.with_name(destination.name + ".part")
        if part_path.exists():
            part_path.unlink()

        try:
            response = self._request_with_retries(url)
            with response:
                if response.status_code >= 400:
                    raise DownloadError(
                        f"The server returned HTTP {response.status_code}",
                        category="http_failure",
                    )
                content_length_text = response.headers.get("Content-Length")
                expected_size = int(content_length_text) if content_length_text else 0
                if expected_size > self.settings.max_response_bytes:
                    raise DownloadError(
                        "The response exceeds the configured size limit",
                        category="response_size_limit",
                    )
                free_bytes = shutil.disk_usage(destination.parent).free
                required_bytes = expected_size or self.settings.max_response_bytes
                if free_bytes < required_bytes:
                    raise DownloadError(
                        "Insufficient free disk space for the bounded response",
                        category="disk_space_failure",
                    )

                total = 0
                prefix = bytearray()
                with part_path.open("xb") as handle:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):
                        if not chunk:
                            continue
                        total += len(chunk)
                        if total > self.settings.max_response_bytes:
                            raise DownloadError(
                                "The response exceeded the configured size limit",
                                category="response_size_limit",
                            )
                        if len(prefix) < 8192:
                            prefix.extend(chunk[: 8192 - len(prefix)])
                        handle.write(chunk)
                    handle.flush()
                    os.fsync(handle.fileno())

                content_problem = classify_content(
                    bytes(prefix), response.headers.get("Content-Type")
                )
                if content_problem:
                    category, message = content_problem
                    raise DownloadError(message, category=category)
                validation_result = validator(part_path)
                os.replace(part_path, destination)
                return validation_result
        except PermissionError as exc:
            raise DownloadError(
                f"Permission denied while writing {destination}",
                category="permission_failure",
            ) from exc
        except OSError as exc:
            if getattr(exc, "winerror", None) == 112 or exc.errno == 28:
                raise DownloadError("Disk space exhausted", category="disk_space_failure") from exc
            raise
        finally:
            if part_path.exists():
                part_path.unlink()
