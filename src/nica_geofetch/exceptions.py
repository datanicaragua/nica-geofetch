"""Domain exceptions with stable categories for CLI and notebook users."""


class NicaGeoFetchError(Exception):
    """Base exception for expected application failures."""


class ConfigurationError(NicaGeoFetchError):
    """Provider or user configuration is invalid."""


class SecurityError(NicaGeoFetchError):
    """A URL or redirect violates the downloader security policy."""


class DownloadError(NicaGeoFetchError):
    """A remote resource could not be downloaded safely."""

    def __init__(self, message: str, *, category: str = "download_failure") -> None:
        super().__init__(message)
        self.category = category


class ValidationError(NicaGeoFetchError):
    """A source document is not a usable vector KML."""


class ConversionError(NicaGeoFetchError):
    """A validated dataset could not be converted or reopened."""
