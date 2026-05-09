# Sprint 6 — Automated Tracking Routines

**Theme**: Uplevel
**Effort**: S (3 to 5 hours after rescope)
**Dependencies**: Sprint 3 (agents are slim, routine runs are cheap)
**Status**: Not started — shrunk 2026-05-09

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

## Task List

- [ ] Decide scheduling mechanism (@architect)
- [ ] Design the routine registry schema (@architect)
- [ ] Implement token health check (@developer)
- [ ] Implement weekly `/track snapshot` routine (@developer)
- [ ] Implement monthly `/track report` routine (@developer)
- [ ] Implement failure logging and retry logic (@developer)
- [ ] Register freecalchub.com in the routine registry (@developer)
- [ ] Run the routines manually once to verify end-to-end; store output in `seo-evidence.md` (@tester)
- [ ] Schedule the routines; observe two scheduled cycles of the snapshot routine (@operator)
- [ ] Document the routine system in README (@documenter)

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
