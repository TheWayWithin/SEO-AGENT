# SEO Progress Tracking Guide

Track SEO performance over time to prove ROI and optimize strategies.

## Quick Start (5 minutes)

### 1. Capture Initial Baseline
```bash
/track baseline yourdomain.com full
```
Creates timestamped performance snapshot before optimizations begin.

### 2. Run SEO Mission
```bash
/coord site-audit
```
Missions automatically capture before/after metrics.

### 3. View Progress
```bash
/track compare yourdomain.com 2025-01-15 today
```
Shows improvements since baseline with specific metrics.

### 4. Calculate ROI
```bash
/track roi yourdomain.com 90d
```
Generates financial value report for stakeholders.

## Core Commands

### Baseline Capture
```bash
/track baseline [domain] [scope]
```
- **When**: Before starting SEO work
- **Scope options**: `full`, `technical`, `content`, `rankings`
- **Output**: `/tracking/baselines/YYYY-MM-DD_domain_baseline.json`

### Progress Snapshots
```bash
/track snapshot [domain] [type]
```
- **Types**: `daily`, `weekly`, `monthly`, `mission`
- **Auto-captured**: During mission execution
- **Storage**: `/tracking/snapshots/[type]/`

### Comparison Reports
```bash
/track compare [domain] [start_date] [end_date]
```
- **Format**: Markdown report with percentage changes
- **Highlights**: Improvements in green, regressions in red
- **Export**: PDF, HTML, or Markdown

### ROI Calculation
```bash
/track roi [domain] [period]
```
- **Metrics**: Traffic value, time savings, revenue impact
- **Formula**: `(Returns - Investment) / Investment × 100`
- **Output**: Executive-friendly financial report

## Automatic Tracking

### Mission Integration
Every mission automatically:
1. Creates baseline (if first run)
2. Captures start snapshot
3. Records completion metrics
4. Generates comparison report

### Agent Tracking Hooks
All agents report metrics during execution:
- **Technical**: Core Web Vitals, crawl errors
- **Content**: Pages optimized, engagement metrics
- **Rankings**: Position changes, new keywords
- **Traffic**: Sessions, conversions, revenue

## Configuration

Edit `/tracking/config/tracking.yml`:

```yaml
tracking:
  auto_baseline: true       # Auto-capture on first mission
  snapshot_frequency: daily # Options: daily, weekly, monthly
  retention_days: 90        # Historical data retention

alerts:
  traffic_drop: -15         # Alert if traffic drops 15%
  ranking_drop: 3           # Alert if rankings drop 3+ positions

roi:
  session_value: 2.50       # Value per organic session
  conversion_rate: 0.02     # Expected conversion rate
```

## Key Metrics Tracked

### Technical Performance
- **Core Web Vitals**: LCP, FID, CLS scores
- **Page Speed**: Load time in seconds
- **Mobile Usability**: Mobile-friendly score
- **Crawl Health**: Errors, broken links, redirects

### Traffic & Engagement
- **Organic Sessions**: Month-over-month growth
- **User Behavior**: Bounce rate, session duration
- **Conversions**: Goals, transactions, revenue
- **Traffic Sources**: Organic vs other channels

### Rankings & Visibility
- **Average Position**: Overall ranking trend
- **Keyword Distribution**: Top 3, 10, 20, 50, 100
- **SERP Features**: Snippets, knowledge panels
- **Click-Through Rate**: Impressions to clicks

### Business Impact
- **Revenue Attribution**: Organic channel value
- **Time Savings**: Hours automated
- **Competitive Position**: Market share changes
- **ROI Percentage**: Return on SEO investment

## Report Types

### Weekly Progress Report
```bash
/track report weekly yourdomain.com
```
- Traffic changes vs previous week
- Top keyword movements
- Technical issues identified
- Action items for next week

### Monthly Executive Summary
```bash
/track report monthly yourdomain.com
```
- High-level KPIs and trends
- ROI calculation with revenue impact
- Competitive positioning update
- Strategic recommendations

### Marketing Case Study
```bash
/track report case-study yourdomain.com 90d
```
- Before/after metrics showcase
- Success story narrative
- Visual charts and graphs
- Client testimonial format

## Data Storage

### Directory Structure
```
/tracking/
├── baselines/          # Initial snapshots
├── snapshots/          # Time-series data
│   ├── daily/
│   ├── weekly/
│   └── monthly/
├── reports/            # Generated reports
│   ├── automated/
│   ├── executive/
│   └── case-studies/
└── config/            # System settings
```

### File Naming Convention
- Baselines: `YYYY-MM-DD_domain_baseline.json`
- Snapshots: `YYYY-MM-DD_HH-mm_domain_snapshot.json`
- Reports: `YYYY-MM-DD_domain_reporttype.md`

## Best Practices

### Baseline Timing
1. Capture baseline BEFORE any changes
2. Create quarterly baselines for long-term tracking
3. Document external factors (algorithm updates, seasonality)

### Consistent Tracking
1. Use same time of day for snapshots
2. Maintain regular tracking schedule
3. Don't skip tracking during low periods

### Actionable Reporting
1. Focus on metrics that drive decisions
2. Include specific next steps
3. Highlight wins for stakeholder buy-in

## Troubleshooting

### Missing Baseline
**Error**: "No baseline found for domain"
**Fix**: Run `/track baseline yourdomain.com full`

### Incomplete Data
**Error**: "Insufficient data for comparison"
**Fix**: Wait 7+ days between comparisons

### API Limits
**Error**: "API quota exceeded"
**Fix**: Check `/tracking/config/tracking.yml` frequency settings

## Value Demonstration

### For Clients
- Prove SEO ROI with financial metrics
- Show ranking improvements visually
- Document time saved through automation

### For Marketing
- Generate case studies automatically
- Create before/after comparisons
- Export presentation-ready reports

### For Optimization
- Identify what's working/not working
- Track algorithm impact
- Benchmark against competitors

---

**Questions?** Run `/coord meeting @seo-analyst` for tracking assistance.