# SITE AUDIT MISSION
## Comprehensive SEO Analysis & Action Plan

**Duration:** 60 minutes
**Agents:** @seo-strategist, @seo-technical, @seo-content, @seo-analyst
**Deliverables:** Executive summary, technical audit, content audit, action plan

## MISSION OBJECTIVES

Conduct a comprehensive SEO audit to:
- Assess current SEO health and performance
- Identify critical issues and opportunities
- Provide prioritized action plan
- Establish performance baselines

## PHASE 1: INITIAL ASSESSMENT (15 minutes)
**Lead:** @seo-strategist + @seo-analyst

### Tasks:
- [ ] Analyze business context and goals
- [ ] Review current SEO strategy
- [ ] Assess competitive landscape
- [ ] Establish baseline metrics

### Deliverables:
- Business context analysis
- Current state assessment
- Competitive positioning
- Baseline performance metrics

## PHASE 2: TECHNICAL ANALYSIS (20 minutes)
**Lead:** @seo-technical + @seo-analyst

### Tasks:
- [ ] Audit Core Web Vitals performance
- [ ] Check crawlability and indexability
- [ ] Evaluate site architecture
- [ ] Assess mobile optimization
- [ ] Review technical SEO elements

### Deliverables:
- Technical audit report
- Core Web Vitals scores
- Crawl error analysis
- Mobile optimization assessment
- Technical issue prioritization

## PHASE 3: CONTENT REVIEW (15 minutes)
**Lead:** @seo-content + @seo-researcher

### Tasks:
- [ ] Analyze content quality and depth
- [ ] Identify content gaps
- [ ] Review on-page optimization
- [ ] Assess internal linking
- [ ] Evaluate keyword targeting

### Deliverables:
- Content audit report
- Content gap analysis
- On-page optimization opportunities
- Internal linking recommendations
- Keyword optimization plan

## PHASE 4: PERFORMANCE SYNTHESIS (10 minutes)
**Lead:** @seo-analyst + @seo-strategist

### Tasks:
- [ ] Consolidate findings
- [ ] Prioritize recommendations
- [ ] Create action plan
- [ ] Define success metrics
- [ ] Prepare executive summary

### Deliverables:
- Executive summary
- Prioritized action plan
- Quick win opportunities
- Timeline and resource needs
- Success metrics framework

## SUCCESS CRITERIA

✅ Comprehensive Coverage:
- All critical SEO areas assessed
- No major issues overlooked
- Complete baseline established

✅ Actionable Insights:
- Clear prioritization provided
- Specific recommendations given
- Resource requirements defined

✅ Business Alignment:
- Recommendations align with goals
- ROI potential identified
- Strategic opportunities highlighted

## OUTPUTS (Sprint 5 Deliverable Contract)

Produce three named files in a run-scoped directory:

```
runs/YYYY-MM-DD-<domain-slug>-site-audit[-<mode>]/
  analysis.md       (REQUIRED) — fill template: templates/deliverables/analysis-report.md
  marketing.md      (REQUIRED) — fill template: templates/deliverables/marketing-report.md
  data.json         (REQUIRED) — validates against: templates/deliverables/aimpactscanner-data.schema.json
```

Phase deliverables (executive summary, technical audit, content audit, action plan) are now sections WITHIN `analysis.md`, not standalone files.

**AI Search lens (Constitution rule 3)**: both AI Search Readiness AND Traditional SEO scorecards required in `analysis.md` and `data.json`. The schema enforces this — `data.json` will fail validation if the AI scorecard is missing.

**Backlog integration (Sprint 9)**:
- READ `seo-backlog.md` before producing the fix list (Constitution rule 1 — don't re-identify items already tracked)
- For each NEW finding not already in the backlog: append to `seo-backlog.md` under "Open items" with status=`identified`, stable ID, source run reference
- For findings that match existing backlog items: cross-reference the ID in `analysis.md` rather than creating a duplicate

**Roadmap touch (Sprint 9)**:
- READ `seo-roadmap.md` if it exists; tag each fix in analysis.md with the roadmap theme it supports (or "no theme" if none applies)
- Update the "Current state" section of `seo-roadmap.md` with this run's scorecards and open backlog count
- Do NOT rewrite themes or strategic objectives — those are quarterly/strategic

**Coordinator verification**: confirm all three files exist on filesystem before marking mission complete. Append a one-line pointer to this run in `seo-evidence.md` so future missions can read prior findings (Constitution rule 1).

## QUALITY CHECKLIST

Before mission completion:
- [ ] All phases completed
- [ ] Deliverables reviewed
- [ ] Data validated
- [ ] Recommendations actionable
- [ ] Executive summary clear
- [ ] Next steps defined

## ESCALATION PROTOCOL

If blocked or delayed:
1. Attempt alternative data sources
2. Focus on available information
3. Document limitations
4. Provide partial recommendations
5. Schedule follow-up if needed

## POST-MISSION ACTIONS

1. Package all deliverables
2. Create implementation timeline
3. Schedule follow-up review
4. Track implementation progress
5. Measure impact metrics

---

**Mission Success:** Comprehensive SEO audit completed with clear, prioritized action plan for improving search visibility and performance.