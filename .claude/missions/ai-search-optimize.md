---
requires_tools: [Bash, WebFetch]
run_top_level: true
---

# AI SEARCH OPTIMIZATION MISSION
## Future-Ready AI Search Infrastructure & Content Strategy

**Duration:** 1-3 days
**Agents:** @seo-strategist, @seo-content, @seo-technical, @seo-researcher
**Deliverables:** Complete llms.txt implementation, AI-optimized content library, technical AI search infrastructure, monitoring dashboard

## CONTEXT (Constitution rule 1)

Check `seo-evidence.md` for prior llms.txt findings, AI-search audits, and schema work on this site before starting. Capture new findings back to `seo-evidence.md` as you go.

## MISSION OBJECTIVES

Optimize for AI-powered search experiences to:
- Implement comprehensive llms.txt framework
- Create AI-discoverable content architecture  
- Establish AI search monitoring systems
- Future-proof SEO strategy for AI search evolution

## PHASE 1: AI SEARCH ANALYSIS (4 hours)
**Lead:** @seo-strategist + @seo-researcher

### Tasks:
- [ ] Analyze current AI search visibility
- [ ] Research AI search behavior patterns
- [ ] Identify AI crawler requirements
- [ ] Map AI search opportunities
- [ ] Assess competitive AI optimization

### Deliverables:
- AI search landscape analysis
- Crawler behavior assessment
- Opportunity identification matrix
- Competitive AI positioning report
- Strategic framework document

## PHASE 2: LLMS.TXT IMPLEMENTATION (6 hours)
**Lead:** @seo-content + @seo-technical

### llms.txt Specification (current best practice)

`llms.txt` is a markdown file at site root that tells LLM crawlers what content the site offers and how to use it. Two-file pattern:

- `/llms.txt` — index file: site name (H1), 1-paragraph summary, then markdown links to key resources organised in sections like `## Docs`, `## Examples`, `## Optional`
- `/llms-full.txt` — full concatenated content of all linked resources, single document, no JS-required content

**Format requirements**:
- Plain markdown, parseable by any LLM
- H1 = site name on first line (no preamble)
- Blockquote summary line
- Sections use H2 with markdown lists of `[Title](URL): description`
- Keep `Optional` section for low-priority links — LLMs with limited context skip it

### Tasks:
- [ ] Audit existing `/llms.txt` and `/llms-full.txt` (curl + visual inspection)
- [ ] Draft or rewrite `/llms.txt` per spec above (site name, summary, sectioned link list)
- [ ] Generate `/llms-full.txt` by concatenating linked resources
- [ ] Verify both files are served as `text/plain` or `text/markdown` with no auth wall
- [ ] Validate links resolve (no 404s, no JS-required pages)

### Deliverables:
- Production-ready `/llms.txt` (under 2,000 tokens; sections clearly labelled)
- `/llms-full.txt` companion (full content, no JS dependencies)
- Validation report: which AI crawlers can fetch and parse the files

## PHASE 3: TECHNICAL INFRASTRUCTURE (4 hours)
**Lead:** @seo-technical + @seo-content

### AI Crawler Policy (robots.txt)

Audit and configure directives for the AI crawlers that matter:

| User-agent | Operator | Common policy |
|---|---|---|
| `GPTBot` | OpenAI (ChatGPT training + search) | Allow if you want to be in ChatGPT answers |
| `ChatGPT-User` | OpenAI (ChatGPT browsing on user request) | Almost always allow |
| `OAI-SearchBot` | OpenAI (SearchGPT index) | Allow for SearchGPT visibility |
| `Claude-User` | Anthropic (Claude browsing) | Almost always allow |
| `ClaudeBot` | Anthropic (training crawler) | Allow if you want to be in Claude's training set |
| `PerplexityBot` | Perplexity (citations) | Allow for Perplexity citation visibility |
| `Perplexity-User` | Perplexity (browsing) | Allow |
| `Google-Extended` | Google (Gemini, Bard training) | Separate from Googlebot — explicit decision needed |
| `CCBot` | Common Crawl (broad training data) | Allow if you want indirect inclusion in many models |
| `anthropic-ai`, `cohere-ai` | Various | Edge-case, usually allow |

For SEO-Agent recommendations: default ALLOW unless the site has a specific reason to block (e.g. paywalled premium content). Blocking AI crawlers reduces visibility in AI-mediated discovery — usually a worse trade than the training-data concern.

### Structured data priorities for AI

LLMs lean on structured data for confident citations. Priority order:

1. **`Organization`** + **`WebSite`** — site identity (always)
2. **`Article` / `BlogPosting`** with `author`, `datePublished`, `dateModified` — provenance
3. **`FAQPage`** — direct LLM lift candidate (one Q+A becomes one citation)
4. **`HowTo`** — step-by-step extraction
5. **`BreadcrumbList`** — site hierarchy
6. **`Product` / `Service`** — commercial intent
7. **`Person`** for author bios — E-E-A-T signal LLMs honour

