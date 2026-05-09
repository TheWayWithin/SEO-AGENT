# Sprint 3 — Agent De-Bloat & Context Consolidation

**Theme**: De-bloat
**Effort**: M (6 to 10 hours after rescope)
**Dependencies**: Sprint 2 (the new constitution shapes what can safely come out of agents)
**Status**: Not started — adjusted 2026-05-09

> **RESCOPE 2026-05-09** (see `sprints/RESCOPE-2026-05-09.md`)
> Agent count is **7** (was 6 — includes seo-coordinator). All 7 still carry the old MANDATORY CONTEXT PROTOCOL.
> Framework already retired `handoff-notes.md` (folded into `agent-context.md`). Our remaining consolidation: archive `seo-context.md`, `seo-handoff.md`, `mission-state.md` templates and update SEO mission/agent references.
> Coordinator enforcement edits target `agents/seo-coordinator.md` only — `.claude/agents/coordinator.md` is framework, leave alone.

## Sprint Goal

Strip the MANDATORY CONTEXT PROTOCOL from all six SEO specialist agents and consolidate four context files down to two, restoring native Claude Code context handling.

## Motivation

Per blueprint section 1: forcing every agent to read and write four meta-files before and after every task is a massive token tax. Claude Code natively handles context much better now. The overhead is costing speed, money, and accuracy without improving output.

## Scope: In

- Strip the MANDATORY CONTEXT PROTOCOL block from the six SEO specialist agents:
  - seo-strategist
  - seo-technical
  - seo-content
  - seo-researcher
  - seo-analyst
  - seo-builder
- Consolidate the four context templates to two:
  - **Keep**: `project-plan.md` (forward-looking roadmap)
  - **Keep**: `seo-evidence.md` (backward-looking artefacts and findings)
  - **Delete/archive**: `seo-context.md`, `seo-handoff.md`, `mission-state.md` as standalone mandatory files
- Update coordinator enforcement logic so it no longer requires the deleted files
- Retain `handoff-notes.md` and `agent-context.md` as optional, lightweight aids (not mandatory at every agent hand-off)
- Measure token cost and output quality before and after

## Scope: Out

- Routing changes (Sprint 4)
- Mission deliverable format (Sprint 5)

## Task List

- [ ] **Baseline capture**: run `/coord site-audit freecalchub.com/calculators/bmi-calculator` on a single page; record token cost, runtime, and output into `seo-evidence.md` (@tester)
- [ ] Inventory the MANDATORY CONTEXT PROTOCOL block across the six agents; capture line counts per agent (@analyst)
- [ ] Strip the protocol from each agent, replacing with a single line reference to the constitution (@developer)
- [ ] Archive redundant templates (`seo-context-template.md`, `seo-handoff-template.md`, `mission-state-template.md`) to `/templates/archive/` (@developer)
- [ ] Update coordinator logic in `.claude/agents/seo-coordinator.md` (and any referring mission files) to remove references to deleted context files (@developer)
- [ ] Update `.claude/commands/coord.md` to drop the initialise-four-files step (@developer)
- [ ] Update all four SEO mission files (`site-audit`, `content-gap`, `technical-fix`, `ai-search-optimize`) to reference only the two retained context files (@developer)
- [ ] **Re-run**: same single-page audit; record new token cost, runtime, output (@tester)
- [ ] Compare baseline vs post-change; document in `progress.md` (@coordinator)

## Acceptance Criteria

- No agent prompt references MANDATORY CONTEXT PROTOCOL
- `seo-context.md`, `seo-handoff.md`, `mission-state.md` are no longer required at mission start
- Token cost for the reference audit drops by at least 25% (target; record actual either way)
- Output quality on the reference audit is equal or better (human review, evidence-based)
- Coordinator does not fail when the deleted files are absent

## Assessment Protocol (freecalchub.com)

1. Pre-sprint baseline audit captured in evidence
2. Post-sprint audit run on the same URL
3. Compare:
   - Token cost delta (target: 25% or more reduction)
   - Runtime delta
   - Output completeness (does it still produce the prioritised fix list?)
4. If output quality regresses, identify which stripped block caused it and restore selectively
5. Store before/after side-by-side in `seo-evidence.md`

DONE means: six agents are slimmer, two context files replace four, and the freecalchub.com audit runs cheaper without losing quality.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Stripping context protocol loses useful hand-off signal mid-mission | Baseline/post-change comparison on a real audit catches regressions |
| Coordinator references deleted files and crashes | Update coordinator in the same PR as agent strips |
| User workflows depend on `mission-state.md` for visibility | `project-plan.md` provides forward-looking state; `progress.md` the backward. Document the migration in README |
| Agents still try to read deleted files | Add explicit "do not require these files" note in agent prompt headers |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- Token cost before/after numbers
- Runtime before/after numbers
- Output quality judgement with evidence links
- List of files archived and new contract for context
