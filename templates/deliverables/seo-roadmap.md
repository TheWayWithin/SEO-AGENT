# SEO Roadmap — {{domain}}

**Owner**: {{site owner / team}}
**Last reviewed**: {{date}}
**Cadence**: review quarterly; update when strategic shifts happen
**Source of truth**: this file is the longer-lived strategic view of where SEO for {{domain}} is heading. Day-to-day operational work lives in `seo-backlog.md`.

---

## Current state

**Last full audit**: {{date}} (`runs/{{run-dir}}/`)
**AI Search Readiness scorecard**: {{n}}/50
**Traditional SEO scorecard**: {{n}}/50
**Open backlog items**: {{count}} (see `seo-backlog.md`)

## Strategic objectives (this quarter)

Pick 1-3 themes. Each has a target metric and a deadline. No more — themes proliferate, focus dies.

### Theme 1 — {{name}}
- **Why**: {{single-sentence rationale tied to business value}}
- **Target metric**: {{specific number, e.g. "organic sessions +25% by Q3 close"}}
- **Owning lever**: {{which Constitution rule or content/tech category drives this}}
- **Deadline**: {{date}}
- **Backlog items contributing**: {{ID list from seo-backlog.md}}

### Theme 2 — {{name}}

…

## Constraints

What we are NOT doing this quarter, and why. Equally important to the themes.

- {{thing we're not doing}} — {{reason}}

## Long-running initiatives (multi-quarter)

Things that span multiple quarters and need explicit tracking even when no immediate action is happening.

| Initiative | Started | Target close | Status | Notes |
|---|---|---|---|---|
| {{e.g. llms.txt v2 migration}} | {{date}} | {{date}} | {{planning / in-flight / paused}} | {{}} |

## Risk register

| Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|
| {{e.g. AI crawler policy change}} | {{low/med/high}} | {{low/med/high}} | {{}} | {{}} |

## Recent retros

Each entry: what theme, what we learned, what changed in the roadmap.

### {{date}} — {{theme}}
- **What we learned**: {{}}
- **Roadmap change**: {{}}

## How this file relates to the rest of SEO-Agent

- **`seo-evidence.md`** — accumulates findings across runs (Constitution rule 1 — read before scanning)
- **`seo-backlog.md`** — operational action list; each item maps to one or more roadmap themes
- **`runs/`** — dated mission outputs; the source data for everything above
- **`tracking/baselines/`** — point-in-time snapshots used for `/track compare`

## Maintenance

Regenerate or update this file:
- After every full `site-audit` (refresh "Current state" + audit the backlog)
- After every quarterly review (refresh themes; archive closed initiatives to "Recent retros")
- When a strategic shift happens (new product launch, pivot, deprecation)

Do NOT regenerate after every routine snapshot or technical-fix — those update `seo-backlog.md` and `seo-evidence.md` only.
