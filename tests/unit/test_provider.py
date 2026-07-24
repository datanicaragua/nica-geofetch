"""Provider configuration, URL construction, and registry behavior."""

from __future__ import annotations

from urllib.parse import parse_qs, urlsplit

import pytest

from nica_geofetch.providers.ineter_pfafstetter import IneterPfafstetterProvider


def test_unicode_url_encoding_and_required_parameters() -> None:
    provider = IneterPfafstetterProvider()
    url = provider.build_url(4)
    assert "Hidrol%C3%B3gica" in url
    query = parse_qs(urlsplit(url).query)
    assert query == {
        "layers": ["wsINETER-RH:Unidad_Hidrológica_Nacional_nivel4_2025"],
        "mode": ["download"],
        "kmattr": ["true"],
        "kmplacemark": ["true"],
    }


def test_provider_lists_only_mvp_dataset() -> None:
    datasets = IneterPfafstetterProvider().list_datasets()
    assert len(datasets) == 1
    assert datasets[0]["dataset_id"] == "ineter-pfafstetter-2025"
    assert datasets[0]["levels"] == [4, 5, 6, 7]


def test_provider_rejects_unconfigured_level() -> None:
    with pytest.raises(ValueError, match="4, 5, 6, or 7"):
        IneterPfafstetterProvider().build_url(3)
