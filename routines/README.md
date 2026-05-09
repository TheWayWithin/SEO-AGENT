# Routines (Mode C — Operational)

Recurring SEO work that runs on Anthropic-managed cloud via Claude Code Routines, not via local `/coord` invocation. No local session required, no laptop awake constraint.

## Setup pattern

For each routine in this directory:

1. Open `claude.ai/code/routines` and click **New routine**.
2. Paste the **Prompt block** from the routine template into the prompt field.
3. Configure:
   - **Repository**: `TheWayWithin/SEO-AGENT` (or fork)
   - **Trigger**: cron schedule per the template's "Cadence" line
   - **Connectors**: per the template's "Connectors required" line
4. Save. The routine fires on the configured schedule.

## Available SEO routines

| Routine | File | Cadence | Output |
|---|---|---|---|
| Weekly Snapshot | `weekly-snapshot.md` | Mondays, 07:00 local | `runs/YYYY-MM-DD-<site>-weekly-snapshot/data.json` |
| Monthly Report | `monthly-report.md` | 1st of month, 08:00 local | `runs/YYYY-MM-01-<site>-monthly-report/{analysis,marketing,data}.{md,json}` |

## Per-site setup

Each routine targets one site. To track multiple sites, create one routine instance per site (each with its own cron + repository config).

Tracked sites (initial): `freecalchub.com`.

## Why routines, not local cron

Per `.claude/CLAUDE.md` Mode C — operational work belongs in Anthropic-managed cloud routines, not local schedulers:

- No "laptop must be awake on Monday morning" failure mode
- Token health checks fail loudly (visible in routine run logs) rather than silently
- Output lands in repo via PR or direct commit (configurable per routine)
- Same execution context as interactive `/coord`, so the SEO Constitution and deliverable contract apply

The `tracking/` Python system can still run locally for ad-hoc snapshots — routines complement it, they don't replace it.

## Routine template structure

Every routine template has these sections:

- **Purpose** — one sentence
- **Cadence** — cron expression + human-readable
- **Connectors required** — GSC, GA4, etc.
- **Prerequisites** — what must exist (tracked site config, baseline)
- **Prompt block** — the verbatim prompt to paste into routine setup UI
- **Setup notes** — repo, trigger config specifics
- **Output** — file paths the routine writes
- **Failure modes** — known issues and recovery
