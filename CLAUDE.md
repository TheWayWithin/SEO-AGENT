# CLAUDE.md — SEO-Agent (product layer)

This file is the SEO Constitution. Five behavioural rules for any SEO work in this repo. Framework rules (Karpathy constitution, mission routing, tracking-file protocols, MCP, hooks, security) live in `.claude/CLAUDE.md`. Read both.

## The Five Rules (SEO Constitution)

1. **Read before scanning.** Check `seo-evidence.md` and Google Search Console data before crawling. Do not re-scrape what you already know.
2. **Prioritise ROI.** Do not recommend a hard technical fix when a content update yields more traffic for less effort. Compare cost-to-fix against estimated traffic impact in every recommendation.
3. **AI Search First.** Evaluate every change against LLM ingestion (llms.txt readiness, structured data, answerability) alongside traditional Google bots. Both scorecards in every output.
4. **Minimal diffs.** When fixing SEO issues in code, change only the necessary tags or schema. Do not refactor surrounding components.
5. **Prove it.** Run `/track baseline` before any change set, `/track compare` after. No claim of improvement without evidence in `seo-evidence.md`.

## Two layers in this repo

| Layer | What | Where |
|---|---|---|
| Agent-11 (framework) | Generic dev squad we use to build SEO-Agent | `.claude/agents/{analyst,architect,coordinator,…}.md` (framework agents), `/missions/mission-*.md`, `/templates/` (non-seo), `/field-manual/`, `/gates/`, `/schemas/`. Refresh via `bash install.sh --upgrade` |
| SEO-Agent (product) | The SEO suite we deploy | `.claude/agents/seo-*.md`, `.claude/missions/{site-audit,content-gap,technical-fix,ai-search-optimize}.md`, `templates/deliverables/*`, `templates/seo-evidence-template.md`, `.claude/commands/{seo-commands,track,tracking-commands}.md`, `runs/` (mission output) |

Sprint work targets the product layer only. Treat the framework as a dependency.

## SEO-Agent product files

- **Agents** (7, in `.claude/agents/`): seo-strategist, seo-coordinator, seo-technical, seo-content, seo-researcher, seo-analyst, seo-builder
- **Missions** (4, in `.claude/missions/`): site-audit, content-gap, technical-fix, ai-search-optimize
- **Deliverable templates** (in `templates/deliverables/`): `analysis-report.md`, `marketing-report.md`, `aimpactscanner-data.schema.json`
- **Run output**: every mission writes to `runs/YYYY-MM-DD-<domain>-<mission>[-<mode>]/` containing `analysis.md` + `data.json` (always) + `marketing.md` (when before/after captured)
- **Tracking files**: `seo-evidence.md` for SEO artefacts and audit history (Constitution rule 1)

## Mission dispatch

`/coord <mission> [mode] [target]` — positional args, no NLP. Examples:
- `/coord site-audit lite freecalchub.com/calculators`
- `/coord ai-search-optimize freecalchub.com`
- `/coord content-gap freecalchub.com/calculators/bmi-calculator`

Mission must be one of the four SEO missions or a framework mission. Full routing table in `.claude/commands/coord.md`.

## SEO-specific commands

- `/track baseline` — set baseline before changes (rule 5)
- `/track compare` — diff vs baseline (rule 5)
- `/track status` — system and performance overview
- `/track roi` — ROI metrics
- `/track report --type weekly|monthly|roi` — generate report
- `/seo-commands` — `/rankings`, `/traffic-report`, `/technical-health`, `/report`
- `/tracking-commands` — tracking helper reference

## SEO routines (Mode C — operational)

Recurring SEO work runs as Claude Code Routines on Anthropic-managed cloud, not local cron. Templates in `routines/`:

- `weekly-snapshot.md` — Mondays 07:00 → `runs/<date>-<site>-weekly-snapshot/data.json`
- `monthly-report.md` — 1st of month 08:00 → full deliverable set (analysis + marketing + data)

Set up at `claude.ai/code/routines`. See `routines/README.md` for the pattern.

## Framework rules

`.claude/CLAUDE.md` covers the Karpathy constitution, mission routing via `/coord`, tracking-file protocols, MCP tool discovery, hooks, security. Defer to it for anything not SEO-specific.
