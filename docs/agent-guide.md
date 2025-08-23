# SEO Agent Guide
## Your Elite SEO Intelligence Squad

> Master the coordination of 6 specialized SEO agents working in harmony to transform your search presence. This guide explains each agent's role, capabilities, and optimal usage patterns.

## Overview

SEOAgent (SearchOps-11™) operates on a hub-and-spoke coordination model with 6 specialized AI agents and 1 central coordinator. Each agent excels in their domain while maintaining strict boundaries to prevent conflicts and ensure mission success.

### The Agent Architecture

```
           @coordinator (Hub)
                  |
    ┌─────────────┼─────────────┐
    |             |             |
@strategist   @technical   @content
    |             |             |
    └─────────────┼─────────────┘
                  |
    ┌─────────────┼─────────────┐
    |             |             |
@researcher   @analyst    @builder
```

## The SEO Specialist Agents

### 🎯 SEO Strategist (@seo-strategist)

**Primary Function**: Strategic planning, competitive analysis, and mission coordination

**Core Capabilities**:
- Develop comprehensive SEO strategies aligned with business goals
- Create quarterly SEO roadmaps with measurable milestones  
- Conduct SWOT analysis of competitive landscape
- Prioritize initiatives using impact/effort matrices
- Define mission objectives and success criteria

**When to Use**:
- Planning new SEO campaigns or initiatives
- Quarterly strategy reviews and goal setting
- Competitive landscape analysis
- Resource allocation decisions
- Mission scoping and planning

**Example Usage**:
```bash
# Strategic planning
@seo-strategist Develop Q1 SEO strategy for ecommerce site focusing on conversion optimization

# Competitive analysis
@seo-strategist Analyze top 3 competitors' SEO strategies in the SaaS space

# Mission planning
@seo-strategist Create strategic framework for increasing organic traffic by 40% in 6 months
```

**Typical Deliverables**:
- Strategic SEO roadmaps with timelines
- Competitive intelligence reports  
- Priority matrices for SEO initiatives
- SWOT analysis documents
- Mission plans with success criteria

### 🔧 Technical SEO Specialist (@seo-technical)

**Primary Function**: Technical optimization, Core Web Vitals, and site performance

**Core Capabilities**:
- Audit and optimize Core Web Vitals (LCP, FID, CLS)
- Implement technical SEO improvements
- Optimize site speed and mobile responsiveness
- Fix crawlability and indexation issues
- Configure structured data and schema markup

**When to Use**:
- Site speed optimization needed
- Core Web Vitals scores are poor
- Mobile responsiveness issues
- Crawl errors or indexation problems
- Schema markup implementation

**Example Usage**:
```bash
# Core Web Vitals optimization
@seo-technical Audit and fix Core Web Vitals issues on homepage - current LCP is 4.2s

# Mobile optimization
@seo-technical Optimize site for mobile-first indexing and improve mobile page speed

# Technical audit
@seo-technical Perform comprehensive technical SEO audit focusing on crawlability
```

**Typical Deliverables**:
- Technical SEO audit reports
- Core Web Vitals improvement plans
- Site speed optimization recommendations
- Mobile optimization checklists
- Schema markup implementations

### 📝 Content SEO Specialist (@seo-content)

**Primary Function**: Content optimization, on-page SEO, and internal linking

**Core Capabilities**:
- Optimize existing content for target keywords
- Create SEO content briefs and guidelines
- Implement on-page SEO best practices
- Design internal linking strategies
- Optimize meta tags, headers, and page structure

**When to Use**:
- Content needs SEO optimization
- Internal linking strategy required
- Meta descriptions/titles need improvement
- On-page SEO audit needed
- Content gaps identified

**Example Usage**:
```bash
# Content optimization
@seo-content Optimize blog post "Ultimate Guide to Email Marketing" for target keyword "email marketing best practices"

# Internal linking
@seo-content Create internal linking strategy to boost authority flow to product pages

# On-page audit
@seo-content Audit top 20 pages for on-page SEO opportunities and create action plan
```

