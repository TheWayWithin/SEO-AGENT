# Agent Context — SEO-Agent v2 Evolution

**Mission**: Evolve SEO-Agent from v1 (Agent-11 v5 clone) to v2 (Agent-11 v6 style: slim, deliverable-first, AI-search-aware)
**Source of truth**: `ideation/SEO-Agent v2 Blueprint_ Applying the Agent-11 Lessons.md`
**Started**: 2026-04-19
**v1 archive**: `project-plan.v1-archive.md`

---

## Mission Objective

Apply five Agent-11 v6 lessons to SEO-Agent, delivered as seven sequential sprints with user sign-off between each:

1. Command Surface Slim-Down — remove generic dev missions
2. Karpathy SEO Constitution — rewrite CLAUDE.md under 80 lines
3. Agent De-Bloat & Context Consolidation — strip MANDATORY CONTEXT PROTOCOL, 4 files to 2
4. Universal Mission Router — natural-language dispatch
5. Deliverable-First Missions — every run produces Analysis + Marketing + AImpactScanner data
6. Automated Tracking Routines — weekly snapshots, monthly reports
7. AI Search First Lens — LLM ingestion scorecard on every output

## Key Decisions Captured

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-19 | Seven-sprint structure agreed | User preference for small assessment cycles, one feature at a time |
| 2026-04-19 | freecalchub.com is the assessment site for every sprint | Real user traffic, representative SEO surface area, user's primary site |
| 2026-04-19 | v1 plan archived, not deleted | Preserve history and rationale for past decisions |
| 2026-04-19 | Blueprint is the source of truth | If blueprint and current code disagree, blueprint wins unless a documented exception is raised |
| 2026-04-19 | Only SEO missions in scope | site-audit, content-gap, technical-fix, ai-search-optimize. All generic dev missions removed in Sprint 1 |
| 2026-04-19 | Context files reduce from 4 to 2 in Sprint 3 | Keep project-plan.md (forward) and seo-evidence.md (backward). Retire seo-context.md, seo-handoff.md, mission-state.md as mandatory |
| 2026-04-19 | handoff-notes.md and agent-context.md remain as optional lightweight aids | They are not mandatory at every agent hand-off under v2 |

## Accumulated Findings

### Sprint 2 — Karpathy SEO Constitution (closed 2026-05-09)

- Project-root `CLAUDE.md` reduced 424 → 50 lines (88% line cut, 82% word cut)
- Old file preserved at `CLAUDE.v1-archive.md`
- Five blueprint rules encoded; two-layer model documented; product file map included
- `/coord site-audit` smoke-dispatch test deferred to Sprint 1 (currently fails with "Unknown mission" because SEO missions not yet registered in framework `/coord`)
- Verified `/track` subcommand names against `.claude/commands/track.md` before drafting (avoided guessed contents)
- Verified `/seo-commands` exposes `/rankings`, `/traffic-report`, `/technical-health`, `/report` (not just `seo-commands` itself)

### Phase Handoff: Sprint 2 → Sprint 1

**Next sprint**: Sprint 1 — Register SEO missions in `/coord`; normalise mission paths.

**Inherited tasks from Sprint 2**:
- Run `/coord site-audit freecalchub.com` smoke dispatch as part of Sprint 1 acceptance — proves both Sprint 1 (registration) and Sprint 2 (constitution) end-to-end.

**Critical context for Sprint 1**:
- Decisions locked in rescope memo: drop NLP routing entirely; move `ai-search-optimize.md` from `/missions/` into `.claude/missions/`.
- Four SEO missions to register: `site-audit`, `content-gap`, `technical-fix`, `ai-search-optimize`.
- Routing should follow framework v6 deterministic style: `/coord <mission> [mode] [target]` positional args. No keyword maps, no inference.
- Edit target: `.claude/commands/coord.md` routing table + Unknown Mission Behaviour section.
- Also update `.claude/commands/seo-commands.md` to point at the four canonical mission paths.

### Sprint 1 — SEO Missions Registered (closed 2026-05-09)

