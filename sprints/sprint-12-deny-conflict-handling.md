# Sprint 12 — Deny-Conflict Handling

**Theme**: Ops — close the conflict-detection loop surfaced by Sprint 11 real-run validation
**Effort**: M (estimated 3-4 hours)
**Dependencies**: Sprint 11 (allowlist provisioning + Phase 0 preflight)
**Status**: COMPLETE 2026-05-17

## Sprint Goal

Make the SEO-Agent library detect and clearly communicate `settings.json` deny-rule conflicts at install time, mission time, and fleet-wide audit time. After Sprint 12, a user can fire `/coord sitewide-verify <domain>` on any workspace and either it works, or the failure surfaces with an exact-diff fix suggestion in seconds — no debugging loops.

The library does NOT auto-modify deny rules — that remains a user security decision. But every detection point surfaces the conflict identically with consistent fix language.

## Motivation

Sprint 11 closed three frictions but real-run validation on freecalchub (2026-05-16) immediately surfaced a fourth: workspaces with broad `Bash(curl:*)` deny rules override the scoped allowlist Sprint 11-C provisions. Same pattern likely affects `wget` and other bulk-HTTP tools.

The Sprint 11 hotfix added detection in `install.sh` but only:
- For `curl` patterns specifically (not `wget` or others)
- With a generic "remove OR replace" message (not an exact copy-paste fix)
- Only at install time (not at mission Phase 0 — settings.json can drift post-install)
- Only per-workspace (not a fleet-wide audit)

Sprint 12 closes all four sub-gaps. Item 6 (`--auto-fix-deny` flag) is explicitly OUT — modifying deny rules automatically is a security decision the user owns.

## Scope: In

### 12-1 — Stricter Phase 0 preflight (mission-time inspection)
- Extend `sitewide-verify.md` Phase 0 to ALSO read the workspace's `.claude/settings.json` and inspect the deny block
- If conflicting rules found (per the patterns from item 12-3), fail fast with same warning install.sh produces
- Catches the case where settings.json drifts AFTER install (user manually edits and breaks their allowlist)

### 12-2 — install.sh outputs exact diff suggestion
- Current warning: "remove these deny rules entirely, OR replace with a more specific pattern"
- Improved: explicit REPLACE/WITH pair the user copies straight into settings.json
- Same message format used by 12-1 mission-time check (consistency)

### 12-3 — Extended pattern matching (wget + httpie)
- install.sh currently inspects only `Bash(curl...)` deny entries
- Extend to monitored tool list: `curl`, `wget`, `httpie`
- Same detection logic per tool; conflict if pattern doesn't restrict to `http://*`

### 12-4 — Fleet-wide audit script
- New script: `audit-fleet-deny.sh` at repo root
- Walks every `~/SEO-Agents/*/` workspace
- Reads each `.claude/settings.json`
- Reports per-workspace: which deny rules conflict with which allowlist entries, with the exact-diff fix suggestion
- Output as a clear table; exit non-zero if any workspace has conflicts (useful for CI hygiene)

### 12-5 — Documentation in field-manual
- New `field-manual/permission-conflicts.md`
- Codifies: why broad denies are common security defaults, why they conflict with sitewide-verify and similar bulk-HTTP missions, canonical `http://*` replacement pattern, when to remove entirely vs scope down, how the three detection points (install.sh, mission Phase 0, fleet audit) work together
- Referenced from install.sh warning + sitewide-verify Phase 0 error block

## Scope: Out

- **Auto-fix flag (item 6 from discussion)** — modifying deny rules automatically is a user security decision; remains explicitly off-limits. Sprint 12 is detection + suggestion, not action.
- Restructuring the whole permission model — out of scope
- Cross-workspace allow/deny rule sync (e.g. "apply this fix everywhere") — out of scope; manual per-workspace edits are the right granularity for security decisions

## Task List

- [x] Create this sprint doc before building (Sprint conventions discipline) (2026-05-17)
- [x] 12-1: Extend sitewide-verify.md Phase 0 with settings.json deny inspection (Task A + B structure; exact-diff error block) (2026-05-17)
- [x] 12-2: install.sh outputs exact REPLACE/WITH diff for each detected conflict (2026-05-17)
- [x] 12-3: install.sh extends detection from curl-only to [curl, wget, httpie, http] (2026-05-17)
- [x] 12-4: Build audit-fleet-deny.sh — Python via stdlib; tabular human output OR --json; exit non-zero on conflict (CI gate) (2026-05-17)
- [x] 12-5: Write field-manual/permission-conflicts.md — codifies the pattern + the three detection points + canonical fix + pattern extension instructions (2026-05-17)
- [x] Smoke test: install.sh on freecalchub workspace — correctly flagged residual wget deny conflict (curl was already fixed) (2026-05-17)
- [x] Smoke test: install.sh on temp workspace with fake wget deny — detected and produced exact REPLACE/WITH suggestion (2026-05-17)
- [x] Smoke test: audit-fleet-deny.sh against ~/SEO-Agents/ — real fleet data: 7 clean, 6 with conflicts, 2 no settings (2026-05-17)
- [x] Update tracking files (sprint-12 task list, project-plan.md row, progress.md entry, agent-context.md handover) (2026-05-17)
- [→] Commit + push (next step)

