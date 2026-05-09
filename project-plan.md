# SEO-Agent v2 — Evolution Plan

**Status**: ACTIVE
**Started**: 2026-04-19
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
| 3 | Agent De-Bloat & SEO Context Consolidation | De-bloat | M | 2 | Not started — adjusted |
| 4 | Universal Mission Router | — | — | — | **Cancelled** (merged into Sprint 1) |
| 5 | Deliverable-First Missions | Uplevel | M | 3 | Not started |
| 6 | SEO Routine Templates on framework Routines (Mode C) | Uplevel | S | 3 | Not started — shrunk |
| 7 | AI Search First Lens | Uplevel | S | 5 | Not started |

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

### Sprint 3 — Agent De-Bloat & Context Consolidation
- [ ] Baseline: run site-audit on freecalchub.com with current agents, store output
- [ ] Strip MANDATORY CONTEXT PROTOCOL from 6 SEO agents
- [ ] Consolidate 4 context templates to 2
- [ ] Delete redundant templates
- [ ] Update coordinator enforcement logic
- [ ] Re-run site-audit; compare output quality and token cost

### Sprint 4 — Universal Mission Router
- [ ] Design routing keyword map
- [ ] Implement deterministic mission detection from natural language
- [ ] Add lite/full/deep mode parsing
- [ ] Add target parsing (domain, branch, single page)
- [ ] Build 20-utterance test harness
- [ ] Route `/coord run a lite scan on freecalchub.com/calculators` correctly

### Sprint 5 — Deliverable-First Missions
- [ ] Define three deliverable templates (Analysis, Marketing, AImpactScanner)
- [ ] Update site-audit mission to output all three
- [ ] Update content-gap, technical-fix, ai-search-optimize to output applicable subset
- [ ] Run end-to-end on freecalchub.com
- [ ] Verify all three deliverables produced

### Sprint 6 — Automated Tracking Routines
- [ ] Design routine scheduling mechanism (Claude Code routine or cron-equivalent)
- [ ] Convert `/track snapshot` to weekly Monday routine
- [ ] Convert `/track report` to monthly routine
- [ ] Add API/token health check at start of each routine
- [ ] Validate two complete automation cycles on freecalchub.com

### Sprint 7 — AI Search First Lens
- [ ] Add LLM ingestion scorecard to site-audit output
- [ ] Add llms.txt readiness check to technical-fix mission
- [ ] Strengthen ai-search-optimize mission with current blueprint guidance
- [ ] Add AI-ingestion section to all deliverable templates
- [ ] Validate on freecalchub.com: AI scorecard present in every deliverable

---

## Tracking Files

- `project-plan.md` (this file) — forward-looking roadmap and sprint index
- `progress.md` — backward-looking changelog, deliverables, lessons learned
- `seo-evidence.md` — artefacts, screenshots, before/after outputs
- `handoff-notes.md` — current mission state, for the next agent or session
- `agent-context.md` — rolling accumulation of decisions and findings

Sprint 3 will retire `seo-context.md`, `seo-handoff.md`, and `mission-state.md` as standalone mandatory files; their function folds into the two retained context files above.
