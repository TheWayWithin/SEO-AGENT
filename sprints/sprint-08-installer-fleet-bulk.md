# Sprint 8 — Installer + Fleet Bulk Operator

**Theme**: Ops — first operational sprint after v2 architectural completion
**Effort**: M (estimated 5-7h; actual ~5h)
**Dependencies**: Sprint 5 (deliverable contract is the SEO product layer install.sh deploys)
**Status**: COMPLETE 2026-05-10

> **BACKFILL 2026-05-16**: This sprint doc was created retroactively from progress.md to restore the sprints/ pattern. Sprints 1-7 had docs; 8-10 only had progress.md entries. Jamie flagged the inconsistency 2026-05-16; backfilled with discipline note for future sprints (see project-plan.md "Sprint conventions" section).

## Sprint Goal

Make SEO-Agent installable at scale. After v2 closed, Jamie has 15 sites to roll the library out to. Manual install on freecalchub took 30+ minutes; 15 manual installs is the wrong shape. Build the installer pattern so each new site takes ~5 minutes.

## Motivation

Sprint 5 fixed the deployment gap (SEO agents → `.claude/agents/`). Sprint 6-7 completed the v2 architecture. But the rollout question remained open: how does the SEO-Agent library actually get from `~/DevProjects/SEOAgent/` onto each of Jamie's other sites?

Jamie's mental model: `~/SEO-Agents/[repo]/` mirrors `~/DevProjects/[repo]/`. Each workspace contains a clone of the target repo PLUS the SEO-Agent product layer installed on top. Per-workspace isolation; SEO history versions independently from product code.

The first manual install (freecalchub) was the discovery run. Sprint 8 turns that into automation.

## Scope: In

- `install.sh` (single-site installer)
  - Takes target path + optional `--clone-from <url> --branch <branch>`
  - Modes: install (default), `--upgrade` (refresh SEO product files only, preserve site config), `--force`, `--dry-run`
  - HARD SAFETY RULE: refuses any target path under `~/DevProjects/` (defence in depth: checked before AND after path canonicalisation)
  - Idempotent: detects existing install via `.seo-agent-version` stamp; auto-switches to `--upgrade` unless `--force`
  - Preserves existing CLAUDE.md by renaming to `CLAUDE-product-dev.md` before installing SEO Constitution
  - Preserves existing `.gitignore` (warns to manually verify `.env*` protection)
- `install-fleet.sh` (bulk operator)
  - Reads `~/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml`
  - For each `tier=active`, `installed!=true` repo: clones into workspace path, calls install.sh
  - Filters: `--filter p1` (priority), `--filter <name>` (substring), `--filter p1,p2` (comma-separated)
  - `--dry-run`, `--keep-going`, `--skip-clone`, `--upgrade` flags
  - YAML parsed with awk (no Python dependency)
- `~/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml`
  - 14 active SEO targets across P1-P4 priority tiers
  - Sourced from agent-11 fleet registry; adds workspace path, public_url, priority
  - P1 (AI Search Mastery portfolio, 5): aisearchmastery, llm-txt-mastery, aimpactscanner-mvp, aisearcharena, aimpactmonitor
  - P2 (other portfolio, 2): mastery-ai-framework, agent-11-website
  - P3 (other ventures, 6): Trader-7, PlebTest, ISOTracker, modeloptix, solomarket, evolve-7
  - P4 (dormant, 1): ASMGE
  - Skip tier (8): SEOAgent itself, BOS-AI, agent-11, Socrates, SoloCMD, mcp-11, mcp-7, test-project

## Scope: Out

- Per-workspace tracking config customisation — install.sh seeds `tracking/config/tracking.yml` but does not customise per-site
- Python tracking system copy — Sprint 5 lesson said skip; same here
- Automatic git workflow setup beyond cloning — branch creation, remote config, etc. left to user
- Multi-machine sync — Shared/ folder handles registry sync; workspaces stay per-machine

## Task List

