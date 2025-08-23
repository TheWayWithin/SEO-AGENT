# SearchOps-11 Quick Start Guide
## Deploy Your SEO Squad in 5 Minutes

## Prerequisites

- Claude Code installed and configured
- Access to your website's Google Search Console
- Google Analytics 4 property set up
- Basic SEO tool access (Ahrefs, SEMrush, or Moz)

## Installation

### 1. Clone and Deploy
```bash
# Clone the repository
git clone https://github.com/YourUsername/searchops-11.git
cd searchops-11

# Run the installation script
./install.sh
```

### 2. Configure Business Context
```bash
# Copy the FreeCalcHub example (or create your own)
cp examples/freecalchub-config.yml .claude/config/business-context.yml

# Edit for your business
nano .claude/config/business-context.yml
```

### 3. Set Up Integrations
```bash
# Run the integration setup script
./scripts/setup-integrations.sh

# Follow prompts to connect:
# - Google Search Console
# - Google Analytics 4
# - Your preferred SEO platform
```

### 4. Validate Configuration
```bash
# Verify everything is working
./scripts/validate-config.sh
```

## First Mission: Site Audit

Launch your first SEO mission:

```bash
# Start Claude Code in your project directory
claude-code

# Run comprehensive site audit
/coord site-audit
```

This will:
- Analyze your site's technical health
- Identify content opportunities
- Benchmark current performance
- Provide prioritized action plan

## Understanding Your Agents

### 🎯 The Strategist
**Role:** Mission coordinator and strategic planner
**When to use:** `/meeting @strategist "need quarterly SEO strategy"`
**Specializes in:** Competitive analysis, goal setting, resource allocation

### 🔧 The Technical
**Role:** Site health and performance optimization
**When to use:** `/meeting @technical "site speed issues"`
**Specializes in:** Core Web Vitals, crawlability, schema markup

### 📝 The Content
**Role:** Content optimization and creation guidance
**When to use:** `/meeting @content "need content briefs"`
**Specializes in:** On-page SEO, content gaps, internal linking

### 🔍 The Researcher
**Role:** Keyword and market intelligence
**When to use:** `/meeting @researcher "keyword opportunities"`
**Specializes in:** Keyword research, SERP analysis, trend identification

### 📊 The Analyst
**Role:** Performance tracking and insights
**When to use:** `/meeting @analyst "traffic analysis"`
**Specializes in:** ROI measurement, trend analysis, reporting

### 🔗 The Builder
**Role:** Link building and digital PR
**When to use:** `/meeting @builder "link campaign"`
**Specializes in:** Outreach, relationship building, authority development

## Essential Commands

### Mission Execution
```bash
/coord                    # Interactive mission launcher
/coord site-audit         # 60-minute comprehensive audit
/coord content-gap        # 2-4 hour content analysis
/coord technical-fix      # 4-8 hour technical optimization
/coord keyword-research   # 2-4 hour market intelligence
/coord ai-search-optimize # 1-3 day future-proofing
```

### Performance Monitoring
```bash
/rankings                 # Current keyword positions
/traffic-report          # Traffic and conversion analysis
/technical-health        # Site health monitoring
/content-performance     # Content engagement metrics
```

### Reporting
```bash
/report weekly           # Weekly performance summary
/report monthly          # Monthly strategic review
/report quarterly        # Quarterly goal assessment
```

## Configuration Examples

### FreeCalcHub Calculator Site
```yaml
business_type: "calculator_website"
primary_domain: "freecalchub.com"
target_audience: "people_needing_calculations"
main_categories:
  - "finance"
  - "math"
  - "health"
  - "conversions"
content_focus: "educational_calculators"
seo_priorities:
  - "technical_optimization"
  - "content_expansion"
  - "ai_search_readiness"
```

### Local Business
```yaml
business_type: "local_service"
primary_domain: "yourlocalbusiness.com"
service_area: "city_state"
target_audience: "local_customers"
main_services:
  - "service_1"
  - "service_2"
seo_priorities:
  - "local_visibility"
  - "review_management"
  - "citation_building"
```

### E-commerce Store
```yaml
business_type: "ecommerce"
primary_domain: "yourstore.com"
platform: "shopify"
product_categories:
  - "category_1"
  - "category_2"
seo_priorities:
  - "product_optimization"
  - "category_structure"
  - "shopping_feeds"
```

## Troubleshooting

### Common Issues

**Agents not responding:**
```bash
# Check agent status
/status

# Restart if needed
./scripts/validate-config.sh
```

**Integration failures:**
```bash
# Re-run integration setup
./scripts/setup-integrations.sh

# Check specific integration
/meeting @analyst "test analytics connection"
```

**Mission timeouts:**
```bash
# Check mission status
ls .claude/missions/active/

# Resume if needed
/coord resume-mission
```

## Next Steps

1. **Complete your first site audit** - Understand current state
2. **Set up weekly reporting** - Track progress automatically
3. **Execute content gap analysis** - Identify opportunities
4. **Implement technical fixes** - Improve site health
5. **Launch keyword research** - Expand visibility

## Getting Help

- Check [Agent Guide](docs/agent-guide.md) for detailed agent capabilities
- Review [Mission Guide](docs/mission-guide.md) for workflow explanations
- See [Integration Guide](docs/integration-guide.md) for setup help
- Visit [Troubleshooting](docs/troubleshooting.md) for common solutions

**Your SEO transformation starts now. Execute your first mission and watch the results.**

