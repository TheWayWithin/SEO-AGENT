# SEO-Agent v2 — Evolution Plan

**Status**: COMPLETE 2026-05-09 (all sprints closed; Sprint 4 cancelled in rescope)
**Started**: 2026-04-19
**Closed**: 2026-05-09
**Source of truth**: `ideation/SEO-Agent v2 Blueprint_ Applying the Agent-11 Lessons.md`
**v1 archive**: `project-plan.v1-archive.md`

---

## Mission

Evolve SEO-Agent from its current v1 architecture (an Agent-11 v5 clone with heavy context preservation overhead) to a v2 architecture that applies the Agent-11 v6 lessons: slim prompts, native Claude Code context handling, deterministic routing, deliverable-focused missions, and automated tracking routines.

The goal is a faster, cheaper, more focused SEO tool that treats AI search (LLM ingestion, llms.txt) as a first-class concern alongside traditional Google SEO.

## Delivery Approach

Seven sprints. One feature per sprint. Assess on freecalchub.com before moving to the next.

## Sprint Index

Rescoped 2026-05-09 after Agent-11 v5 → v6.1.1 framework upgrade. See `sprints/RESCOPE-2026-05-09.md` for the layer model and per-sprint deltas. Six sprints, not seven.

| # | Sprint | Theme | Effort | Dependencies | Status |
|---|--------|-------|--------|--------------|--------|
| 2 | Karpathy SEO Constitution (project-root `CLAUDE.md`) | De-bloat | S | none | **COMPLETE 2026-05-09** (424 → 50 lines) |
| 1 | Register SEO missions in `/coord`; normalise mission paths | De-bloat | S | none | **COMPLETE 2026-05-09** (Mode D added; ai-search-optimize moved) |
| 3 | Agent De-Bloat & SEO Context Consolidation | De-bloat | M | 2 | **COMPLETE 2026-05-09** (-214 lines / -8.7% words across 7 agents; 3 templates + 2 docs archived) |
| 4 | Universal Mission Router | — | — | — | **Cancelled** (merged into Sprint 1) |
| 5 | Deliverable-First Missions | Uplevel | M | 3 | **COMPLETE 2026-05-09** (3 deliverable templates + JSON Schema; 4 missions wired; deployment gap fixed) |
| 6 | SEO Routine Templates on framework Routines (Mode C) | Uplevel | S | 3 | **COMPLETE 2026-05-09** (2 routine templates: weekly-snapshot, monthly-report) |
| 7 | AI Search First Lens | Uplevel | S | 5 | **COMPLETE 2026-05-09** (ai-search-optimize strengthened with concrete blueprint guidance; AI lens reminder in seo-strategist; AI scorecard explicit in all 4 mission OUTPUTS) |
| 8 | Installer + Fleet Bulk Operator | Ops | M | 5 | **COMPLETE 2026-05-10** (install.sh, install-fleet.sh, seo-fleet-registry.yaml with 14 active SEO targets across P1-P4) |
| 9 | Plan + Compare (close-the-loop discipline) | Ops | M | 5,8 | **COMPLETE 2026-05-11** (seo-roadmap + seo-backlog templates with lifecycle states; comparison-report template; /track baseline + /track compare design honest about Python legacy; validated on freecalchub data) |
| 10 | Sitewide-verify mission + Python /track retirement | Ops | S | 9 | **COMPLETE 2026-05-11** (sitewide-verify Mode D mission file; technical-fix wired to point at it; coord.md SEO Mode D restored + 5th mission added; install.sh updated; tracking/legacy/ archive of 11 Python files with revival README) |

Sprint detail lives in `/sprints/sprint-0N-name.md`. Each affected file carries a `RESCOPE 2026-05-09` callout at the top.

## Layer Model (added 2026-05-09)

This repo holds two layers:

- **Agent-11 (framework)** — generic dev squad we use to build SEO-Agent. Lives in `.claude/` plus `/missions/mission-*.md`, `/templates/` (non-seo), `/field-manual/`, `/gates/`, `/schemas/`. Refresh via `bash install.sh --upgrade`.
- **SEO-Agent (product)** — the SEO suite we deploy elsewhere. Lives in `/agents/seo-*.md`, `.claude/missions/{site-audit,content-gap,technical-fix}.md`, `/missions/ai-search-optimize.md` (to be moved), `/templates/seo-*-template.md`, `.claude/commands/{seo-commands,track,tracking-commands}.md`.

