# Sprint 5 — Deliverable-First Missions

**Theme**: Uplevel
**Effort**: M (10 to 14 hours)
**Dependencies**: Sprint 3 (agents are slim), Sprint 4 (router dispatches cleanly)
**Status**: Not started

## Sprint Goal

Make every SEO mission produce three named deliverables instead of free-form prose, so outputs are directly usable for implementation, marketing, and the AImpactScanner dashboard.

## Motivation

Per blueprint section 3: the most valuable code in the repo is the tracking system, but mission output is still prose. Users want three concrete artefacts every time: a prioritised fix list with ROI, marketing-ready before/after examples, and data the AImpactScanner MVP can ingest. Shift from "agent writes a report" to "mission produces three deliverables".

## Scope: In

- Three deliverable templates in `/templates/deliverables/`:
  1. **Analysis Report** — prioritised fix list (easy/high-impact first), ROI estimate per fix, estimated effort, expected traffic lift
  2. **Marketing Report** — before/after examples suitable for case studies, screenshots, narrative framing
  3. **AImpactScanner Data** — structured JSON or YAML matching the dashboard ingestion schema
- Update `site-audit` mission to output all three
- Update `content-gap`, `technical-fix`, `ai-search-optimize` to output the applicable subset (at minimum Analysis Report plus AImpactScanner Data; Marketing Report where before/after makes sense)
- Validate on freecalchub.com: end-to-end run produces all three deliverables for site-audit
- Store each deliverable as a discrete file in a run-scoped directory (for example `/runs/2026-04-19-freecalchub-site-audit/`)

## Scope: Out

- Routing (Sprint 4)
- Automation (Sprint 6)
- AI search lens integration (Sprint 7)

## Task List

- [ ] Inspect existing tracking system output to understand AImpactScanner data schema (@analyst)
- [ ] Draft Analysis Report template (@strategist)
- [ ] Draft Marketing Report template (@marketer)
- [ ] Draft AImpactScanner Data schema and example (@architect)
- [ ] Decide run-scoped output directory convention (@architect)
- [ ] Update `site-audit` mission to produce all three deliverables (@developer)
- [ ] Update `content-gap` mission to produce Analysis Report + AImpactScanner Data (@developer)
- [ ] Update `technical-fix` mission to produce Analysis Report + AImpactScanner Data, and Marketing Report when a before/after is captured (@developer)
- [ ] Update `ai-search-optimize` mission to produce Analysis Report + AImpactScanner Data with explicit AI readiness scoring (@developer)
- [ ] End-to-end run on freecalchub.com; confirm three files produced (@tester)
- [ ] Validate AImpactScanner Data parses correctly against the dashboard schema (@developer)
- [ ] Document the deliverable contract in README (@documenter)

## Acceptance Criteria

- `/coord site-audit freecalchub.com` produces exactly three files in a run-scoped directory
- Analysis Report includes prioritised fix list with ROI and effort estimates
- Marketing Report includes at least one before/after example with visual or narrative evidence
- AImpactScanner Data validates against the dashboard schema
- Other missions produce their applicable deliverable subset
- Deliverable templates are versioned in `/templates/deliverables/`

## Assessment Protocol (freecalchub.com)

1. Run `/coord site-audit freecalchub.com` end to end
2. Confirm three deliverable files produced in a dated run directory
3. Manually inspect each:
   - Analysis: are fixes sorted easy/high-impact first? Is ROI quantified?
   - Marketing: is there a usable before/after? Is the framing case-study-ready?
   - AImpactScanner Data: does it parse against the dashboard schema?
4. Run the same on a single page: `/coord site-audit freecalchub.com/calculators/bmi-calculator`
5. Store all deliverables in `seo-evidence.md` for future reference

DONE means: a single site-audit run on freecalchub.com yields three production-quality deliverables in a predictable location.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Templates over-prescribe and strip nuance from agent output | Templates define required sections, not word-for-word structure |
| AImpactScanner schema drifts from what the dashboard expects | Lock schema in this sprint; any schema change goes through a migration note in progress.md |
| Agents produce prose instead of structured output | Mission file explicitly requires the three files; coordinator verifies filesystem after run |
| Marketing Report forced on missions where before/after makes no sense | Mark it optional for content-gap and ai-search-optimize |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- Paths to the three example deliverables produced for freecalchub.com
- The locked AImpactScanner data schema version
- Any agent or mission that needed extra coaching to produce structured output
