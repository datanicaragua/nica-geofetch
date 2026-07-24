"""Allow `python -m nica_geofetch` to invoke the technical CLI."""

from nica_geofetch.cli import main

raise SystemExit(main())