- New **Mode D — SEO** introduced in `coord.md` (per-run scoped, loads `seo-evidence.md` only). Cleaner than folding into Maintenance B2.
- All 4 SEO missions now co-located in `.claude/missions/` (`ai-search-optimize.md` moved via `git mv`).
- coord.md additions wrapped in `<!-- SEO-PRODUCT-LAYER-START/END -->` marker comments for upgrade resilience. After any framework refresh, search for the marker; if absent, re-apply per progress.md Sprint 1 entry.
- `seo-commands.md` confirmed untouched — uses `@agent` delegation directly, no mission paths to update.
- Rejected alternative: standalone `/seo` wrapper command. Edited framework `coord.md` instead per rescope memo wording. Trade-off accepted: maintenance friction vs cleaner UX.

### Phase Handoff: Sprint 1 → Sprint 3

**Next sprint**: Sprint 3 — Agent de-bloat & SEO context consolidation.
**Skipping Sprint 4** (cancelled in rescope; merged into Sprint 1 above).
**First Full-gate sprint** — requires real freecalchub.com audit before/after.

**Critical context for Sprint 3**:
- 7 SEO agents to de-bloat (not 6 — count includes `seo-coordinator`): seo-strategist, seo-coordinator, seo-technical, seo-content, seo-researcher, seo-analyst, seo-builder. All ~200-260 lines each, total ~1,544 lines.
- All 7 confirmed (via grep) to still carry MANDATORY CONTEXT PROTOCOL block.
- Templates to archive: `seo-context-template.md`, `seo-handoff-template.md`, `mission-state-template.md` (note: `mission-state-template.md` exists in `/templates/` but no `seo-` prefix; verify it's actually SEO-specific).
- Templates to keep: `seo-evidence-template.md` (the back-looking artefact store, referenced by SEO Constitution rule 1).
- Coordinator enforcement edits target `agents/seo-coordinator.md` only — leave `.claude/agents/coordinator.md` (framework) alone.
- Mission files in `.claude/missions/` (all 4) likely reference the old context files in their CONTEXT INITIALIZATION sections — example seen in `ai-search-optimize.md` lines 9-15. Will need de-referencing.
- Baseline + post-change freecalchub.com audit on the same single page (recommend `freecalchub.com/calculators/bmi-calculator` per original Sprint 3 doc) for real token-cost and quality comparison.
- Now that SEO missions dispatch via Sprint 1, Sprint 3's baseline audit is actually runnable end-to-end.

### Sprint 3 — Agent De-Bloat (closed 2026-05-09, Option B hybrid gate)

- Stripped MANDATORY CONTEXT PROTOCOL header + CONTEXT PRESERVATION REQUIREMENTS section + 3 scattered tracking lines from all 7 SEO agents. Net: −214 lines (−13.9%), −740 words (−8.7%) across 7 agents.
- Coordinator extras: cleaned Mission Planning Protocol + Mission Execution Framework of `mission-state.md` and `/workspace/` references.
- ai-search-optimize.md: stripped CONTEXT INITIALIZATION + Phase 1 Context Requirements. Other 3 missions (site-audit, content-gap, technical-fix) confirmed clean by grep.
- 3 SEO templates archived to `templates/archive/` via `git mv` (seo-context-template, seo-handoff-template, mission-state-template). seo-evidence-template retained per Constitution rule 1.
- 2 obsolete docs archived to `docs/archive/` via `git mv` (context-preservation-implementation, context-preservation-complete).
- README.md and `.claude/commands/track.md` updated to reference only `seo-evidence.md`.
- Repo-wide grep verification: ZERO context-protocol residue in active source. Historical references in planning docs are correct and retained.

**Gate decision rationale**: Option B chosen by user over original strict full-gate plan to respect 90-day IPP time pressure. Static measurement provides defensible "prompts are smaller" evidence; live audit deferred to user discretion.

**Finding for downstream sprints — DEPLOYMENT GAP**:
SEO agents at `/agents/seo-*.md` are NOT deployed to `.claude/agents/` (where Claude Code's Task tool looks). Current SEO mission flow uses `@agent` text-syntax delegation, not Task-tool dispatch. The slimmed agent prompts function as reference profiles, not loaded prompts. **Sprint 5 should resolve this** — either by deploying the agents into `.claude/agents/` or by explicitly documenting that the SEO system runs as text delegation only.

### Phase Handoff: Sprint 3 → Sprint 5

**Next sprint**: Sprint 5 — Deliverable-First Missions (Sprint 4 cancelled in rescope).
**Gate**: Full freecalchub.com run required (per rescope conditional matrix).

**Critical context for Sprint 5**:
- Slimmer agents now in place — Sprint 3 baseline metrics in this changelog if you want to compare token cost in a real run later.
- Three deliverable templates needed: Analysis Report, Marketing Report, AImpactScanner Data.
- Update site-audit, content-gap, technical-fix, ai-search-optimize missions to produce all three (or applicable subset).
- **Resolve the deployment gap noted above** before the gate run, otherwise the live audit won't actually exercise the SEO agents.
- End-to-end freecalchub.com run (not single-page) — gate requires three named deliverables to appear.
- ai-search-optimize.md was substantively trimmed in Sprint 3 — check whether the deliverable templates fit cleanly with the reduced structure.

### Sprint 5 — Deliverable-First Missions (closed 2026-05-09)

- **Deployment gap RESOLVED** — 7 SEO agents `git mv`'d from `/agents/seo-*.md` to `.claude/agents/seo-*.md`. Task tool dispatch now works.
- **Built on existing infrastructure**: `tracking/schemas/baseline.schema.json` (178-line schema) extended into `aimpactscanner-data.schema.json` v1.0 with AI-readiness scorecard, fixes array, prior-findings reference. `tracking/templates/` left untouched (those serve `/track report` Python flow). Created agent-friendly markdown deliverables in `templates/deliverables/`.
- **Three deliverable templates locked**: analysis-report.md, marketing-report.md, aimpactscanner-data.schema.json + README.md (in `templates/deliverables/`).
- **Run directory convention locked**: `runs/YYYY-MM-DD-<domain-slug>-<mission>[-<mode>]/`. Created `runs/.gitkeep` as landing zone.
- **All 4 SEO missions wired** with OUTPUTS section. Per-mission subset documented. Coordinator must verify required files exist on filesystem before marking complete.
- **Sprint 5 estimated M (10-14h), actual 2-3h** — existing infrastructure made the difference.

**Decisions in execution**:
- Schema $ref to `tracking/schemas/baseline.schema.json` is a relative path (not standard URI). Acceptable as documentation; AImpactScanner can interpret. If strict JSON Schema validation matters later, inline the baseline shape into aimpactscanner-data.schema.json.
- Marketing Report is OPTIONAL for content-gap and ai-search-optimize (no meaningful before/after immediately); RECOMMENDED for technical-fix (CWV deltas are naturally case-study material); REQUIRED for site-audit (always has baseline to compare).

### Phase Handoff: Sprint 5 → Sprint 6

**Next sprint**: Sprint 6 — SEO Routine Templates on framework Routines (Mode C). Effort S (3-5h after rescope — framework provides scheduling, we just write the SEO routine prompts).

**Critical context for Sprint 6**:
- Framework v6 introduced Routines (Mode C). Templates exist in `routines/` directory: pr-review.md, nightly-qa.md, backlog-triage.md. Pattern is established — copy and adapt.
- Add two SEO routine templates: `routines/weekly-snapshot.md` (Monday baseline capture for tracked sites) and `routines/monthly-report.md` (first-of-month executive report).
- Each routine should reference the deliverable contract from Sprint 5 — produce `data.json` per the AImpactScanner schema, write to `runs/` directory.
- Each routine should run a token health check first (per original Sprint 6 doc) — fail loudly if GSC/GA4 tokens are stale.
- Set up on `claude.ai/code/routines` for freecalchub.com; observe two cycles before close.
- Cadence-keyword detection in `/coord` already routes "weekly", "monthly" etc. to the Routine pointer (see `.claude/commands/coord.md` Routine Detection section). May need to add SEO-specific phrases ("weekly SEO snapshot", "monthly SEO report") if framework permits.

**Available end-to-end test for Sprints 1-5**: User can now fire `/coord site-audit freecalchub.com` and meaningfully exercise the full pipeline — agents deployed, mission registered, OUTPUTS contract specified, deliverable templates ready to fill, run directory landing zone exists. This was not possible in any prior sprint.

### Sprint 6 — SEO Routine Templates (closed 2026-05-09)

- Discovered `routines/` directory didn't exist — framework promised templates but install didn't create them. Built from scratch using cues in `.claude/commands/coord.md` Routine Detection section.
- 3 deliverables: `routines/README.md` (pattern), `routines/weekly-snapshot.md` (Mondays 07:00), `routines/monthly-report.md` (1st of month 08:00).
- Routines compose with prior sprints: reference SEO missions registered in Sprint 1, use slim agent prompts from Sprint 3, write to `runs/` per Sprint 5 deliverable contract.
- Token health check is STEP 1 of each routine prompt — fails loudly via GitHub issue rather than silently producing bad data.
- "No inflation" guardrail in monthly-report — skip marketing.md if no honest before/after story (Constitution rule 5).
- Sprint 6 estimated S (3-5h), actual ~1h. Framework handles cron; no registry/log file needed.

**Decisions in execution**:
- No SEO-specific cadence keywords added to `/coord` — generic "weekly" / "monthly" already trigger Routine pointer per existing coord.md Routine Detection.
- Routines write outputs as PRs (not direct commits) so a human can review before merge.
- Failure surfacing uses GitHub issues, not local log files — visible to humans, persistent, threadable.
- Backfill protocol uses interactive `/coord` with tag suffix (`-weekly-snapshot-backfill`) for audit clarity.

### Phase Handoff: Sprint 6 → Sprint 7

**Next sprint**: Sprint 7 — AI Search First Lens. Effort S. Last sprint of v2 evolution.

**Critical context for Sprint 7**:
- AI Search Readiness scorecard is **already encoded** in:
  - `templates/deliverables/aimpactscanner-data.schema.json` (`scorecards.ai_search_readiness` required, 5 dimensions: llms_txt, structured_data_coverage, answerability, sitemap_freshness, ai_crawler_policy)
  - `templates/deliverables/analysis-report.md` (AI Search Readiness Scorecard section)
- AI Search lens is **already in every mission** because every mission produces the deliverable contract. The schema requires the AI scorecard; missions inherit this requirement.
- Remaining Sprint 7 work:
  1. Strengthen `ai-search-optimize.md` mission with current blueprint guidance (llms.txt workflow specifics, schema priorities, answerability patterns) — content depth, not structural change
  2. Verify the four SEO missions all explicitly reference the AI scorecard requirement (they should, via the OUTPUTS contract pointing at the schema)
  3. Add a one-line AI lens reminder to seo-strategist agent prompt (since strategist scopes missions)
  4. Update CLAUDE.md if the AI lens needs more emphasis (Constitution rule 3 already covers it — may need nothing)
- Constitution rule 3 ("AI Search First") is already in CLAUDE.md from Sprint 2 — Sprint 7 just enforces it consistently.
- This is genuinely a small sprint. May complete in <1h.

**End-to-end opportunity**: After Sprint 7, every Sprint 1-7 deliverable is in place. User can fire `/coord site-audit freecalchub.com` for the whole-programme acceptance test.

### Sprint 7 — AI Search First Lens (closed 2026-05-09 — v2 EVOLUTION PROGRAMME COMPLETE)

- AI scorecard already encoded in deliverable contract from Sprint 5 — schema validation alone enforces the lens. Sprint 7 was content depth + explicit reminders.
- ai-search-optimize.md strengthened with concrete blueprint content: llms.txt two-file specification, 10-crawler AI policy table, 7-schema priority ranking, 7 answerability patterns. Removed duplicated MISSION DELIVERABLES section.
- Added AI lens reminder to seo-strategist agent (one line) — strategist scopes missions, so the lens propagates at planning time.
- Added tailored "AI Search lens (Constitution rule 3)" line to OUTPUTS section of site-audit, content-gap, technical-fix.
- ai-search-optimize.md grew from ~190 → 223 lines (intentional — deep-dive mission needs depth).
- Sprint 7 estimated S (originally up to M), actual ~30-45min.

### V2 EVOLUTION PROGRAMME — COMPLETE 2026-05-09

All 7 sprints closed in a single day (Sprint 4 cancelled in rescope, work merged into Sprint 1):

| # | Sprint | Outcome |
|---|---|---|
| 1 | Register SEO missions in /coord | Mode D added; ai-search-optimize.md moved into .claude/missions/ |
| 2 | Karpathy SEO Constitution | CLAUDE.md 424 → 50 lines (-88%) with Five Rules |
| 3 | Agent de-bloat | 7 SEO agents -14% lines / -9% words; 3 templates archived; 2 docs archived |
| 4 | Universal mission router | CANCELLED (v6 forbids NLP) |
| 5 | Deliverable-first missions | 3 deliverable templates + JSON Schema v1.0; 4 missions wired; deployment gap fixed |
| 6 | SEO routine templates | weekly-snapshot.md + monthly-report.md created |
| 7 | AI search lens | Lens enforced at strategist + all 4 mission OUTPUTS; ai-search-optimize.md strengthened with concrete content |

**Programme closed**: every blueprint goal addressed. Open user actions are operational (fire freecalchub.com test, set up routines on claude.ai/code/routines) not architectural.

**No further sprints planned** — what comes next is a fresh conversation about post-v2 priorities.

## Known Constraints

- British English in all output
- No em-dashes in output intended for publishing
- Prefer tight, action-oriented content over prose
- User (Jamie) has ADHD; keep each sprint scope tight and anchor to one task at a time
- Sprint gates are mandatory; cannot skip assessment to get to the next feature

## Dependencies Between Sprints

```
Sprint 1 -> Sprint 4
Sprint 2 -> Sprint 3
Sprint 3 -> Sprint 5, Sprint 6
Sprint 4 -> Sprint 5
Sprint 5 -> Sprint 7
```

Sprint 1 and Sprint 2 can run in parallel; they share no files.

## Open Questions

None at this point. Any question surfaced mid-sprint should be logged here with a decision or a note that it is deferred.

## Glossary

- **AImpactScanner** — the dashboard MVP that consumes structured run output
- **llms.txt** — a proposed standard file for telling LLM crawlers what content a site offers and how to use it
- **Twin scorecard** — traditional SEO score and AI ingestion score presented side by side in Sprint 7
- **Run-scoped directory** — a dated directory under `/runs/` that holds all deliverables from a single mission invocation

---

## Migrated from handoff-notes.md (2026-05-07)

# Handoff Notes — SEO-Agent v2 Evolution

**Last Updated**: 2026-04-19
**Current Phase**: Planning complete, Sprint 1 ready to kick off
**Next Agent**: User-invoked specialist for Sprint 1 execution (likely @developer and @strategist)

---

## Mission State

The SEO-Agent v2 evolution plan has been authored. Seven sprints are defined, each independently shippable and assessable on freecalchub.com before starting the next.

## What Was Just Done

- Reviewed the blueprint at `ideation/SEO-Agent v2 Blueprint_ Applying the Agent-11 Lessons.md`
- Archived the v1 project plan to `project-plan.v1-archive.md`
- Authored a new v2 `project-plan.md` as the overarching roadmap
- Created `/sprints/` with seven sprint documents
- Initialised this handoff file and `agent-context.md`

## What Happens Next

The user kicks off Sprint 1 when ready.

**Sprint 1 entry point**:
1. Read `sprints/sprint-01-command-surface.md`
2. Confirm target mission list: site-audit, content-gap, technical-fix, ai-search-optimize
3. Run a grep sweep for references to missions marked for deletion
4. Proceed through the task list

## Decisions in Force

- Seven-sprint structure with user sign-off at each sprint gate
- freecalchub.com is the assessment site for every sprint
- Only SEO missions are in scope (site-audit, content-gap, technical-fix, ai-search-optimize)
- The blueprint is the source of truth; if it and current code disagree, the blueprint wins unless a documented exception is raised

## Open Questions

None at this point.

## Files Created This Session

- `project-plan.md` (new v2)
- `sprints/sprint-01-command-surface.md`
- `sprints/sprint-02-seo-constitution.md`
- `sprints/sprint-03-agent-debloat.md`
- `sprints/sprint-04-universal-router.md`
- `sprints/sprint-05-deliverable-missions.md`
- `sprints/sprint-06-tracking-routines.md`
- `sprints/sprint-07-ai-search-lens.md`
- `handoff-notes.md` (this file)
- `agent-context.md`

## Files Archived This Session

- `project-plan.v1-archive.md` (the previous 100%-complete v1 plan)

## What To Do On Resume

1. Read this file
2. Read `project-plan.md` and note the sprint index
3. Pick the next sprint with status "Not started" and no blocking dependencies
4. Read that sprint's doc in `/sprints/` for the task list
5. Execute one task at a time; mark [x] with a timestamp as each completes
6. When all sprint tasks complete, run the Assessment Protocol on freecalchub.com
7. Close the sprint with Exit Notes in this file
8. Move to the next sprint
