# Contributing

Read `AGENTS.md`, `docs/PROJECT_STATUS.md`, and `docs/HANDOFF.md` before
changing the project. MVP-1 accepts focused improvements to the implemented
INETER Pfafstetter provider, validation, conversion, packaging, documentation,
and offline tests.

Do not commit institutional source data. Use compact synthetic KML fixtures.
Do not add a provider without a documented source, access protocol, attribution
and licensing assessment.

## Branches and pull requests

Use one branch for each coherent change set or milestone. Do not create a
branch for every trivial typo, and do not combine unrelated features.

Use these branch patterns:

- `fix/<milestone>-<short-purpose>`
- `feat/<milestone-or-domain>-<short-purpose>`
- `docs/<short-purpose>`
- `chore/<short-purpose>`
- `release/<version>`

The durable workflow for every nontrivial change is:

1. Do not commit directly to `main`; create a focused task branch.
2. Keep one coherent change set on that branch.
3. Record the governing prompt tag in the pull request.
4. Run all applicable local quality gates before pushing.
5. Open a draft pull request before final review.
6. Require green GitHub Actions before marking the pull request ready.
7. Submit the open pull request and evidence to ChatGPT Project for independent
   review.
8. Obtain human approval before merging.
9. Obtain separate explicit human approval before creating any tag or release.
10. Never add institutional datasets to Git.

Do not force push, rewrite shared history, enable auto-merge, or merge without
the applicable human authorization.

## Local quality gates

Run before proposing a change:

```bash
ruff check .
mypy src
pytest -q
python -m nica_geofetch.cli --help
```

Update `CHANGELOG.md` for user-visible changes and the continuity documents
when changing milestone state or the recommended next action.
