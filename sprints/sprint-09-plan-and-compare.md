# Sprint 9 — Plan + Compare (Close-the-Loop Discipline)

**Theme**: Ops — make Constitution rule 5 ("Prove it") actually operational
**Effort**: M (estimated 4-6h; actual ~3h)
**Dependencies**: Sprint 5 (deliverable contract), Sprint 8 (installer enables rollout)
**Status**: COMPLETE 2026-05-11

> **BACKFILL 2026-05-16**: Created retroactively from progress.md to restore the sprints/ pattern. See project-plan.md "Sprint conventions" for the discipline going forward.

## Sprint Goal

Build the operational discipline freecalchub field work surfaced: baseline sites before making changes, capture findings into a managed action plan, drive actions through a lifecycle to completion, and prove (or disprove) that fixes actually moved metrics.

After Sprint 9, the close-the-loop SEO workflow has explicit support: BASELINE → ANALYSE → PLAN → EXECUTE → (VERIFY) → RE-BASELINE → COMPARE → UPDATE PLAN. Sprint 10 adds the missing VERIFY step.

## Motivation

Trigger: Jamie's field findings doc captured in `docs/library-improvements-input.md` after the first freecalchub work session. Top 5 priority gaps from real use:

1. `/track` documented as "Complete and Tested" but actually just config — biggest credibility risk
2. No roadmap template — Sprint 9 introduces one
3. No standard backlog file — Sprint 9 introduces one
4. Missions don't define "done" as "live and verified" — Sprint 9 partially addresses; Sprint 10 completes
5. No post-deploy sitewide verification — Sprint 10 addresses

Sprint 9 addresses #1 honestly (without yet retiring the Python — that's Sprint 10), #2, #3, and the structural piece of #4 (technical-fix refuses to mark items verified).

## Scope: In

### Plan side
- `templates/deliverables/seo-roadmap.md` — strategic per-site, longer-lived. Themes with target metrics + deadlines, constraints, long-running initiatives, risk register, retros. Refreshed quarterly.
- `templates/deliverables/seo-backlog.md` — operational action list with stable item IDs (e.g. `FCH-001`) and 6-state lifecycle:
  ```
  identified → planned → in_progress → shipped → verified → closed
                                            ↓
                                         reverted
  ```
- Tables: open items, in-flight, recently-shipped-awaiting-verify, recently-verified-awaiting-impact, archive
- `site-audit.md` mission updated: READ backlog before producing fixes (Constitution rule 1 — no duplicates); WRITE new identified items; touch roadmap "Current state" only
- `technical-fix.md` mission updated: drive items through identified → in_progress → shipped ONLY. Refuses to mark verified or closed (verified requires sitewide-verify in Sprint 10; closed requires /track compare confirming metric movement per rule 5)

### Compare side
- `templates/deliverables/comparison-report.md` — markdown deltas with scorecard breakdowns, live metrics deltas (when available), backlog item closures triggered by the comparison, regressions section, "what we cannot prove" section enforcing rule 5
- `.claude/commands/track.md` rewritten honestly:
  - **SHIPPED COMMANDS** (Sprint 9): `/track baseline <domain>`, `/track compare <domain>` — agent-prompt path operating on Sprint 5 data.json files
  - **LEGACY COMMANDS** (Python): `status`, `roi`, `report` — surface defined in `tracking/track_cli.py` (463 lines) but `tracking/baselines/` and `tracking/snapshots/` empty in source repo. Documented as "not validated end-to-end; treat outputs as exploratory until validated"
  - (Sprint 10 formally retires the Python path)

## Scope: Out

- Building agent-prompt versions of `/track status`, `roi`, `report` — only baseline + compare were urgent; others deferred
- Python tracking system validation OR retirement — Sprint 9 makes docs honest; Sprint 10 either proves or retires
- Sitewide-verify mission — Sprint 10
- Roadmap themes / strategic content per site — template provided; population is per-workspace operational work

## Task List

