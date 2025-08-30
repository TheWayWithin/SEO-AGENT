---
name: report
description: Generate comprehensive stakeholder progress reports
---

# REPORT GENERATION COMMAND 📊

**Command**: `/report [date]`

**Arguments**: 
- No arguments: Generate full project report
- Date (YYYY-MM-DD): Generate report since specified date

## REPORT GENERATION PROTOCOL

You are generating a comprehensive stakeholder progress report for the SEOAgent project.

### REPORT STRUCTURE

#### 1. EXECUTIVE SUMMARY
- Project overview and current status
- Key achievements and metrics
- Critical issues and resolutions
- Resource utilization

#### 2. COMPLETED WORK
Review all completed tasks and missions:
- Task description and impact
- Completion date and time invested
- Metrics improved or goals achieved
- Stakeholder benefits

#### 3. PERFORMANCE METRICS
Analyze key performance indicators:
- **SEO Metrics**: Rankings, traffic, conversions
- **Technical Metrics**: Core Web Vitals, crawlability
- **Content Metrics**: Pages indexed, engagement
- **Business Metrics**: ROI, revenue impact

#### 4. ISSUES & RESOLUTIONS
Document challenges encountered:
- Issue description and severity
- Root cause analysis
- Resolution approach
- Prevention measures

#### 5. CURRENT STATUS
Present snapshot of project state:
- Active missions and progress
- Pending tasks and blockers
- Resource allocation
- Timeline adherence

#### 6. NEXT MILESTONES
Outline upcoming objectives:
- Next phase deliverables
- Resource requirements
- Risk factors
- Success criteria

### DATA SOURCES

Gather information from:
1. **Project Files**:
   - `/project-plan.md` - Task tracking
   - `/progress.md` - Issue logging
   - `/tracking/reports/` - Previous reports

2. **Mission Records**:
   - Completed missions in `/missions/`
   - Agent performance logs
   - Deliverable artifacts

3. **Tracking System**:
   - Baseline metrics from `/tracking/baselines/`
   - Snapshots from `/tracking/snapshots/`
   - ROI calculations from tracking system

### REPORT FORMATS

Generate report in requested format:
- **Executive**: High-level summary for C-suite
- **Technical**: Detailed technical metrics
- **Marketing**: Growth and engagement focus
- **Financial**: ROI and revenue emphasis

### EXAMPLE USAGE

```bash
# Full project report
/report

# Report since last week
/report 2025-08-20

# Report for specific period
/report 2025-08-01
```

### REPORT TEMPLATE

```markdown
# SEOAgent Progress Report
**Date**: [Current Date]
**Period**: [Reporting Period]

## Executive Summary
[2-3 paragraphs summarizing overall progress]

## Completed Tasks
### [Date Range]
- ✅ **[Task Name]**: [Impact/Result]
  - Metrics: [Before] → [After]
  - Time: [Duration]
  - Value: [Business Impact]

## Performance Metrics
### SEO Performance
- Organic Traffic: [Change %]
- Keyword Rankings: [Improvements]
- Conversion Rate: [Change %]

### Technical Health
- Core Web Vitals: [Scores]
- Crawl Coverage: [Percentage]
- Mobile Performance: [Score]

## Issues Encountered
### [Issue #1]
- **Severity**: [High/Medium/Low]
- **Resolution**: [How resolved]
- **Prevention**: [Future prevention]

## Current Status
- **Active Missions**: [List]
- **Progress**: [Percentage]
- **Blockers**: [If any]

## Next Milestones
1. [Milestone 1] - [Date]
2. [Milestone 2] - [Date]
3. [Milestone 3] - [Date]

## Resource Needs
- [Resource 1]: [Justification]
- [Resource 2]: [Justification]

## Recommendations
[Strategic recommendations based on data]
```

### SUCCESS CRITERIA

- Accurate data from all sources
- Clear executive communication
- Actionable insights included
- Metrics properly tracked
- ROI clearly demonstrated

## BEGIN REPORT GENERATION

Generate the appropriate report based on the provided arguments. Include all relevant metrics, completed work, and strategic recommendations.