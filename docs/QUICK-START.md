# SEO Agent Library - Quick Start Guide
## Deploy Your SEO Squad in 30 Minutes

> Transform your SEO operations with an elite AI agent squad. This comprehensive guide will take you from installation to running your first successful SEO mission.

**Time to Complete:** 20-30 minutes  
**What You'll Learn:** Full deployment, configuration, and execution of your first SEO audit

## Prerequisites

### System Requirements
- **Claude Code:** Latest version (claude.ai/code)
- **Operating System:** macOS, Linux, or Windows with WSL2
- **Memory:** 8GB RAM minimum (16GB recommended)
- **Storage:** 2GB available space
- **Internet:** Stable broadband connection
- **Git:** Version 2.20 or higher

### Required Account Access
- **Google Search Console:** Verified property access for your domain
- **Google Analytics 4:** Admin or Editor access to your GA4 property
- **Claude AI:** Active subscription with API access

### Recommended SEO Platform Integration (Choose One)
- **Ahrefs:** API access for advanced keyword and backlink data
- **SEMrush:** API credentials for competitive intelligence
- **Moz:** Pro account for domain authority and link metrics

### API Keys Checklist
Gather these credentials before starting:
- [ ] Google Search Console API access
- [ ] Google Analytics 4 measurement ID
- [ ] SEO platform API key (Ahrefs/SEMrush/Moz)
- [ ] Claude API key (if using programmatic access)
- [ ] Domain verification tokens (if needed)

## Installation

### 1. Clone and Setup Repository

```bash
# Clone the SEO Agent Library
git clone https://github.com/TheWayWithin/SEO-AGENT.git
cd SEO-AGENT

# Make installation script executable
chmod +x scripts/install.sh

# Run the installation script
./scripts/install.sh
```

**What the install script does:**
- Creates necessary directory structure
- Sets up agent configurations
- Validates system requirements
- Configures default mission templates
- Creates example configuration files

### 2. Understanding the Directory Structure

```
SEO-AGENT/
├── .claude/                    # Claude Code configuration
│   ├── agents/                 # Individual agent definitions
│   ├── commands/              # Custom command definitions
│   ├── config/                # Business context and settings
│   └── missions/              # Mission templates
├── agents/                    # Agent implementation files
├── docs/                      # Documentation and guides
├── examples/                  # Example configurations
├── missions/                  # Mission library and templates
├── scripts/                   # Installation and utility scripts
└── templates/                 # Agent and mission templates
```

### 3. Configure Your Business Context

**Essential Step:** Configure your business information before starting:

```bash
# Copy the example configuration
cp examples/seoagent-work-config.yml .claude/config/business-context.yml

# Edit with your business details
nano .claude/config/business-context.yml
```

**Required configuration fields:**
```yaml
business_info:
  name: "Your Business Name"          # Replace with your business
  domain: "yourdomain.com"             # Your primary domain
  industry: "your_industry"            # e.g., "ecommerce", "saas", "consulting"
  target_audience: "your_audience"     # Primary customer segment
  
seo_objectives:
  primary_goals:
    - "increase_organic_traffic"       # Your main SEO goals
    - "improve_local_visibility"
    - "boost_conversion_rates"
```

### 4. MCP Integration Setup

**For enhanced functionality, configure MCP (Model Context Protocol) connections:**

```bash
# Install MCP dependencies (if not already installed)
npm install -g @modelcontextprotocol/cli

# Configure MCP for Google integrations
# Follow the detailed guide in docs/mcp-integration-guide.md
```

**Quick MCP setup for Google services:**
1. Enable Google Search Console API in Google Cloud Console
2. Create service account and download credentials JSON
3. Add credentials to `.claude/config/google-credentials.json`
4. Configure MCP servers in Claude Code settings

### 5. Start Claude Code

```bash
# In the SEO-AGENT directory
claude-code

# Verify startup (should see agent loading messages)
```

