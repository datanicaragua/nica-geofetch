"""Offline tests for network security, classification, limits, and atomic files."""

from __future__ import annotations

from pathlib import Path

import pytest
import requests
import responses

from nica_geofetch.diagnostics import classify_request_exception
from nica_geofetch.download import SecureDownloader, validate_remote_url
from nica_geofetch.exceptions import DownloadError, SecurityError
from nica_geofetch.models import DownloadMetadata, DownloadSettings

OFFICIAL_URL = "https://geoserveridefn.ineter.gob.ni/geoserver/wms/kml?test=1"
ALLOWED_HOSTS = ("geoserveridefn.ineter.gob.ni",)


def settings(*, max_bytes: int = 1024 * 1024) -> DownloadSettings:
    return DownloadSettings(
        timeout_connect_seconds=1,
        timeout_read_seconds=1,
        max_response_bytes=max_bytes,
        retries=0,
        backoff_seconds=0,
        polite_delay_seconds=0,
        user_agent="Nica-GeoFetch-test",
    )


def downloader(*, max_bytes: int = 1024 * 1024) -> SecureDownloader:
    return SecureDownloader(allowed_hosts=ALLOWED_HOSTS, settings=settings(max_bytes=max_bytes))


def test_host_allowlisting() -> None:
    validate_remote_url(OFFICIAL_URL, ALLOWED_HOSTS)
    with pytest.raises(SecurityError, match="allowlisted"):
        validate_remote_url("https://example.invalid/data.kml", ALLOWED_HOSTS)
    with pytest.raises(SecurityError, match="HTTPS"):
        validate_remote_url(
            "http://geoserveridefn.ineter.gob.ni/data.kml",
            ALLOWED_HOSTS,
        )


@responses.activate
def test_redirect_to_non_allowlisted_host_is_rejected() -> None:
    responses.add(
        responses.GET,
        OFFICIAL_URL,
        status=302,
        headers={"Location": "https://example.invalid/redirected.kml"},
    )
    with pytest.raises(SecurityError, match="allowlisted"):
        downloader().probe(OFFICIAL_URL)


@responses.activate
def test_http_200_ogc_error_is_classified() -> None:
    responses.add(
        responses.GET,
        OFFICIAL_URL,
        status=200,
        body=b"<?xml version='1.0'?><ServiceExceptionReport/>",
        content_type="application/xml",
    )
    report = downloader().probe(OFFICIAL_URL)
    assert not report.ok
    assert report.category == "ogc_error"
    assert report.official_url == OFFICIAL_URL
    assert "browser" in (report.manual_download_instructions or "")


@responses.activate
def test_response_size_limit_removes_part_file(tmp_path: Path) -> None:
    responses.add(
        responses.GET,
        OFFICIAL_URL,
        status=200,
        body=b"x" * 100,
        headers={"Content-Length": "100"},
    )
    destination = tmp_path / "source.kml"
    with pytest.raises(DownloadError) as raised:
        downloader(max_bytes=50).download(
            OFFICIAL_URL,
            destination,
            lambda path, _metadata: path,
        )
    assert raised.value.category == "response_size_limit"
    assert not destination.exists()
    assert not (tmp_path / "source.kml.part").exists()


@responses.activate
def test_atomic_file_handling(tmp_path: Path) -> None:
    body = b"<?xml version='1.0'?><kml/>"
    responses.add(responses.GET, OFFICIAL_URL, status=200, body=body)
    destination = tmp_path / "source.kml"

    def validate_part(part: Path, metadata: DownloadMetadata) -> bytes:
        assert part.name.endswith(".part")
        assert part.exists()
        assert not destination.exists()
        assert metadata.source_url == OFFICIAL_URL
        assert metadata.byte_size == len(body)
        return part.read_bytes()

    result = downloader().download(OFFICIAL_URL, destination, validate_part)
    assert result == body
    assert destination.read_bytes() == body
    assert not (tmp_path / "source.kml.part").exists()


def test_dns_diagnostic_classification() -> None:
    exception = requests.ConnectionError("getaddrinfo failed: 11001")
    assert classify_request_exception(exception)[0] == "dns_failure"


@pytest.mark.parametrize(
    ("exception", "category"),
    [
        (requests.exceptions.ConnectTimeout(), "connection_timeout"),
        (requests.exceptions.ReadTimeout(), "read_timeout"),
        (requests.exceptions.SSLError(), "tls_failure"),
        (requests.exceptions.ProxyError(), "proxy_failure"),
    ],
)
def test_timeout_tls_and_proxy_classification(
    exception: requests.RequestException,
    category: str,
) -> None:
    assert classify_request_exception(exception)[0] == category
