# Contributing

Read `AGENTS.md`, `docs/PROJECT_STATUS.md`, and `docs/HANDOFF.md` before
changing the project. MVP-1 accepts focused improvements to the implemented
INETER Pfafstetter provider, validation, conversion, packaging, documentation,
and offline tests.

Do not commit institutional source data. Use compact synthetic KML fixtures.
Do not add a provider without a documented source, access protocol, attribution
and licensing assessment.

Run before proposing a change:

```bash
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
```

Update `CHANGELOG.md` for user-visible changes and the continuity documents
when changing milestone state or the recommended next action.
