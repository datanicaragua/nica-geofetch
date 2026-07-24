"""Audit publication candidates for forbidden data and common secret signatures."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_KML_PREFIX = "tests/fixtures/"
FORBIDDEN_DATA_SUFFIXES = {
    ".gpkg",
    ".kmz",
    ".shp",
    ".shx",
    ".dbf",
    ".prj",
    ".cpg",
}
SENSITIVE_FILE_NAMES = {
    ".env",
    "credentials.json",
    "id_rsa",
    "id_ed25519",
    "service-account.json",
}
SECRET_PATTERNS = {
    "private_key": re.compile("-" * 5 + r"BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY"),
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    "aws_access_key": re.compile(r"AKIA[A-Z0-9]{16}"),
    "google_api_key": re.compile(r"AIza[A-Za-z0-9_-]{30,}"),
    "slack_token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
}


def publication_candidates() -> list[str]:
    """List tracked plus untracked/non-ignored files for pre-commit auditing."""

    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(set(result.stdout.splitlines()))


def main() -> int:
    """Print a compact JSON audit and fail when a release blocker is found."""

    candidates = publication_candidates()
    forbidden_data = [
        name
        for name in candidates
        if Path(name).suffix.lower() in FORBIDDEN_DATA_SUFFIXES
        or (
            name.lower().endswith(".kml")
            and not name.replace("\\", "/").startswith(ALLOWED_KML_PREFIX)
        )
    ]
    sensitive_names = [
        name for name in candidates if Path(name).name.lower() in SENSITIVE_FILE_NAMES
    ]
    secret_findings: list[dict[str, object]] = []
    for name in candidates:
        path = REPOSITORY_ROOT / name
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for kind, pattern in SECRET_PATTERNS.items():
                if pattern.search(line):
                    secret_findings.append({"file": name, "line": line_number, "kind": kind})

    report = {
        "candidate_file_count": len(candidates),
        "forbidden_institutional_data": forbidden_data,
        "sensitive_file_names": sensitive_names,
        "secret_findings": secret_findings,
        "passed": not (forbidden_data or sensitive_names or secret_findings),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