All sprint work targets the product layer. The framework layer is a dependency.

## Success Criteria (whole programme)

- Agent prompts reduced in size by 40% or more without loss of capability
- Only SEO-relevant missions remain in `/missions/`
- Context files reduced from 4 to 2 (project-plan.md + seo-evidence.md)
- `/coord run a lite scan on freecalchub.com/calculators` routes correctly without a mission name
- Every site-audit run produces three named deliverables: Analysis Report, Marketing Report, AImpactScanner dashboard data
- `/track snapshot` runs automatically each week, `/track report` each month
- Every mission evaluates LLM ingestion readiness (llms.txt, schema, answerability) alongside traditional SEO

## Sprint Gate Protocol

Before closing any sprint and starting the next:

1. All sprint tasks marked [x] in the sprint doc and in this plan
2. Acceptance criteria for the sprint met and documented in `progress.md`
3. **Gate evidence appropriate to sprint type** (see matrix below); stored in `seo-evidence.md`
4. User sign-off recorded in `agent-context.md` Phase Handoff block
5. Any lessons learned captured in `progress.md`

If any check fails: stop, remediate, re-run. Do not start the next sprint.

### Conditional gate matrix (set 2026-05-09)

| Sprint | Gate type | Closing evidence |
|---|---|---|
| 1 — Register SEO missions | Smoke | `/coord site-audit` dispatches without "Unknown mission"; `/coord` help lists the four SEO missions |
| 2 — Slim project-root CLAUDE.md | Smoke | Line count <80; diff reviewed; one `/coord site-audit` dispatch test |
| 3 — Agent de-bloat | Full freecalchub run | Token cost + output quality before/after on the same audit URL |
| 5 — Deliverable-first missions | Full freecalchub run | Three named deliverables present after a fresh audit |
| 6 — SEO routine templates | Full freecalchub run | Two consecutive scheduled snapshot cycles complete |
| 7 — AI search lens | Full freecalchub run | LLM ingestion scorecard present in every deliverable |

Sprints with **Smoke** gates close on diff + dispatch test (minutes). Sprints with **Full** gates require an actual SEO-Agent run on freecalchub.com (hour+).

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| Stripping context protocol breaks mid-flight missions | Medium | Sprint 3 runs a site-audit before and after; compare output quality |
| Deleting generic missions breaks latent references in docs | Low | Sprint 1 runs a grep sweep for mission names |
| Router misrouts natural-language commands | Medium | Sprint 4 includes a test harness with 20 example utterances |
| Automated routines run on stale auth/API tokens | Medium | Sprint 6 includes token health check as first step of every routine |
| AI search lens drifts from traditional SEO | Low | Sprint 7 keeps both scorecards side-by-side in every report |

## Per-Sprint Tasks (Index)

Detail in `/sprints/`. This index tracks completion across sprints.

### Sprint 1 — Register SEO Missions in /coord — COMPLETE 2026-05-09
- [x] Move `ai-search-optimize.md` into `.claude/missions/` (all four SEO missions co-located)
- [x] Add Mode D — SEO to coord.md routing table with marker comments for upgrade resilience
- [x] Extend coord.md dispatch logic to load Mode D missions from `.claude/missions/[name].md`
- [x] Update Unknown Mission help and Examples sections
- [→] Live `/coord site-audit freecalchub.com` dispatch — for user to fire when ready (Sprint 2 deferred check; smoke evidence by inspection: parse logic now accepts site-audit and loads from .claude/missions/)

### Sprint 2 — Karpathy SEO Constitution — COMPLETE 2026-05-09
- [x] Draft new <80-line CLAUDE.md (50 lines)
- [x] Encode 5 behavioural rules
- [x] Review against blueprint
- [x] Replace existing CLAUDE.md (archived to `CLAUDE.v1-archive.md`)
- [→] Test constitution holds during a site-audit run — deferred to Sprint 1 verification (blocked: SEO missions not registered in `/coord` yet)

