# Weekly SEO Progress Report
**Domain:** {{domain}}  
**Period:** {{start_date}} - {{end_date}}  
**Generated:** {{timestamp}}

## Executive Summary
{{executive_summary}}

## Key Performance Indicators

### 📈 Traffic Performance
| Metric | Previous Week | This Week | Change | Trend |
|--------|---------------|-----------|--------|-------|
| Organic Sessions | {{prev_sessions}} | {{curr_sessions}} | {{sessions_change}}% | {{sessions_trend}} |
| Users | {{prev_users}} | {{curr_users}} | {{users_change}}% | {{users_trend}} |
| Pageviews | {{prev_pageviews}} | {{curr_pageviews}} | {{pageviews_change}}% | {{pageviews_trend}} |
| Avg Session Duration | {{prev_duration}} | {{curr_duration}} | {{duration_change}}% | {{duration_trend}} |
| Bounce Rate | {{prev_bounce}} | {{curr_bounce}} | {{bounce_change}}% | {{bounce_trend}} |

### 🎯 Ranking Performance
| Metric | Previous Week | This Week | Change | Status |
|--------|---------------|-----------|--------|--------|
| Avg Position | {{prev_position}} | {{curr_position}} | {{position_change}} | {{position_status}} |
| Keywords in Top 10 | {{prev_top10}} | {{curr_top10}} | {{top10_change}} | {{top10_status}} |
| Impressions | {{prev_impressions}} | {{curr_impressions}} | {{impressions_change}}% | {{impressions_status}} |
| Click-Through Rate | {{prev_ctr}}% | {{curr_ctr}}% | {{ctr_change}}% | {{ctr_status}} |

### 🔧 Technical Health
| Metric | Score | Change | Issues | Priority |
|--------|-------|--------|--------|----------|
| Core Web Vitals | {{cwv_score}}/100 | {{cwv_change}} | {{cwv_issues}} | {{cwv_priority}} |
| Mobile Usability | {{mobile_score}}/100 | {{mobile_change}} | {{mobile_issues}} | {{mobile_priority}} |
| Crawl Errors | {{crawl_errors}} | {{crawl_change}} | {{crawl_details}} | {{crawl_priority}} |
| Page Speed | {{speed_score}}/100 | {{speed_change}} | {{speed_issues}} | {{speed_priority}} |

## Mission Progress

### Completed Missions
{{#each completed_missions}}
- **{{mission_name}}** ({{completion_date}})
  - Objective: {{objective}}
  - Result: {{result}}
  - Impact: {{impact}}
{{/each}}

### Active Missions
{{#each active_missions}}
- **{{mission_name}}** ({{progress}}% complete)
  - Started: {{start_date}}
  - Expected Completion: {{expected_completion}}
  - Current Status: {{status}}
{{/each}}

## Top Wins 🏆
{{#each wins}}
1. {{win_description}}
   - Impact: {{win_impact}}
   - Metric: {{win_metric}}
{{/each}}

## Critical Issues ⚠️
{{#each issues}}
1. **{{issue_title}}**
   - Severity: {{severity}}
   - Impact: {{impact}}
   - Recommended Action: {{action}}
   - Owner: {{owner}}
{{/each}}

## Keyword Movement

### Top Gainers 📈
| Keyword | Previous Position | Current Position | Change | Traffic Impact |
|---------|-------------------|------------------|--------|----------------|
{{#each keyword_gainers}}
| {{keyword}} | {{prev_pos}} | {{curr_pos}} | +{{change}} | {{traffic}} |
{{/each}}

### Top Losers 📉
| Keyword | Previous Position | Current Position | Change | Action Required |
|---------|-------------------|------------------|--------|-----------------|
{{#each keyword_losers}}
| {{keyword}} | {{prev_pos}} | {{curr_pos}} | -{{change}} | {{action}} |
{{/each}}

## Content Performance

### Top Performing Pages
| Page | Sessions | Engagement | Conversions | Optimization |
|------|----------|------------|-------------|--------------|
{{#each top_pages}}
| {{page_title}} | {{sessions}} | {{engagement}} | {{conversions}} | {{optimization}} |
{{/each}}

### Content Opportunities
{{#each content_opportunities}}
- **{{opportunity}}**: {{description}}
  - Potential Impact: {{impact}}
  - Effort Required: {{effort}}
{{/each}}

## Competitive Analysis

### Market Position
- **Share of Voice**: {{sov}}% ({{sov_change}} from last week)
- **Visibility Score**: {{visibility}}/100 ({{visibility_change}} points)
- **Competitive Gaps**: {{gaps_count}} identified

### Competitor Movement
| Competitor | Their Change | Our Opportunity | Action |
|------------|--------------|-----------------|--------|
{{#each competitors}}
| {{name}} | {{change}} | {{opportunity}} | {{action}} |
{{/each}}

## ROI & Business Impact

### Value Generated This Week
- **Organic Traffic Value**: ${{traffic_value}}
- **Conversions from Organic**: {{conversions}}
- **Revenue Attribution**: ${{revenue}}
- **Cost Savings**: ${{savings}} ({{hours_saved}} hours automated)

### Cumulative ROI
- **Total Investment**: ${{total_investment}}
- **Total Returns**: ${{total_returns}}
- **ROI Percentage**: {{roi_percentage}}%
- **Payback Period**: {{payback_period}}

## Recommendations for Next Week

### Priority Actions
{{#each priority_actions}}
1. **{{action}}**
   - Owner: {{owner}}
   - Deadline: {{deadline}}
   - Expected Impact: {{impact}}
{{/each}}

### Strategic Focus Areas
{{#each focus_areas}}
- {{area}}: {{description}}
{{/each}}

## Automated Agent Activity

### Agent Performance
| Agent | Tasks Completed | Success Rate | Time Saved |
|-------|-----------------|--------------|------------|
{{#each agent_activity}}
| {{agent_name}} | {{tasks}} | {{success_rate}}% | {{time_saved}} hrs |
{{/each}}

### System Health
- **Uptime**: {{uptime}}%
- **API Calls**: {{api_calls}} ({{api_remaining}} remaining)
- **Data Quality**: {{data_quality}}/100
- **Next Scheduled Mission**: {{next_mission}}

---

**Next Report:** {{next_report_date}}  
**Questions?** Review the [SEO Agent Documentation](../docs/) or run `/coord meeting @seo-analyst`

*Generated by SEO Agent Library v1.0*