### Tasks:
- [ ] Audit `/robots.txt` against the AI crawler table above; document current policy and rationale
- [ ] Add explicit Allow/Disallow per AI crawler with comments explaining the choice
- [ ] Run JSON-LD audit across 5-10 representative URLs; identify schema coverage gaps
- [ ] Implement priority schema (1-3 above) on pages that lack them
- [ ] Verify schema with Google Rich Results Test AND with a direct LLM fetch (paste URL into Claude/ChatGPT and check what's extracted)
- [ ] Confirm sitemap.xml is fresh (last 7 days) and ai-discoverable (linked from /robots.txt)

### Deliverables:
- Updated `/robots.txt` with AI crawler policy comments
- Schema implementation report: pages updated, schema types added, validation status
- AI crawler accessibility report: which crawlers can reach which content
- Sitemap freshness confirmation

## PHASE 4: CONTENT STRATEGY — ANSWERABILITY (6 hours)
**Lead:** @seo-content + @seo-researcher

### Answerability patterns (why LLMs cite some pages and not others)

LLMs lift content that is structurally easy to extract. The pattern that wins:

1. **Question-format headings** — H2/H3 phrased as the question a user would type. "How do I calculate BMI?" beats "BMI Calculation Method".
2. **Short paragraph answer FIRST** — 1-3 sentences directly under the heading, before any deep explanation. LLMs grab the lead paragraph; if your answer is buried after 600 words of preamble, it gets skipped.
3. **Definition blocks** — for any term, a `<dl>` or bolded inline definition near the first use. LLMs love structured definitions.
4. **TL;DR / Summary blocks** — a labelled summary at the top of long articles. Usually the LLM's citation source.
5. **FAQPage schema** — every Q+A becomes a discrete extraction unit. Worth implementing even on pages that aren't traditionally "FAQ".
6. **Stable URLs and stable content** — LLMs cite pages they've seen multiple times. Don't break URLs; don't rewrite the canonical answer.
7. **Single concrete answer per page** — multi-topic pages confuse extraction. Split into focused pages where possible.

### Tasks:
- [ ] Audit top 10 pages by traffic for answerability score (1-10 per page based on patterns above)
- [ ] Identify the 5 pages with highest traffic + lowest answerability — these are the highest-ROI content fixes
- [ ] Rewrite each: question-format heading, lead-paragraph answer, FAQPage schema where relevant
- [ ] Add TL;DR blocks to articles over 800 words
- [ ] Convert procedural content to HowTo schema
- [ ] Create content template: question-heading, lead-answer, deep-detail, schema markup — to enforce the pattern on new content

### Deliverables:
- Answerability audit (top 10 pages, scored)
- Rewritten lead-paragraph answers for top 5 fix candidates (before/after side-by-side)
- FAQPage / HowTo schema additions per page
- Content template enforcing answerability for future writing

## PHASE 5: MONITORING SETUP (4 hours)
**Lead:** @seo-analyst + @seo-technical

### Tasks:
- [ ] Set up AI search performance tracking
- [ ] Configure AI crawler monitoring
- [ ] Implement AI visibility dashboards
- [ ] Create AI search alerting system
- [ ] Establish AI performance baselines

### Deliverables:
- AI search monitoring dashboard
- Crawler behavior tracking system
- Performance alert configuration
- Baseline metrics report
- Monitoring maintenance guide

## SUCCESS CRITERIA

✅ Technical Implementation:
- Complete llms.txt file deployed
- AI crawler accessibility verified
- Semantic markup implemented
- Performance baselines established

✅ Content Optimization:
- AI-friendly content formats created
- Conversational content templates ready
- Semantic clustering implemented
- FAQ structures optimized

✅ Monitoring Foundation:
- AI search tracking configured
- Performance dashboards active
- Alert systems functional
- Baseline metrics captured

## QUALITY CHECKLIST

Before mission completion:
- [ ] llms.txt file validated and deployed
- [ ] AI content formats tested
- [ ] Technical infrastructure verified
- [ ] Monitoring systems operational
- [ ] Performance baselines established
- [ ] Documentation complete

## ESCALATION PROTOCOL

If technical limitations encountered:
1. Document current AI search capabilities
2. Implement available optimizations
3. Create future enhancement roadmap
4. Establish monitoring for new features
5. Schedule regular capability reviews

## OUTPUTS (Sprint 5 Deliverable Contract)

Produce named files in a run-scoped directory:

```
runs/YYYY-MM-DD-<domain-slug>-ai-search-optimize/
  analysis.md       (REQUIRED) — fill template: templates/deliverables/analysis-report.md
  data.json         (REQUIRED) — validates against: templates/deliverables/aimpactscanner-data.schema.json
  marketing.md      (OPTIONAL) — AI search wins are slow to materialise; produce only when llms.txt crawler engagement or AI-referral traffic data is available
```

**AI Search Readiness Scorecard** is the headline section of `analysis.md` for this mission — emphasise llms.txt status, structured data coverage, answerability, and AI crawler policy. The traditional SEO scorecard is secondary here.

**Coordinator verification**: confirm required files exist on filesystem before marking mission complete. Append a one-line pointer to this run in `seo-evidence.md` so future missions can read prior findings (Constitution rule 1).

## POST-MISSION ACTIONS

1. Monitor AI search performance metrics
2. Track llms.txt crawler engagement
3. Analyze AI content consumption patterns
4. Refine optimization strategies
5. Plan iterative improvements

---

**Mission Success:** Comprehensive AI search optimization completed with future-ready infrastructure, content strategy, and monitoring systems for emerging AI search technologies.