"""Nica-GeoFetch: reproducible access to institutional geodata for Nicaragua."""

from nica_geofetch.models import OutputFormat, RetrievalMode
from nica_geofetch.providers.ineter_pfafstetter import IneterPfafstetterProvider

__all__ = ["IneterPfafstetterProvider", "OutputFormat", "RetrievalMode"]
__version__ = "0.1.0"