**Successful startup indicators:**
- "Loading SEO agents..." message appears
- All 6 specialist agents load without errors
- Mission templates are available
- Configuration validation passes

### 6. Verify Agent Deployment

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

**Troubleshooting Agent Loading:**
If agents don't load properly:

```bash
# Check agent files exist
ls -la .claude/agents/

# Verify agent syntax
# Each agent file should be valid markdown with proper headers

# Restart Claude Code
# Exit and restart if agents aren't loading
```

**Testing Agent Communication:**
```
You: @seo-strategist Hello, are you ready?
Claude (as SEO Strategist): Ready for strategic SEO planning! What's your primary objective?
```

## Your First Mission: Complete Site Audit Walkthrough

### Pre-Mission Configuration

**Step 1: Configure Your Domain**
Ensure your domain is properly configured in business context:

```yaml
# In .claude/config/business-context.yml
business_info:
  domain: "yourdomain.com"  # Your actual domain
```

**Step 2: Verify Access**
Confirm you have:
- [ ] Google Search Console access for your domain
- [ ] Google Analytics tracking installed
- [ ] Admin access to make website changes

### Running Your First Comprehensive Audit

```bash
# Execute a 60-minute comprehensive SEO audit
/coord site-audit

# Or specify your domain explicitly  
/coord site-audit --domain=www.yourdomain.com

# For verbose output with detailed logging
/coord site-audit --verbose --domain=www.yourdomain.com
```

**What Happens During the Audit:**

1. **Phase 1: Technical Analysis (15 minutes)**
   - Core Web Vitals assessment
   - Mobile responsiveness check
   - Site speed analysis
   - Crawlability and indexation review

2. **Phase 2: Content Evaluation (20 minutes)**
   - On-page SEO analysis
   - Content gaps identification
   - Internal linking structure
   - Meta tag optimization opportunities

3. **Phase 3: Competitive Intelligence (15 minutes)**
   - Competitor benchmarking
   - Keyword gap analysis
   - Backlink profile comparison
   - Market positioning assessment

4. **Phase 4: Strategic Recommendations (10 minutes)**
   - Prioritized action plan
   - Resource allocation suggestions
   - Timeline recommendations
   - ROI projections

### Understanding Your Audit Results

The site audit produces a comprehensive report with:

#### 1. Executive Summary
- **Overall SEO Score** (0-100)
- **Top 3 Critical Issues** requiring immediate attention
- **Quick Wins** for immediate implementation
- **Strategic Opportunities** for long-term growth

#### 2. Technical Health Report
- **Core Web Vitals Status**
  - Largest Contentful Paint (LCP)
  - First Input Delay (FID)
  - Cumulative Layout Shift (CLS)
- **Mobile Optimization Score**
- **Site Speed Metrics**
- **Crawl Error Summary**
- **Schema Markup Analysis**

#### 3. Content Optimization Analysis
- **Page-by-Page SEO Scores**
- **Missing or Duplicate Meta Tags**
- **Content Gap Opportunities**
- **Internal Linking Recommendations**
- **Image Optimization Needs**

#### 4. Competitive Landscape
- **Market Position Analysis**
- **Competitor Keyword Advantages**
- **Content Topics to Target**
- **Link Building Opportunities**

#### 5. Prioritized Action Plan
```
IMMEDIATE (Week 1):
□ Fix Core Web Vitals issues on homepage
□ Add missing meta descriptions
□ Optimize images for page speed

SHORT-TERM (Month 1):
□ Create content for identified gaps
□ Implement technical SEO fixes
□ Build internal linking structure

LONG-TERM (Quarters 1-2):
□ Execute link building strategy
□ Expand content marketing
□ Monitor and iterate
```

### Acting on Audit Recommendations

**Immediate Actions (First 24 Hours):**

1. **Fix Critical Technical Issues**
```bash
# Launch technical fix mission for urgent items
/coord technical-fix --priority=critical
```

2. **Optimize High-Impact Pages**
```bash
# Focus on top-performing pages
@seo-content optimize meta tags for top 10 pages
```

