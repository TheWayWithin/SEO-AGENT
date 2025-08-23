# MCP Integration Guide for SEO Agent Library

## Overview

Model Context Protocol (MCP) integrations are essential for connecting your SEO agents to external platforms and data sources. This guide provides step-by-step instructions for integrating the required MCPs to power your SEO Agent Library with real-time data and automation capabilities.

**Time to complete:** 2-4 hours (depending on API approvals)  
**Prerequisites:** Active accounts on Google Search Console, Google Analytics, and at least one SEO platform

## Integration Priority Matrix

| Priority | Integration | Required For | Setup Time |
|----------|-------------|--------------|------------|
| **CRITICAL** | Google Search Console | All agents | 30 minutes |
| **CRITICAL** | Google Analytics 4 | SEO Strategist, Analyst | 45 minutes |
| **HIGH** | Ahrefs/SEMrush/Moz | SEO Strategist, Researcher | 1-2 hours |
| **MEDIUM** | WordPress/CMS | SEO Content | 30 minutes |
| **OPTIONAL** | Screaming Frog | SEO Technical | 15 minutes |

## 1. Google Search Console MCP Setup

### Prerequisites
- Verified property in Google Search Console
- Google Cloud Platform project (free tier sufficient)
- Domain verification completed

### Step-by-Step Configuration

#### 1.1 Enable Google Search Console API
```bash
# Navigate to Google Cloud Console
# Enable Search Console API for your project
https://console.cloud.google.com/apis/library/searchconsole.googleapis.com
```

#### 1.2 Create Service Account
1. Go to **IAM & Admin > Service Accounts**
2. Click **Create Service Account**
3. Name: `seo-agents-gsc`
4. Description: `SEO Agent Library - Google Search Console access`
5. Click **Create and Continue**

#### 1.3 Download Credentials
1. Select your service account
2. Go to **Keys** tab
3. Click **Add Key > Create New Key**
4. Choose **JSON** format
5. Save as `gsc-credentials.json` in secure location

#### 1.4 Grant Search Console Access
1. Open Google Search Console
2. Go to **Settings > Users and permissions**
3. Click **Add user**
4. Add your service account email (ends with `.iam.gserviceaccount.com`)
5. Set permission to **Full**

#### 1.5 Configure MCP Connection
```yaml
# Add to .claude/config/mcp-connections.yml
google_search_console:
  type: gsc
  credentials_path: "/path/to/gsc-credentials.json"
  properties:
    - "https://www.yourdomain.com/"
    - "sc-domain:yourdomain.com"
  rate_limits:
    requests_per_day: 1000
    requests_per_minute: 10
```

#### 1.6 Test Connection
```bash
# Run connection test
claude-code test-mcp --service=google_search_console

# Expected output:
# ✅ GSC Connection: Active
# ✅ Property Access: 2 properties found
# ✅ Data Retrieval: Last 7 days available
```

### Common Troubleshooting

**Error: "Insufficient permissions"**
- Verify service account has Full access in GSC
- Check property URL matches exactly (with/without www)
- Ensure domain verification is complete

**Error: "API quota exceeded"**
- Default quota: 1000 requests/day
- Monitor usage in Google Cloud Console
- Request quota increase if needed

## 2. Google Analytics 4 MCP Setup

### Prerequisites
- GA4 property configured and collecting data
- Google Cloud Platform project
- Admin access to GA4 property

### Step-by-Step Configuration

#### 2.1 Enable Google Analytics API
```bash
# Navigate to Google Cloud Console
# Enable Analytics Reporting API and Analytics Data API
https://console.cloud.google.com/apis/library/analyticsreporting.googleapis.com
https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com
```

#### 2.2 Create Service Account (if not done for GSC)
1. Go to **IAM & Admin > Service Accounts**
2. Click **Create Service Account**
3. Name: `seo-agents-analytics`
4. Description: `SEO Agent Library - Google Analytics access`
5. Download JSON credentials

#### 2.3 Grant Analytics Access
1. Open Google Analytics 4
2. Go to **Admin > Property > Property Access Management**
3. Click **+** to add user
4. Add service account email
5. Set role to **Viewer** (sufficient for reporting)

#### 2.4 Find Property ID
1. In GA4, go to **Admin > Property Settings**
2. Copy **Property ID** (format: 12345678901)

