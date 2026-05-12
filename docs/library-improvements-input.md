# SEO-Agent Library Improvements — Input for Future Scoping Session

**Source**: Jamie's learnings from running SEO-Agent on freecalchub.com (2026-05-09 → 2026-05-11).
**Status**: INPUT only — not a project plan. Pick 1-2 items in the next scoping session; ignore the rest until they become relevant.
**Captured**: 2026-05-11

---

## Top 5 priority gaps (Jamie's ranking)

> Full doc reportedly has theme-grouped list, lessons, suggested artefacts, and "what's working" sections. Get the full text from Jamie before the next scoping session.

1. **`/track` command is vapourware** — documented as "Complete and Tested", reality is just a config file. **Biggest credibility risk.** Either implement the minimum viable version or rewrite the doc to match reality.
2. **No roadmap template** — Jamie identified this on freecalchub. Promote the freecalchub-drafted `seo-roadmap.md` into the library as a deliverable template.
3. **No standard backlog file** — same pattern. Promote freecalchub's `seo-backlog.md` to a template in the library.
4. **Missions don't define "done" as "live and verified"** — dev-centric vs live-centric framing caused real friction on freecalchub. Structural fix needed in mission contracts.
5. **No post-deploy sitewide verification** — the freecalchub Twitter-tag gap (2 pages missed) was caught by luck, not by mission contract. Add a "sitewide verify" phase to `technical-fix`.

## Key lessons (encode in the library, not just bullets)

- **Local commit ≠ shipped.** Default "done" must mean LIVE on the deployed site.
- **Sitewide verification catches what spot-checks miss.** Sample-N-pages is a starting point, not a finish line.

## Suggested new library artefacts (10 items, priority-ordered per Jamie)

To capture from his full doc:
- Roadmap template
- Backlog template
- Snapshot schema
- Comparison schema
- Sitewide-verify script
- Fetch-lighthouse script
- Scoring rubrics doc
- Lessons doc
- "Deploy & Verify" mission phase
- (10th item — recover from full doc)

## Jamie's recommendation for the next session

> "Pick 1-2 from the Top 5 (probably #1 and #2 together would cover the majority of friction observed) and ignore the rest until they become relevant. Don't try to fix all of this in one pass."

**Most likely Sprint 9 scope**: #1 (`/track` honesty pass) + #2 (roadmap template promotion).

## How to use this file

- Read at the start of the next SEO-Agent library scoping session
- Get the full doc from Jamie (theme-grouped list, what's working section, all 10 artefacts)
- Decide Sprint 9 scope by picking 1-2 of the Top 5
- Move the picked items into `sprints/sprint-08-...md` or similar; leave the rest here as the running backlog
- Do not try to address everything in one sprint

## NOT this session's job

The current session (2026-05-11) is focused on rolling out SEO-Agent to aisearcharena and the rest of the P1-P3 fleet. This document is parked input for whenever Jamie returns to library development.