3. **Address Core Web Vitals**
```bash
# Target specific performance issues
@seo-technical fix LCP issues on homepage
```

**First Week Actions:**

1. **Content Gap Analysis**
```bash
# Identify content opportunities
/coord content-gap --focus=quick-wins
```

2. **Competitive Research**
```bash
# Analyze top competitors
@seo-researcher analyze top 3 competitors in [your industry]
```

3. **Performance Baseline**
```bash
# Establish tracking benchmarks
@seo-analyst create performance baseline report
```

## Complete Command Reference

### Mission Execution Commands

#### Core SEO Missions
```bash
# Interactive mission launcher with guided setup
/coord

# Comprehensive site analysis (60 minutes)
/coord site-audit [--domain=example.com] [--verbose]

# Content opportunity discovery (2-4 hours)
/coord content-gap [--focus=keywords|topics|competitors] [--depth=shallow|deep]

# Technical optimization mission (4-8 hours)
/coord technical-fix [--priority=critical|high|medium] [--focus=speed|mobile|crawl]

# Keyword research and analysis (1-3 hours)
/coord keyword-research [--industry=niche] [--location=city,country]

# Link building strategy development (3-6 hours)
/coord link-building [--strategy=outreach|content|broken] [--budget=low|medium|high]
```

#### Development and Deployment Missions
```bash
# Build new features or pages
/coord build [feature_name] [--priority=low|medium|high]

# Fix existing issues
/coord fix [issue_description] [--urgent]

# Refactor and optimize existing code
/coord refactor [component_name] [--scope=performance|structure|both]

# MVP development for new projects
/coord mvp [project_name] [--timeline=weeks]

# Deployment and launch coordination
/coord deploy [environment] [--checks=full|basic]
```

### Direct Agent Communication

#### Strategic Planning
```bash
# Long-term strategy development
/meeting @seo-strategist "develop Q1 SEO strategy for [industry]"
/meeting @seo-strategist "analyze competitor landscape in [niche]"
/meeting @seo-strategist "create content marketing roadmap"
```

#### Technical Optimization
```bash
# Core Web Vitals and performance
/meeting @seo-technical "audit Core Web Vitals for homepage"
/meeting @seo-technical "optimize site speed for mobile users"
/meeting @seo-technical "implement structured data for products"
```

#### Content Development
```bash
# Content optimization and creation
/meeting @seo-content "optimize meta descriptions for blog posts"
/meeting @seo-content "create content brief for [topic]"
/meeting @seo-content "audit internal linking structure"
```

#### Keyword Research
```bash
# Market and keyword intelligence
/meeting @seo-researcher "find long-tail keywords for [topic]"
/meeting @seo-researcher "analyze seasonal search trends"
/meeting @seo-researcher "identify local SEO opportunities"
```

#### Performance Analysis
```bash
# Data analysis and reporting
/meeting @seo-analyst "create monthly performance report"
/meeting @seo-analyst "analyze traffic drop for [date range]"
/meeting @seo-analyst "track keyword ranking improvements"
```

#### Link Building
```bash
# Authority building and outreach
/meeting @seo-builder "identify link opportunities in [niche]"
/meeting @seo-builder "create outreach strategy for [campaign]"
/meeting @seo-builder "audit current backlink profile"
```

### Performance Monitoring Commands

#### Real-time Tracking
```bash
# Current keyword position tracking
/rankings [--keywords=primary|secondary|all] [--period=week|month|quarter]

# Traffic and conversion analysis
/traffic-report [--period=7d|30d|90d] [--compare=previous|year]

# Technical health monitoring
/technical-health [--checks=speed|mobile|crawl|all] [--format=summary|detailed]

# Competitive position tracking
/competitor-watch [--competitors=list] [--metrics=rankings|traffic|content]
```

