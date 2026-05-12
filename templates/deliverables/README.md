# Mission Deliverables

Every SEO mission produces named deliverables in a run-scoped directory. No free-form prose dumped in a chat reply — concrete files at predictable paths.

## The deliverables

### Per-run deliverables (in `runs/<date>-<domain>-<mission>/`)

| Deliverable | Filename | Format | Purpose |
|---|---|---|---|
| Analysis Report | `analysis.md` | Markdown | Prioritised fix list with ROI, effort, expected lift. The "what to do" doc. |
| Marketing Report | `marketing.md` | Markdown | Before/after framing suitable for case studies, blog posts, social. The "what to tell people" doc. |
| AImpactScanner Data | `data.json` | JSON (validates against `aimpactscanner-data.schema.json`) | Structured ingestion file. The "what the dashboard reads" file. |
| Comparison Report | `comparison.md` | Markdown (when applicable) | Delta between two snapshots. Produced by `/track compare` and by missions that re-baseline. |

### Per-site persistent deliverables (in workspace root, updated across runs)

| Deliverable | Filename | Format | Purpose |
|---|---|---|---|
| SEO Roadmap | `seo-roadmap.md` | Markdown | Strategic, longer-lived view of where SEO is heading for this site. Refreshed quarterly or on strategic shifts. |
| SEO Backlog | `seo-backlog.md` | Markdown | Operational action list with stable item IDs and lifecycle states. Updated by every mission. |
| SEO Evidence | `seo-evidence.md` | Markdown | Rolling artefact store + run pointers. Constitution rule 1: read before scanning. |

## Per-mission deliverable subset

| Mission | analysis.md | marketing.md | data.json |
|---|---|---|---|
| `site-audit` | required | required | required |
| `content-gap` | required | optional (when before/after captured) | required |
| `technical-fix` | required | optional (when before/after captured) | required |
| `ai-search-optimize` | required | optional | required |

`marketing.md` is optional where there is no meaningful before/after to compare. Missions that only produce required files do not create the optional ones — no empty placeholders.

## Run directory convention

All three files land in:

```
runs/YYYY-MM-DD-<domain-slug>-<mission>[-<mode>]/
```

Examples:

```
runs/2026-05-09-freecalchub-site-audit-lite/
  analysis.md
  marketing.md
  data.json
runs/2026-05-09-freecalchub-content-gap/
  analysis.md
  data.json
```

`<domain-slug>` is the domain with dots replaced by hyphens (`freecalchub-com`) or just the hostname stem (`freecalchub`). Choose readable.

`<mode>` is included only when the mission was run in a non-default mode (`lite`, `full`, `deep`).

Ad-hoc evidence files (screenshots, raw API responses, crawl exports) sit alongside in the same run directory.

## Contract obligations

The mission file is the contract. Each SEO mission's `## OUTPUTS` section names the required deliverables and the run directory. The coordinator verifies all required files exist on the filesystem after the run; missing files = mission incomplete, do not mark the run done.

The seo-evidence.md file (Constitution rule 1) accumulates a pointer to each completed run's analysis.md so future missions can read prior findings.

## Templates

- `analysis-report.md` — markdown structure agents fill in
- `marketing-report.md` — markdown structure agents fill in
- `aimpactscanner-data.schema.json` — JSON Schema agents validate `data.json` against; reuses and extends `tracking/schemas/baseline.schema.json` with AI-readiness fields

## Why this exists

Constitution rule 5 — Prove it. Constitution rule 2 — Prioritise ROI. Free-form mission output buries the answer; structured deliverables surface it. The `/track` system can ingest `data.json` over time to show trends; the dashboard can render it; the marketer can lift `marketing.md`; the operator can work the prioritised `analysis.md` list.