#### 2.5 Configure MCP Connection
```yaml
# Add to .claude/config/mcp-connections.yml
google_analytics:
  type: ga4
  credentials_path: "/path/to/ga4-credentials.json"
  property_id: "123456789"
  default_date_range: "30daysAgo"
  rate_limits:
    requests_per_day: 25000
    concurrent_requests: 10
```

#### 2.6 Test Connection
```bash
# Run connection test
claude-code test-mcp --service=google_analytics

# Expected output:
# ✅ GA4 Connection: Active
# ✅ Property Access: Property 123456789
# ✅ Data Retrieval: 30 days of data available
```

### Data Streams and Dimensions

**Critical Metrics Available:**
- Sessions, Users, Page Views
- Organic traffic (source/medium = organic)
- Conversion events and revenue
- User behavior and engagement metrics

**Custom Dimensions Setup:**
1. Configure **Content Group** for page categorization
2. Set up **Custom Parameters** for SEO tracking
3. Enable **Enhanced Ecommerce** for revenue attribution

## 3. SEO Platform MCPs (Ahrefs/SEMrush/Moz)

### Option A: Ahrefs MCP Integration

#### Prerequisites
- Active Ahrefs subscription (Lite plan minimum)
- API access enabled in account settings

#### Setup Process
1. **Get API Key:**
   - Login to Ahrefs > Account & Billing > API Access
   - Generate new API token
   - Note monthly query limits based on plan

2. **Configure Connection:**
```yaml
# Add to .claude/config/mcp-connections.yml
ahrefs:
  type: ahrefs
  api_key: "your_ahrefs_api_key"
  rate_limits:
    requests_per_minute: 60  # Standard plan
    requests_per_month: 5000 # Varies by plan
  endpoints:
    - domain_rating
    - backlinks
    - organic_keywords
    - content_gap
```

3. **Test Integration:**
```bash
claude-code test-mcp --service=ahrefs
# Should return domain metrics for test domain
```

#### Cost Considerations
- **Lite Plan:** $99/month, 5,000 API queries
- **Standard Plan:** $199/month, 15,000 API queries  
- **Advanced Plan:** $399/month, 30,000 API queries

### Option B: SEMrush MCP Integration

#### Prerequisites
- SEMrush subscription with API access
- API units available in account

#### Setup Process
1. **Get API Key:**
   - SEMrush > My Profile > API
   - Copy API key
   - Check available API units

2. **Configure Connection:**
```yaml
# Add to .claude/config/mcp-connections.yml
semrush:
  type: semrush
  api_key: "your_semrush_api_key"
  rate_limits:
    requests_per_second: 1
    api_units_per_month: 10000  # Based on plan
  databases:
    - us  # Primary database
    - uk  # Additional if needed
```

### Option C: Moz MCP Integration

#### Prerequisites  
- Moz Pro subscription
- API access credentials

#### Setup Process
1. **Get Credentials:**
   - Moz > Help > API Documentation
   - Generate Access ID and Secret Key

2. **Configure Connection:**
```yaml
# Add to .claude/config/mcp-connections.yml
moz:
  type: moz
  access_id: "your_moz_access_id"
  secret_key: "your_moz_secret_key"
  rate_limits:
    requests_per_10_seconds: 10
    rows_per_month: 120000  # Medium plan
```

### Free Alternatives for Testing

**Limited Free Options:**
1. **Google Keyword Planner** - Keyword research (requires Google Ads account)
2. **Bing Webmaster Tools** - Basic search performance data
3. **Serpstat Free Plan** - 50 queries/day
4. **Ubersuggest Free** - 3 searches/day

**Configuration for Free Tools:**
```yaml
# Add to .claude/config/mcp-connections.yml
free_tools:
  google_keyword_planner:
    type: gkp
    credentials_path: "/path/to/google-ads-credentials.json"
  bing_webmaster_tools:
    type: bwt
    api_key: "your_bing_api_key"
```

## 4. Agent-MCP Mapping Table

### Complete Integration Matrix

| Agent | Google Search Console | Google Analytics 4 | SEO Platform | CMS Integration | Technical Tools |
|-------|----------------------|-------------------|--------------|----------------|-----------------|
| **SEO Strategist** | ✅ Required | ✅ Required | ✅ Required | ❌ | ❌ |
| **SEO Technical** | ✅ Required | ❌ | ❌ | ❌ | ✅ Required |
| **SEO Content** | ✅ Required | ⚠️ Optional | ⚠️ Optional | ✅ Required | ❌ |
| **SEO Researcher** | ⚠️ Optional | ❌ | ✅ Required | ❌ | ❌ |
| **SEO Analyst** | ✅ Required | ✅ Required | ⚠️ Optional | ❌ | ❌ |
| **SEO Builder** | ⚠️ Optional | ❌ | ✅ Required | ❌ | ⚠️ Optional |

