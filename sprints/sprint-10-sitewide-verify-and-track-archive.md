# Sprint 10 — Sitewide-Verify Mission + Python /track Retirement

**Theme**: Ops — close the VERIFY gap in the close-the-loop workflow; finish the /track honesty pass started in Sprint 9
**Effort**: S-M (estimated 3-4h; actual ~2h)
**Dependencies**: Sprint 9 (lifecycle states + backlog integration; VERIFY transition needs this)
**Status**: COMPLETE 2026-05-11

> **BACKFILL 2026-05-16**: Created retroactively from progress.md to restore the sprints/ pattern. See project-plan.md "Sprint conventions" for the discipline going forward.

## Sprint Goal

Add the missing VERIFY step to the close-the-loop workflow: a sitewide-verify mission that takes items in `shipped` state and confirms they're actually LIVE across the affected scope (not just locally committed). Plus formally retire the Python /track code path that Sprint 9 documented as "not validated end-to-end."

After Sprint 10, all 5 priority gaps from Jamie's freecalchub field findings are closed and the close-the-loop workflow has explicit support for all 8 steps.

## Motivation

Sprint 9 closed with two open items:
1. The `verified` lifecycle state had no mission to populate it — technical-fix refuses to mark verified, but there was nothing to do it instead
2. The Python /track decision was left dangling (Sprint 9 made docs honest but didn't structurally retire)

Plus Jamie's field finding #5: the freecalchub Twitter-tag class of bug (2 of 110 pages missed) was caught by spot-checking, not by structural sitewide verification. Without a mission that ENFORCES sitewide-not-sample, that bug class keeps happening.

Sprint 10 closes both opens.

## Scope: In

### Sitewide-verify mission (closes Top 5 #4 + #5)
- New mission file: `.claude/missions/sitewide-verify.md`
- Mode D mission, invoked via `/coord sitewide-verify <domain>`
- Reads `seo-backlog.md` for items in `shipped` status
- For each item, fetches the LIVE site and verifies the change actually landed
- Per-category verification methods: HTML head tags (canonical, meta, OG), JSON-LD schema, robots.txt directives, llms.txt presence, page content
- **Critical rule**: claims of "sitewide" coverage require checking 100% of the affected directory pattern, NOT a sample. Closes the freecalchub Twitter-tag class of gap
- Updates backlog: `shipped → verified` for confirmed; `shipped → in_progress` for commit-found-but-not-deployed; `shipped → reverted` for broke-something
- Refuses to mark items `closed` (closure still requires `/track compare` confirming metric movement, Constitution rule 5)
- Produces `verification.md` deliverable in `runs/<date>-<domain>-sitewide-verify/`

### coord.md restoration + 5th SEO mission
- Discovered: dev repo's `.claude/commands/coord.md` had been reverted to framework version at some point (lost SEO Mode D additions). Would have propagated broken coord.md to any new install.sh run
- Restored Mode D block (4 SEO missions) AND added `sitewide-verify` as the 5th in same edit
- Wrapped in `<!-- SEO-PRODUCT-LAYER-START/END -->` markers per established convention
- Updated dispatch step 5, Unknown Mission help, Examples section to include new mission
- Updated mode legend to document seo-backlog.md context loading per Sprint 9

### technical-fix wiring
- `technical-fix.md` OUTPUTS section explicitly directs users to `/coord sitewide-verify <domain>` as the canonical next step after items reach `shipped` state
- No more vague "verification pass needed" prose

### Python /track retirement (closes Top 5 #1)
- Sprint 9 made docs honest. Sprint 10 makes structure match.
- Moved 11 Python files from `tracking/` to `tracking/legacy/` via `git mv`:
  - `track.py`, `track_cli.py` (main /track entry)
  - `client_dashboard.py`, `competitive_benchmarking.py`, `marketing_automation.py`, `marketing_generator.py`, `presentation_exports.py`, `report_engine.py`, `report_exports.py`, `report_types.py`, `test_data.py` (supporting modules)
- Added `tracking/legacy/README.md`: full archive context, what was in each file, what replaced it (Sprint 9 agent-prompt /track baseline + compare), revival instructions
- Kept `tracking/schemas/` and `tracking/templates/` at top level — schemas still useful as documentation; Mustache templates may be reused for future report generation
- Updated `.claude/commands/track.md` "LEGACY COMMANDS" → "ARCHIVED PATH" pointing at `tracking/legacy/`. No more documented commands that don't actually work

### install.sh extension
- Phase 3 SEO mission count 4 → 5; copies `sitewide-verify.md` alongside the other four

## Scope: Out

- Validating the Python /track code end-to-end — would have taken hours and likely surfaced bit-rot; archive path is faster and aligned with Sprint 9 agent-prompt direction. Revival instructions in tracking/legacy/README.md preserve option
- Per-domain settings.json provisioning — Sprint 11 candidate (surfaced 2026-05-16 when sitewide-verify was actually run for the first time)
- Updating 14 existing workspaces with new sitewide-verify mission — operational task left to user (later done 2026-05-16 via install-fleet.sh --upgrade)

## Task List

- [x] Build sitewide-verify mission file (.claude/missions/sitewide-verify.md) with per-category verification methods, sitewide enforcement rule, backlog state transition logic (2026-05-11)
- [x] Restore SEO Mode D to dev repo's coord.md AND add sitewide-verify as 5th Mode D mission (one edit; SEO-PRODUCT-LAYER markers) (2026-05-11)
- [x] Update technical-fix.md to point at /coord sitewide-verify as canonical next step (2026-05-11)
- [x] Archive 11 Python /track files to tracking/legacy/ via git mv (2026-05-11)
- [x] Write tracking/legacy/README.md with full context + revival instructions (2026-05-11)
- [x] Update .claude/commands/track.md: LEGACY → ARCHIVED PATH (2026-05-11)
- [x] Extend install.sh Phase 3 to include sitewide-verify (2026-05-11)
- [x] Smoke test install.sh --dry-run picks up sitewide-verify + restored Mode D coord.md (2026-05-11)
- [x] Update tracking files (project-plan.md Sprint 10 row, progress.md entry) (2026-05-11)
- [x] Commit + push (2026-05-11, commit 566483b)

## Acceptance Criteria

- `.claude/missions/sitewide-verify.md` exists; Mode D mission; reads backlog; fetches live site; updates backlog state
- `/coord` routing accepts `sitewide-verify` as 5th SEO mission name; Unknown Mission help lists all 5
- technical-fix.md explicitly names `/coord sitewide-verify` as the next step after `shipped` state
- `tracking/legacy/` contains all 11 Python files via `git mv` (history preserved)
- `tracking/legacy/README.md` documents the archive rationale + revival path
- install.sh Phase 3 copies 5 SEO missions (including sitewide-verify)
- `bash install.sh /tmp/install-test --dry-run` confirms the new mission appears in install plan

## Assessment Protocol (freecalchub.com)

Validation deferred to next freecalchub work session — Sprint 10 is structural; the real test is running `/coord sitewide-verify freecalchub.com` against the May-10 shipped items.

(Done 2026-05-16 — surfaced Sprint 11 candidates: nested subagent Bash refusal, AskUserQuestion non-propagation, production curl allowlist required. Mission completed as `deferred` per Constitution rule 5; freecalchub items FCH-TF-003 + FCH-TF-004 stay shipped-deferred until Sprint 11 lands.)

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Python archive accidentally breaks something that quietly depended on those files | git mv preserves history; revival is one mv command per file; tracking/legacy/README documents path; no callers in active SEO product layer (verified by grep) |
| sitewide-verify mission fabricates "verified" state without real evidence | Critical don'ts in mission file: "DON'T spot-check items claimed to be sitewide"; "DON'T move items to closed from this mission"; "DON'T mark verified based on local commit messages" |
| coord.md changes overwritten by future framework upgrade | SEO-PRODUCT-LAYER-START/END markers per established pattern; install.sh re-applies on --upgrade |
| 14 existing workspaces don't auto-receive sitewide-verify until user runs upgrade | Documented in exit notes; later done 2026-05-16 |

## Exit Notes

Captured in progress.md 2026-05-11:
- All 5 priority gaps from Jamie's freecalchub field findings now closed
- Close-the-loop workflow has explicit support for all 8 steps (BASELINE / ANALYSE / PLAN / EXECUTE / VERIFY / RE-BASELINE / COMPARE / UPDATE PLAN)
- "No further sprints planned" at Sprint 10 close — operational sprints (8+) emerged from real use; assumption was the v2 architecture was now structurally complete

Validation outcome (2026-05-16):
- Sprint 10's mission DID work structurally — Phase 1 scoping ran cleanly, no-fabrication discipline held under pressure
- BUT: real-world execution surfaced 3 new harness/permission frictions documented as Sprint 11 candidates
- Sprint 10's claim "all 5 priority gaps closed" was architecturally true but practically incomplete; operating the library against production introduces a tier of frictions architecture-without-use doesn't surface

The discipline of using the library on real problems IS what surfaces next-tier frictions. Constitution rule 5 (Prove it) applies to the library itself.
