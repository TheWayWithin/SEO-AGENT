# Weekly Snapshot Routine

## Purpose

Capture a structured `data.json` snapshot of one tracked site every Monday morning, conforming to `templates/deliverables/aimpactscanner-data.schema.json`. Builds a time series the AImpactScanner dashboard and the monthly-report routine consume.

## Cadence

`0 7 * * 1` — Mondays at 07:00 local time.

(Adjust per site's primary timezone if multiple sites are tracked.)

## Connectors required

- Google Search Console (impressions, clicks, average position, CTR)
- Google Analytics 4 (organic sessions, conversions)
- PageSpeed Insights API (Core Web Vitals)
- HTTP fetch (for `/llms.txt`, `/robots.txt`, schema crawl)

## Prerequisites

- Site is tracked: confirmed in `tracking/config/` or equivalent
- Baseline exists: at least one prior snapshot OR the user has run `/track baseline <site>` manually
- API tokens valid and not stale (routine checks this first; fails loudly if stale)

## Prompt block

Paste the following block into the routine's prompt field on `claude.ai/code/routines`. Replace `<SITE>` with the actual domain (e.g. `freecalchub.com`):

```
You are running the WEEKLY SNAPSHOT routine for <SITE>.

Constitution: Read project-root CLAUDE.md for the Five Rules. Constitution rule 5 (Prove it) drives this routine — every snapshot must produce verifiable structured data.

STEP 1 — Token health check (FAIL LOUDLY if any token stale):
- GSC API token: verify it can fetch yesterday's impressions for <SITE>
- GA4 API token: verify it can fetch yesterday's organic sessions for <SITE>
- PageSpeed API: verify it returns a score for <SITE>
If any check fails: open a GitHub issue titled "Routine: weekly-snapshot token failure for <SITE>" with the specific stale token and stop. Do NOT proceed with partial data.

STEP 2 — Capture metrics:
- Core Web Vitals (LCP, INP, CLS) via PageSpeed API
- Lighthouse scores (performance, SEO, accessibility, best practices)
- Crawl errors, broken links, missing meta (use crawl tooling)
- Organic sessions, users, pageviews (GA4, last 7 days)
- Search visibility: avg position, impressions, clicks, CTR (GSC, last 7 days)
- Keyword distribution: top 3 / 10 / 20 / 50 / 100 counts (GSC)
- llms.txt status: present / partial / missing (HTTP fetch /llms.txt)
- AI crawler policy: parse /robots.txt for GPTBot, Claude-User, PerplexityBot directives
- Structured data coverage: spot-check 5 representative URLs for JSON-LD presence

STEP 3 — Compute scorecards (per templates/deliverables/aimpactscanner-data.schema.json):
- AI Search Readiness scorecard (5 dimensions, 0-10 each, total /50)
- Traditional SEO scorecard (5 dimensions, 0-10 each, total /50)

STEP 4 — Reference prior findings (Constitution rule 1):
- Read seo-evidence.md
- For each notable change since last snapshot, record under prior_findings_referenced in data.json

STEP 5 — Write output:
- Path: runs/YYYY-MM-DD-<site-slug>-weekly-snapshot/data.json
  (where YYYY-MM-DD is today's date, <site-slug> is <SITE> with dots replaced by hyphens)
- Validate the JSON against templates/deliverables/aimpactscanner-data.schema.json
- Set mission.name to "site-audit", mission.mode to "lite", mission.run_directory to the path above
- Set fixes array to TOP 5 highest-ROI fixes only (this is a snapshot, not a full audit)
- Set next_suggested_mission based on dominant gap: "technical-fix" if traditional scorecard worst, "ai-search-optimize" if AI scorecard worst

STEP 6 — Append pointer to seo-evidence.md:
- One line: "<DATE> | weekly-snapshot | <SITE> | data.json: runs/<dir>/data.json | AI: <X>/50, Traditional: <Y>/50, top fix: <title>"

STEP 7 — Commit:
- Branch: routines/weekly-snapshot/<DATE>
- Commit message: "routine(weekly-snapshot): <SITE> <DATE>"
- Open PR titled "Weekly snapshot: <SITE> <DATE>" — auto-merge enabled if checks pass

DO NOT produce analysis.md or marketing.md from this routine — those are monthly. This is data capture only.
```

## Setup notes

- **Repository**: `TheWayWithin/SEO-AGENT`
- **Trigger**: Cron `0 7 * * 1` (Mondays 07:00)
- **Connectors**: Google (for GSC + GA4), Anthropic API for routine execution
- **Estimated runtime**: 5-10 minutes per site
- **Estimated cost per run**: ~$0.10-0.30 (light reads + structured output, no large content generation)

## Output

```
runs/YYYY-MM-DD-<site-slug>-weekly-snapshot/
  data.json
```

Plus one new line appended to `seo-evidence.md`.

PR opened against `main` for human review (or auto-merge if you trust the routine).

## Failure modes

| Failure | Recovery |
|---|---|
| Token stale | Routine opens issue; rotate token; re-run manually for missed week if needed |
| API rate limit | Routine retries once with 60s backoff; if still failing, opens issue |
| Schema validation fails | Routine commits the data.json with a `_validation_error` field and opens issue with diff |
| Site unreachable | Routine writes minimal data.json with `mission.notes` field describing the outage |

## Backfill

If a routine run is missed (e.g. routine paused), trigger manually via `/coord site-audit <SITE> lite` interactively in this repo and tag the resulting `runs/` directory `-weekly-snapshot-backfill` to flag it as catch-up data.
