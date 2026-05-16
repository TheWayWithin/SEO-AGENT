---
requires_tools: [Bash, WebFetch]
run_top_level: true
---

# CONTENT GAP ANALYSIS MISSION
## Strategic Content Opportunity Discovery

**Duration:** 2-4 hours
**Agents:** @seo-researcher, @seo-content, @seo-strategist, @seo-analyst
**Deliverables:** Content opportunity report, keyword clusters, content calendar, competitive gaps

## MISSION OBJECTIVES

Identify and prioritize content opportunities to:
- Discover untapped keyword opportunities
- Analyze competitive content strategies
- Map content to user journey stages
- Create strategic content roadmap

## PHASE 1: MARKET INTELLIGENCE (45 minutes)
**Lead:** @seo-researcher + @seo-strategist

### Tasks:
- [ ] Conduct comprehensive keyword research
- [ ] Analyze search intent patterns
- [ ] Identify trending topics
- [ ] Map competitive keyword landscape

### Deliverables:
- 500+ keyword opportunities
- Search intent classification
- Trend analysis report
- Competitive keyword matrix

## PHASE 2: CONTENT GAP IDENTIFICATION (60 minutes)
**Lead:** @seo-content + @seo-researcher

### Tasks:
- [ ] Audit existing content coverage
- [ ] Identify topic gaps
- [ ] Analyze content depth requirements
- [ ] Map keyword clusters

### Deliverables:
- Content inventory audit
- Gap analysis matrix
- Topic cluster map
- Content depth recommendations

## PHASE 3: COMPETITIVE INTELLIGENCE (45 minutes)
**Lead:** @seo-strategist + @seo-content

### Tasks:
- [ ] Analyze competitor content strategies
- [ ] Identify competitive advantages
- [ ] Discover differentiation opportunities
- [ ] Evaluate content quality benchmarks

### Deliverables:
- Competitive content analysis
- Differentiation strategy
- Quality benchmark report
- Competitive gap opportunities

## PHASE 4: STRATEGIC PLANNING (30 minutes)
**Lead:** @seo-strategist + @seo-content

### Tasks:
- [ ] Prioritize content opportunities
- [ ] Create content calendar
- [ ] Define resource requirements
- [ ] Establish success metrics

### Deliverables:
- Prioritized opportunity list
- 12-month content calendar
- Resource allocation plan
- KPI framework

## SUCCESS CRITERIA

✅ Comprehensive Discovery:
- 500+ relevant keywords identified
- All major topic gaps discovered
- Competitive landscape mapped

✅ Strategic Alignment:
- Content aligned with business goals
- Clear prioritization framework
- Resource requirements defined

✅ Actionable Output:
- Specific content briefs created
- Clear implementation timeline
- Measurable success metrics

## MISSION DELIVERABLES

### 1. Content Opportunity Report
- Executive summary
- Top 50 content opportunities
- Priority scoring matrix
- Implementation roadmap

### 2. Keyword Cluster Map
- Primary topic clusters
- Supporting keywords
- Search volume data
- Competition analysis

### 3. Content Calendar
- 12-month publication schedule
- Content types and formats
- Topic distribution
- Resource allocation

### 4. Competitive Analysis
- Competitor content strategies
- Gap opportunities
- Differentiation tactics
- Quality benchmarks

## QUALITY CHECKLIST

Before mission completion:
- [ ] All keyword research completed
- [ ] Content gaps identified
- [ ] Competitive analysis thorough
- [ ] Calendar realistic and resourced
- [ ] Success metrics defined
- [ ] Deliverables packaged

## ESCALATION PROTOCOL

If data limitations encountered:
1. Use available data sources
2. Document data gaps
3. Provide confidence levels
4. Recommend data acquisition
5. Adjust scope accordingly

## OUTPUTS (Sprint 5 Deliverable Contract)

Produce named files in a run-scoped directory:

```
runs/YYYY-MM-DD-<domain-slug>-content-gap/
  analysis.md       (REQUIRED) — fill template: templates/deliverables/analysis-report.md
  data.json         (REQUIRED) — validates against: templates/deliverables/aimpactscanner-data.schema.json
  marketing.md      (OPTIONAL) — only when meaningful before/after content performance captured
```

**AI Search lens (Constitution rule 3)**: content gaps include LLM citation gaps — pages where competitors get cited by ChatGPT/Claude/Perplexity but you don't. Score answerability per the AI Search Readiness scorecard in `analysis.md` and `data.json`. Look for question-format heading gaps, missing FAQPage schema, lead-paragraph answer absence.

**Coordinator verification**: confirm required files exist on filesystem before marking mission complete. Append a one-line pointer to this run in `seo-evidence.md` so future missions can read prior findings (Constitution rule 1).

## POST-MISSION ACTIONS

1. Distribute content briefs to writers
2. Set up content tracking system
3. Schedule content reviews
4. Monitor early performance
5. Adjust strategy based on results

---

**Mission Success:** Comprehensive content gap analysis completed with strategic content roadmap for capturing untapped search opportunities.