### Detailed Agent Requirements

#### SEO Strategist
```yaml
required_mcps:
  - google_search_console    # Performance analysis
  - google_analytics        # Traffic insights  
  - ahrefs_or_semrush       # Competitive intelligence
optional_mcps:
  - google_ads              # Paid search coordination
  - social_media_apis       # Social signals
```

#### SEO Technical  
```yaml
required_mcps:
  - google_search_console    # Technical health monitoring
  - screaming_frog          # Site crawling
  - pagespeed_insights       # Performance metrics
optional_mcps:
  - lighthouse              # Automated auditing
  - gtmetrix                # Additional performance data
```

#### SEO Content
```yaml
required_mcps:
  - google_search_console    # Content performance
  - wordpress_or_cms         # Content management
optional_mcps:
  - clearscope              # Content optimization
  - surfer_seo              # On-page optimization
  - google_analytics        # Content engagement
```

#### SEO Researcher
```yaml
required_mcps:
  - ahrefs_or_semrush       # Keyword research
  - google_keyword_planner  # Search volume data
optional_mcps:
  - answer_the_public       # Question research
  - google_trends           # Trend analysis
```

#### SEO Analyst
```yaml
required_mcps:
  - google_analytics        # Traffic analysis
  - google_search_console   # Search performance
optional_mcps:
  - data_studio             # Advanced reporting
  - microsoft_clarity       # User behavior analysis
```

#### SEO Builder
```yaml
required_mcps:
  - ahrefs_or_semrush       # Link prospecting
  - hunter_io               # Email finding
optional_mcps:
  - haro                    # PR opportunities
  - buzzsumo                # Content outreach
```

### CMS Integration Details

#### WordPress MCP Setup
```yaml
wordpress:
  type: wp_rest_api
  site_url: "https://yoursite.com"
  username: "api_user"
  application_password: "xxxx xxxx xxxx xxxx"
  capabilities:
    - edit_posts
    - manage_options
    - upload_files
```

#### Shopify MCP Setup
```yaml
shopify:
  type: shopify_admin_api
  shop_domain: "yourstore.myshopify.com"
  access_token: "shpat_xxxxxx"
  api_version: "2023-10"
  scopes:
    - read_products
    - write_products
    - read_content
```

## 5. Testing & Validation

### Pre-Deployment Checklist

#### Connection Tests
```bash
# Test all critical connections
claude-code test-mcp --service=all

# Individual service tests
claude-code test-mcp --service=google_search_console
claude-code test-mcp --service=google_analytics
claude-code test-mcp --service=ahrefs
```

#### Data Retrieval Validation
```bash
# Validate data access for each agent
claude-code validate-agent-data --agent=seo-strategist
claude-code validate-agent-data --agent=seo-technical  
claude-code validate-agent-data --agent=seo-content
claude-code validate-agent-data --agent=seo-researcher
claude-code validate-agent-data --agent=seo-analyst
claude-code validate-agent-data --agent=seo-builder
```

### Expected Test Results

#### Google Search Console Test
```json
{
  "status": "connected",
  "properties": [
    {
      "property_url": "https://www.yourdomain.com/",
      "verification_status": "verified",
      "permission_level": "full"
    }
  ],
  "data_availability": {
    "clicks": "90 days",
    "impressions": "90 days", 
    "coverage": "current",
    "mobile_usability": "current"
  }
}
```

#### Google Analytics Test
```json
{
  "status": "connected",
  "property_id": "123456789",
  "account_name": "Your Business",
  "data_streams": [
    {
      "stream_id": "987654321",
      "stream_name": "Web data stream",
      "url": "https://www.yourdomain.com"
    }
  ],
  "available_metrics": ["sessions", "users", "pageviews", "conversions"],
  "date_range": "365 days"
}
```

#### SEO Platform Test (Ahrefs Example)
```json
{
  "status": "connected",
  "subscription": "standard",
  "api_limits": {
    "monthly_quota": 15000,
    "used_this_month": 1247,
    "remaining": 13753
  },
  "available_endpoints": [
    "domain_rating",
    "backlinks", 
    "organic_keywords",
    "content_gap"
  ]
}
```