### Sprint 3 — Agent De-Bloat & Context Consolidation — COMPLETE 2026-05-09
- [x] Static baseline captured (Option B hybrid gate — agreed in lieu of full audit)
- [x] Strip MANDATORY CONTEXT PROTOCOL from 7 SEO agents (was 6 — count corrected)
- [x] Archive 3 SEO context templates (seo-context, seo-handoff, mission-state) → templates/archive/
- [x] Update seo-coordinator Mission Planning + Execution frameworks (no longer references retired files)
- [x] Strip CONTEXT INITIALIZATION blocks from ai-search-optimize.md (other 3 SEO missions already clean)
- [x] Update README.md and .claude/commands/track.md to reference only seo-evidence.md
- [x] Archive 2 obsolete context-preservation docs to docs/archive/
- [→] Live freecalchub re-run deferred — see Sprint 3 doc for caveat about /agents/ vs .claude/agents/ deployment

### Sprint 4 — Universal Mission Router
- [ ] Design routing keyword map
- [ ] Implement deterministic mission detection from natural language
- [ ] Add lite/full/deep mode parsing
- [ ] Add target parsing (domain, branch, single page)
- [ ] Build 20-utterance test harness
- [ ] Route `/coord run a lite scan on freecalchub.com/calculators` correctly

### Sprint 5 — Deliverable-First Missions — COMPLETE 2026-05-09
- [x] Three deliverable templates created in `templates/deliverables/` (analysis-report.md, marketing-report.md, aimpactscanner-data.schema.json) + README.md
- [x] Run-scoped directory convention agreed: `runs/YYYY-MM-DD-<domain-slug>-<mission>[-<mode>]/`
- [x] `site-audit` mission updated to require all three deliverables
- [x] `content-gap`, `technical-fix`, `ai-search-optimize` updated with OUTPUTS sections (applicable subset)
- [x] Deployment gap fix bundled: 7 SEO agents moved from `/agents/` to `.claude/agents/` for Task tool dispatch
- [x] CLAUDE.md and README.md updated with deliverables contract
- [→] End-to-end freecalchub.com run — for user to fire when ready (now actually possible end-to-end)

### Sprint 6 — SEO Routine Templates — COMPLETE 2026-05-09
- [x] Scheduling mechanism: framework Routines (Mode C) — no local cron needed
- [x] Created `routines/weekly-snapshot.md` (Mondays 07:00, produces data.json snapshot)
- [x] Created `routines/monthly-report.md` (1st of month, aggregates weekly snapshots into full deliverable set)
- [x] Token health check is STEP 1 of each routine prompt; fails loudly via GitHub issue
- [x] CLAUDE.md updated with SEO routines section
- [→] Manual setup on `claude.ai/code/routines` + observe 2 cycles — for user to do when ready

### Sprint 7 — AI Search First Lens — COMPLETE 2026-05-09
- [x] AI scorecard already encoded in `aimpactscanner-data.schema.json` (Sprint 5) — schema validation enforces presence
- [x] AI scorecard section already in `templates/deliverables/analysis-report.md` (Sprint 5)
- [x] Strengthened `ai-search-optimize.md`: added llms.txt spec (two-file pattern, format requirements), AI crawler policy table (10 crawlers with operator + recommended policy), structured data priorities for AI (7 schema types ranked), answerability patterns (7 concrete patterns LLMs reward)
- [x] Removed duplicated MISSION DELIVERABLES section from ai-search-optimize.md (now redundant with OUTPUTS contract)
- [x] Added AI lens reminder to `seo-strategist.md` agent ("Every mission you scope must include AI Search Readiness alongside traditional SEO")
- [x] Added explicit "AI Search lens (Constitution rule 3)" line to OUTPUTS section of site-audit, content-gap, technical-fix missions (each tailored to mission focus)

---

## Tracking Files

- `project-plan.md` (this file) — forward-looking roadmap and sprint index
- `progress.md` — backward-looking changelog, deliverables, lessons learned
- `seo-evidence.md` — artefacts, screenshots, before/after outputs
- `handoff-notes.md` — current mission state, for the next agent or session
- `agent-context.md` — rolling accumulation of decisions and findings

Sprint 3 will retire `seo-context.md`, `seo-handoff.md`, and `mission-state.md` as standalone mandatory files; their function folds into the two retained context files above.