**Typical Deliverables**:
- Optimized content with proper keyword targeting
- Internal linking strategies and implementations
- On-page SEO audit reports
- Content optimization checklists
- Meta tag optimization recommendations

### 🔍 SEO Researcher (@seo-researcher)

**Primary Function**: Keyword research, market intelligence, and search trend analysis

**Core Capabilities**:
- Conduct comprehensive keyword research
- Analyze search trends and seasonal patterns
- Research competitor keyword strategies
- Identify content gaps and opportunities
- Monitor SERP features and ranking opportunities

**When to Use**:
- Starting new content projects
- Expanding into new markets or topics
- Competitor keyword analysis needed
- Seasonal content planning
- Search trend research required

**Example Usage**:
```bash
# Keyword research
@seo-researcher Find long-tail keywords for "project management software" with low competition

# Market analysis  
@seo-researcher Analyze search trends for "remote work tools" over past 12 months

# Competitor research
@seo-researcher Identify keyword gaps between our site and top 3 competitors in the fitness niche
```

**Typical Deliverables**:
- Comprehensive keyword research reports
- Search trend analysis with seasonal insights
- Competitor keyword gap analysis
- Content opportunity identification
- SERP feature opportunity reports

### 📊 SEO Analyst (@seo-analyst)

**Primary Function**: Performance tracking, reporting, and ROI analysis

**Core Capabilities**:
- Track and analyze SEO performance metrics
- Create comprehensive SEO reports
- Monitor keyword rankings and traffic changes
- Calculate SEO ROI and conversion attribution
- Set up performance alerts and monitoring

**When to Use**:
- Monthly/quarterly performance reviews
- Traffic drop investigations needed
- ROI analysis required
- Performance baseline establishment
- Ranking change analysis needed

**Example Usage**:
```bash
# Performance analysis
@seo-analyst Create monthly SEO performance report for Q4 showing traffic, rankings, and conversions

# Traffic investigation
@seo-analyst Analyze 30% traffic drop on Dec 15th and identify potential causes

# ROI calculation
@seo-analyst Calculate SEO ROI for past 6 months including organic conversions and revenue attribution
```

**Typical Deliverables**:
- Monthly/quarterly SEO performance reports
- Traffic analysis and investigation reports
- Keyword ranking change analyses
- SEO ROI and conversion reports
- Performance alert configurations

### 🔗 Link Building Specialist (@seo-builder)

**Primary Function**: Authority building, link acquisition, and outreach strategies

**Core Capabilities**:
- Develop comprehensive link building strategies
- Identify high-quality link opportunities
- Create personalized outreach campaigns
- Monitor backlink profile health
- Build relationships with industry influencers

**When to Use**:
- Domain authority improvement needed
- Link building campaigns required
- Backlink profile audit needed
- Competitor link analysis required
- Outreach strategy development

**Example Usage**:
```bash
# Link building strategy
@seo-builder Create 90-day link building strategy targeting DA 50+ sites in the marketing niche

# Opportunity identification
@seo-builder Find 20 high-quality link opportunities for "sustainable fashion" content

# Backlink audit
@seo-builder Audit current backlink profile and identify toxic links for disavowal
```

**Typical Deliverables**:
- Link building strategies and timelines
- Link opportunity research reports
- Outreach templates and campaigns
- Backlink profile audit reports
- Relationship building recommendations

## Agent Coordination Patterns

### The Hub-and-Spoke Model

All inter-agent communication flows through the central @coordinator to prevent conflicts and ensure optimal resource allocation.

**Correct Communication Pattern**:
```bash
# When SEO Strategist needs technical implementation
@coordinator Request @seo-technical to implement Core Web Vitals fixes based on strategy document

# When Content Specialist needs keyword research
@coordinator Request @seo-researcher to provide keyword analysis for content optimization project
```

**Incorrect Pattern** (Never do this):
```bash
# WRONG: Direct agent-to-agent communication
@seo-content @seo-researcher Can you give me keywords for this article?
```

