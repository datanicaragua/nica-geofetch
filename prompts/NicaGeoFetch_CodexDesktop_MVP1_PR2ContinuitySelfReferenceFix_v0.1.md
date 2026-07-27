Continue work in:

C:\Dev\nica-geofetch

PROMPT TAG
NicaGeoFetch_CodexDesktop_MVP1_PR2ContinuitySelfReferenceFix_v0.1

PROMPT VERSION
0.1

STATUS
FINAL — READY FOR EXECUTION

TARGET
Codex Desktop

PROJECT
Nica-GeoFetch

MILESTONE
MVP-1 — PR #2 continuity self-reference correction

EXISTING BRANCH
docs/mvp1-pr1-merge-continuity

EXISTING PULL REQUEST
https://github.com/datanicaragua/nica-geofetch/pull/2

CURRENT REMOTE HEAD
acee30115bff7b53687ffd5e3eb29572d18e2d6c

PURPOSE

Correct two self-stale continuity statements before PR #2 is merged.

The existing PR correctly records PR #1, human Colab validation, ChatGPT Project
audit, post-merge CI, and the remaining v0.1.0 gates.

Do not redesign or broadly rewrite the continuity documents.

PROBLEM

PROJECT_STATUS.md currently describes:

main at 141915416606abd47831775e677d89c6877643fb

as the active project baseline.

HANDOFF.md currently says local and remote main remain at 1419154.

Those statements are true before PR #2 merges but become false immediately
after PR #2 creates a new merge commit on main.

Continuity documentation must distinguish a historical implementation baseline
from the mutable current main HEAD.

REQUIRED CHANGES

Update:

- docs/PROJECT_STATUS.md
- docs/HANDOFF.md

In PROJECT_STATUS.md:

1. Replace the concept:

   Active project baseline: main at 1419154...

   with:

   MVP-1 implementation baseline from merged PR #1:
   141915416606abd47831775e677d89c6877643fb

2. Replace:

   Continuity task branch

   with:

   PR #2 continuity source branch

3. Do not claim that 1419154 will remain the current main HEAD after PR #2.

4. Preserve:
   - PR #1 merge evidence;
   - completed human validation;
   - completed ChatGPT audit;
   - remaining release gates;
   - release readiness not declared.

In HANDOFF.md:

1. Remove the statement that local and remote main remain at 1419154 after this
   closeout.

2. State instead that:
   - this documentation branch was created from PR #1 implementation baseline
     141915416606abd47831775e677d89c6877643fb;
   - after PR #2 integration, local main must be synchronized from origin/main
     using fast-forward only;
   - the actual PR #2 merge commit, once created, becomes the repository HEAD;
   - GitHub PR metadata is the source of truth for that future merge SHA.

3. Avoid predicting a merge SHA.

PROMPT TRACEABILITY

Archive this prompt at:

prompts/NicaGeoFetch_CodexDesktop_MVP1_PR2ContinuitySelfReferenceFix_v0.1.md

Register it in:

prompts/PROMPT_REGISTRY.md

GIT POLICY

Do not amend the already-pushed commit.

Do not force push.

Create one normal follow-up commit on the existing branch.

Suggested commit:

docs: avoid self-stale post-merge status

Push normally to:

docs/mvp1-pr1-merge-continuity

Update existing PR #2 only.

Do not create another branch or PR.

VALIDATION

Run:

pre-commit run --all-files
python scripts/publication_audit.py

Confirm:

- only documentation and prompt-traceability files changed;
- no code, notebook, provider configuration, data, tag, or release changed;
- working tree is clean after commit;
- PR #2 CI is green.

PR UPDATE

Add a concise PR comment explaining:

- the self-reference issue;
- files corrected;
- new commit SHA;
- no force push;
- final CI;
- merge still pending human authorization.

Do not merge PR #2.

Do not create a tag or release.

FINAL RESPONSE

Report:

1. Prompt tag.
2. Preflight.
3. Files changed.
4. Self-reference correction.
5. Commit SHA.
6. Normal push result.
7. PR #2 state and URL.
8. CI result.
9. Confirmation of no force push.
10. Confirmation of no merge, tag, or release.
11. Git status.
