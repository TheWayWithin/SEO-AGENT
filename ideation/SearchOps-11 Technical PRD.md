# SearchOps-11 Technical PRD
## SEO Agent Suite Implementation Specification

**Project:** SearchOps-11 SEO Agent Suite  
**Purpose:** Automated SEO management for freecalchub.com and other websites  
**Platform:** Claude Code sub-agents with MCP integrations  
**Timeline:** Immediate development and deployment  

## Project Overview

Build a working SEO agent suite using Claude Code's sub-agent system to automate SEO tasks for freecalchub.com. The system should handle technical audits, content optimization, keyword research, performance monitoring, and AI search optimization through specialized agents with specific tool assignments.

## Technical Architecture

### Platform Requirements
- **Claude Code** - Primary execution environment
- **Sub-agent system** - Individual agents with focused tool assignments
- **MCP integrations** - External tool connections per agent
- **Project-local deployment** - Business context isolation

### Repository Structure
```
searchops-11/
├── README.md
├── .claude/
│   ├── agents/           # Individual agent prompt files
│   ├── missions/         # Mission workflow templates  
│   └── config/           # Configuration and commands
├── docs/                 # Implementation guides
├── examples/             # Site-specific configurations
└── scripts/              # Utility scripts
```

## Agent Specifications

### 1. SEO Strategist Agent
**File:** `.claude/agents/strategist.md`

**Purpose:** Strategic planning, competitive analysis, mission coordination

**Claude Code Tools:**
- `web_search` - Market research and competitive intelligence
- `file_read`, `file_write` - Strategy documentation
- `browser_navigate`, `browser_view` - Competitive analysis

**MCP Integrations:**
- Google Search Console MCP - Performance analysis
- Google Analytics 4 MCP - Traffic analysis  
- Ahrefs MCP - Competitive intelligence
- SEMrush MCP - Market positioning

**Key Responsibilities:**
- Develop SEO strategies aligned with business goals
- Conduct competitive analysis and market intelligence
- Coordinate missions across agents
- Set priorities and allocate resources

**Deliverables:**
- SEO strategy roadmaps with quarterly milestones
- Competitive analysis reports with opportunities
- Mission coordination plans with timelines
- Strategic KPI dashboards

### 2. Technical SEO Agent
**File:** `.claude/agents/technical.md`

**Purpose:** Technical optimization, Core Web Vitals, schema markup

**Claude Code Tools:**
- `shell_exec` - Server-side optimization
- `browser_navigate`, `browser_view` - Performance testing
- `file_read`, `file_write`, `file_edit` - Code implementation

**MCP Integrations:**
- Screaming Frog MCP - Site crawling and analysis
- Google PageSpeed Insights MCP - Performance optimization
- Lighthouse MCP - Automated auditing
- Google Search Console MCP - Technical health monitoring

**Key Responsibilities:**
- Conduct technical SEO audits
- Optimize Core Web Vitals (LCP, INP, CLS)
- Implement schema markup and structured data
- Monitor site health and crawlability

**Deliverables:**
- Technical audit reports with prioritized fixes
- Core Web Vitals optimization implementations
- Schema markup code and validation
- Performance monitoring dashboards

### 3. Content Optimizer Agent
**File:** `.claude/agents/content.md`

**Purpose:** Content optimization, on-page SEO, content strategy

**Claude Code Tools:**
- `file_read`, `file_write`, `file_edit` - Content creation/optimization
- `web_search` - Content research
- `browser_navigate` - Content performance analysis

**MCP Integrations:**
- WordPress MCP - Direct content optimization
- Clearscope MCP - Content optimization scoring
- Grammarly MCP - Content quality assurance
- Google Search Console MCP - Content performance

**Key Responsibilities:**
- Optimize existing content for SEO
- Create content briefs with SEO specifications
- Develop internal linking strategies
- Analyze content gaps and opportunities

**Deliverables:**
- Content optimization reports with specific improvements
- SEO content briefs with keyword targeting
- Internal linking implementation plans
- Content performance analysis

### 4. Keyword Researcher Agent
**File:** `.claude/agents/researcher.md`

**Purpose:** Keyword research, market intelligence, opportunity discovery

**Claude Code Tools:**
- `web_search` - Market research and keyword discovery
- `file_write`, `file_read` - Research documentation
- `browser_navigate` - SERP analysis

