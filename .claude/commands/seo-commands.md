---
name: seo-commands
description: SEO-specific command suite for rankings, traffic, technical health, and reporting
---

# SEO COMMAND SUITE 📊

**Available Commands**: `/rankings`, `/traffic-report`, `/technical-health`, `/report`

## COMMAND: /rankings

**Command**: `/rankings [domain] [keyword-group]`
**Purpose**: Check current keyword ranking positions
**Arguments Provided**: $ARGUMENTS

### EXECUTION PROTOCOL

**Command Parsing**:
1. **Domain** (required) - Target domain for ranking analysis
2. **Keyword Group** (optional) - Specific keyword set or "all" for comprehensive check

**If No Arguments Provided**:
- Request domain input interactively
- Ask for keyword group preference (branded, commercial, informational, or all)
- Confirm scope before proceeding

**Immediate Delegation to @seo-analyst**:
```
@seo-analyst Execute comprehensive keyword ranking analysis for [domain].

Requirements:
- Fetch current positions for [keyword-group] keywords
- Include ranking change trends (week/month comparisons)
- Identify SERP features captured or lost
- Flag ranking volatility or significant changes
- Calculate average position and visibility metrics

Deliver results in table format:
| Keyword | Current Position | Change (7d) | Change (30d) | URL | SERP Features |

Include executive summary with:
- Total keywords tracked
- Ranking improvements/declines
- SERP feature opportunities
- Priority keywords needing attention
```

**Error Handling**:
- If ranking data unavailable: Document limitations and suggest alternative tracking setup
- If domain not verified: Provide verification requirements through @coordinator
- If keyword data insufficient: Recommend keyword research expansion

---

## COMMAND: /traffic-report

**Command**: `/traffic-report [period] [domain]`  
**Purpose**: Generate comprehensive traffic analysis report
**Arguments Provided**: $ARGUMENTS

### EXECUTION PROTOCOL

**Command Parsing**:
1. **Period** (required) - Analysis timeframe: "weekly", "monthly", "quarterly", "ytd"
2. **Domain** (required) - Target domain for traffic analysis

**If Insufficient Arguments**:
- Request period selection (default: monthly)
- Request domain input
- Confirm analytics access availability

**Immediate Delegation to @seo-analyst**:
```
@seo-analyst Generate comprehensive traffic analysis report for [domain] covering [period] period.

Analytics Requirements:
- Sessions, users, pageviews with period-over-period comparison
- Organic traffic breakdown by device, geography, source
- Conversion metrics: goals, transactions, revenue attribution
- User engagement: bounce rate, session duration, pages per session
- Landing page performance with traffic distribution

Report Sections Required:
1. Executive Summary - Key metrics and trends
2. Traffic Performance - Detailed analytics breakdown  
3. Conversion Analysis - Goal completion and revenue tracking
4. User Behavior - Engagement patterns and flows
5. Recommendations - Data-driven optimization opportunities

Deliver formatted report with visualizations and actionable insights.
```

**Error Handling**:
- If GA4 access unavailable: Document requirements and setup guidance
- If data discrepancies detected: Flag data quality issues and provide confidence intervals
- If conversion tracking missing: Recommend tracking implementation

---

## COMMAND: /technical-health

**Command**: `/technical-health [domain]`
**Purpose**: Quick technical SEO health check
**Arguments Provided**: $ARGUMENTS

### EXECUTION PROTOCOL

**Command Parsing**:
1. **Domain** (required) - Target domain for technical assessment

**If No Domain Provided**:
- Request domain input interactively
- Confirm crawl access and permissions
- Set expectations for scan depth

**Immediate Delegation to @seo-technical**:
```
@seo-technical Execute comprehensive technical SEO health assessment for [domain].

Technical Audit Scope:
- Core Web Vitals performance (LCP, INP, CLS, FID)
- Mobile-first indexing readiness
- Crawlability and indexability status
- HTTPS implementation and security headers
- Schema markup validation
- XML sitemap and robots.txt analysis

Critical Health Indicators:
- Page load speed and performance metrics
- Mobile optimization score
- Indexable pages vs. blocked pages
- Technical errors and crawl issues
- Structured data coverage and validation

Deliver health score dashboard with:
- Overall technical health score (0-100)
- Priority issues requiring immediate attention
- Performance benchmarks vs. industry standards
- Improvement roadmap with impact estimates
```

