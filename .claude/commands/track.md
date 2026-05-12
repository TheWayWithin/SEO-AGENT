# /track - SEO Performance Tracking & Reporting

**PURPOSE**: Capture point-in-time snapshots of SEO state and compare them over time to prove (or disprove) that fixes moved the needle. Constitution rule 5 ("Prove it") made operational.

## SHIPPED COMMANDS (Sprint 9, 2026-05-11)

### `/track baseline <domain>`

Capture the current SEO state for a domain as a versioned baseline snapshot.

**What it does**:
1. Finds the most recent `runs/<date>-<domain>-*/data.json` for the domain
2. Copies it to `tracking/baselines/<date>-<domain>.json`
3. Appends a baseline pointer line to `seo-evidence.md` ("BASELINE | <date> | <domain> | tracking/baselines/<file>.json | scores AI X/50, Trad Y/50")

**Implementation**: thin layer over Sprint 5 `data.json` deliverables. Does NOT independently fetch metrics — uses whatever the most recent site-audit run captured. To force a fresh metric capture before baselining, run `/coord site-audit lite <domain>` first, then `/track baseline <domain>`.

**Prerequisites**: at least one `runs/<date>-<domain>-*/data.json` must exist. If none, the command exits with "no run data — fire /coord site-audit lite first".

### `/track compare <domain> [--baseline <file>] [--against <file>]`

Diff two snapshots and produce a comparison report.

**What it does**:
1. Loads two `data.json` snapshots — defaults: latest baseline in `tracking/baselines/` AND latest run in `runs/`
2. Renders the deltas into a `comparison.md` per `templates/deliverables/comparison-report.md`
3. Saves output to `runs/<today>-<domain>-comparison/comparison.md`
4. Updates `seo-backlog.md`: items with confirmed metric movement move from `verified → closed`
5. Appends a comparison pointer to `seo-evidence.md`

**Honest constraints called out in every comparison report**:
- What metrics were not measurable (e.g. GA4 not connected)
- Whether the comparison window is long enough for the metrics in question
- Whether deltas exceed natural noise floors

## ARCHIVED PATH (Python — formally retired Sprint 10)

The `tracking/` Python system (`track.py`, `track_cli.py`, etc., defining `status`, `roi`, `report` subcommands) was archived to `tracking/legacy/` on 2026-05-11. It had defined CLI surface but no validated runtime path; `tracking/baselines/` and `tracking/snapshots/` were empty in source.

If `/track status`, `/track roi`, or `/track report` are needed, build agent-prompt versions following the Sprint 9 pattern (operate on existing `data.json` files and `seo-evidence.md`). Do not revive the Python without an explicit re-validation pass.

See `tracking/legacy/README.md` for full archive context and revival instructions.

## INTEGRATION WITH MISSIONS

The tracking system automatically integrates with SEO Agent missions and context preservation:

### Mission Lifecycle Tracking
1. **Pre-Mission**: Captures baseline performance metrics
2. **During Mission**: Monitors progress and evidence capture to `seo-evidence.md`
3. **Post-Mission**: Calculates impact and ROI attribution
4. **Reporting**: Generates before/after analysis and case studies

### Evidence Integration
- **Evidence File**: `seo-evidence.md` — single backward-looking artefact store (Constitution rule 1)
- **Mission State**: tracked in `agent-context.md` (framework convention)

### Agent Data Collection
- `@seo-analyst`: Performance monitoring and metrics analysis
- `@seo-technical`: Core Web Vitals and technical health tracking
- `@seo-content`: Content performance and engagement metrics
- `@seo-strategist`: Ranking improvements and competitive analysis

## REPORT TYPES GENERATED

### 1. Weekly Progress Reports
**Audience:** Operations teams, marketing managers  
**Contents:**
- Traffic growth metrics and trends
- Ranking position changes by keyword
- Technical health status and alerts
- Mission progress and completion status
- Agent activity and automation metrics

### 2. Monthly Executive Summaries
**Audience:** C-level executives, department heads  
**Contents:**
- High-level ROI and business impact
- Strategic wins and competitive advantages
- Market position and share of voice
- Resource allocation and efficiency gains
- Next month priorities and objectives

### 3. Before/After Mission Analysis
**Audience:** Project stakeholders, case study development  
**Contents:**
- Detailed performance comparison metrics
- Business value generated calculations
- Success factors and lessons learned
- Technical improvement documentation
- Sustainability and future outlook

