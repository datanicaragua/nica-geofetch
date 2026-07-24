"""Technical command-line interface for Nica-GeoFetch MVP-1."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

from nica_geofetch.exceptions import NicaGeoFetchError
from nica_geofetch.logging_utils import configure_logging
from nica_geofetch.models import OutputFormat
from nica_geofetch.providers.ineter_pfafstetter import IneterPfafstetterProvider
from nica_geofetch.workflows import download_workflow, import_local_workflow

PROVIDER_ID = "ineter-pfafstetter"
FORMAT_CHOICES = [item.value for item in OutputFormat] + ["all"]


def _provider(value: str) -> IneterPfafstetterProvider:
    if value != PROVIDER_ID:
        raise ValueError(f"Unknown provider: {value}")
    return IneterPfafstetterProvider()


def _formats(values: list[str]) -> list[OutputFormat]:
    if "all" in values:
        return list(OutputFormat)
    return [OutputFormat(value) for value in values]


def _print_json(value: Any, *, stream: TextIO | None = None) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False), file=stream or sys.stdout)


def _providers_list(_args: argparse.Namespace) -> int:
    provider = IneterPfafstetterProvider()
    _print_json(
        [
            {
                "provider_id": provider.provider_id,
                "title": provider.config.title,
                "status": "implemented",
            }
        ]
    )
    return 0


def _datasets_list(args: argparse.Namespace) -> int:
    _print_json(_provider(args.provider).list_datasets())
    return 0


def _diagnose(args: argparse.Namespace) -> int:
    report = _provider(args.provider).diagnose(
        args.level,
        ca_bundle=args.ca_bundle,
    )
    _print_json(report.to_dict())
    return 0 if report.ok else 1


def _download(args: argparse.Namespace) -> int:
    result = download_workflow(
        levels=args.levels,
        formats=_formats(args.formats),
        output_directory=args.output,
        repair=args.repair,
        ca_bundle=args.ca_bundle,
        provider=_provider(args.provider),
    )
    _print_json(
        {
            "valid": result.valid,
            "output_directory": str(result.output_directory),
            "archive": str(result.archive_path),
            "summary": result.summary_rows(),
        }
    )
    return 0


def _validate(args: argparse.Namespace) -> int:
    report = IneterPfafstetterProvider().import_local(
        args.input,
        args.level,
        repair=args.repair,
    )
    _print_json(report.to_dict())
    return 0 if report.valid else 1


def _import_local(args: argparse.Namespace) -> int:
    result = import_local_workflow(
        input_path=args.input,
        level=args.level,
        formats=_formats(args.formats),
        output_directory=args.output,
        repair=args.repair,
    )
    _print_json(
        {
            "valid": result.valid,
            "output_directory": str(result.output_directory),
            "archive": str(result.archive_path),
            "summary": result.summary_rows(),
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the public CLI parser for help and smoke testing."""

    parser = argparse.ArgumentParser(
        prog="nica-geofetch",
        description="Reproducible access to trusted institutional geodata for Nicaragua.",
    )
    parser.add_argument("--verbose", action="store_true", help="Show detailed progress logs.")
    commands = parser.add_subparsers(dest="command", required=True)

    providers = commands.add_parser("providers", help="Inspect implemented providers.")
    provider_commands = providers.add_subparsers(dest="providers_command", required=True)
    providers_list = provider_commands.add_parser("list", help="List implemented providers.")
    providers_list.set_defaults(handler=_providers_list)

    datasets = commands.add_parser("datasets", help="Inspect configured datasets.")
    dataset_commands = datasets.add_subparsers(dest="datasets_command", required=True)
    datasets_list = dataset_commands.add_parser("list", help="List provider datasets.")
    datasets_list.add_argument("--provider", required=True, choices=[PROVIDER_ID])
    datasets_list.set_defaults(handler=_datasets_list)

    diagnose = commands.add_parser("diagnose", help="Diagnose official endpoint access.")
    diagnose.add_argument("--provider", required=True, choices=[PROVIDER_ID])
    diagnose.add_argument("--level", type=int, choices=[4, 5, 6, 7], default=4)
    diagnose.add_argument("--ca-bundle", type=Path)
    diagnose.set_defaults(handler=_diagnose)

    download = commands.add_parser(
        "download",
        help="Download, validate, convert, audit, and package selected levels.",
    )
    download.add_argument("--provider", required=True, choices=[PROVIDER_ID])
    download.add_argument("--levels", nargs="+", type=int, choices=[4, 5, 6, 7], required=True)
    download.add_argument("--formats", nargs="+", choices=FORMAT_CHOICES, required=True)
    download.add_argument("--output", type=Path, required=True)
    download.add_argument(
        "--repair", action="store_true", help="Explicitly repair invalid geometry."
    )
    download.add_argument("--ca-bundle", type=Path)
    download.set_defaults(handler=_download)

    validate = commands.add_parser("validate", help="Validate one local KML without conversion.")
    validate.add_argument("--input", type=Path, required=True)
    validate.add_argument("--level", type=int, choices=[4, 5, 6, 7], required=True)
    validate.add_argument(
        "--repair", action="store_true", help="Explicitly repair invalid geometry."
    )
    validate.set_defaults(handler=_validate)

    import_local = commands.add_parser(
        "import-local",
        help="Validate, convert, audit, and package a manually supplied KML.",
    )
    import_local.add_argument("--level", type=int, choices=[4, 5, 6, 7], required=True)
    import_local.add_argument("--input", type=Path, required=True)
    import_local.add_argument("--formats", nargs="+", choices=FORMAT_CHOICES, required=True)
    import_local.add_argument("--output", type=Path, required=True)
    import_local.add_argument(
        "--repair", action="store_true", help="Explicitly repair invalid geometry."
    )
    import_local.set_defaults(handler=_import_local)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""

    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)
    try:
        return int(args.handler(args))
    except (NicaGeoFetchError, OSError, ValueError) as exc:
        category = getattr(exc, "category", exc.__class__.__name__)
        _print_json(
            {"ok": False, "category": category, "message": str(exc)},
            stream=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