**Error Handling**:
- If website access restricted: Document access requirements and provide alternative analysis methods
- If technical tools fail: Use fallback diagnostic approaches and document limitations
- If critical issues detected: Escalate urgent problems requiring immediate attention

---

## COMMAND: /report

**Command**: `/report [weekly|monthly] [domain]`
**Purpose**: Automated comprehensive SEO reporting
**Arguments Provided**: $ARGUMENTS

### EXECUTION PROTOCOL

**Command Parsing**:
1. **Frequency** (required) - Report type: "weekly" or "monthly"
2. **Domain** (required) - Target domain for comprehensive analysis

**If Insufficient Arguments**:
- Request report frequency selection
- Request domain input
- Confirm stakeholder requirements and distribution list

**Multi-Agent Orchestration**:

**Phase 1 - Performance Analysis**:
```
@seo-analyst Generate performance metrics summary for [domain] [frequency] report.

Required Metrics:
- Organic traffic trends and growth patterns
- Keyword ranking performance and volatility
- Conversion metrics and revenue attribution
- User engagement and behavior analysis
- Competitive benchmark positioning
```

**Phase 2 - Technical Assessment** (Monthly only):
```
@seo-technical Conduct technical health assessment for [domain] monthly report.

Technical Metrics Required:
- Core Web Vitals performance status
- Technical SEO score and improvement trends
- Mobile optimization and indexing status
- Critical technical issues requiring attention
```

**Phase 3 - Report Compilation**:
```
@seo-analyst Compile comprehensive SEO report combining all specialist findings.

Executive Summary Requirements:
- Key performance highlights and concerns
- Strategic recommendations with priority ranking
- Action items for next period with owners
- ROI analysis and investment recommendations

Report Structure:
1. Executive Summary (1 page)
2. Performance Overview (traffic, rankings, conversions)
3. Technical Health Status (monthly reports only)
4. Recommendations and Action Items
5. Appendices (detailed metrics and methodologies)
```

**Weekly Report Focus**:
- Performance trends and alerts
- Ranking changes and opportunities  
- Quick wins and immediate actions
- Progress tracking on ongoing initiatives

**Monthly Report Focus**:
- Comprehensive performance analysis
- Technical health assessment
- Strategic recommendations
- Competitive intelligence updates
- ROI analysis and forecasting

**Error Handling**:
- If data access limited: Document gaps and provide partial report with limitations noted
- If agent coordination fails: Retry with individual specialist reports and manual compilation
- If report generation times out: Provide preliminary findings with completion timeline

---

## COMMAND COORDINATION RULES

**Delegation Protocol**:
- ALL technical work delegated to appropriate SEO specialists
- NEVER implement changes directly - always use @specialist syntax
- WAIT for specialist responses before proceeding
- Document all delegated tasks and completion status

**Error Escalation**:
- Data access issues → @coordinator for resource coordination  
- Technical implementation conflicts → @seo-technical for resolution
- Strategic questions → @seo-strategist through @coordinator
- Cross-specialist coordination → @coordinator for orchestration

**Quality Standards**:
- All reports include confidence levels and data sources
- Technical assessments provide specific implementation guidance
- Performance analysis includes actionable recommendations
- Error handling maintains data integrity and user experience

## SPECIALIST DELEGATION EXAMPLES

**Correct Delegation**:
```
@seo-analyst Execute ranking analysis now for example.com...
[Wait for response and results]
```

**Incorrect Approach**:
```
Will ask @seo-analyst to analyze rankings when ready
[No immediate action or delegation]
```

Remember: These commands orchestrate SEO specialists for comprehensive analysis and reporting. Always delegate immediately and wait for specialist completion before proceeding to next steps.