#### Reporting and Analytics
```bash
# Generate comprehensive reports
/generate-report [--type=monthly|quarterly|annual] [--format=pdf|html|dashboard]

# Performance alerts and notifications
/set-alerts [--metrics=rankings|traffic|errors] [--threshold=percentage]

# ROI and conversion tracking
/roi-analysis [--period=month|quarter] [--attribution=first|last|multi]
```

### Common Command Patterns

#### Troubleshooting Commands
```bash
# Debug agent communication issues
/debug agents [--verbose]

# Validate configuration files
/validate config [--fix-errors]

# Check system health
/system-check [--detailed]

# Reset agent states
/reset agents [--confirm]
```

#### Batch Operations
```bash
# Execute multiple missions in sequence
/coord batch [mission1,mission2,mission3] [--parallel=false]

# Bulk content optimization
/meeting @seo-content "batch optimize [page_list] for target keywords"

# Mass data collection
/meeting @seo-researcher "bulk keyword research for [topic_list]"
```

#### Advanced Configurations
```bash
# Custom mission creation
/create-mission [mission_name] [--template=existing_mission]

# Agent behavior modification
/tune-agent @agent-name [--parameter=value] [--save-preset=name]

# Integration testing
/test-integration [--service=gsc|ga4|ahrefs] [--verbose]
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

## Configuration Deep Dive

### 1. Business Context Customization

**Complete business configuration template:**

```yaml
# .claude/config/business-context.yml
business_info:
  name: "Your Business Name"
  domain: "yourdomain.com"
  primary_domain: "yourdomain.com"      # Main domain
  additional_domains:                    # Subdomains or other domains
    - "blog.yourdomain.com"
    - "shop.yourdomain.com"
  industry: "your_industry"              # e.g., "ecommerce", "saas", "consulting"
  business_type: "b2b"                   # b2b, b2c, or both
  target_audience: "your_audience"       # Primary customer segment
  geographic_focus:
    - "United States"
    - "Canada"
  languages:
    - "en-US"
    - "en-CA"
  company_size: "startup"                # startup, small, medium, enterprise
  
seo_objectives:
  primary_goals:
    - "increase_organic_traffic"         # Main SEO objectives
    - "improve_local_visibility"
    - "boost_conversion_rates"
    - "enhance_brand_awareness"
  success_metrics:
    - "organic_sessions"                 # Key performance indicators
    - "keyword_rankings"
    - "conversion_rate"
    - "revenue_from_organic"
  quarterly_targets:
    q1: "20% traffic increase"           # Specific quarterly goals
    q2: "50 new keyword rankings"
    q3: "15% conversion improvement"
    q4: "30% revenue growth"

target_keywords:
  primary:                              # Top priority keywords
    - "main keyword 1"
    - "main keyword 2"
    - "main keyword 3"
  secondary:                            # Supporting keywords
    - "supporting keyword 1"
    - "supporting keyword 2"
    - "long tail keyword phrase"
  local:                                # Location-based keywords
    - "service in city"
    - "business near me"
  branded:                              # Brand-related keywords
    - "your brand name"
    - "your brand + service"

competitor_info:
  primary_competitors:                  # Direct competitors
    - domain: "competitor1.com"
      name: "Competitor One"
      strength: "content marketing"
    - domain: "competitor2.com"
      name: "Competitor Two"
      strength: "technical SEO"
  secondary_competitors:                # Indirect competitors
    - "competitor3.com"
    - "competitor4.com"

content_strategy:
  content_types:                        # Types of content to create
    - "blog_posts"
    - "product_pages"
    - "landing_pages"
    - "case_studies"
  content_themes:                       # Main content topics
    - "industry_insights"
    - "how_to_guides"
    - "product_comparisons"
  publishing_frequency: "weekly"        # Content publishing schedule
  content_goals:
    - "establish_authority"
    - "drive_conversions"
    - "support_customer_journey"

technical_setup:
  cms: "wordpress"                      # Content management system
  hosting: "aws"                        # Hosting provider
  cdn: "cloudflare"                     # Content delivery network
  analytics:
    google_analytics: "GA4-MEASUREMENT-ID"
    google_tag_manager: "GTM-ID"
  integrations:
    google_search_console: true
    google_my_business: true
    social_media_profiles:
      - "https://linkedin.com/company/yourcompany"
      - "https://twitter.com/yourhandle"
