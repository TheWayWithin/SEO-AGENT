# Sprint 11 — Runtime Readiness

**Theme**: Ops — make missions actually runnable in real workspaces, not just structurally complete
**Effort**: M (4-6 hours)
**Dependencies**: Sprint 10 (sitewide-verify mission ships, needs this to actually execute unattended)
**Status**: Not started

## Sprint Goal

Close the three frictions that made `/coord sitewide-verify freecalchub.com` complete as `deferred` rather than `verified` on 2026-05-16. The mission scaffolded cleanly but couldn't execute — three structural gaps between "mission exists" and "mission runs unattended on a real workspace" surfaced in a single attempted run.

By Sprint 11 close, firing `/coord sitewide-verify <domain>` on any of the 15 SEO workspaces completes end-to-end without interactive approval prompts or harness denials.

## Motivation

Sprint 10 closed with the claim "all 5 priority gaps from Jamie's freecalchub field findings are closed." That was structurally true but practically incomplete — operating the library against production introduces a tier of frictions that no amount of architecture-without-use would have surfaced.

Today's `/coord sitewide-verify freecalchub.com` attempt produced:
- The coordinator subagent (Task-tool delegated) could not run Bash, so the mission scaffolded but couldn't execute the 110 live HTTP fetches
- Jamie's in-conversation "Allow curl, 8 parallel" approval did not propagate to the harness permission layer; subsequent curl calls were still hard-denied
- Three curl variants to `freecalchub.com` were auto-denied without inline prompts because the workspace `.claude/settings.json` had no allowlist for that domain

The mission completed as `deferred` (not `failed`) per Constitution rule 5 — no fabrication, full friction captured in `~/SEO-Agents/freecalchub/runs/2026-05-16-freecalchub-com-sitewide-verify/verification.md`.

Sprint 11 fixes all three at the right level so the loop Sprint 9+10 designed for actually runs.

## Scope: In

### 11-A — Mission tool requirements + dispatch routing
- Add frontmatter or top-of-file declaration to mission files listing required tools (e.g. `requires_tools: [Bash, WebFetch]`)
- Update `/coord` dispatch logic in `.claude/commands/coord.md` to inspect this declaration
- If mission requires Bash (or any tool unavailable to coordinator subagent), `/coord` runs the mission TOP-LEVEL instead of delegating to `@seo-coordinator` via Task tool
- Default behaviour for missions with no declared tool requirements: existing delegation path (preserves backward compatibility)
- Scope of edit: `sitewide-verify.md` (declares Bash), other 4 SEO missions (declare no special requirements), `coord.md` dispatch logic, brief note in `field-manual/` if one exists