- [x] Inventory current /track + plan/backlog state (Python code exists at 311+463 lines but baselines/snapshots empty; zero existing backlog template; freecalchub runs/ has 2 complete deliverable sets for validation) (2026-05-11)
- [x] Design Plan side: roadmap + backlog templates + 6-state lifecycle + mission integration (2026-05-11)
- [x] Design Compare side: minimum viable /track baseline + compare via agent prompts on data.json files (not Python — alignment with v6 architecture) (2026-05-11)
- [x] Build templates/deliverables/seo-roadmap.md (2026-05-11)
- [x] Build templates/deliverables/seo-backlog.md (2026-05-11)
- [x] Build templates/deliverables/comparison-report.md (2026-05-11)
- [x] Update site-audit.md OUTPUTS section: backlog read/write integration (2026-05-11)
- [x] Update technical-fix.md OUTPUTS section: lifecycle drive identified→in_progress→shipped only (2026-05-11)
- [x] Rewrite .claude/commands/track.md honestly: shipped vs legacy (2026-05-11)
- [x] Update templates/deliverables/README.md with new artefacts and per-site vs per-run classification (2026-05-11)
- [x] Validate against freecalchub data: backlog template works on 8 fixes from site-audit data.json; roadmap scorecards populate; compare deltas computable; all top-level schema keys present (2026-05-11)
- [x] Update tracking files (project-plan.md, progress.md) (2026-05-11)
- [x] Commit + push (2026-05-11, commit 03efb2a)

## Acceptance Criteria

- Three deliverable templates exist in `templates/deliverables/`: seo-roadmap.md, seo-backlog.md, comparison-report.md
- site-audit and technical-fix missions explicitly reference the backlog in their OUTPUTS sections
- technical-fix mission refuses to mark items verified or closed in its instructions
- `.claude/commands/track.md` honestly distinguishes shipped from legacy command surface
- Templates validate against freecalchub's existing runs/ data without schema modification

## Assessment Protocol (freecalchub.com)

Validation done against existing freecalchub run data, no new freecalchub run required:

1. Load freecalchub's site-audit data.json (8 fixes with stable IDs, ROI, category) — drop into seo-backlog.md rows: **PASS**
2. Compute scorecards before/after from site-audit + technical-fix data.json — populate roadmap "Current state": **PASS** (AI 39→43, Trad 36→41)
3. Compute deltas from two data.json files — populate comparison-report.md: **PASS** (matches 2026-05-10 seo-evidence.md entry)
4. Verify schema integrity: all top-level keys present (schema_version, mission, site, scorecards, fixes, prior_findings_referenced, next_suggested_mission): **PASS**

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Lifecycle states too rigid for real-world messiness | 6 states + reverted; explicit "in_progress → shipped only" rule for technical-fix prevents overclaiming; sitewide-verify (Sprint 10) handles edge cases |
| Item ID convention conflicts across sites | Per-site prefix (FCH, ASM, LTM, etc.); IDs stable across sessions; closed items keep IDs forever |
| Roadmap + backlog file conflict with seo-evidence.md (already-existing site-level state) | Three clearly differentiated roles: roadmap = strategy, backlog = ops, evidence = artefact store. Each has explicit "How this relates to the others" section |
| Compare templates require GA4/GSC data that's not always available | Comparison template has explicit "what we cannot prove" section enforcing rule 5; works without live metrics by using scorecards as the comparison axis |
| Python /track retirement leaves users hanging | Sprint 9 makes docs honest; doesn't archive until Sprint 10. Two-step approach reduces blast radius |

## Exit Notes

Captured in progress.md 2026-05-11:
- 4 new deliverable templates (roadmap, backlog, comparison + updated README)
- 2 missions updated with backlog integration
- track.md rewritten with shipped/legacy distinction
- Validated end-to-end against freecalchub's existing run data
- Sprint estimated M (4-6h), actual ~3h — existing infrastructure (Sprint 5 schema, tracking/schemas/baseline.schema.json, Mustache templates in tracking/templates/) made the difference; reused conceptually rather than reinvented

What this enabled going forward: every site running through SEO-Agent now has a managed backlog with lifecycle tracking, a strategic roadmap, and the ability to compare snapshots over time to prove (or disprove) impact. Constitution rule 5 ("Prove it") has the artefacts to be operational, not just principled.

Open items for Sprint 10: VERIFY step (sitewide-verify mission) + Python /track final decision (prove or retire).
