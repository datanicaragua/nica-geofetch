## Summary

Describe the focused change and its motivation.

## Verification

- [ ] `ruff check .`
- [ ] `mypy src`
- [ ] `pytest -q`
- [ ] `python -m nica_geofetch.cli --help`
- [ ] `python scripts/publication_audit.py`
- [ ] `pre-commit run --all-files`
- [ ] wheel and sdist contents inspected
- [ ] clean-wheel installation smoke passed when release-facing packaging changed
- [ ] Continuity docs updated when milestone state changed
- [ ] No real institutional data, credentials, or generated data outputs added
- [ ] Dataset/software licensing separation preserved
- [ ] no tag, release, PyPI publication, repository-setting change, or institutional-data publication performed