```

### 2. Agent Fine-Tuning

**Customize agent behavior for your specific needs:**

```yaml
# .claude/config/agent-preferences.yml
agent_settings:
  seo_strategist:
    focus_areas:
      - "competitive_analysis"
      - "market_research"
      - "strategic_planning"
    analysis_depth: "comprehensive"      # shallow, moderate, comprehensive
    reporting_style: "executive"         # technical, balanced, executive
    
  seo_technical:
    priority_metrics:
      - "core_web_vitals"
      - "mobile_optimization"
      - "site_speed"
    technical_level: "advanced"          # basic, intermediate, advanced
    automation_preference: "high"        # low, medium, high
    
  seo_content:
    writing_style: "professional"        # casual, professional, academic
    content_length_preference: "long_form" # short, medium, long_form
    optimization_focus:
      - "user_experience"
      - "search_visibility"
      - "conversion_optimization"
      
  seo_researcher:
    data_sources:
      - "google_keyword_planner"
      - "search_console"
      - "third_party_tools"
    research_scope: "comprehensive"      # focused, balanced, comprehensive
    keyword_difficulty_preference: "mixed" # easy, medium, hard, mixed
    
  seo_analyst:
    reporting_frequency: "weekly"        # daily, weekly, monthly
    data_visualization: "detailed"       # simple, standard, detailed
    focus_metrics:
      - "organic_traffic"
      - "keyword_rankings"
      - "conversion_rates"
      - "technical_health"
      
  seo_builder:
    outreach_style: "personalized"       # template, semi_custom, personalized
    link_quality_standard: "high"        # medium, high, premium
    relationship_focus: "long_term"       # transactional, balanced, long_term
```

### 3. Mission Scheduling and Automation

**Set up automated SEO workflows:**

```yaml
# .claude/config/mission-schedule.yml
scheduled_missions:
  daily:
    - mission: "technical-health"
      time: "09:00"
      parameters:
        checks: ["uptime", "speed", "errors"]
        
  weekly:
    - mission: "traffic-report"
      day: "monday"
      time: "10:00"
      recipients: ["team@company.com"]
      
    - mission: "ranking-update"
      day: "friday"
      time: "14:00"
      focus: "primary_keywords"
      
  monthly:
    - mission: "site-audit"
      day: 1
      time: "08:00"
      depth: "comprehensive"
      
    - mission: "content-gap"
      day: 15
      time: "11:00"
      focus: "competitor_analysis"
      
  quarterly:
    - mission: "strategy-review"
      month: [1, 4, 7, 10]
      day: 15
      deliverables:
        - "performance_report"
        - "strategy_updates"
        - "goal_adjustments"
        
automation_rules:
  traffic_alerts:
    threshold: "-20%"                    # Alert if traffic drops 20%
    comparison_period: "week_over_week"
    notification_methods: ["email", "slack"]
    
  ranking_alerts:
    position_change: 5                   # Alert if rankings drop 5+ positions
    keywords: "primary"                  # Monitor primary keywords only
    frequency: "daily"
    
  technical_alerts:
    core_web_vitals_threshold: "poor"    # Alert on poor CWV scores
    uptime_threshold: 99.5               # Alert if uptime drops below 99.5%
    response_time_threshold: 3000        # Alert if response time > 3s
```

### 4. Performance Optimization Settings

**Configure system performance for optimal agent operation:**

```yaml
# .claude/config/performance.yml
performance_settings:
  concurrent_missions: 2                 # Max missions running simultaneously
  agent_response_timeout: 300           # Seconds before agent times out
  data_cache_duration: 3600             # Cache duration in seconds
  batch_processing_size: 50             # Items processed in each batch
  