**MCP Integrations:**
- Ahrefs MCP - Comprehensive keyword data
- SEMrush MCP - Keyword research and analysis
- Google Keyword Planner MCP - Search volume data
- Google Trends MCP - Trend analysis

**Key Responsibilities:**
- Discover high-value keyword opportunities
- Analyze competitor keyword strategies
- Identify search trends and seasonal patterns
- Organize keywords into topic clusters

**Deliverables:**
- Keyword opportunity matrices with 500+ keywords
- Competitive keyword analysis with gaps
- Market intelligence reports with trends
- Topic cluster maps for content architecture

### 5. SEO Analyst Agent
**File:** `.claude/agents/analyst.md`

**Purpose:** Performance tracking, data analysis, ROI measurement

**Claude Code Tools:**
- `file_read`, `file_write` - Data analysis and reporting
- `browser_navigate` - Analytics platform access
- `web_search` - Benchmarking research

**MCP Integrations:**
- Google Analytics 4 MCP - Traffic and conversion analysis
- Google Search Console MCP - Search performance data
- Ahrefs MCP - Ranking and visibility tracking
- Google Data Studio MCP - Advanced reporting

**Key Responsibilities:**
- Monitor SEO performance metrics
- Analyze traffic and ranking data
- Generate insights and recommendations
- Track ROI and business impact

**Deliverables:**
- Performance reports with trend analysis
- ROI analysis with business impact measurement
- Real-time dashboards with key metrics
- Predictive analytics and forecasting

### 6. Link Builder Agent
**File:** `.claude/agents/builder.md`

**Purpose:** Link building, digital PR, authority development

**Claude Code Tools:**
- `web_search` - Prospect research and opportunity identification
- `file_write`, `file_read` - Outreach planning and tracking
- `browser_navigate` - Link prospect evaluation

**MCP Integrations:**
- Ahrefs MCP - Backlink analysis and prospects
- Hunter.io MCP - Email discovery and verification
- HARO MCP - Journalist relationship building
- Mention.com MCP - Brand monitoring

**Key Responsibilities:**
- Develop link building strategies
- Execute outreach campaigns
- Build industry relationships
- Monitor brand mentions and convert to links

**Deliverables:**
- Link building strategies with target identification
- Outreach campaign results with metrics
- Relationship development plans
- Authority building reports with domain growth

### 7. Mission Coordinator Agent
**File:** `.claude/agents/coordinator.md`

**Purpose:** Mission orchestration, quality assurance, workflow management

**Claude Code Tools:**
- `file_read`, `file_write`, `file_edit` - Mission planning
- `shell_exec` - Workflow automation

**MCP Integrations:**
- Asana MCP - Task management and coordination
- Slack MCP - Communication and status updates
- Project management tools - Mission tracking

**Key Responsibilities:**
- Orchestrate complex multi-agent missions
- Ensure quality standards and deliverable review
- Coordinate agent communication and handoffs
- Monitor progress and resolve issues

**Deliverables:**
- Mission briefs with objectives and timelines
- Quality assurance reports with standards compliance
- Workflow documentation with optimization
- Agent coordination plans with resource allocation

## Mission Templates

### 1. Site Audit Mission
**File:** `.claude/missions/site-audit.md`

**Duration:** 60 minutes  
**Agents:** Strategist, Technical, Content, Analyst

**Workflow:**
1. **Initial Assessment** (15 min) - Strategist + Analyst
   - Business context analysis and baseline metrics
2. **Technical Analysis** (20 min) - Technical + Analyst  
   - Core Web Vitals and technical health check
3. **Content Review** (15 min) - Content + Researcher
   - Content gaps and on-page optimization
4. **Performance Synthesis** (10 min) - Analyst + Strategist
   - Traffic analysis and strategic recommendations

**Deliverables:**
- Executive summary with SEO health score
- Top 5 critical issues and quick wins
- Prioritized action plan with timelines
- Performance baseline with projections

### 2. Content Gap Analysis Mission
**File:** `.claude/missions/content-gap.md`

**Duration:** 2-4 hours  
**Agents:** Researcher, Content, Strategist, Analyst

**Workflow:**
1. **Market Intelligence** (45 min) - Researcher + Strategist
   - Competitive analysis and keyword discovery
2. **Content Gap Identification** (60 min) - Content + Researcher
   - Topic clusters and content opportunities
3. **Competitive Intelligence** (45 min) - Strategist + Content
   - Content differentiation and positioning
4. **Strategic Planning** (30 min) - Strategist + Content
   - Prioritization and resource allocation