### 4. Marketing Case Studies
**Audience:** Sales team, prospect communication  
**Contents:**
- Client success story narrative
- Compelling performance improvements
- ROI and business impact highlights
- Testimonial-ready content format

## ROI CALCULATION FRAMEWORK

### Traffic Value
```
Traffic Value = Session Increase × $2.50 (configurable)
```

### Conversion Impact  
```
Conversion Value = Traffic × 2% conversion rate × $100 AOV
```

### Operational Savings
```
Cost Savings = Hours Saved × $150/hour SEO rate
```

### Total ROI
```
Total Value = Traffic + Conversions + Savings
ROI % = (Total Value / Investment) × 100
```

## DATA SOURCES

### Required Integrations
- **Google Analytics 4**: Traffic, user behavior, conversion data
- **Google Search Console**: Ranking positions, impressions, CTR
- **Core Web Vitals**: Performance and user experience metrics
- **Mission Data**: Agent activities, task completion, time tracking

### Data Processing
- Real-time metric aggregation
- Trend analysis and pattern recognition
- Anomaly detection and alerting
- Competitive benchmarking integration

## EXPORT CAPABILITIES

### Format Options
- **Text**: Console output for quick checks
- **Markdown**: Documentation and internal reporting
- **HTML**: Styled reports for stakeholder sharing
- **JSON**: API integration and data exchange
- **PDF**: Executive presentations and client delivery

### Distribution
- Local file system storage
- Automated email delivery (configurable)
- Slack integration for team notifications
- API endpoints for external system integration

## EXAMPLES

### Quick Status Check
```bash
/track status
# Shows: system health, traffic growth, ROI summary
```

### Weekly Team Report
```bash
/track report --type weekly --format html
# Generates: styled weekly progress report
```

### Executive ROI Summary
```bash
/track roi --detailed
# Creates: comprehensive ROI report with business impact
```

### Mission Impact Analysis
```bash
/track compare --period monthly --export
# Produces: detailed before/after comparison report
```

### Marketing Case Study
```bash
/track report --type case_study --client "Success Story"
# Builds: marketing-ready case study document
```

## AUTOMATION FEATURES

### Scheduled Reports
- **Weekly**: Every Monday for operations teams
- **Monthly**: 1st of month for executive summaries
- **Mission-Based**: Automatically triggered post-mission
- **Alert-Based**: Performance threshold notifications

### Marketing Intelligence
- Success story identification and extraction
- Competitive advantage documentation
- ROI narrative generation for sales materials
- Stakeholder communication automation

## SYSTEM REQUIREMENTS

### Minimal Setup
- Python 3.8+ (built-in libraries only)
- Basic JSON data processing
- File system access for data storage

### Full Features
- `pyyaml` for configuration management
- `markdown` for HTML export generation  
- `pdfkit` + `wkhtmltopdf` for PDF creation
- External API integrations (GA4, GSC)

## FILE STRUCTURE

```
tracking/
├── track.py              # Simple CLI interface
├── report_engine.py      # Core data processing
├── report_types.py       # Report implementations
├── report_exports.py     # Export system
├── config/tracking.yml   # System configuration
├── templates/            # Report templates
├── baselines/           # Performance baselines
├── snapshots/           # Historical data
└── reports/             # Generated reports
```

## SUCCESS METRICS

### System Performance
- Report generation time < 30 seconds
- Data accuracy 99.9%
- Export success rate 100%
- ROI calculation precision ±2%

### Business Impact
- Executive adoption rate of monthly summaries
- Marketing utilization of case studies
- Sales team usage of ROI reports
- Stakeholder satisfaction scores

## INTEGRATION POINTS

### With Other Commands
- `/coord site-audit` → Baseline establishment
- `/coord missions` → Progress tracking integration
- Mission completion → Automatic impact analysis

### With SEO Agents
- All agents contribute performance data
- Automated data collection during missions
- Cross-agent coordination for comprehensive reporting

---

**IMPLEMENTATION STATUS:** ✅ Complete and Tested  
**DEPENDENCIES:** Core Python libraries (minimal setup)  
**TESTING:** Sample data generation and report validation  
**DOCUMENTATION:** Comprehensive README and examples available

This tracking system transforms SEO data into executive-friendly insights and marketing-ready materials, providing clear ROI justification and strategic direction for continued SEO investment.