# SEO Backlog — {{domain}}

**Last updated**: {{date}} by {{mission}}
**Total items**: {{count}} ({{open count}} open, {{shipped count}} shipped, {{verified count}} verified, {{closed count}} closed)
**Source of truth**: this file is the operational action list. Each row is a discrete fix with stable ID, status, owner, and target metric. Strategic context lives in `seo-roadmap.md`.

---

## Lifecycle states

```
identified → planned → in_progress → shipped → verified → closed
                                          ↓
                                       reverted (rollback)
```

- **identified** — found by an audit/run, not yet scheduled
- **planned** — picked up into the next mission scope; specifics agreed
- **in_progress** — being worked on right now
- **shipped** — change merged/deployed but not yet verified live
- **verified** — confirmed live on the deployed site (sitewide where applicable)
- **closed** — verified AND target metric moved as expected (Constitution rule 5: Prove it)
- **reverted** — shipped but rolled back; reasons in Notes column

## Open items

Sort by ROI descending. Status `closed` and `reverted` move to "Archive" below.

| ID | Title | Category | ROI | Status | Owner | Target metric | Source run | Notes |
|---|---|---|---|---|---|---|---|---|
| FCH-001 | {{example: Add canonical to mortgage calculator}} | technical | 8.0 | identified | @seo-technical | "fix lands on live site" | runs/2026-05-10-…-site-audit-lite | {{}} |
| | | | | | | | | |

## In-flight (status = in_progress)

Items currently being worked. Surface them at the top of every coordinator session.

| ID | Title | Started | Owner | Blocked? | Next action |
|---|---|---|---|---|---|
| | | | | | |

## Recently shipped (awaiting verification)

Status = shipped. These need a sitewide verify pass before moving to verified.

| ID | Title | Shipped | Verification needed | Verifier |
|---|---|---|---|---|
| | | | {{e.g. "all 110 pages have canonical"}} | @seo-technical |

## Recently verified (awaiting impact measurement)

Status = verified. Need a `/track compare` cycle to confirm metric movement before closing.

| ID | Title | Verified | Target metric | Compare baseline | Compare against |
|---|---|---|---|---|---|
| | | | | runs/<date>/data.json | next snapshot |

## Archive (closed and reverted items)

Closed items stay in the file as historical record (Constitution rule 1 — re-use prior findings).

### Closed

| ID | Title | Closed | Outcome | Run that closed it |
|---|---|---|---|---|
| | | | | |

### Reverted

| ID | Title | Reverted | Reason | Lesson |
|---|---|---|---|---|
| | | | | |

## Item ID convention

`{{SITE-CODE}}-{{N}}` where SITE-CODE is a stable 3-4 letter abbreviation:
- `FCH` for freecalchub.com
- `ASM` for aisearchmastery.com
- `LTM` for llmtxtmastery.com
- `AIS` for aisearcharena
- etc.

N is sequential, never reused, never renumbered. Closed items keep their ID forever.

## How missions read/write this file

- **`/coord site-audit`**: reads existing IDs to avoid duplicates; appends new identified items from the audit's fix list; never moves status forward
- **`/coord technical-fix`**: reads identified/planned items in scope; moves them through in_progress → shipped; never closes (closing requires verification + impact measurement)
- **`/coord` sitewide-verify** (when added): moves shipped → verified
- **`/track compare`**: when target metric movement is confirmed, moves verified → closed

## Reading this file (for the human)

If you only have 60 seconds:
- Open items table sorted top = highest ROI work to do next
- In-flight table = check for stalled work
- Recently shipped = needs verification love
- Recently verified = needs `/track compare` to close

If you have 10 minutes, also scan the archive for patterns (categories that close fast, categories that revert often).
