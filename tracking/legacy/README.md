# Legacy Python Tracking System (Archived 2026-05-11, Sprint 10)

**Status**: Archived. Not part of the active SEO-Agent surface.
**Why archived**: documented as "Complete and Tested" in older docs but never validated end-to-end. `tracking/baselines/` and `tracking/snapshots/` were empty in source — meaning `/track baseline`, `/track compare`, `/track status`, `/track roi`, `/track report` all had defined CLI surfaces but no proven runtime path. Per Jamie's freecalchub field finding (Top 5 #1, captured in `docs/library-improvements-input.md`).

## What's in here

| File | Lines | Defined surface | Validated? |
|---|---|---|---|
| `track.py` | 311 | Main `/track` entry point (config loader, command dispatch) | No |
| `track_cli.py` | 463 | argparse subparsers for `baseline`, `compare`, `roi`, `status`, `report` | No |
| `client_dashboard.py` | — | Client dashboard generation | No |
| `competitive_benchmarking.py` | — | Competitive analysis | No |
| `marketing_automation.py` | — | Marketing automation hooks | No |
| `marketing_generator.py` | — | Marketing content generation | No |
| `presentation_exports.py` | — | PowerPoint/presentation export | No |
| `report_engine.py` | — | Report generation engine | No |
| `report_exports.py` | — | Report format exports | No |
| `report_types.py` | — | Report type definitions | No |
| `test_data.py` | — | Test data generators | No |

## What replaced it

- **`/track baseline` and `/track compare`** — re-implemented in Sprint 9 as agent-prompt commands operating on the `data.json` files produced by `/coord site-audit` runs. Defined in `.claude/commands/track.md` (project root). Validated against freecalchub data 2026-05-11.
- **No replacement for `/track status`, `/track roi`, `/track report`** — these were never validated either. If demand resurfaces, build agent-prompt versions following the Sprint 9 pattern (operate on existing `data.json` and `seo-evidence.md` rather than separate Python state).

## How to revive (if needed)

If a future sprint determines this Python path is worth proving end-to-end:

1. Move files back to `tracking/` (`git mv tracking/legacy/* tracking/` followed by removing this README)
2. Wire `/track` slash command (`.claude/commands/track.md`) to invoke `python3 tracking/track_cli.py <subcommand>`
3. Populate `tracking/baselines/` and `tracking/snapshots/` (likely needs re-implementation of capture path — the existing code may have bit-rotted)
4. End-to-end test on a real site (freecalchub workspace would be the natural choice given existing run data)
5. Update `.claude/commands/track.md` and `tracking/legacy/README.md` to reflect re-validation

## Schemas kept at top level

`tracking/schemas/baseline.schema.json` and other schema files remain at `tracking/schemas/` (NOT moved into legacy). They're still useful as documentation references for the `data.json` shape, even though the Python code that wrote them is archived.

## Templates kept at top level

`tracking/templates/{baseline-template.json, executive-summary.md, before-after.md, case-study-executive.md, weekly-progress.md, marketing-config.yml}` remain at `tracking/templates/`. These are Mustache-style templates that could be useful for future report-generation work; not coupled to the archived Python code.

## Source repo state when archived

- Source SEO-Agent repo: `/Users/jamiewatters/DevProjects/SEOAgent`
- Commit before archive: `03efb2a` (Sprint 9 close)
- Archive date: 2026-05-11
- Archived by: Sprint 10 work session
