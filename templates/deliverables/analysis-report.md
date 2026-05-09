# Analysis Report — {{domain}} {{mission}} {{date}}

**Run directory**: `runs/{{date}}-{{domain-slug}}-{{mission}}/`
**Mission mode**: {{mode}}
**Pages assessed**: {{page_count}}
**Constitution rules applied**: 1 (Read before scanning), 2 (Prioritise ROI), 3 (AI Search First), 4 (Minimal diffs)

## Summary

{{2-3 sentences: top finding, total estimated traffic lift if all fixes shipped, biggest risk}}

## Prioritised Fix List

Sort by ROI descending. Highest-impact-lowest-effort fixes at the top.

| # | Fix | Category | Impact (1-10) | Effort (1-10) | ROI | Est. lift | Min-diff? | Owner |
|---|-----|----------|---------------|---------------|-----|-----------|-----------|-------|
| 1 | {{fix description}} | technical / content / authority / ai-search | {{n}} | {{n}} | {{impact/effort}} | {{traffic est}} | yes/no | @seo-{{role}} |
| 2 | … |  |  |  |  |  |  |  |

**Effort scale**: 1 = single tag/line edit. 5 = mid-size refactor of one component. 10 = multi-week project.
**Min-diff?**: yes = changes only the necessary tags/schema (Constitution rule 4). no = touches surrounding code.

## Per-Fix Detail

### Fix #1 — {{title}}

**Why**: {{root cause, one paragraph}}
**Where**: {{file paths, URLs, schema fields affected}}
**Replication**: {{exact steps to verify the issue}}
**Implementation**: {{exact change to make, including code/markup snippets where relevant}}
**Rollback**: {{how to revert if it makes things worse}}
**Evidence**: {{path to evidence in seo-evidence.md or this run directory}}

### Fix #2 — {{title}}

…

## AI Search Readiness Scorecard (Constitution rule 3)

| Dimension | Status | Score | Notes |
|---|---|---|---|
| llms.txt | present / partial / missing | {{n}}/10 | {{}} |
| Structured data coverage | {{n}}% of pages | {{n}}/10 | {{}} |
| Answerability (LLM-friendly headings, FAQ schema, summary blocks) | {{n}}/10 | {{n}}/10 | {{}} |
| Sitemap freshness | {{date}} | {{n}}/10 | {{}} |
| Robots policy for AI crawlers (GPTBot, Claude-User, PerplexityBot, etc.) | allow / block / partial | {{n}}/10 | {{}} |

**AI scorecard total**: {{n}}/50

## Traditional SEO Scorecard

| Dimension | Status | Score | Notes |
|---|---|---|---|
| Core Web Vitals (LCP/INP/CLS) | pass / needs improvement / fail | {{n}}/10 | {{}} |
| Crawlability and indexability | {{n}} indexed / {{n}} blocked | {{n}}/10 | {{}} |
| On-page (titles, descriptions, headings) | {{n}}% complete | {{n}}/10 | {{}} |
| Internal linking | {{n}}/10 | {{n}}/10 | {{}} |
| Authority signals (backlinks, mentions) | DR {{n}} | {{n}}/10 | {{}} |

**Traditional scorecard total**: {{n}}/50

## Risks and Caveats

{{What we couldn't measure, what assumptions were made, what needs confirmation before acting}}

## What Was Re-Used (Constitution rule 1)

Findings from prior runs (read from `seo-evidence.md`) we built on rather than re-discovered:

- {{prior finding 1, with run date}}
- {{prior finding 2}}

## Next Suggested Mission

{{If site-audit reveals AI gaps, point to ai-search-optimize. If technical issues dominate, point to technical-fix. Etc.}}