### Stay in Lane Principle

Each agent has strict scope boundaries and will escalate tasks outside their expertise:

**SEO Strategist Boundaries**:
- ✅ Strategy development, competitive analysis, mission planning
- ❌ Technical implementation, content writing, link outreach

**Technical SEO Boundaries**:
- ✅ Technical audits, speed optimization, schema implementation
- ❌ Content creation, link building, keyword research

**Content SEO Boundaries**:
- ✅ Content optimization, on-page SEO, internal linking
- ❌ Technical fixes, link outreach, performance tracking

## Mission Coordination Workflows

### Standard Mission Pattern

1. **Mission Initiation**: @coordinator receives request and assigns lead agent
2. **Lead Agent Analysis**: Primary agent analyzes requirements and creates plan
3. **Multi-Agent Coordination**: @coordinator orchestrates required specialists
4. **Execution**: Agents work in parallel or sequence as planned
5. **Quality Review**: @coordinator validates deliverables
6. **Mission Completion**: Results delivered with performance metrics

### Common Coordination Scenarios

#### Comprehensive Site Audit
```bash
# Phase 1: Strategic overview
@coordinator Assign @seo-strategist to create audit framework

# Phase 2: Technical analysis  
@coordinator Assign @seo-technical to audit technical performance

# Phase 3: Content review
@coordinator Assign @seo-content to analyze on-page optimization

# Phase 4: Competitive analysis
@coordinator Assign @seo-researcher to research competitor strategies

# Phase 5: Performance baseline
@coordinator Assign @seo-analyst to establish current metrics

# Phase 6: Authority assessment
@coordinator Assign @seo-builder to audit backlink profile
```

#### Content Gap Analysis Mission
```bash
# Phase 1: Strategic framework
@coordinator @seo-strategist Define content strategy objectives

# Phase 2: Keyword opportunity research
@coordinator @seo-researcher Identify content gaps via keyword analysis

# Phase 3: Competitive content analysis
@coordinator @seo-researcher Analyze competitor content strategies

# Phase 4: Content optimization recommendations
@coordinator @seo-content Create optimization framework for identified gaps

# Phase 5: Performance tracking setup
@coordinator @seo-analyst Configure tracking for content performance
```

## Agent Performance Optimization

### Effective Agent Communication

**Be Specific with Requests**:
```bash
# Good: Specific and actionable
@seo-technical Optimize homepage for mobile Core Web Vitals - current LCP is 3.8s, target under 2.5s

# Poor: Vague and unclear
@seo-technical Make the site faster
```

**Provide Context and Constraints**:
```bash
# Good: Includes business context
@seo-strategist Develop Q1 strategy for B2B SaaS company targeting enterprise clients, budget $50k/quarter

# Poor: Missing critical context  
@seo-strategist Create an SEO strategy
```

**Define Success Criteria**:
```bash
# Good: Clear success metrics
@seo-content Optimize product pages to increase organic CTR from 3.2% to 5%+ within 30 days

# Poor: No measurable goals
@seo-content Make our product pages better
```

### Agent Specialization Maximization

**Leverage Each Agent's Strengths**:
- Use @seo-strategist for high-level planning and competitive intelligence
- Use @seo-technical for implementation of technical improvements
- Use @seo-content for content optimization and on-page work
- Use @seo-researcher for data-driven keyword and market research
- Use @seo-analyst for performance tracking and ROI analysis
- Use @seo-builder for authority building and relationship development

**Sequential vs Parallel Execution**:
- **Sequential**: Strategy → Research → Implementation → Analysis
- **Parallel**: Technical audit + Content audit + Competitor analysis simultaneously

## Troubleshooting Agent Issues

### Agent Not Responding or Generic Responses

**Symptoms**:
- Agent gives generic SEO advice instead of specialized insights
- Responses don't reflect agent's specific expertise area
- Agent doesn't reference business context

