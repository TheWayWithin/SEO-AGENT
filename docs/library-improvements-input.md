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

---

# Sprint 11 candidates — captured 2026-05-16

Surfaced by running `/coord sitewide-verify freecalchub.com` in anger after Sprint 10 close. Three distinct frictions hit in a single mission attempt; mission completed as **deferred** (not failed) per Constitution rule 5. Full record in `~/SEO-Agents/freecalchub/runs/2026-05-16-freecalchub-com-sitewide-verify/verification.md`.

## Finding 11-A — Nested subagent Bash refusal

**Symptom**: When `/coord sitewide-verify freecalchub.com` dispatched via Task tool to the coordinator agent, the coordinator (correctly) refused to fabricate verification data because nested subagents can't run Bash. The coordinator agent itself behaved exactly right per Constitution rule 5 — no fabrication, honest no-op, scaffolded the verification.md, surfaced the gap.

**Architectural truth**: Task-tool-delegated subagents only have Read/Edit/Write/Grep/Glob. Bash, WebFetch, and most MCP tools are top-level-session only. Any mission that REQUIRES Bash (or any non-subagent tool) must run top-level, not via coordinator delegation.

**Fix candidates**:
1. Add explicit frontmatter / instructions to mission files declaring "this mission runs top-level; coordinator can scaffold but cannot execute Bash phases"
2. Build a dispatch convention: missions list their tool requirements; coord auto-routes Bash-needing missions to top-level execution rather than coordinator delegation
3. Document the pattern in `field-manual/` so future mission authors know

Recommendation: option 1 (lowest effort, highest leverage). Each mission that needs Bash adds a one-liner.

## Finding 11-B — AskUserQuestion approval doesn't propagate

**Symptom**: User answered AskUserQuestion with "Allow curl, 8 parallel" — explicit in-conversation approval. Subsequent `curl` Bash calls were STILL hard-denied by the harness sandbox layer. The in-conversation approval is meaningful at the agent reasoning layer but doesn't grant the harness any new permission.

**Architectural truth**: AskUserQuestion = "what should I do?" approval. `.claude/settings.json` permissions = "what am I allowed to do?" governance. The two layers don't talk to each other. Approvals on the first don't add capability on the second.

**Fix candidates**:
1. Treat as documentation problem: tell users explicitly that allowlist setup is the only path to unattended automation; AskUserQuestion is only for in-mission strategy decisions
2. Make missions that need outbound HTTP fail FAST with a clear error pointing at the allowlist setup, rather than getting stuck in an approval loop
3. Build a setup checker that runs at mission start and refuses to dispatch if required permissions aren't in settings.json

Recommendation: option 2 (fail-fast). Don't let a mission consume tokens on coordinator scaffolding if it'll be blocked at curl. Add a Phase 0 "permission preflight" check.

## Finding 11-C — Production curl needs explicit allowlist

**Symptom**: Harness hard-blocks outbound `curl` to `https://www.freecalchub.com/*` even after in-conversation approval. Three curl variants tried (different UAs, with/without -L), all auto-denied without inline prompts.

**Architectural truth**: For sitewide-verify (or any mission needing bulk HTTP) to work unattended, the workspace needs explicit `.claude/settings.json` permissions for the target domain. This is per-workspace setup. With 15 sites, that's 15 settings.json edits.

**Fix candidates**:
1. **install.sh provisions the allowlist** — read public_url from seo-fleet-registry.yaml, generate a `.claude/settings.json` permissions block for `curl https://<public_url>/*` per workspace, merge into existing settings.json if present. One-shot at install time; survives forever. **This is the right fix.**
2. Document setup as manual prerequisite for sitewide-verify — onerous, error-prone, doesn't scale to 15 sites
3. Use a different tool (WebFetch) instead of Bash curl — WebFetch is designed for single-URL summaries with AI, not bulk parallel fetches with grep; not a good fit for sitewide-verify

Recommendation: option 1. install.sh extension. Specific scope: only allow curl to the registered public_url, not arbitrary outbound HTTP. Settings.json merge logic needs care (don't clobber existing user permissions).

## Cumulative Sprint 11 picture

Three findings + the install.sh extension form a coherent Sprint 11 scope:

1. Mission frontmatter declares tool requirements (Finding 11-A, 11-B preflight)
2. coord routes Bash-needing missions to top-level (Finding 11-A)
3. install.sh provisions per-workspace curl allowlist from registry (Finding 11-C)
4. Mission preflight check refuses dispatch if permissions missing (Finding 11-B)

Total effort estimate: M (4-6h). All four pieces are small individually; collectively they make sitewide-verify (and future Bash-needing missions) actually feasible unattended.

## What Sprint 11 unblocks

Once these land:
- `/coord sitewide-verify <domain>` runs unattended end-to-end on any P1-P4 workspace
- The deferred FCH-TF-003 + FCH-TF-004 items in freecalchub's backlog can finally move to verified
- Future bulk-HTTP missions (eg. content-gap competitor crawl, ai-search-optimize llms.txt fetch) inherit the same unblocking
- The close-the-loop workflow (Sprint 9) is fully automatable rather than partially manual

## Stopping evidence

Sprint 10 closed yesterday declared "all 5 priority gaps from Jamie's field findings are closed." Sprint 11 was meant to remain unscoped. Today's real-world run surfaced 3 new structural frictions in 30 minutes. The discipline of trying to USE the library on a real problem is what surfaces these. Constitution rule 5 (Prove it) applies to the library itself: claims of "operational completeness" need verification by actual use.

The deferred mission outcome IS the evidence Sprint 11 is needed.