**Deliverables:**
- Content opportunity report with 500+ keywords
- 12-month content calendar with strategic topics
- Content briefs with SEO specifications
- Competitive intelligence with differentiation strategies

### 3. Technical Fix Mission
**File:** `.claude/missions/technical-fix.md`

**Duration:** 4-8 hours  
**Agents:** Technical, Coordinator, Analyst

**Workflow:**
1. **Technical Audit** (90 min) - Technical + Analyst
   - Comprehensive technical issue identification
2. **Performance Implementation** (120 min) - Technical + Coordinator
   - Core Web Vitals and speed optimization
3. **Schema Implementation** (60 min) - Technical + Content
   - Structured data and rich snippets
4. **Quality Assurance** (30 min) - Coordinator + Technical
   - Validation and monitoring setup

**Deliverables:**
- Technical fix implementation with before/after
- Performance optimization documentation
- Schema markup implementation guide
- Monitoring dashboard setup

### 4. AI Search Optimization Mission
**File:** `.claude/missions/ai-search-optimize.md`

**Duration:** 1-3 days  
**Agents:** Strategist, Content, Technical, Researcher

**Workflow:**
1. **AI Search Analysis** (4 hours) - Strategist + Researcher
   - AI search landscape and competitive analysis
2. **llms.txt Implementation** (6 hours) - Content + Technical
   - AI-friendly content structure and optimization
3. **Technical Infrastructure** (4 hours) - Technical + Content
   - AI crawler optimization and structured data
4. **Content Strategy** (6 hours) - Content + Researcher
   - AI-first content development
5. **Monitoring Setup** (4 hours) - Analyst + Technical
   - AI search performance tracking

**Deliverables:**
- Complete llms.txt implementation
- AI-optimized content library
- Technical AI search infrastructure
- AI search monitoring dashboard

## Command System Implementation

### Core Commands
**File:** `.claude/config/commands.md`

```bash
# Mission execution
/coord                              # Interactive mission launcher
/coord site-audit                   # Execute site audit mission
/coord content-gap                  # Execute content gap analysis
/coord technical-fix                # Execute technical optimization
/coord ai-search-optimize          # Execute AI search optimization

# Agent communication
/meeting @strategist "topic"        # Direct agent communication
/meeting @technical "issue"         # Technical consultation
/meeting @content "optimization"    # Content strategy discussion

# Performance monitoring
/rankings                          # Current keyword positions
/traffic-report                    # Traffic analysis
/technical-health                  # Site health check
/report weekly                     # Automated reporting
```

### Command Implementation
- Parse command syntax and route to appropriate agents
- Maintain mission state and progress tracking
- Handle agent coordination and communication
- Generate reports and deliverables

## Configuration System

### Business Context Configuration
**File:** `examples/freecalchub-config.yml`

```yaml
business_info:
  name: "FreeCalcHub"
  domain: "freecalchub.com"
  industry: "calculator_tools"
  target_audience: "people_needing_calculations"

seo_objectives:
  primary_goals:
    - "increase_calculator_usage"
    - "improve_educational_content_rankings"
    - "enhance_user_experience"
    - "ai_search_optimization"

content_strategy:
  content_categories:
    - "finance_calculators"
    - "math_calculators"  
    - "health_calculators"
    - "conversion_calculators"

technical_priorities:
  - "calculator_performance_optimization"
  - "mobile_calculator_experience"
  - "schema_markup_for_tools"
  - "core_web_vitals_excellence"
```

## MCP Integration Requirements

### Essential MCPs
- **Google Search Console MCP** - Search performance and technical health
- **Google Analytics 4 MCP** - Traffic analysis and conversions
- **Ahrefs MCP** - Competitive intelligence and keyword research
- **SEMrush MCP** - Market analysis and keyword research

### Recommended MCPs
- **Screaming Frog MCP** - Technical SEO auditing
- **PageSpeed Insights MCP** - Performance optimization
- **WordPress MCP** - Content management integration
- **Hunter.io MCP** - Email discovery for outreach

### Agent-MCP Mapping
- **Strategist**: Google Search Console, Analytics, Ahrefs, SEMrush
- **Technical**: Screaming Frog, PageSpeed, Lighthouse, Search Console
- **Content**: WordPress, Clearscope, Grammarly, Search Console
- **Researcher**: Ahrefs, SEMrush, Keyword Planner, Trends
- **Analyst**: Analytics, Search Console, Data Studio, Ahrefs
- **Builder**: Ahrefs, Hunter.io, HARO, Mention.com
- **Coordinator**: Asana, Slack, Project Management tools

