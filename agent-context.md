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

None yet (planning sprint just closed).

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
