# Monthly Report Routine

## Purpose

On the first of each month, aggregate the previous month's weekly snapshots into a full deliverable set (`analysis.md` + `marketing.md` + `data.json`) per the Sprint 5 contract. This is the executive-readable monthly artifact for one tracked site.

## Cadence

`0 8 1 * *` — 1st of month at 08:00 local time.

## Connectors required

Same as weekly-snapshot:
- Google Search Console
- Google Analytics 4
- PageSpeed Insights API
- HTTP fetch

Plus filesystem access to read `runs/` for prior weekly snapshots.

## Prerequisites

- At least 2 weekly snapshots from the previous month exist in `runs/`
- Site is tracked
- API tokens valid

## Prompt block

Paste the following block into the routine's prompt field on `claude.ai/code/routines`. Replace `<SITE>` with the actual domain:

```
You are running the MONTHLY REPORT routine for <SITE>.

Constitution: Read project-root CLAUDE.md for the Five Rules. This routine produces the executive-readable monthly artifact set per the Sprint 5 deliverable contract (templates/deliverables/).

STEP 1 — Token health check (FAIL LOUDLY if stale):
Same as weekly-snapshot routine. Open issue and stop if any token failed.

STEP 2 — Read prior snapshots:
- Find all runs/YYYY-MM-DD-<site-slug>-weekly-snapshot/data.json files for the PREVIOUS month
- If fewer than 2 exist: open issue titled "Routine: monthly-report insufficient snapshots for <SITE>"; produce a partial report with explicit note about data gap
- Load each data.json and parse scorecards + fixes

STEP 3 — Capture current state:
Run the same metric capture as weekly-snapshot (Core Web Vitals, GSC, GA4, llms.txt, etc.) — this becomes the "after" state for month-over-month comparison.

STEP 4 — Read prior findings (Constitution rule 1):
- Read seo-evidence.md for the last 6 weeks of entries
- Identify which fixes were shipped and which remained open

STEP 5 — Produce three deliverables:

5a. data.json (templates/deliverables/aimpactscanner-data.schema.json)
- mission.name = "site-audit", mission.mode = "full"
- fixes array: ALL open issues sorted by ROI (not just top 5 — this is the full monthly view)
- prior_findings_referenced: every weekly snapshot consumed
- metrics_snapshot: current month's data

5b. analysis.md (templates/deliverables/analysis-report.md)
- Fill the template completely
- Sort fix list by ROI descending
- Both AI Search Readiness and Traditional SEO scorecards present (Constitution rule 3)
- Include "Re-used (Constitution rule 1)" section listing weekly snapshots consumed
- Identify the next suggested mission based on dominant gap

5c. marketing.md (templates/deliverables/marketing-report.md)
- Fill the template completely
- Headline: best concrete win this month with a number
- Before/After table: month-start vs month-end metrics from snapshots
- Case-study framing section: filled and ready for blog/social repurposing
- If month-over-month delta is negative or flat, write an honest "what we learned, what's next" framing — do not inflate

STEP 6 — Write output:
- Path: runs/YYYY-MM-01-<site-slug>-monthly-report/
  Files: analysis.md, marketing.md, data.json
- Validate data.json against the schema

STEP 7 — Append to seo-evidence.md:
- One line: "<DATE> | monthly-report | <SITE> | dir: runs/<dir>/ | AI: <X>/50 (delta <±N>), Traditional: <Y>/50 (delta <±N>), shipped: <count> fixes"

STEP 8 — Commit and notify:
- Branch: routines/monthly-report/YYYY-MM
- Commit message: "routine(monthly-report): <SITE> YYYY-MM"
- Open PR titled "Monthly SEO report: <SITE> YYYY-MM"
- Add label "monthly-report"
- Auto-merge if checks pass; otherwise notify via routine output channel

If marketing.md cannot honestly be produced (no meaningful delta, no story), note this in the PR description and skip the file. Constitution rule 5 — Prove it. No inflation.
```

## Setup notes

- **Repository**: `TheWayWithin/SEO-AGENT`
- **Trigger**: Cron `0 8 1 * *` (1st of month, 08:00)
- **Connectors**: Google (GSC + GA4), Anthropic API
- **Estimated runtime**: 15-30 minutes (longer than weekly because of full deliverable production)
- **Estimated cost per run**: ~$1-3 (markdown generation across two deliverables + JSON output)

## Output

```
runs/YYYY-MM-01-<site-slug>-monthly-report/
  analysis.md
  marketing.md   (skipped only when no honest before/after possible)
  data.json
```

Plus one line in `seo-evidence.md` and a PR.

## Failure modes

| Failure | Recovery |
|---|---|
| <2 weekly snapshots in prior month | Routine produces partial report with explicit gap note |
| Token stale | Routine opens issue and stops; re-run manually after token rotation |
| Schema validation fails | data.json committed with `_validation_error` field; PR opens with diff for human review |
| Marketing.md framing is dishonest (forced positive on a flat month) | Skip the file; add note to PR; do not inflate |

## Backfill

If a monthly report is missed, trigger manually via `/coord site-audit <SITE> full` and tag the run directory `-monthly-report-backfill` for audit clarity.