### Validation Commands

#### SEO Strategist Validation
```bash
# Test strategic data access
@seo-strategist "retrieve competitor analysis data for top 3 competitors"

# Expected response should include:
# - Domain authority metrics
# - Top organic keywords
# - Traffic estimates
# - Content gap opportunities
```

#### SEO Technical Validation  
```bash
# Test technical audit capabilities
@seo-technical "perform basic technical audit of homepage"

# Expected response should include:
# - Core Web Vitals scores
# - Technical SEO issues
# - Schema markup status
# - Mobile-friendly test results
```

#### SEO Analyst Validation
```bash
# Test analytics access
@seo-analyst "provide 30-day traffic summary"

# Expected response should include:
# - Organic traffic trends
# - Top performing pages
# - Conversion data
# - User behavior metrics
```

### Troubleshooting Common Issues

#### Authentication Errors
```bash
# Check credential file permissions
chmod 600 /path/to/credentials.json

# Verify service account email format
# Should end with @project-id.iam.gserviceaccount.com

# Test individual API endpoints
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://searchconsole.googleapis.com/webmasters/v3/sites"
```

#### Rate Limiting Issues
```yaml
# Adjust rate limits in configuration
rate_limits:
  requests_per_minute: 30    # Reduce if hitting limits
  concurrent_requests: 3     # Lower concurrency
  retry_delays: [1, 2, 4, 8] # Exponential backoff
```

#### Data Access Problems
1. **Verify permissions** in each platform
2. **Check date ranges** for data availability
3. **Confirm property/domain** matches exactly
4. **Test with minimal queries** first

### Performance Monitoring

#### Monitor API Usage
```bash
# Check API quota usage
claude-code monitor-api-usage --period=daily

# Set up alerts for quota limits
claude-code set-quota-alerts --threshold=80
```

#### Track Integration Health
```yaml
# Add to monitoring configuration
health_checks:
  google_search_console:
    frequency: hourly
    timeout: 30
    alerts: slack_webhook
  google_analytics:
    frequency: hourly  
    timeout: 45
    alerts: email
  seo_platform:
    frequency: daily
    timeout: 60
    alerts: slack_webhook
```

## Security Best Practices

### Credential Management
1. **Never commit credentials** to version control
2. **Use environment variables** for API keys
3. **Rotate credentials regularly** (quarterly)
4. **Implement least-privilege access** for service accounts
5. **Monitor access logs** for unusual activity

### API Security
```yaml
# Secure configuration example
security:
  credential_encryption: true
  api_key_rotation: 90  # days
  access_logging: enabled
  ip_restrictions: 
    - "your.office.ip.range"
  rate_limit_monitoring: enabled
```

### Access Control
- **Separate service accounts** for each environment (dev/staging/prod)
- **Limited scope permissions** based on agent requirements  
- **Regular access audits** and cleanup of unused accounts
- **Multi-factor authentication** on all platform accounts

## Support and Resources

### Documentation Links
- **Google Search Console API:** https://developers.google.com/webmaster-tools
- **Google Analytics API:** https://developers.google.com/analytics/devguides/reporting/data/v1
- **Ahrefs API:** https://ahrefs.com/api/documentation
- **SEMrush API:** https://www.semrush.com/api-documentation/
- **Moz API:** https://moz.com/help/guides/moz-api

### Getting Help
- **Setup Issues:** Check integration logs in `/logs/mcp-setup.log`
- **API Errors:** Consult platform-specific error codes and solutions
- **Performance Problems:** Monitor rate limits and adjust configurations
- **Agent Communication:** Verify MCP mappings match agent requirements

### Community Resources
- **GitHub Issues:** Report integration bugs and feature requests
- **Discord Community:** Get help from other SEO Agent Library users
- **Documentation Updates:** Contribute improvements to this guide

---

## Next Steps

1. ✅ **Start with Google Search Console** - Critical for all agents
2. ✅ **Add Google Analytics 4** - Essential for SEO Strategist and Analyst  
3. ✅ **Choose SEO platform** - Based on budget and feature needs
4. ✅ **Test all connections** - Validate before deploying agents
5. ✅ **Configure monitoring** - Set up health checks and alerts
6. ✅ **Run first mission** - Execute `/coord site-audit` to verify everything works

**Ready to power up your SEO agents? Start with the Google Search Console integration now!**