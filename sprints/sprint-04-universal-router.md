# Sprint 4 — Universal Mission Router

**Theme**: Uplevel
**Effort**: —
**Dependencies**: —
**Status**: CANCELLED 2026-05-09 (merged into Sprint 1)

> **RESCOPE 2026-05-09** (see `sprints/RESCOPE-2026-05-09.md`)
> v6 `/coord` is deterministic and **explicitly forbids NLP** ("No NLP inference" — `.claude/commands/coord.md`).
> Original NLP-routing goal diverges from the framework — risky to maintain across upgrades.
> Decision: honour the framework. Sprint 4 work reduces to "register SEO missions in routing table" — moved into revised Sprint 1.
> Users dispatch via positional args: `/coord site-audit lite freecalchub.com/calculators`.
> If natural-language is later required, build it as a standalone `/seo "<utterance>"` command that parses then calls `/coord` — this keeps the framework untouched. Capture as a future sprint if needed.

## Sprint Goal

Enable natural-language dispatch so the user can type `/coord run a lite scan on freecalchub.com/calculators` and have it automatically resolve to the `site-audit` mission in lite mode with the correct target.

## Motivation

Per blueprint section 2: Agent-11 v6 uses deterministic routing based on the mission name. A universal `/coord` command that reads intent and dispatches correctly reduces friction and locks in the mission roster from Sprint 1.

## Scope: In

- Deterministic keyword map for mission detection (for example: "audit" or "scan" maps to `site-audit`; "gap" or "missing content" maps to `content-gap`; "crawl errors" or "speed" or "schema" maps to `technical-fix`; "llm" or "ai search" or "llms.txt" maps to `ai-search-optimize`)
- Mode parsing: `lite`, `full`, `deep`
- Target parsing:
  - Whole domain (`freecalchub.com`)
  - Branch or path (`freecalchub.com/calculators`)
  - Single page (`freecalchub.com/calculators/bmi-calculator`)
- Update `/coord` command to accept free-form input
- Test harness with at least 20 realistic utterances
- Backwards compatible: explicit `/coord site-audit freecalchub.com` still works

## Scope: Out

- Deliverable format (Sprint 5)
- Automated scheduling (Sprint 6)

## Task List

- [ ] Draft the routing keyword map (@strategist)
- [ ] Draft the mode and target parsing rules (@architect)
- [ ] Write 20 example utterances covering each mission, each mode, and each target type (@strategist)
- [ ] Implement routing in `.claude/commands/coord.md` (@developer)
- [ ] Implement target parser (domain, branch, single page) (@developer)
- [ ] Implement mode parser (lite, full, deep) (@developer)
- [ ] Wire the parsed output to existing mission invocation (@developer)
- [ ] Run the 20-utterance test harness; record hits and misses (@tester)
- [ ] Iterate on keyword map until all 20 route correctly (@developer)
- [ ] Document the router contract in README (@documenter)

## Acceptance Criteria

- `/coord run a lite scan on freecalchub.com/calculators` routes to `site-audit` with `mode=lite` and `target=freecalchub.com/calculators`
- `/coord check llm readiness for freecalchub.com` routes to `ai-search-optimize` for the whole domain
- `/coord find content gaps on freecalchub.com/calculators/bmi-calculator` routes to `content-gap` for a single page
- All 20 test utterances route correctly
- Explicit mission names still work: `/coord site-audit freecalchub.com` unchanged
- If ambiguity cannot be resolved, router asks one clarifying question rather than guessing

## Assessment Protocol (freecalchub.com)

1. Run each of the 20 test utterances; capture router output (chosen mission, mode, target) into `seo-evidence.md`
2. For three representative utterances, run end-to-end and confirm the intended mission fires
3. Include at least one deliberately ambiguous utterance to verify the router asks a clarifying question

DONE means: natural-language `/coord` dispatches correctly for 20 test cases on freecalchub.com, and an explicit-mode invocation still works.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Keyword map over-matches and routes wrong mission | Test harness forces 20 diverse utterances through before shipping |
| Target parser fails on URL variations (trailing slash, www, https) | Normalise URL parsing in a single utility with tests |
| Mode parser misreads "full" in "full-stack" as mode=full | Scope mode keywords to immediately after a verb ("scan", "audit", "run") |
| Users bypass router because it feels unreliable | Keep explicit-mode invocation working; router is additive, not a replacement |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- Final keyword map
- The 20 test utterances and their resolved routes
- Any utterance that required a fallback clarifying question
- Confirmation that `/coord site-audit freecalchub.com` still dispatches as before