- [x] Design seo-fleet-registry.yaml schema; draft from agent-11 fleet registry with public_url additions (2026-05-10)
- [x] Triage 17 active agent-11 repos: which need SEO? Confirmed 14 active + 1 already installed (freecalchub) = 15 SEO targets (2026-05-10)
- [x] Build install.sh with 11 phases, dry-run support, DevProjects refusal (2026-05-10)
- [x] Build install-fleet.sh with filter, dry-run, keep-going (2026-05-10)
- [x] Smoke test install.sh on `/tmp/install-test` — full dry-run output verified (2026-05-10)
- [x] Smoke test DevProjects safety rule — confirmed immediate refusal (2026-05-10)
- [x] Dry-run install-fleet --filter p1 — 5 P1 repos planned correctly (2026-05-10)
- [x] Dry-run install-fleet (full) — 14 planned, freecalchub skipped (2026-05-10)
- [x] Real run install-fleet --filter p1 — 5/5 succeeded (2026-05-10)
- [x] Real run install-fleet --filter p2,p3 — first attempt halted at Trader-7 (URL stale in agent-11 registry; repo was named llm-trading-system); fixed in SEO registry, re-ran with --keep-going (2026-05-10)
- [x] Re-run install-fleet --filter Trader-7 with corrected URL — success (2026-05-10)
- [x] Verify 14 workspaces in ~/SEO-Agents/ (excluding freecalchub which was already there) (2026-05-10)
- [x] Update tracking files (project-plan.md Sprint 8 row, progress.md entry) (2026-05-10)
- [x] Commit + push (2026-05-10, commit b16d62e)

## Acceptance Criteria

- `bash install.sh ~/SEO-Agents/<name>` installs SEO product layer additively over existing Agent-11 v6 framework, preserves site-specific files, refuses `~/DevProjects/` paths
- `bash install-fleet.sh --dry-run` shows planned actions for every tier=active repo without filesystem changes
- `bash install-fleet.sh --filter p1` installs P1 cohort only; freecalchub correctly skipped (installed=true)
- Total workspaces in ~/SEO-Agents/ after Sprint 8: 14 + freecalchub = 15
- install.sh and install-fleet.sh both executable (`chmod +x`) and self-documenting (`--help`)

## Assessment Protocol (freecalchub.com)

Not applicable — this is an Ops sprint. Validation is by successful real runs across the fleet:

1. P1 cohort run: 5/5 succeeded with no manual intervention
2. P2+P3 cohort run: surfaces Trader-7 URL bug (agent-11 registry stale); fix + re-run completes 6/6
3. Final tree state: 14 SEO workspaces (excluding freecalchub) in ~/SEO-Agents/

Sprint close test: re-run install-fleet --dry-run; should show all 14 active repos as "installed" (workspace exists), proving idempotency.

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| install.sh accidentally targets ~/DevProjects/ | Hard refusal at two check points (pre- and post-canonicalisation); tested |
| Existing CLAUDE.md in target workspace gets clobbered | Preservation logic renames existing → CLAUDE-product-dev.md before installing SEO Constitution |
| YAML parser breaks on registry edits | Pure awk parser; keep registry structurally simple; smoke-test after any edit |
| Future framework upgrade overwrites SEO-augmented coord.md in workspaces | SEO-PRODUCT-LAYER-START/END markers; install.sh re-applies on --upgrade |
| Trader-7 URL stale-style problems propagate to other repos | --keep-going + dry-run before real runs; flag for agent-11 fleet registry sync |

## Exit Notes

Captured in progress.md 2026-05-10:
- 13 workspaces installed on first day (5 P1 + 2 P2 + 6 P3 after Trader-7 retry)
- ASMGE P4 deferred per user choice (later picked up on 2026-05-16 upgrade pass)
- Agent-11 fleet registry has stale Trader-7 URL — flagged for separate cleanup pass
- All P1 repos already had .gitignore — installer correctly preserved; manual verification of .env* protection recommended before any commits land in those workspaces

What this enabled going forward: each new SEO site takes ~5 minutes via `bash install-fleet.sh --filter <name>` after a 2-line addition to the registry, instead of ~30 minutes of manual cp dance.
