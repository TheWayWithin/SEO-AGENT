# Sprint 2 — Karpathy SEO Constitution

**Theme**: De-bloat
**Effort**: S (3 to 5 hours)
**Dependencies**: None (can run in parallel with Sprint 1)
**Status**: COMPLETE 2026-05-09

> **RESCOPE 2026-05-09** (see `sprints/RESCOPE-2026-05-09.md`)
> Target file is project-root `CLAUDE.md` only (currently 424 lines, still v5-era prose).
> Do **not** touch `.claude/CLAUDE.md` — that is the framework constitution, already rewritten by v6.1.1 to 78 Karpathy-style lines.
> Five SEO behavioural rules from blueprint go into project-root `CLAUDE.md`.

## Sprint Goal

Replace the current sprawling `CLAUDE.md` with a slim, under-80-line constitution that encodes the five behavioural rules for an SEO tool.

## Motivation

Per blueprint section 4: the current CLAUDE.md carries all the boilerplate of Agent-11 v5 plus BOS-AI context preservation overhead. Most of it is prose Claude never uses. A tight constitution with clear rules beats a long one that nobody reads.

## Scope: In

- Draft a new root `CLAUDE.md` of <80 lines
- Encode the five rules from the blueprint:
  1. **Read before scanning** — check `seo-evidence.md` and Google Search Console data before crawling
  2. **Prioritise ROI** — do not recommend a hard technical fix if a simple content update yields more traffic
  3. **AI Search First** — evaluate how changes impact LLM ingestion (llms.txt readiness) alongside traditional Google bots
  4. **Minimal Diffs** — when fixing SEO issues in code, change only the necessary tags or schema; do not refactor surrounding components
  5. **Prove it** — always run `/track baseline` before changes and `/track compare` after
- Archive the current CLAUDE.md as `CLAUDE.v1-archive.md`
- Keep the `.claude/CLAUDE.md` (project-level) intact for now; it may be revisited in Sprint 3

## Scope: Out

- Agent prompt changes (Sprint 3)
- Mission file content changes (Sprint 5)
- Tracking automation (Sprint 6)

## Task List

- [x] Read the current root `CLAUDE.md` and list what must be retained for safety versus what is boilerplate (2026-05-09)
- [x] Draft the new CLAUDE.md under 80 lines, encoding the five rules plus essential safety text (2026-05-09)
- [x] Review the draft against the blueprint — five rules verified by grep (2026-05-09)
- [x] Archive current `CLAUDE.md` to `CLAUDE.v1-archive.md` (2026-05-09, 424 lines, 17.2KB)
- [x] Replace root `CLAUDE.md` with the new version (2026-05-09, 50 lines, 3.1KB)
- [→] Run `/coord site-audit freecalchub.com` — DEFERRED to Sprint 1 verification (Sprint 1 registers SEO missions in `/coord`; CLAUDE.md change does not affect dispatch logic)
- [x] Capture line count and word count before/after in `progress.md` (2026-05-09)

## Acceptance Criteria

- New root `CLAUDE.md` is fewer than 80 lines
- All five rules are present and named
- Old file archived at `CLAUDE.v1-archive.md`
- Site-audit on freecalchub.com produces output consistent with the new rules (for example, a proposed technical fix must be weighed against a content alternative)

## Assessment Protocol (freecalchub.com)

1. Before replacement: run `/coord site-audit freecalchub.com` on a single page; capture the output
2. Replace CLAUDE.md
3. Run the same audit again
4. Compare: the v2 output should explicitly weigh ROI, reference AI search readiness, and avoid over-refactoring suggestions
5. Record before/after in `seo-evidence.md`

DONE means: CLAUDE.md is under 80 lines, and a site-audit run visibly reflects the five rules.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Useful safety text accidentally stripped | Review task explicitly lists what stays |
| Agents revert to old behaviour because agent prompts still carry their own rules | Sprint 3 follows; this sprint is just the constitution layer |
| Line-count target forces omission of essential content | If hard floor is hit, accept up to 100 lines and document rationale |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- The final line count and token count of the new CLAUDE.md
- Any safety text retained from the old version with rationale
- Confirmation that the freecalchub.com audit visibly reflects the new rules