### 11-B — Permission preflight (Phase 0)
- Add a Phase 0 step to missions that need external permissions: a tiny test call (e.g. one `curl -I` to the target domain) that verifies the permission layer allows what the mission needs
- If Phase 0 fails: mission exits immediately with an actionable error block including the exact `.claude/settings.json` snippet to add
- If Phase 0 passes: mission proceeds to Phase 1
- Initial scope: only `sitewide-verify` gets Phase 0 (it's the one with confirmed friction). Pattern available for any future Bash-needing mission to adopt.

### 11-C — install.sh provisions per-workspace curl allowlist
- `install.sh` reads `public_url` from `~/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml` for the workspace being installed (matched by workspace path or name)
- Generates a `.claude/settings.json` permissions block scoped to that domain: `curl https://<public_url>/*`
- Merge logic: if `.claude/settings.json` already exists, merge the new allowlist entries WITHOUT clobbering existing user permissions; if it doesn't exist, create it
- Per-workspace, not global
- Specifically scoped to the registered public URL, not arbitrary outbound HTTP
- Idempotent: re-running install.sh doesn't duplicate entries or unset existing ones
- Works in both fresh install and `--upgrade` modes

### Re-run validation
- After Sprint 11 build complete, re-run `/coord sitewide-verify freecalchub.com` on the upgraded freecalchub workspace
- Expected outcome: mission completes end-to-end unattended; FCH-TF-003 and FCH-TF-004 move from `shipped` (deferred) to either `verified` or partial-with-failed-URLs
- This is the structural validation that Sprint 11 closes the friction Sprint 10's mission surfaced

## Scope: Out

- WebFetch-based bulk fetch alternative — designed for single-URL summaries, not bulk parallel grep; not a viable substitute
- Settings.json deny rules / policy management — too broad; out of scope for this sprint
- Global (not per-workspace) allowlist setup — security risk, doesn't scale; out of scope
- Backfilling sprint docs for Sprints 8, 9, 10 — separate housekeeping decision; out of this sprint

## Task List

- [ ] Inventory the 5 SEO mission files: which require Bash, which need only subagent-accessible tools? (@strategist or @architect)
- [ ] Add `requires_tools:` frontmatter declarations to all 5 SEO mission files; sitewide-verify declares Bash; others declare no requirements (@developer)
- [ ] Update `.claude/commands/coord.md` dispatch logic to read mission requirements and route accordingly (top-level vs coordinator delegation) (@developer)
- [ ] Add Phase 0 permission preflight section to `sitewide-verify.md`; small test curl call; clear fail-fast error message with exact settings.json snippet (@developer)
- [ ] Extend `install.sh` to read `public_url` from `seo-fleet-registry.yaml` for the workspace being installed (@developer)
- [ ] Implement settings.json merge logic in `install.sh`: scoped allowlist for `curl https://<public_url>/*` only, no clobber of existing user permissions, idempotent (@developer)
- [ ] Smoke test `install.sh --upgrade` on `/tmp/install-test` with a fake registry entry; verify settings.json gets the right allowlist (@tester)
- [ ] Run `bash install-fleet.sh --upgrade` to retrofit all 15 existing SEO workspaces with their per-domain allowlists (@operator)
- [ ] Re-run `/coord sitewide-verify freecalchub.com` from the upgraded workspace; expect end-to-end completion (@tester)
- [ ] Update tracking files: project-plan.md row, progress.md entry, agent-context.md handoff, docs/library-improvements-input.md (mark 11-A/B/C closed)
- [ ] Commit + push

## Acceptance Criteria

- `/coord sitewide-verify freecalchub.com` runs end-to-end unattended on a freshly-upgraded workspace and produces a verification.md with real per-URL pass/fail data for all 110 calculator pages
- FCH-TF-003 and FCH-TF-004 backlog items move from `shipped (deferred)` to `verified` (or to `shipped` with specific failed URLs flagged) — no longer stuck in deferred state
- Re-running `install.sh --upgrade` on an existing workspace does not duplicate allowlist entries or unset existing user permissions in `.claude/settings.json`
- A mission file declared with `requires_tools: [Bash]` is correctly routed top-level by `/coord`; one declared without is delegated to coordinator subagent as before
- Phase 0 permission preflight in sitewide-verify fails fast with an actionable error if curl allowlist is missing — does not waste tokens scaffolding work it can't execute

## Assessment Protocol (freecalchub.com)

This is the real-world test that defines sprint close:

1. After Sprint 11 build, run `bash install.sh ~/SEO-Agents/freecalchub --upgrade` to retrofit the workspace with the new allowlist
2. Inspect `~/SEO-Agents/freecalchub/.claude/settings.json` — confirm the allowlist entry for `curl https://www.freecalchub.com/*` is present and that any pre-existing user permissions are intact
3. Fire `/coord sitewide-verify freecalchub.com` from the workspace
4. Expected: mission completes end-to-end without permission prompts, without harness denials, in roughly 2-5 min
5. Inspect the produced `verification.md`: should have real per-URL pass/fail data for all 110 calculator pages
6. Confirm seo-backlog.md has been updated — FCH-TF-003 and FCH-TF-004 should have moved out of the "deferred" state
7. Record the timing and result in seo-evidence.md as a sprint-close gate evidence

If any step fails: stop, document in progress.md, decide whether to fix in this sprint or open Sprint 12.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| settings.json merge logic clobbers user permissions | Write merge as additive-only with explicit conflict detection; refuse to write if a conflict found; spot-check on freecalchub which already has settings.json |
| Per-mission frontmatter convention conflicts with future framework upgrades to coord.md | Document the convention in field-manual/ so framework upgrades preserve it; wrap mission dispatch logic additions in SEO-PRODUCT-LAYER markers per established pattern |
| Phase 0 preflight slows down every mission run | Phase 0 runs only on missions that declare external tool requirements; scoped to a single test call; sub-second when permissions are correctly set |
| Per-workspace allowlist setup still requires manual settings.json edit for any workspaces NOT in the SEO fleet registry | Document the fallback: workspaces outside the registry can manually add their allowlist; install.sh only auto-provisions for registered workspaces |
| Re-running sitewide-verify on freecalchub finds the 2 Twitter-tag pages still missing (the original Sprint 10-motivating bug) | That would be a SUCCESS for Sprint 11 — the mission correctly surfaced a real production gap. Open a backlog item for the gap, fix it, re-verify. Constitution rule 5 working as intended. |

## Exit Notes

When closing this sprint, update `agent-context.md` with:
- Phase 11 → Phase 12 handoff (if any) OR explicit "operational close — no further sprints planned without new field findings"
- Confirmation that the deferred FCH-TF-003 + FCH-TF-004 items have moved out of `shipped (deferred)` state
- The sprint-close verification.md path for permanent reference
- Whether the 2 Twitter-tag pages (original Sprint 10 motivator) actually exist on freecalchub — if so, a new backlog item

Capture in `progress.md`:
- The three structural fixes (11-A, 11-B, 11-C) with brief implementation notes
- The retrofit result on all 15 workspaces (did install-fleet --upgrade work cleanly across the fleet?)
- Any settings.json conflicts encountered and how resolved
- Total time from "fire mission" to "mission complete" on the validation run

Field-finding capture for future sprints:
- If new frictions emerge during validation, add to `docs/library-improvements-input.md` as Sprint 12+ candidates
- The discipline of testing on real production is what surfaces the next tier; assume each sprint will reveal something

---

## Why this sprint exists at the right level

Sprint 10 claimed "all 5 priority gaps closed." Today's deferred mission proved that claim was about architecture, not operations. Sprint 11 closes the operations gap so the architecture actually functions in real workspaces.

After Sprint 11, the close-the-loop workflow (Sprint 9) is fully automatable rather than partially manual. Constitution rule 5 (Prove it) gets made operational across the entire fleet, not just in principle.