## Implementation Priorities

### Phase 1: Core Infrastructure (Week 1)
1. **Repository Setup** - Create GitHub repository with structure
2. **Agent Prompts** - Implement 7 agent prompt files with tool assignments
3. **Basic Commands** - Implement core command parsing and routing
4. **Configuration System** - Business context and agent configuration

### Phase 2: Mission Implementation (Week 2)
1. **Site Audit Mission** - Complete workflow with agent coordination
2. **Mission Orchestration** - Coordinator agent implementation
3. **Quality Assurance** - Deliverable review and validation
4. **FreeCalcHub Configuration** - Site-specific optimization

### Phase 3: Advanced Features (Week 3)
1. **Content Gap Mission** - Strategic content analysis workflow
2. **Technical Fix Mission** - Implementation and optimization workflow
3. **Performance Monitoring** - Automated tracking and reporting
4. **Integration Testing** - MCP connections and validation

### Phase 4: AI Optimization (Week 4)
1. **AI Search Mission** - Future-proofing workflow implementation
2. **llms.txt Generation** - Automated AI-friendly content creation
3. **Advanced Analytics** - Predictive insights and forecasting
4. **Continuous Optimization** - Automated monitoring and alerts

## Quality Assurance Requirements

### Agent Performance Standards
- **Response Time** - Agents must respond within 30 seconds
- **Deliverable Quality** - All outputs must meet defined standards
- **Tool Integration** - MCPs must function reliably
- **Error Handling** - Graceful failure and recovery mechanisms

### Mission Success Criteria
- **Site Audit** - 95% issue identification accuracy
- **Content Gap** - 500+ relevant keyword opportunities identified
- **Technical Fix** - Measurable performance improvements
- **AI Optimization** - Successful llms.txt implementation

### Testing Requirements
- **Unit Testing** - Individual agent functionality
- **Integration Testing** - Agent coordination and MCP connections
- **End-to-End Testing** - Complete mission workflows
- **Performance Testing** - Response times and reliability

## Deployment Requirements

### Environment Setup
- **Claude Code** - Latest version with sub-agent support
- **MCP Connections** - All required integrations configured
- **File System** - Proper permissions and directory structure
- **Configuration** - Business context and agent settings

### Installation Process
1. **Repository Clone** - Download complete codebase
2. **Configuration Setup** - Customize for specific business needs
3. **MCP Integration** - Connect external tools and platforms
4. **Validation Testing** - Verify all components function correctly

### Monitoring and Maintenance
- **Performance Monitoring** - Track agent response times and success rates
- **Error Logging** - Capture and analyze failures
- **Regular Updates** - Keep agents and missions current
- **Backup Systems** - Protect configuration and data

## Success Metrics

### Technical Performance
- **Agent Response Time** - <30 seconds average
- **Mission Completion Rate** - 95%+ success rate
- **MCP Integration Reliability** - 99%+ uptime
- **Error Rate** - <1% system failures

### SEO Performance (FreeCalcHub)
- **Organic Traffic Growth** - 50%+ increase in 90 days
- **Core Web Vitals** - 95%+ pass rate
- **Keyword Rankings** - Top 10 for primary calculator terms
- **Calculator Engagement** - 80%+ completion rate

### Business Impact
- **Time Savings** - 80%+ reduction in manual SEO tasks
- **ROI Measurement** - Quantifiable business value
- **Competitive Advantage** - Measurable market position improvement
- **Scalability** - System handles multiple websites efficiently

## Risk Mitigation

### Technical Risks
- **MCP Failures** - Fallback mechanisms and error handling
- **Agent Coordination Issues** - Robust communication protocols
- **Performance Degradation** - Monitoring and optimization systems
- **Data Loss** - Backup and recovery procedures

### Business Risks
- **SEO Algorithm Changes** - Adaptive strategies and monitoring
- **Competitive Response** - Continuous intelligence and adjustment
- **Resource Constraints** - Efficient workflows and automation
- **Quality Issues** - Comprehensive testing and validation

This PRD provides the complete technical specification for building a working SearchOps-11 system that will automate SEO tasks for freecalchub.com and other websites. The focus is on practical implementation with real agents that perform actual SEO work, not theoretical concepts or commercial features.

