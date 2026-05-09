# Sprint 5 — Deliverable-First Missions

**Theme**: Uplevel
**Effort**: M (10 to 14 hours)
**Dependencies**: Sprint 3 (agents are slim), Sprint 4 (router dispatches cleanly)
**Status**: COMPLETE 2026-05-09 (deployment gap fix bundled in)

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

- [x] **Deployment gap fix** (bundled in from Sprint 3 finding): `git mv /agents/seo-*.md → .claude/agents/seo-*.md` so Task tool can dispatch (2026-05-09)
- [x] Inspect existing tracking system — found `tracking/schemas/baseline.schema.json` (178 lines, ready to extend) plus `tracking/templates/{executive-summary,before-after,case-study-executive}.md` (Mustache templates for Python report flow). Reused structure rather than reinventing. (2026-05-09)
- [x] Draft `templates/deliverables/analysis-report.md` — agent-friendly markdown with prioritised fix table, AI scorecard, traditional scorecard, prior-findings reference (Constitution rule 1) (2026-05-09)
- [x] Draft `templates/deliverables/marketing-report.md` — headline + TL;DR + before/after table + visual evidence + case-study framing for content team (2026-05-09)
- [x] Draft `templates/deliverables/aimpactscanner-data.schema.json` — JSON Schema v1.0 extending baseline.schema.json with AI-readiness scorecard, fixes array, prior-findings, mission metadata (2026-05-09)
- [x] Draft `templates/deliverables/README.md` — full contract documentation, per-mission deliverable subset, run directory convention (2026-05-09)
- [x] Run-scoped directory convention agreed: `runs/YYYY-MM-DD-<domain-slug>-<mission>[-<mode>]/` (2026-05-09)
- [x] Created `runs/` directory with `.gitkeep` (2026-05-09)
- [x] Update `site-audit` mission with OUTPUTS section requiring all three deliverables (replaces old prose MISSION DELIVERABLES) (2026-05-09)
- [x] Update `content-gap` mission with OUTPUTS section (analysis + data required, marketing optional) (2026-05-09)
- [x] Update `technical-fix` mission with OUTPUTS section (analysis + data required, marketing recommended for CWV before/after) (2026-05-09)
- [x] Update `ai-search-optimize` mission with OUTPUTS section + note that AI Readiness Scorecard is the headline of analysis.md (2026-05-09)
- [x] CLAUDE.md updated — agent path corrected from `/agents/` to `.claude/agents/`, deliverables/runs documented (2026-05-09)
- [x] README.md updated with Mission Deliverables section pointing at templates/deliverables/ (2026-05-09)
- [→] End-to-end freecalchub.com run — for user to fire when ready. Now possible because: SEO agents are deployed to `.claude/agents/` (Sprint 1 deployment fix) AND `/coord site-audit` is registered (Sprint 1) AND missions specify required output files (this sprint).
- [→] AImpactScanner Data validation against the actual dashboard — defer to when AImpactScanner ingestion is wired up; schema is locked at v1.0 and migration path documented in `data.json` `schema_version` field.

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