## Fleet audit findings (2026-05-17 first run)

The 15 SEO workspaces split into three groups:

**Clean (7)** — no inherited deny rules at install (allow=0, deny=0): ASMGE, ISOTracker, PlebTest, Trader-7, aimpactmonitor, aisearcharena, modeloptix. Likely had no settings.json before SEO-Agent install; install.sh's Phase 11 created fresh files with only the curl allowlist.

**With conflicts (6)** — inherited Agent-11 framework's broad curl + wget denies: agent-11-website, aimpactscanner-mvp, aisearchmastery, llm-txt-mastery, solomarket need BOTH curl + wget fixed; freecalchub needs only wget (curl was fixed manually 2026-05-17).

**No settings (2)** — evolve-7, mastery-ai-framework: settings.json doesn't exist. Sitewide-verify will fail at Phase 0 Task B (live curl preflight) when run; Phase 0 Task A (settings inspection) has nothing to check. Could be addressed via install.sh --upgrade re-run when their public_url is filled in.

**Pattern recognition**: the conflict is NOT freecalchub-specific. It correlates with whether the workspace inherited Agent-11 framework settings.json (which has the broad denies as security defaults). The fix is identical across all affected workspaces. Manual per-workspace edit (library doesn't auto-modify; security decision).

## Acceptance Criteria

- `bash install.sh <workspace>` produces a warning that names the SPECIFIC conflicting line(s) AND the exact replacement text (not a generic "remove OR replace")
- `/coord sitewide-verify <domain>` Phase 0 reads the workspace settings.json deny block and fails fast on conflict (regardless of whether install.sh was last run before or after the conflict was introduced)
- `bash audit-fleet-deny.sh` walks ~/SEO-Agents/, reports each workspace's conflict state, exits 0 if clean / non-zero if any conflicts
- Detection patterns cover curl, wget, httpie (extensible to more tools by adding to a list)
- `field-manual/permission-conflicts.md` documents the pattern and is referenced from the install.sh warning + mission Phase 0 error block
- No deny rule is ever automatically modified by any tool in this sprint (security boundary held)

## Assessment Protocol

Three real-world tests:

1. **install.sh on currently-clean freecalchub**: should report 0 conflicts (we fixed the deny rule on 2026-05-17). Validates Phase 11 detection runs cleanly when nothing to flag.
2. **install.sh on a temp test dir with a deliberately-added wget deny rule**: should detect and surface the warning with exact-diff. Validates 12-3 extended pattern matching.
3. **Fleet audit on ~/SEO-Agents/**: should produce a clear per-workspace report. Freecalchub clean; other 14 workspaces still have the original broad deny patterns from their initial setup. Validates 12-4 + surfaces remaining fleet hygiene work.

Sprint close test: re-fire `/coord sitewide-verify freecalchub.com` from the freecalchub workspace. Phase 0 should NOW pass (deny rule fixed, allowlist provisioned). Mission should complete end-to-end and verify the still-deferred FCH-TF-003 + FCH-TF-004.

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Pattern matching too aggressive — flags legitimate broad denies users actually want | Detection is informational warning, not failure; user can ignore. Mission Phase 0 IS a hard fail but only triggers when actually trying to run sitewide-verify (i.e. the conflict is preventing the mission from working). |
| Tool list (curl/wget/httpie) becomes stale as new tools emerge | Documented in field-manual; trivial to extend (add to a Python list in install.sh). Future sprint when new tool needed. |
| Phase 0 settings.json inspection adds latency to every sitewide-verify run | Settings.json is small (typically <5KB); regex scan is millisecond. Negligible. |
| Fleet audit reveals patterns we don't have install.sh logic for yet | Audit reports the unknown patterns explicitly; user can decide whether to extend install.sh or treat as acceptable per-workspace choice. |

## Exit Notes

When closing this sprint, update `agent-context.md` with:
- Whether the freecalchub validation re-run actually completed (FCH-TF-003 + FCH-TF-004 finally verified, or new friction surfaced as Sprint 13 candidate)
- Fleet audit results: how many of the 14 other workspaces have conflicting deny rules
- Whether any deny patterns surfaced that need install.sh logic we don't have yet

Capture in `progress.md`:
- Per-item completion status
- Whether item 12-3's extended list (curl/wget/httpie) needs further extension based on real workspace patterns
- Decision: do we make `--auto-fix-deny` a future sprint candidate, or leave it permanently out-of-scope as a security decision

---

## Why this sprint exists

Sprint 11 closed three frictions. Real-run validation surfaced a fourth (deny conflict). Hotfix added basic detection. Sprint 12 closes the detection loop properly so the same friction can't keep surfacing in slightly-different forms across the remaining 14 workspaces. Constitution rule 5 (Prove it) applied iteratively: each sprint surfaces the next layer of friction, closes it cleanly, leaves the library more operational than before.
