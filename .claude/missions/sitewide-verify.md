---
requires_tools: [Bash]
run_top_level: true
---

# SITEWIDE VERIFY MISSION
## Confirm shipped fixes are LIVE, not just locally committed

**Duration**: 30-90 minutes depending on scope
**Agents**: @seo-technical (lead), @seo-coordinator
**Trigger**: After `/coord technical-fix` ships items, before closing them
**Deliverable**: `verification.md` + backlog updates

## CONTEXT (Constitution rule 1)

Read `seo-evidence.md` for prior verification runs and known site quirks. Read `seo-backlog.md` to find items in `shipped` status — those are this mission's scope.

## PHASE 0: PERMISSION PREFLIGHT (Sprint 11-B) — RUN FIRST, FAIL FAST

Before any scaffolding work, verify the harness will let this mission do its job. Sprint 10 first run wasted ~5 min of agent token spend scaffolding verification work that couldn't execute because curl was harness-denied.

### Task
- [ ] Identify the target domain from the `/coord` arguments (e.g. `freecalchub.com`)
- [ ] Run a tiny test curl: `curl -sI -o /dev/null -w "%{http_code}\n" --max-time 10 https://www.<domain>/robots.txt`
- [ ] If the curl is harness-denied OR returns a permission error: STOP IMMEDIATELY and output the actionable error block below
- [ ] If the curl runs successfully (any HTTP status 200-599 is fine — we're testing permission, not page content): proceed to Phase 1

### Actionable error block (paste verbatim if preflight fails)

```
SITEWIDE-VERIFY HALTED AT PHASE 0 — PERMISSION PREFLIGHT

The harness denied a test curl to https://www.<domain>/robots.txt. This
mission needs to fetch ~110 live pages from <domain>; without curl
permission it cannot execute.

FIX: add the following 3 entries to permissions.allow in
.claude/settings.json (workspace root):

    "Bash(curl https://<domain>/*)",
    "Bash(curl -* https://<domain>/*)",
    "Bash(curl * https://<domain>/*)"

Or run `bash <path-to-SEO-Agent>/install.sh <this-workspace-path> --upgrade`
to provision the allowlist automatically (Sprint 11-C). The installer reads
public_url from ~/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml
and merges the entries without clobbering existing settings.

After the allowlist is in place, re-run `/coord sitewide-verify <domain>`.

DO NOT proceed past Phase 0 without permission — Phase 1+ depend on
curl. Constitution rule 5 (Prove it): no fabricated verification.
```

### Why this exists

Sprint 10's first real-world run completed scaffolding then hit the harness wall on curl. ~5 min of agent token spend before discovering the mission couldn't actually execute. Phase 0 catches the same situation in ~5 seconds with an explicit, actionable error rather than getting stuck.

## MISSION OBJECTIVES

Close the gap that caused freecalchub's Twitter-tag class of bug: 2 of 110 pages missed in a "shipped" change because verification was a spot-check, not sitewide.

This mission moves backlog items from `shipped → verified` only when the change is confirmed live across the affected scope. Items that fail verification get flagged (potentially `reverted` if rollback is needed).

## PHASE 1: SCOPE FROM BACKLOG (5 minutes)
**Lead**: @seo-coordinator

### Tasks
- [ ] Read `seo-backlog.md` "Recently shipped (awaiting verification)" table
- [ ] For each item, identify:
  - **Affected scope**: single page, single template, all pages of type X, sitewide
  - **Verification method**: HTTP fetch + grep, JSON-LD parse, robots.txt parse, etc.
  - **Pass criteria**: what evidence proves the change is live
  - **Sample size**: every page in scope, OR a representative sample with explicit sample size

### Deliverables
- A scoped verification plan in `verification.md` listing each item with method + pass criteria

## PHASE 2: SITEWIDE FETCH AND CHECK (15-60 minutes)
**Lead**: @seo-technical

### Verification methods by category

**HTML head tags** (canonical, meta description, OG, Twitter cards):
- Fetch every page in scope (or representative sample if scope is "sitewide" and >50 pages)
- For "sitewide" claims: verify EVERY page in the affected directory pattern, not just samples
- Grep for the specific tag pattern; report pass / fail per URL
- Honest about sample size in verification.md

**Schema markup (JSON-LD)**:
- Fetch the page, extract `<script type="application/ld+json">` blocks
- Parse JSON; assert required schema types present
- Report parse errors as fails (broken JSON-LD = no schema)

**robots.txt directives**:
- Fetch `https://<domain>/robots.txt`
- Grep for the specific User-agent + Allow/Disallow patterns
- One-shot check; pass/fail

**llms.txt presence and format**:
- Fetch `https://<domain>/llms.txt` and `https://<domain>/llms-full.txt`
- Verify served as text; verify H1 + summary + sections present per spec
- Report any 404s or auth walls as fails

**Page content changes** (rewritten lead paragraphs, added FAQ blocks, etc.):
- Fetch the page
- Search for the new content; verify position (top of page, in FAQ schema, etc.)
- Spot-check rather than full-text-diff (full-text-diff is too noisy for prose changes)

### Tasks
- [ ] Execute the verification method for each item
- [ ] Record per-item pass/fail with evidence (URL fetched, what was found, what was expected)
- [ ] For sitewide items: report total pages checked, pass count, fail count, failure URLs

### Deliverables
- Detailed verification log per item in `verification.md`

## PHASE 3: BACKLOG STATE UPDATES (10 minutes)
**Lead**: @seo-coordinator

### Tasks
- [ ] For items where ALL pages in scope passed: update `seo-backlog.md` status from `shipped → verified`. Record verification date + verifier (@seo-technical).
- [ ] For items where SOME pages failed: keep status as `shipped` and add a note row "verification partial — N of M passed; failed URLs: ..." Item stays open until either re-shipped to cover the gap or scope corrected.
- [ ] For items where NO pages passed (likely deploy didn't actually push): mark item back to `in_progress` with note "shipped commit found but not deployed — re-trigger deploy". Open a separate row to track the deploy gap.
- [ ] For items where the change is live but BREAKS something: mark `reverted` with rollback note. Open a new high-priority backlog item for the fix-the-fix work.

### Deliverables
- Updated `seo-backlog.md` with state transitions
- Pointer line in `seo-evidence.md`: "VERIFY | <date> | <domain> | runs/<dir>/verification.md | N items verified, M items partial, K items reverted"

## OUTPUTS (Sprint 5 + 10 deliverable contract)

Produce in run-scoped directory:

```
runs/YYYY-MM-DD-<domain-slug>-sitewide-verify/
  verification.md   (REQUIRED) — per-item verification log with pass/fail evidence
  data.json         (OPTIONAL) — only if scorecards re-computed; usually skipped
                                 (verify is about confirming live, not re-scoring)
```

Plus updates to persistent files in workspace root:
- `seo-backlog.md` — state transitions per Phase 3
- `seo-evidence.md` — one-line pointer per Phase 3

## QUALITY CHECKLIST

Before mission completion:
- [ ] Every `shipped` item in the backlog at mission start has been processed
- [ ] No item moved to `verified` without filesystem-verifiable HTTP evidence in verification.md
- [ ] Sitewide items report explicit page counts (total in scope, passed, failed)
- [ ] No item moved to `closed` from this mission — closure requires `/track compare` confirming metric movement (Constitution rule 5)

## CRITICAL DON'TS

- **DON'T spot-check items claimed to be sitewide.** If the claim is "all 110 calculator pages updated", check all 110 (or at minimum a 100% sample of the directory pattern). Sample-N rules don't apply to sitewide claims — that's how the 2-of-110 freecalchub gap happened.
- **DON'T move items to `closed`.** That state requires metric movement via /track compare, not just live verification.
- **DON'T mark items `verified` based on local commit messages.** Verify the LIVE site. Local commit ≠ shipped (Jamie's freecalchub field finding encoded structurally).
- **DON'T silently skip items that errored on fetch.** Report fetch errors explicitly in verification.md as "could not verify — manual check needed".

## ESCALATION

If verification reveals systemic problems (e.g. deploy pipeline broken, CDN caching old version, large fraction of supposedly-shipped items not actually live):
- Halt verification of further items until the systemic issue is understood
- Open a backlog item for the systemic problem itself
- Note in verification.md "halted at item N due to systemic issue X"

---

**Mission Success**: Every backlog item that was `shipped` at mission start has either been verified live, flagged with a specific gap, or marked reverted. No silent fails. Constitution rule 5 (Prove it) made operational at the verification layer.