memory_management:
  max_context_length: 32000             # Maximum context window
  cleanup_frequency: "daily"            # Cleanup temp files daily
  log_retention: "30_days"              # Keep logs for 30 days
  
api_rate_limits:
  google_search_console:
    requests_per_day: 25000
    requests_per_100_seconds: 1200
  google_analytics:
    requests_per_day: 50000
    requests_per_100_seconds: 2000
  third_party_seo_tools:
    requests_per_minute: 60
    daily_limit: 10000
```

### 5. Integration Configuration

**Set up third-party service integrations:**

```yaml
# .claude/config/integrations.yml
integrations:
  google_services:
    search_console:
      property_url: "https://yourdomain.com/"
      site_verification: "google-site-verification=TOKEN"
    analytics:
      measurement_id: "G-XXXXXXXXXX"
      property_id: "123456789"
      
  seo_tools:
    ahrefs:
      api_key: "${AHREFS_API_KEY}"       # Environment variable
      rate_limit: 500                    # Requests per hour
    semrush:
      api_key: "${SEMRUSH_API_KEY}"
      database: "us"                     # Geographic database
    moz:
      access_id: "${MOZ_ACCESS_ID}"
      secret_key: "${MOZ_SECRET_KEY}"
      
  cms_integrations:
    wordpress:
      site_url: "https://yourdomain.com"
      api_endpoint: "/wp-json/wp/v2/"
      authentication: "jwt"             # jwt, basic, or oauth
    shopify:
      shop_name: "yourshop"
      api_version: "2023-04"
      
  notification_services:
    slack:
      webhook_url: "${SLACK_WEBHOOK_URL}"
      channel: "#seo-alerts"
    email:
      smtp_server: "smtp.gmail.com"
      port: 587
      recipients:
        - "seo-team@company.com"
        - "marketing@company.com"
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

## Comprehensive Troubleshooting Guide

### Common Installation Issues

#### Problem: Installation Script Fails
**Symptoms:**
- `./scripts/install.sh` returns errors
- Permission denied messages
- Missing dependencies

**Solutions:**
```bash
# Fix permissions
chmod +x scripts/install.sh

# Install missing dependencies (macOS)
brew install git node npm

# Install missing dependencies (Ubuntu/Debian)
sudo apt update && sudo apt install git nodejs npm

# Run with verbose output to see detailed errors
bash -x scripts/install.sh
```

#### Problem: Git Clone Fails
**Symptoms:**
- Repository not found errors
- Authentication failures
- Network timeouts

**Solutions:**
```bash
# Use HTTPS instead of SSH
git clone https://github.com/TheWayWithin/SEO-AGENT.git

# Configure git credentials
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check internet connection
ping github.com
```

### Agent Communication Issues

#### Problem: Agents Not Loading
**Symptoms:**
- "Agent not found" errors
- Empty agent list
- Incomplete agent responses

**Diagnostic Steps:**
```bash
# Check agent files exist and are valid
ls -la .claude/agents/
wc -l .claude/agents/*.md

# Validate agent file syntax
# Each agent file should have:
# - Proper markdown headers
# - Required sections (CORE CAPABILITIES, SCOPE BOUNDARIES)
# - No syntax errors

# Check Claude Code configuration
cat .claude/config.json
```

**Solutions:**
```bash
# Reinstall agents
cp -r templates/agents/* .claude/agents/

# Reset Claude Code configuration
rm -rf .claude/config.json
claude-code --reset

# Restart with verbose logging
claude-code --verbose
```

#### Problem: Agent Responses Are Generic
**Symptoms:**
- Agents don't use specialized knowledge
- Responses lack SEO expertise
- No context from business configuration

**Solutions:**
```bash
# Verify business context is loaded
cat .claude/config/business-context.yml

# Check agent specialization files
grep -n "CORE CAPABILITIES" .claude/agents/seo-*.md

# Reload agents with fresh context
/reset agents --confirm
/coord --reload-context
```

### Mission Execution Problems

