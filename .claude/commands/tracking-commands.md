# SEO TRACKING COMMANDS

Execute tracking operations for baseline capture, progress monitoring, and ROI measurement.

## COMMAND REFERENCE

### /track baseline
**Purpose**: Capture initial performance state for a domain
**Syntax**: `/track baseline [domain] [scope]`
**Parameters**:
- `domain`: Target domain (e.g., example.com)
- `scope`: full|technical|content|rankings (default: full)

**Execution Flow**:
1. Parse domain and scope parameters
2. Delegate to @seo-analyst for metrics collection
3. Store baseline in `/tracking/baselines/YYYY-MM-DD_domain_baseline.json`
4. Return confirmation with key metrics summary

**Example**:
```bash
/track baseline freecalchub.com full
```

---

### /track snapshot
**Purpose**: Record current performance metrics
**Syntax**: `/track snapshot [domain] [type]`
**Parameters**:
- `domain`: Target domain
- `type`: daily|weekly|monthly|mission (default: daily)

**Execution Flow**:
1. Validate tracking configuration exists
2. Delegate to appropriate agents for data collection:
   - @seo-technical for technical metrics
   - @seo-analyst for traffic and rankings
   - @seo-content for content metrics
3. Store snapshot with timestamp
4. Compare with previous snapshot if available

**Example**:
```bash
/track snapshot freecalchub.com weekly
```

---

### /track compare
**Purpose**: Generate before/after comparison report
**Syntax**: `/track compare [domain] [start_date] [end_date]`
**Parameters**:
- `domain`: Target domain
- `start_date`: Baseline or start date (YYYY-MM-DD)
- `end_date`: Comparison date (default: today)

**Execution Flow**:
1. Load baseline and target snapshots
2. Calculate percentage changes for all metrics
3. Identify improvements and regressions
4. Generate comparison report
5. Store in `/tracking/reports/`

**Output Format**:
```markdown
## Comparison Report: [domain]
Period: [start_date] to [end_date]

### Key Improvements
- Organic Traffic: +45% (1,234 → 1,789 sessions)
- Core Web Vitals: +12 points (78 → 90)
- Keywords in Top 10: +8 (12 → 20)

### Areas Needing Attention
- Bounce Rate: +5% (needs investigation)
- Page Load Speed: -0.3s regression
```

---

### /track report
**Purpose**: Create comprehensive progress report
**Syntax**: `/track report [type] [domain] [period]`
**Parameters**:
- `type`: weekly|monthly|quarterly|custom
- `domain`: Target domain
- `period`: Number of days/weeks/months

**Execution Flow**:
1. Aggregate tracking data for period
2. Calculate trends and patterns
3. Generate visualizations (ASCII charts)
4. Create executive summary
5. Include ROI calculations
6. Export to specified format

**Delegation**:
- @seo-analyst: Data aggregation and analysis
- @seo-strategist: Strategic insights and recommendations
- @coordinator: Report assembly and quality check

**Note**: For stakeholder progress reports, use `/report` command

---

### /track roi
**Purpose**: Calculate return on investment metrics
**Syntax**: `/track roi [domain] [period] [investment]`
**Parameters**:
- `domain`: Target domain
- `period`: Measurement period
- `investment`: Optional manual investment amount

**Calculation Components**:
```yaml
roi_calculation:
  returns:
    - organic_traffic_value: sessions * $2.50
    - conversion_value: conversions * avg_order_value
    - time_savings: hours_automated * $150
    - competitive_advantage: market_share_gain * category_value
  
  investment:
    - tool_costs: subscription_fees
    - time_investment: setup_hours * hourly_rate
    - opportunity_cost: alternative_investment_return
  
  formula: (returns - investment) / investment * 100
```

**Output Example**:
```
ROI Analysis for freecalchub.com
Period: Last 90 days

Returns:
- Organic Traffic Value: $12,450
- Conversion Revenue: $8,900
- Time Savings: $4,500
- Total Returns: $25,850

Investment:
- SEO Agent Setup: $2,000
- Monthly Operations: $1,500
- Total Investment: $3,500

ROI: 639% (($25,850 - $3,500) / $3,500)
Payback Period: 2 weeks
```

---

### /track trends
**Purpose**: Analyze performance trends and patterns
**Syntax**: `/track trends [domain] [metric] [period]`
**Parameters**:
- `domain`: Target domain
- `metric`: traffic|rankings|technical|all
- `period`: 30d|90d|6m|1y

**Analysis Types**:
- Seasonal patterns detection
- Growth trajectory calculation
- Anomaly identification
- Predictive forecasting

---

### /track competitors
**Purpose**: Track competitive positioning
**Syntax**: `/track competitors [domain] [competitors_list]`
**Parameters**:
- `domain`: Your domain
- `competitors_list`: Comma-separated competitor domains

**Metrics Tracked**:
- Share of voice comparison
- Ranking overlap analysis
- Traffic gap identification
- Backlink gap analysis

---

## ERROR HANDLING

### Common Issues and Resolutions

**No Baseline Found**:
```bash
ERROR: No baseline exists for domain
ACTION: Run `/track baseline [domain]` first
```

**Data Source Unavailable**:
```bash
ERROR: Cannot connect to Google Analytics
ACTION: Check MCP configuration in /docs/mcp-integration-guide.md
FALLBACK: Use available data sources only
```

**Insufficient Data**:
```bash
ERROR: Not enough data for comparison (minimum 7 days required)
ACTION: Wait for more data collection or adjust period
```

---

## INTEGRATION POINTS

### Mission Integration
All missions automatically trigger tracking:
```yaml
mission_start:
  - auto_baseline: true (if first run)
  - snapshot_type: "mission_start"

mission_complete:
  - snapshot_type: "mission_complete"
  - auto_compare: true
  - generate_report: true
```

### Agent Hooks
Agents report metrics during execution:
```javascript
// In agent execution
@tracking.record("technical", {
  metric: "core_web_vitals",
  value: 92,
  timestamp: new Date().toISOString()
});
```

---

## CONFIGURATION

### Tracking Settings
Configure in `/tracking/config/tracking.yml`:
```yaml
tracking:
  auto_baseline: true
  snapshot_frequency: "daily"
  retention_days: 90
  
alerts:
  traffic_drop: -15%
  ranking_drop: 3
  
roi:
  session_value: 2.50
  conversion_rate: 0.02
```

---

## QUALITY STANDARDS

### Data Validation
- All metrics must pass schema validation
- Timestamp accuracy within 1 minute
- Data completeness >95%
- Anomaly detection for outliers

### Report Quality
- Executive summary <100 words
- Key metrics highlighted
- Actionable recommendations included
- Visual elements for clarity

---

## SUCCESS METRICS

**Tracking System Performance**:
- Baseline capture: <60 seconds
- Snapshot creation: <30 seconds
- Report generation: <5 seconds
- Data accuracy: >99%

**Business Value Delivery**:
- ROI clearly quantified
- Trends identified accurately
- Competitive insights actionable
- Marketing value documented

---

---

## ADDITIONAL ANALYSIS COMMANDS

### /report
**Purpose**: Generate comprehensive stakeholder progress reports
**Syntax**: `/report [date]`
**Description**: Creates executive-level progress reports with completed tasks, metrics, issues, and milestones. See `/report` command documentation for details.

### /pmd
**Purpose**: Post Mortem Diagnostic - Root cause analysis
**Syntax**: `/pmd [issue]`
**Description**: Conducts deep analysis of failures, performance issues, and systemic problems. See `/pmd` command documentation for details.

---

*SEO Agent Tracking System v1.0 - Measure, Optimize, Succeed*