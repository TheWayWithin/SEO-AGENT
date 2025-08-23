# SEO Agent Library - Quick Start Guide
## Deploy Your SEO Squad in 5 Minutes

## Prerequisites

- Claude Code installed and configured
- Access to your website's Google Search Console (optional but recommended)
- Google Analytics 4 property set up (optional but recommended)
- Git installed on your system

## Installation

### 1. Clone the Repository

```bash
# Clone the SEO Agent Library
git clone https://github.com/TheWayWithin/SEO-AGENT.git
cd SEO-AGENT

# Run the installation script
./scripts/install.sh
```

### 2. Start Claude Code

```bash
# In the SEO-AGENT directory
claude-code
```

### 3. Verify Agents Are Available

Once Claude Code is running, verify your SEO agents are loaded:

```
You: List available SEO agents
Claude: You have 6 SEO specialist agents available:
- @seo-strategist - Strategic planning and competitive analysis
- @seo-technical - Technical SEO and Core Web Vitals
- @seo-content - Content optimization and on-page SEO
- @seo-researcher - Keyword research and market intelligence
- @seo-analyst - Performance tracking and ROI analysis
- @seo-builder - Link building and authority development
```

## Your First Mission: Site Audit

### Running a Comprehensive Audit

```bash
# Execute a 60-minute comprehensive SEO audit
/coord site-audit

# Or specify your domain
/coord site-audit --domain=www.seoagent.work
```

This will:
- Analyze your site's technical health
- Identify content opportunities
- Benchmark current performance
- Provide a prioritized action plan

### Understanding the Output

The site audit produces:
1. **Executive Summary** - High-level findings and priorities
2. **Technical Audit** - Core Web Vitals, crawlability, mobile optimization
3. **Content Analysis** - Gaps, opportunities, optimization needs
4. **Action Plan** - Prioritized tasks with timelines

## Available Commands

### Mission Execution
```bash
/coord                    # Interactive mission launcher
/coord site-audit         # 60-minute comprehensive audit
/coord content-gap        # 2-4 hour content analysis
/coord technical-fix      # 4-8 hour technical optimization
```

### Direct Agent Communication
```bash
/meeting @seo-strategist "develop Q1 strategy"
/meeting @seo-technical "fix Core Web Vitals"
/meeting @seo-content "optimize product pages"
/meeting @seo-researcher "find keyword opportunities"
```

### Performance Monitoring
```bash
/rankings                 # Current keyword positions
/traffic-report          # Traffic and conversion analysis
/technical-health        # Site health monitoring
```

## Understanding Your SEO Agents

### 🎯 SEO Strategist
- **When to use:** Planning, competitive analysis, strategy development
- **Example:** `@seo-strategist analyze competitor strategies for [competitor.com]`

### 🔧 Technical SEO
- **When to use:** Site speed, Core Web Vitals, technical issues
- **Example:** `@seo-technical audit Core Web Vitals for homepage`

### 📝 Content Optimizer
- **When to use:** Content optimization, on-page SEO, internal linking
- **Example:** `@seo-content optimize meta descriptions for blog posts`

### 🔍 Keyword Researcher
- **When to use:** Keyword discovery, search trends, topic research
- **Example:** `@seo-researcher find long-tail keywords for [topic]`

### 📊 SEO Analyst
- **When to use:** Performance tracking, reporting, ROI analysis
- **Example:** `@seo-analyst create monthly performance report`

### 🔗 Link Builder
- **When to use:** Backlink strategies, outreach, authority building
- **Example:** `@seo-builder identify link opportunities in [niche]`

## Customizing for Your Site

### 1. Update Business Configuration

Edit `.claude/config/business-context.yml`:

```yaml
business_info:
  name: "Your Business"
  domain: "yourdomain.com"
  industry: "your_industry"
  target_audience: "your_audience"

seo_objectives:
  primary_goals:
    - "your_goal_1"
    - "your_goal_2"
```

### 2. Set Priority Keywords

Add your target keywords to track:

```yaml
target_keywords:
  primary:
    - "main keyword 1"
    - "main keyword 2"
  secondary:
    - "supporting keyword 1"
    - "supporting keyword 2"
```

## Common Workflows

### New Website Launch
1. `/coord site-audit` - Baseline assessment
2. `/coord technical-fix` - Resolve critical issues
3. `/coord content-gap` - Content strategy
4. `/coord keyword-research` - Keyword opportunities

### Ongoing Optimization
1. Weekly: `/traffic-report` - Monitor performance
2. Monthly: `/coord content-gap` - New opportunities
3. Quarterly: `/coord site-audit` - Comprehensive review

### Competitive Analysis
1. `@seo-strategist analyze top 3 competitors`
2. `@seo-researcher identify competitor keyword gaps`
3. `@seo-content create content to capture gaps`

## Troubleshooting

### Agents Not Responding
- Verify Claude Code is running
- Check agents are in `.claude/agents/` directory
- Restart Claude Code if needed

### Mission Failures
- Check error messages for specific issues
- Ensure all required agents are available
- Try running individual agent tasks

### Performance Issues
- Limit concurrent missions
- Run resource-intensive missions separately
- Monitor system resources

## Best Practices

1. **Start with an Audit** - Always baseline before optimizing
2. **Focus on Quick Wins** - Implement high-impact, low-effort changes first
3. **Track Everything** - Use @seo-analyst to monitor all changes
4. **Iterate Regularly** - Run missions on a schedule
5. **Document Changes** - Keep project-plan.md updated

## Getting Help

- **Documentation:** Check `/docs` folder
- **Issues:** https://github.com/TheWayWithin/SEO-AGENT/issues
- **Discussions:** https://github.com/TheWayWithin/SEO-AGENT/discussions
- **Website:** https://www.seoagent.work

## Next Steps

1. ✅ Run your first site audit
2. 📊 Review the findings
3. 🔧 Execute technical fixes
4. 📝 Implement content recommendations
5. 📈 Monitor improvements

---

**Ready to transform your SEO? Start with `/coord site-audit` now!**