**Solutions**:
1. Verify agent files are properly loaded in `.claude/agents/`
2. Check business context is configured in `.claude/config/business-context.yml`
3. Restart Claude Code to reload agent configurations
4. Use more specific agent commands with clear scope

### Agent Scope Confusion

**Symptoms**:
- Agents attempt tasks outside their specialization
- Multiple agents provide conflicting advice
- Tasks aren't properly escalated to @coordinator

**Solutions**:
1. Review agent scope boundaries in their configuration files
2. Always use @coordinator for multi-agent coordination
3. Be explicit about which agent should handle which aspect
4. Use the "stay in lane" principle consistently

### Poor Mission Coordination

**Symptoms**:
- Mission phases overlap inefficiently
- Agents work on conflicting priorities
- Deliverables don't integrate well

**Solutions**:
1. Start missions through @coordinator, not individual agents
2. Use mission templates from the `/missions` folder
3. Define clear phase dependencies and handoffs
4. Set explicit success criteria for each phase

## Best Practices for Agent Management

### Daily Agent Operations

**Morning Routine**:
```bash
# Check system status
@coordinator Status report on all active missions

# Review overnight alerts
@seo-analyst Any performance alerts from past 24 hours?

# Plan daily priorities
@coordinator Prioritize today's SEO tasks based on mission progress
```

**Weekly Reviews**:
```bash
# Performance review
@seo-analyst Generate weekly SEO performance summary

# Strategic check-in
@seo-strategist Review progress on quarterly SEO objectives

# Technical health check
@seo-technical Weekly technical SEO health assessment
```

### Mission Planning Best Practices

1. **Start with Strategy**: Always begin missions with @seo-strategist for framework
2. **Define Clear Phases**: Break complex missions into manageable phases
3. **Set Success Criteria**: Each agent task needs measurable success metrics
4. **Plan Dependencies**: Identify which tasks must be sequential vs parallel
5. **Include Quality Gates**: Build in review points before mission completion

### Resource Optimization

**Efficient Agent Utilization**:
- Keep agents focused on their core specializations
- Use parallel processing when tasks don't have dependencies
- Batch similar tasks to maximize efficiency
- Always include @seo-analyst for performance measurement

**Avoid Agent Conflicts**:
- Never assign overlapping responsibilities
- Use @coordinator for all multi-agent coordination
- Maintain clear phase boundaries in missions
- Document agent decisions for future reference

## Integration with SEO Tools

### Agent Tool Access

Each agent has access to specific tools optimized for their specialization:

**All Agents**: WebSearch, WebFetch, Read, Write, Edit, Bash
**Technical Specialist**: Additional access to performance monitoring tools
**Analyst**: Enhanced data visualization and reporting capabilities
**Researcher**: Advanced keyword research and competitive analysis tools

### MCP Integration Benefits

With MCP (Model Context Protocol) enabled, agents gain enhanced capabilities:
- Direct Google Search Console data access
- Real-time Google Analytics integration
- SEO platform API connections (Ahrefs, SEMrush, Moz)
- Automated report generation and scheduling

## Next Steps

After mastering the agent system:

1. **Practice Mission Coordination**: Start with simple site audits to understand agent interactions
2. **Customize Agent Behavior**: Adjust agent preferences in configuration files
3. **Build Custom Missions**: Create specialized missions for your unique SEO needs
4. **Monitor Performance**: Use tracking system to optimize agent efficiency
5. **Scale Operations**: Implement automated missions and scheduled reports

## Quick Reference Commands

```bash
# Agent status and health
@coordinator Status report on all agents
/debug agents --status-report

# Direct agent communication
@seo-[specialist] [specific request with context and success criteria]

# Mission coordination
/coord [mission-name] [parameters]
/meeting @agent-name "[detailed request]"

# Agent troubleshooting
/reset agents --confirm
/validate config --fix-errors
```

---

**Remember**: The power of SEOAgent comes from coordinated specialist expertise, not individual agent heroics. Master the coordination patterns, respect agent boundaries, and watch your SEO performance transform through intelligent automation.