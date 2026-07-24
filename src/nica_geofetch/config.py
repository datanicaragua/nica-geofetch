"""Provider configuration loading with validated built-in defaults."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from nica_geofetch.exceptions import ConfigurationError
from nica_geofetch.models import DownloadSettings, ProviderConfig

DEFAULT_PROVIDER_DATA: dict[str, Any] = {
    "provider_id": "ineter-pfafstetter",
    "title": "INETER Pfafstetter-adjusted national hydrographic units, 2025",
    "endpoint": "https://geoserveridefn.ineter.gob.ni/geoserver/wms/kml",
    "allowed_hosts": ["geoserveridefn.ineter.gob.ni"],
    "layers": {
        4: "wsINETER-RH:Unidad_Hidrológica_Nacional_nivel4_2025",
        5: "wsINETER-RH:Unidad_Hidrológica_Nacional_nivel5_2025",
        6: "wsINETER-RH:Unidad_Hidrológica_Nacional_nivel6_2025",
        7: "wsINETER-RH:Unidad_Hidrológica_Nacional_nivel7_2025",
    },
    "code_aliases": {
        4: ["n4", "pfaf_n4", "pfaf4", "code_pfafs", "pfaf_code"],
        5: ["n5", "pfaf_n5", "pfaf5", "code_pfafs", "pfaf_code"],
        6: ["n6_", "n6", "pfaf_n6", "pfaf6", "code_pfafs", "pfaf_code"],
        7: ["code_pfafs", "pfaf_n7", "pfaf7", "pfaf_code", "n7"],
    },
    "plausible_bounds": [-88.5, 9.5, -82.0, 15.5],
    "network": {
        "timeout_connect_seconds": 10,
        "timeout_read_seconds": 90,
        "max_response_bytes": 100_000_000,
        "retries": 2,
        "backoff_seconds": 1,
        "polite_delay_seconds": 1,
        "user_agent": "Nica-GeoFetch/0.1 (+https://github.com/DataNicaTools/nica-geofetch)",
    },
}


def _repository_config_path() -> Path:
    return Path(__file__).resolve().parents[2] / "configs/providers/ineter_pfafstetter_2025.yml"


def _int_keyed_mapping(raw: Any, field_name: str) -> dict[int, Any]:
    if not isinstance(raw, dict):
        raise ConfigurationError(f"{field_name} must be a mapping")
    try:
        result = {int(key): value for key, value in raw.items()}
    except (TypeError, ValueError) as exc:
        raise ConfigurationError(f"{field_name} keys must be integer levels") from exc
    if set(result) != {4, 5, 6, 7}:
        raise ConfigurationError(f"{field_name} must configure exactly levels 4, 5, 6, and 7")
    return result


def load_provider_config(path: Path | None = None) -> ProviderConfig:
    """Load the provider YAML or fall back to the equivalent packaged defaults."""

    candidate = path or _repository_config_path()
    if candidate.exists():
        try:
            loaded = yaml.safe_load(candidate.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            raise ConfigurationError(f"Cannot load provider config {candidate}: {exc}") from exc
        if not isinstance(loaded, dict):
            raise ConfigurationError("Provider configuration root must be a mapping")
        data: dict[str, Any] = loaded
    elif path is not None:
        raise ConfigurationError(f"Provider configuration not found: {candidate}")
    else:
        data = DEFAULT_PROVIDER_DATA

    try:
        layers_raw = _int_keyed_mapping(data["layers"], "layers")
        aliases_raw = _int_keyed_mapping(data["code_aliases"], "code_aliases")
        bounds = tuple(float(value) for value in data["plausible_bounds"])
        network = data.get("network", {})
        if not isinstance(network, dict):
            raise ConfigurationError("network must be a mapping")
        if len(bounds) != 4:
            raise ConfigurationError("plausible_bounds must contain four numbers")
        layers = {level: str(value) for level, value in layers_raw.items()}
        aliases = {
            level: tuple(str(alias).strip().lower() for alias in value)
            for level, value in aliases_raw.items()
        }
        allowed_hosts = tuple(str(host).strip().lower() for host in data["allowed_hosts"])
        config = ProviderConfig(
            provider_id=str(data["provider_id"]),
            title=str(data["title"]),
            endpoint=str(data["endpoint"]),
            allowed_hosts=allowed_hosts,
            layers=layers,
            code_aliases=aliases,
            plausible_bounds=(bounds[0], bounds[1], bounds[2], bounds[3]),
            timeout_connect_seconds=float(network.get("timeout_connect_seconds", 10)),
            timeout_read_seconds=float(network.get("timeout_read_seconds", 90)),
            max_response_bytes=int(network.get("max_response_bytes", 100_000_000)),
            retries=int(network.get("retries", 2)),
            backoff_seconds=float(network.get("backoff_seconds", 1)),
            polite_delay_seconds=float(network.get("polite_delay_seconds", 1)),
            user_agent=str(
                network.get(
                    "user_agent",
                    "Nica-GeoFetch/0.1 (+https://github.com/DataNicaTools/nica-geofetch)",
                )
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise ConfigurationError(f"Invalid provider configuration: {exc}") from exc

    if not config.allowed_hosts or not all(config.allowed_hosts):
        raise ConfigurationError("At least one non-empty allowed host is required")
    if config.max_response_bytes <= 0 or config.retries < 0:
        raise ConfigurationError("Response limit must be positive and retries cannot be negative")
    return config


def download_settings(config: ProviderConfig, ca_bundle: Path | None = None) -> DownloadSettings:
    """Create immutable downloader settings from provider configuration."""

    return DownloadSettings(
        timeout_connect_seconds=config.timeout_connect_seconds,
        timeout_read_seconds=config.timeout_read_seconds,
        max_response_bytes=config.max_response_bytes,
        retries=config.retries,
        backoff_seconds=config.backoff_seconds,
        polite_delay_seconds=config.polite_delay_seconds,
        user_agent=config.user_agent,
        ca_bundle=ca_bundle,
    )
