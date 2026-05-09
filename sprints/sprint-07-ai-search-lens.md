# Sprint 7 — AI Search First Lens

**Theme**: Uplevel
**Effort**: S to M (6 to 10 hours)
**Dependencies**: Sprint 5 (deliverable templates are in place and can absorb an AI scorecard)
**Status**: Not started

## Sprint Goal

Make LLM ingestion readiness a first-class dimension in every mission output, not a side note reserved for the `ai-search-optimize` mission.

## Motivation

Per blueprint section 4, rule 3: AI Search First is a core behavioural rule. A site that ranks on Google but is invisible to LLM-driven search is losing ground. Every fix, every gap, every technical change should be evaluated on both axes: traditional SEO and AI ingestion.

## Scope: In

- Add an AI ingestion scorecard section to the Analysis Report and AImpactScanner Data templates from Sprint 5
- The scorecard evaluates at least:
  - `llms.txt` present and well-formed
  - Schema markup completeness (Organization, FAQ, HowTo, Product where relevant)
  - Answerability: are the key questions on the page addressed in a single extractable block
  - Citation-worthiness: is the content distinctive enough for an LLM to cite
  - Crawl surface for LLM user agents
- Add llms.txt readiness check to the `technical-fix` mission
- Strengthen the `ai-search-optimize` mission with current blueprint guidance (llms.txt workflow, schema priorities, answerability patterns)
- Update the site-audit output to show both scorecards side by side: traditional SEO and AI ingestion
- Validate on freecalchub.com: the audit must produce an AI ingestion scorecard for every page scanned

## Scope: Out

- New missions (scope holds at the four SEO missions from Sprint 1)
- Scheduling changes (Sprint 6)
- Template format changes beyond the scorecard addition (Sprint 5 locked those)

## Task List

- [ ] Research the current best practice for llms.txt, schema, and answerability (@researcher or @analyst)
- [ ] Define the AI ingestion scorecard schema (@architect)
- [ ] Update Analysis Report template to include AI scorecard (@developer)
- [ ] Update AImpactScanner Data template to include AI scorecard fields (@developer)
- [ ] Add llms.txt readiness check to `technical-fix` mission (@developer)
- [ ] Update `ai-search-optimize` mission prompt with current guidance (@developer)
- [ ] Update `site-audit` mission to show both traditional and AI scorecards (@developer)
- [ ] Run `/coord site-audit freecalchub.com` end to end; verify AI scorecard present (@tester)
- [ ] Document the AI scorecard contract in README (@documenter)

## Acceptance Criteria

- Every deliverable produced by any mission includes an AI ingestion scorecard section (or explicitly declares it not applicable with reasoning)
- `llms.txt` readiness is visible in `technical-fix` output
- `site-audit` output shows traditional SEO and AI ingestion scores side by side
- The `ai-search-optimize` mission reflects current blueprint guidance and is usable as a standalone campaign

## Assessment Protocol (freecalchub.com)

1. Run `/coord site-audit freecalchub.com` end to end
2. Confirm the Analysis Report contains an AI ingestion scorecard with every listed field scored
3. Confirm the AImpactScanner Data file contains the same scores in structured form
4. Run `/coord technical-fix freecalchub.com` and confirm llms.txt readiness is flagged
5. Run `/coord ai-search-optimize freecalchub.com` and confirm output reflects current guidance (llms.txt, schema, answerability)
6. Store each output in `seo-evidence.md`

DONE means: a freecalchub.com audit produces twin scorecards (traditional SEO and AI ingestion) in every deliverable, and the llms.txt readiness signal is visible in the technical-fix output.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| AI scorecard drifts from what LLM providers actually reward | Keep the scorecard schema versioned; plan a quarterly review |
| Scorecard adds noise on pages where AI ingestion is irrelevant (for example, login pages) | Allow "N/A with reason" as a valid score state |
| Agents treat the scorecard as optional | Mission files require the scorecard; coordinator verifies presence after run |
| Current llms.txt best practice changes during the sprint | Lock guidance at sprint start; plan a follow-up review in the first post-launch sprint |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- The locked AI scorecard schema version
- Example outputs from freecalchub.com with twin scorecards
- Any fields that needed manual judgement rather than automated scoring
- A note on when the AI scorecard guidance should next be reviewed