#### Problem: Missions Fail to Start
**Symptoms:**
- "Mission not found" errors
- Timeout during mission initialization
- Missing mission parameters

**Diagnostic Commands:**
```bash
# List available missions
ls -la missions/
ls -la .claude/missions/

# Validate mission file syntax
head -20 missions/mission-*.md

# Check system resources
top
df -h
```

**Solutions:**
```bash
# Reinstall mission templates
cp -r missions/* .claude/missions/

# Fix mission file permissions
chmod 644 .claude/missions/*.md

# Run with debug mode
/coord site-audit --debug --verbose
```

#### Problem: Missions Stop Mid-Execution
**Symptoms:**
- Missions hang or freeze
- Partial results delivered
- Agent communication timeouts

**Solutions:**
```bash
# Check for resource constraints
# Increase memory limit if needed
export NODE_OPTIONS="--max-old-space-size=8192"

# Reduce concurrent operations
# Edit .claude/config/performance.yml:
# concurrent_missions: 1

# Clear caches and temporary files
rm -rf .claude/temp/*
rm -rf .claude/cache/*

# Restart with clean state
/reset system --confirm
```

### Integration and API Issues

#### Problem: Google Services Not Working
**Symptoms:**
- Google Search Console data not available
- Google Analytics integration fails
- Authentication errors

**Solutions:**
```bash
# Verify API credentials
cat .claude/config/google-credentials.json

# Test API connectivity
# This should be done through the agents:
@seo-analyst test Google Search Console connection
@seo-analyst verify Google Analytics access

# Regenerate API credentials if needed
# 1. Go to Google Cloud Console
# 2. Create new service account
# 3. Download new credentials JSON
# 4. Replace .claude/config/google-credentials.json
```

#### Problem: SEO Tool APIs Failing
**Symptoms:**
- Ahrefs/SEMrush/Moz data not loading
- Rate limit errors
- Invalid API key messages

**Solutions:**
```bash
# Check API key configuration
grep -r "API_KEY" .claude/config/

# Test API keys (replace with your actual keys)
curl -H "Authorization: Bearer YOUR_API_KEY" "https://apiv2.ahrefs.com/v2/domain-rating"

# Configure rate limiting
# Edit .claude/config/integrations.yml
# Reduce request rates if hitting limits
```

### Performance and Resource Issues

#### Problem: Slow Performance
**Symptoms:**
- Long response times (>30 seconds)
- High CPU/memory usage
- System freezing during operations

**Performance Optimization:**
```bash
# Monitor resource usage
top -p $(pgrep -f claude-code)
htop

# Optimize configuration
# In .claude/config/performance.yml:
concurrent_missions: 1          # Reduce from default 2
agent_response_timeout: 180     # Reduce from default 300
data_cache_duration: 7200       # Increase cache duration

# Clear system caches
sudo purge  # macOS
sudo sysctl -w vm.drop_caches=3  # Linux

# Restart services
pkill -f claude-code
claude-code
```

#### Problem: Memory Issues
**Symptoms:**
- Out of memory errors
- System becoming unresponsive
- Process killed messages

**Solutions:**
```bash
# Increase Node.js memory limit
export NODE_OPTIONS="--max-old-space-size=16384"

# Monitor memory usage
ps aux | grep claude-code
watch -n 1 'ps aux | grep claude-code'

# Optimize memory usage
# In .claude/config/performance.yml:
max_context_length: 16000       # Reduce from default 32000
batch_processing_size: 25       # Reduce from default 50
cleanup_frequency: "hourly"     # More frequent cleanup
```

### Debug Mode and Logging

#### Enable Comprehensive Logging
```bash
# Start Claude Code with maximum verbosity
claude-code --verbose --debug --log-level=debug

# Enable mission-specific logging
/coord site-audit --verbose --debug --log-file=audit.log

# Enable agent communication logging
/debug agents --trace-communication
```

