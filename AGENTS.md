# Agent guide

Nica-GeoFetch is a focused DataNicaTools Python package for reproducible access
to trusted institutional geodata for Nicaragua. MVP-1 implements only the
INETER Pfafstetter 2025 KML provider (levels 4-7), validation, conversion,
packaging, CLI, notebook, and supporting documentation.

Do not build a web UI, API, server, mirror, generalized plugin platform, or
future providers in MVP-1. Run `ruff check .`, `mypy src`, `pytest -q`, and
`python -m nica_geofetch.cli --help` before declaring work stable.

Durable documentation starts at `docs/index.md`. Milestone truth lives in
`docs/PROJECT_STATUS.md`; resume from `docs/HANDOFF.md`; record decisions and
completed work in `docs/DECISION_LOG.md` and `docs/PHASE_LOG.md`.

Before adding a component, apply the component value gate in
`docs/ARCHITECTURE.md`. Components without a demonstrated user need, acceptance
test, and justified maintenance burden remain deferred.

Institutional datasets are third-party data, not Apache-2.0 software. Never
commit or publish real KML or converted institutional data. Do not call INETER
data open unless an explicit license is found. Never push, publish, or upload
institutional data from this repository.

## Resume protocol

Before continuing any future task:

1. Read `AGENTS.md`.
2. Read `docs/index.md`.
3. Read `docs/PROJECT_STATUS.md`.
4. Read `docs/HANDOFF.md`.
5. Review `docs/ROADMAP.md`.
6. Run `git status`.
7. Inspect the current branch and recent commits.
8. Run the documented smoke test.
9. Continue from `NEXT_ACTION` in `HANDOFF.md`.
10. Update `PROJECT_STATUS.md`, `PHASE_LOG.md`, and `HANDOFF.md` before stopping.
