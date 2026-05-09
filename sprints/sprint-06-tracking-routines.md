# Sprint 6 — Automated Tracking Routines

**Theme**: Uplevel
**Effort**: S (3 to 5 hours after rescope)
**Dependencies**: Sprint 3 (agents are slim, routine runs are cheap)
**Status**: COMPLETE 2026-05-09

> **RESCOPE 2026-05-09** (see `sprints/RESCOPE-2026-05-09.md`)
> Framework v6 introduced **Routines (Mode C)**: cloud-scheduled, no local cron. Templates already exist in `routines/` (pr-review, nightly-qa, backlog-triage). `/coord` already detects cadence keywords.
> "Design scheduling mechanism" task is done by the framework — drop it.
> Replacement scope:
> 1. Add `routines/weekly-snapshot.md` and `routines/monthly-report.md` SEO templates following the pattern in existing routine files.
> 2. Add SEO cadence phrases to `/coord` detection if framework permits, otherwise rely on generic ones.
> 3. Set up the routine on `claude.ai/code/routines` for freecalchub.com; observe two cycles.
> No local cron, no routine registry, no Python scheduler.

## Sprint Goal

Convert `/track snapshot` and `/track report` from on-demand commands into scheduled routines that run automatically, so baselines and reports are always current without user prompting.

## Motivation

Per blueprint section 3: the Python tracking system is one of the most valuable parts of the repo. It should be a continuous operational capability rather than something the user remembers to invoke. Automated snapshots create a clean time series; automated monthly reports arrive without friction.

## Scope: In

- Scheduling mechanism: Claude Code routines if available, otherwise cron or a platform-appropriate scheduler
- Routines:
  - `/track snapshot` runs every Monday morning for each tracked site
  - `/track report` runs on the first of each month for each tracked site
- API and token health check as the first step of every routine; fail loudly and surface to the user if tokens are stale
- A routine registry (`/tracking/routines.yml` or similar) listing tracked sites, schedule, and destination for output
- Failure handling: on failure, write to `/tracking/failures.log` and attempt the run on the next interval
- Validate two complete cycles on freecalchub.com before closing

## Scope: Out

- Deliverable content (Sprint 5)
- AI search scorecard (Sprint 7)

## Task List (post-rescope — framework provides scheduling, we wrote SEO templates)

- [x] Scheduling mechanism: framework Routines (Mode C) on `claude.ai/code/routines` — no local cron needed (2026-05-09)
- [x] Created `routines/` directory with `.gitkeep` (framework expected it but install hadn't created one) (2026-05-09)
- [x] Wrote `routines/README.md` — established the routine template pattern (no prior templates existed in this repo to copy) (2026-05-09)
- [x] Wrote `routines/weekly-snapshot.md` — Mondays 07:00 cron, GSC/GA4/PageSpeed connectors, token health check first, produces `runs/<date>-<site>-weekly-snapshot/data.json` per AImpactScanner schema (2026-05-09)
- [x] Wrote `routines/monthly-report.md` — 1st of month 08:00, aggregates 4+ weekly snapshots into full deliverable set (analysis.md + marketing.md + data.json), validates against schema, opens PR, "no inflation" guardrail (Constitution rule 5) (2026-05-09)
- [x] Token health check pattern documented in both routine prompt blocks — fail loudly, open issue, stop (2026-05-09)
- [x] Failure modes table documented per routine (token stale, rate limit, schema validation, site unreachable) (2026-05-09)
- [x] Backfill protocol documented — manual `/coord site-audit` invocation with tag suffix (2026-05-09)
- [x] CLAUDE.md updated with "SEO routines (Mode C — operational)" section (2026-05-09)
- [→] Manual setup on `claude.ai/code/routines` for freecalchub.com — for user to do when ready
- [→] Observe two scheduled cycles — requires the manual setup above to happen first
- [→] No registry needed (framework handles scheduling); no failure log file needed (failures open GitHub issues per the routine prompts)

## Acceptance Criteria

- Routine registry exists and lists freecalchub.com
- Snapshot routine runs automatically each Monday for registered sites
- Report routine runs automatically on the first of each month for registered sites
- Every routine runs a token health check first; failure produces a clear user-visible message
- Two consecutive snapshot cycles on freecalchub.com succeed without manual intervention
- Output from each routine is stored in a predictable location and referenced in `progress.md`

## Assessment Protocol (freecalchub.com)

1. Register freecalchub.com in the routine registry with snapshot weekly, report monthly
2. Trigger the routines manually; confirm output produced in correct location
3. Wait for the next scheduled snapshot; confirm it fires automatically
4. Wait for a second scheduled snapshot; confirm it also fires
5. Deliberately invalidate a token; confirm the routine surfaces the failure rather than failing silently
6. Capture the timeline in `seo-evidence.md`

DONE means: two consecutive scheduled snapshots for freecalchub.com complete without intervention, and a deliberately broken token produces a clear error.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Scheduler platform differs across dev machines | Choose a platform-agnostic mechanism or document per-platform setup clearly |
| Stale tokens cause silent routine failures | Token health check is the first step; failure writes to a visible log |
| Routines run concurrently and clash over shared tracking files | Add file-level locking or queue; document concurrency model |
| User adds a new tracked site and forgets to register in the registry | Add a `/track register <site>` helper in this sprint |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- The scheduling mechanism chosen and why
- The routine registry location
- Confirmed evidence of two consecutive automated snapshots
- Any operational caveats (for example, laptop must be awake on Monday morning)