#### Log File Locations
```bash
# System logs
tail -f .claude/logs/system.log
tail -f .claude/logs/missions.log
tail -f .claude/logs/agents.log

# Error logs
tail -f .claude/logs/errors.log
grep -i error .claude/logs/*.log

# Performance logs
tail -f .claude/logs/performance.log
```

### Getting Help and Support

#### Before Contacting Support
Gather this diagnostic information:

```bash
# System information
system_profiler SPSoftwareDataType  # macOS
uname -a && lsb_release -a          # Linux

# Claude Code version
claude-code --version

# Configuration validation
/validate config --full-report

# Recent error logs
tail -50 .claude/logs/errors.log

# Agent status
/debug agents --status-report
```

#### Support Channels
- **GitHub Issues**: [Create detailed bug report](https://github.com/TheWayWithin/SEO-AGENT/issues)
- **Documentation**: Check `/docs` folder for additional guides
- **Community Forum**: [Join discussions](https://github.com/TheWayWithin/SEO-AGENT/discussions)
- **Website**: [Visit support center](https://www.seoagent.work/support)

#### Creating Effective Bug Reports
Include these details:
1. **Environment**: OS, Claude Code version, system specs
2. **Configuration**: Relevant config files (sanitized)
3. **Steps to Reproduce**: Exact commands that cause the issue
4. **Expected vs Actual**: What should happen vs what actually happens
5. **Logs**: Relevant log entries and error messages
6. **Screenshots**: If UI-related issues

### Emergency Recovery Procedures

#### Complete System Reset
```bash
# Backup current configuration
cp -r .claude/config .claude/config.backup

# Reset to defaults
rm -rf .claude/agents/* .claude/missions/* .claude/config/*
./scripts/install.sh

# Restore business configuration
cp .claude/config.backup/business-context.yml .claude/config/

# Restart Claude Code
claude-code
```

#### Selective Recovery
```bash
# Reset only agents
rm -rf .claude/agents/*
cp -r agents/* .claude/agents/

# Reset only missions
rm -rf .claude/missions/*
cp -r missions/* .claude/missions/

# Reset only configuration (keep business context)
find .claude/config -name "*.yml" ! -name "business-context.yml" -delete
./scripts/configure.sh
```

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

## Success Checklist

### Initial Setup Complete ✅
- [ ] Repository cloned and installed
- [ ] Business context configured
- [ ] All 6 agents loaded successfully
- [ ] Google integrations connected
- [ ] First audit mission completed

### First Week Milestones 🎯
- [ ] Critical technical issues addressed
- [ ] Content optimization priorities identified
- [ ] Performance baseline established
- [ ] Competitive analysis completed
- [ ] Action plan created and prioritized

### Ongoing Operations 📈
- [ ] Weekly performance monitoring
- [ ] Monthly comprehensive audits
- [ ] Quarterly strategy reviews
- [ ] Continuous optimization based on data

## What's Next?

### Immediate Actions (Next 2 Hours)
1. **Run Your First Audit**: `/coord site-audit --domain=yourdomain.com`
2. **Review Results**: Understand your current SEO baseline
3. **Prioritize Actions**: Focus on high-impact, quick-win opportunities
4. **Set Up Monitoring**: Configure performance tracking and alerts

### This Week's Focus
1. **Technical Optimization**: Address Core Web Vitals and site speed
2. **Content Analysis**: Identify and fill content gaps
3. **Competitive Research**: Understand your market landscape
4. **Baseline Establishment**: Document current performance metrics

### Long-term Success
1. **Strategic Planning**: Develop comprehensive SEO roadmap
2. **Content Calendar**: Plan and execute content marketing
3. **Authority Building**: Implement link building strategies
4. **Performance Optimization**: Continuously improve based on data

---

**Ready to transform your SEO? Start with `/coord site-audit` now!**

> 💡 **Pro Tip**: Your first audit will take 45-60 minutes but will provide a comprehensive foundation for all future SEO efforts. The insights you gain will guide your optimization strategy for months to come.

**Need help?** Use `/coord` for guided mission selection or `/debug agents` if you encounter any issues.