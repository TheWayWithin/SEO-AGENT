# Troubleshooting Guide
## Resolve Issues and Optimize SEOAgent Performance

> Comprehensive troubleshooting guide for common issues, error resolution, and performance optimization. Get your SEO agents back to peak performance quickly.

## Quick Diagnostic Checklist

Before diving into specific issues, try these general solutions:

- [ ] **System Status Check**: Verify Claude Code is running properly
- [ ] **Agent Status**: Confirm all 6 SEO agents are loaded correctly  
- [ ] **Configuration Validation**: Check business context and integration settings
- [ ] **Recent Changes**: Review any recent configuration or system changes
- [ ] **Resource Availability**: Ensure adequate memory and processing capacity
- [ ] **API Connectivity**: Test connections to Google services and SEO tools

## Common Issues and Solutions

### Installation and Setup Issues

#### Problem: Installation Script Fails

**Symptoms**:
- `./scripts/install.sh` returns permission or dependency errors
- Missing files or incomplete directory structure
- Agent files not loading properly

**Solutions**:

```bash
# Fix permissions
chmod +x scripts/install.sh

# Install missing dependencies (macOS)
brew install git node npm

# Install missing dependencies (Ubuntu/Debian)  
sudo apt update && sudo apt install git nodejs npm

# Run with verbose output to see detailed errors
bash -x scripts/install.sh

# Manual installation if script fails
mkdir -p .claude/{agents,config,missions,commands}
cp agents/* .claude/agents/
cp missions/* .claude/missions/
cp examples/seoagent-work-config.yml .claude/config/business-context.yml
```

**Prevention**:
- Verify system requirements before installation
- Check internet connectivity for dependency downloads
- Run installation script from repository root directory

#### Problem: Business Context Configuration Errors

**Symptoms**:
- Agents provide generic responses without business context
- Missing domain or industry-specific insights
- Configuration validation fails

**Solutions**:

```bash
# Verify business context file exists and is valid
cat .claude/config/business-context.yml

# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('.claude/config/business-context.yml'))"

# Copy and customize from template if missing
cp examples/seoagent-work-config.yml .claude/config/business-context.yml
nano .claude/config/business-context.yml

# Minimal required configuration
cat > .claude/config/business-context.yml << EOF
business_info:
  name: "Your Business Name"
  domain: "yourdomain.com"
  industry: "your_industry"
  target_audience: "your_audience"
  
seo_objectives:
  primary_goals:
    - "increase_organic_traffic"
    - "improve_conversion_rates"
EOF
```

### Agent Communication Issues

#### Problem: Agents Not Loading or Responding

**Symptoms**:
- "Agent not found" errors when using @seo-[agent] commands
- Generic responses instead of specialized expertise
- Empty or incomplete agent responses

**Diagnostic Steps**:
```bash
# Check agent files exist
ls -la .claude/agents/
echo "Expected files: seo-strategist.md, seo-technical.md, seo-content.md, seo-researcher.md, seo-analyst.md, seo-builder.md"

# Verify agent file structure
head -10 .claude/agents/seo-strategist.md
wc -l .claude/agents/*.md

# Check for syntax errors in agent files
grep -n "^#" .claude/agents/seo-strategist.md
```

**Solutions**:
```bash
# Reinstall agent files from source
cp agents/* .claude/agents/

# Verify agent files have proper permissions
chmod 644 .claude/agents/*.md

# Restart Claude Code to reload agents
# Exit Claude Code and restart

# Test agent communication individually
echo "Testing agent responses..."
# In Claude Code interface:
# @seo-strategist Hello, are you ready?
# @seo-technical Can you perform a basic health check?
```

#### Problem: Agent Scope Confusion or Conflicts

**Symptoms**:
- Multiple agents attempting same tasks
- Agents working outside their specialization
- Conflicting recommendations from different agents

**Solutions**:
```bash
# Review agent scope boundaries
grep -A 5 -B 5 "SCOPE BOUNDARIES" .claude/agents/*.md

# Reset agent coordination
@coordinator Reset all agent coordination and clarify scope boundaries

# Use explicit coordination protocols
@coordinator Request @seo-technical to handle Core Web Vitals optimization only
@coordinator Request @seo-content to focus on on-page optimization only

# Clear agent task assignment
@coordinator Assign specific agent responsibilities:
- @seo-strategist: Strategy and competitive analysis only
- @seo-technical: Technical implementation only  
- @seo-content: Content optimization only
```

### Mission Execution Problems

#### Problem: Missions Fail to Start or Complete

**Symptoms**:
- Mission initialization errors or timeouts
- Missions hang or stop mid-execution
- Incomplete deliverables or partial results

**Diagnostic Commands**:
```bash
# Check system resources
top | grep -i claude
df -h  # Check disk space
free -h  # Check available memory

# Validate mission templates
ls -la missions/
head -20 missions/site-audit.md

# Check for mission conflicts
# Look for overlapping or concurrent mission attempts
```

**Solutions**:
```bash
# Clear mission cache and temporary files
rm -rf .claude/temp/* .claude/cache/*

# Reduce system load
# Close unnecessary applications
# Limit concurrent missions to 1

# Restart with clean state  
# Exit Claude Code completely
# Clear system caches (if on macOS): sudo purge
# Restart Claude Code

# Use single-phase missions if full missions fail
@seo-strategist Perform strategic analysis only for [domain]
@seo-technical Audit Core Web Vitals only for homepage
```

#### Problem: Mission Coordination Failures

**Symptoms**:
- Agents not working together effectively
- Missing handoffs between mission phases  
- Inconsistent or conflicting deliverables

**Solutions**:
```bash
# Use explicit coordination patterns
@coordinator Coordinate mission phases explicitly:
1. @seo-strategist: Define audit scope and objectives
2. Wait for completion, then assign @seo-technical
3. Wait for technical analysis, then assign @seo-content

# Break complex missions into smaller parts
/coord site-audit-technical-only --domain=example.com
/coord site-audit-content-only --domain=example.com
/coord site-audit-strategic-only --domain=example.com

# Use sequential rather than parallel execution
@coordinator Execute mission phases in strict sequence with validation gates
```

### API and Integration Issues

#### Problem: Google Services Integration Failing

**Symptoms**:
- "Authentication failed" errors for Google Search Console
- Missing Google Analytics data in reports
- API quota exceeded messages

**Solutions**:

```bash
# Check Google service account credentials
ls -la .claude/config/google-credentials.json

# Test API connectivity (replace with actual testing method)
@seo-analyst Test Google Search Console connection for [domain]
@seo-analyst Verify Google Analytics access for property [GA4-ID]

# Regenerate Google credentials if needed:
# 1. Go to Google Cloud Console (console.cloud.google.com)
# 2. Navigate to APIs & Services > Credentials
# 3. Create new service account or download existing JSON key
# 4. Save as .claude/config/google-credentials.json
# 5. Ensure service account has proper permissions

# Configure API rate limiting
cat > .claude/config/api-limits.yml << EOF
google_search_console:
  requests_per_day: 25000
  requests_per_100_seconds: 1200
google_analytics:
  requests_per_day: 50000  
  requests_per_100_seconds: 2000
EOF
```

#### Problem: SEO Tool API Failures (Ahrefs/SEMrush/Moz)

**Symptoms**:
- Third-party SEO data not loading
- "Invalid API key" errors
- Rate limit exceeded messages

**Solutions**:
```bash
# Check API key configuration
grep -r "API_KEY" .claude/config/ 2>/dev/null || echo "No API keys found in config"

# Verify API key validity (example for Ahrefs)
# curl -H "Authorization: Bearer YOUR_API_KEY" "https://apiv2.ahrefs.com/v3/site-explorer/overview"

# Configure environment variables for API keys
echo 'export AHREFS_API_KEY="your_key_here"' >> ~/.bash_profile
echo 'export SEMRUSH_API_KEY="your_key_here"' >> ~/.bash_profile
source ~/.bash_profile

# Set conservative rate limits
cat > .claude/config/integrations.yml << EOF
seo_tools:
  ahrefs:
    requests_per_hour: 500
    daily_limit: 10000
  semrush:  
    requests_per_minute: 60
    daily_limit: 5000
EOF
```

### Performance and Resource Issues

#### Problem: Slow Performance or High Resource Usage

**Symptoms**:
- Long response times (>30 seconds) from agents
- High CPU or memory usage
- System becoming unresponsive during missions

**Performance Optimization**:
```bash
# Monitor resource usage
top -p $(pgrep -f claude) 2>/dev/null || echo "Claude process not found"
ps aux | grep claude | head -5

# Optimize configuration for performance
cat > .claude/config/performance.yml << EOF
performance_settings:
  concurrent_missions: 1          # Reduce from default 2
  agent_response_timeout: 120     # Reduce from default 300  
  data_cache_duration: 7200       # Increase cache duration
  batch_processing_size: 25       # Reduce batch size

memory_management:
  max_context_length: 16000       # Reduce from default 32000
  cleanup_frequency: "hourly"     # More frequent cleanup
  log_retention: "7_days"         # Reduce from default 30 days
EOF

# Clear system caches
# macOS: sudo purge
# Linux: sudo sysctl -w vm.drop_caches=3

# Increase Node.js memory limit if needed
export NODE_OPTIONS="--max-old-space-size=8192"
```

#### Problem: Memory Issues and Crashes

**Symptoms**:
- Out of memory errors
- Process killed unexpectedly
- System freezing during large missions

**Solutions**:
```bash
# Check memory usage patterns
while true; do ps aux | grep claude | grep -v grep; sleep 5; done

# Configure memory limits
export NODE_OPTIONS="--max-old-space-size=16384"  # 16GB limit

# Optimize memory usage
cat >> .claude/config/performance.yml << EOF
memory_optimization:
  enable_garbage_collection: true
  gc_frequency: "after_mission"
  clear_cache_on_completion: true
  max_concurrent_processes: 1
EOF

# Use memory-efficient mission patterns  
# Instead of: /coord site-audit --comprehensive
# Use: /coord site-audit-technical && /coord site-audit-content
```

## Error Code Reference

### Common Error Codes and Solutions

#### E001: Configuration Error
**Message**: "Business context configuration not found or invalid"
**Solution**: Verify `.claude/config/business-context.yml` exists and has valid YAML syntax

#### E002: Agent Loading Error  
**Message**: "Failed to load SEO specialist agents"
**Solution**: Check agent files in `.claude/agents/` directory, verify permissions and syntax

#### E003: Mission Template Error
**Message**: "Mission template not found or invalid"  
**Solution**: Verify mission files exist in `missions/` directory, check template syntax

#### E004: API Authentication Error
**Message**: "Failed to authenticate with external API"
**Solution**: Check API credentials, verify service account permissions, test connectivity

#### E005: Resource Limit Error
**Message**: "System resource limit exceeded"
**Solution**: Reduce concurrent operations, increase memory allocation, optimize configuration

#### E006: Mission Timeout Error
**Message**: "Mission exceeded maximum execution time"
**Solution**: Break mission into smaller phases, increase timeout limits, optimize agent performance

## System Health Monitoring

### Regular Health Checks

#### Daily Health Check Routine
```bash
# Morning system verification
@coordinator Perform system health check:
- Verify all agents are responsive
- Check API connectivity status
- Review overnight mission results
- Validate configuration integrity
```

#### Weekly Performance Review
```bash
# Weekly optimization assessment
@seo-analyst Generate weekly performance report:
- Mission success rates and timing
- Agent performance metrics  
- Resource utilization patterns
- Error frequency and resolution times
```

### Automated Monitoring Setup

#### Performance Alerts
```bash
# Configure automatic performance monitoring
cat > .claude/config/monitoring.yml << EOF
alerts:
  memory_usage:
    threshold: 85%
    action: "reduce_concurrent_missions"
  response_time:
    threshold: 30_seconds
    action: "escalate_to_support"  
  mission_failure:
    threshold: 3_consecutive
    action: "system_health_check"
EOF
```

#### Log Monitoring
```bash
# Set up log rotation and monitoring
mkdir -p .claude/logs
echo "*/5 * * * * /usr/bin/tail -100 .claude/logs/errors.log | grep ERROR" | crontab -

# Monitor critical error patterns
tail -f .claude/logs/system.log | grep -i "error\|warning\|failed"
```

## Performance Optimization

### Configuration Optimization

#### Optimal Settings for Different Use Cases

**Small Business / Low Volume**:
```yaml
# .claude/config/performance.yml
performance_settings:
  concurrent_missions: 1
  agent_response_timeout: 180
  data_cache_duration: 3600
  batch_processing_size: 20
```

**Enterprise / High Volume**:
```yaml  
# .claude/config/performance.yml
performance_settings:
  concurrent_missions: 3
  agent_response_timeout: 300
  data_cache_duration: 7200
  batch_processing_size: 50
```

**Development / Testing**:
```yaml
# .claude/config/performance.yml  
performance_settings:
  concurrent_missions: 1
  agent_response_timeout: 60
  data_cache_duration: 1800
  batch_processing_size: 10
```

### Mission Optimization Strategies

#### Efficient Mission Planning
1. **Start Small**: Begin with focused, single-agent tasks
2. **Build Up**: Gradually increase mission complexity as system stabilizes
3. **Monitor Results**: Track mission performance and adjust accordingly
4. **Use Templates**: Leverage proven mission patterns rather than custom approaches

#### Resource-Efficient Patterns
```bash
# Instead of comprehensive missions
/coord site-audit --comprehensive --all-agents

# Use focused, sequential missions  
/coord technical-audit --core-web-vitals
# Wait for completion, then:
/coord content-audit --top-pages
# Wait for completion, then:
/coord strategic-recommendations --based-on-previous
```

## Getting Help and Support

### Self-Service Resources

#### Built-in Diagnostic Tools
```bash
# System diagnostic commands
/debug agents --full-report
/validate config --comprehensive
/system-health --detailed-report
/performance-analysis --last-7-days
```

#### Documentation Resources
- **Agent Guide**: `/docs/agent-guide.md` - Complete agent system documentation
- **Mission Guide**: `/docs/mission-guide.md` - Mission execution and coordination
- **Quick Start**: `/docs/QUICK-START.md` - Installation and initial setup
- **Integration Guide**: `/docs/mcp-integration-guide.md` - MCP and API setup

### Community Support

#### GitHub Repository
- **Issues**: Report bugs and request features
- **Discussions**: Community Q&A and best practices sharing  
- **Wiki**: Extended documentation and tutorials
- **Release Notes**: Latest updates and improvements

#### Support Channels
- **Documentation**: Check relevant guide sections first
- **GitHub Issues**: Technical problems and bug reports
- **Community Forum**: Usage questions and optimization tips  
- **Professional Support**: Available for enterprise deployments

### Creating Effective Support Requests

#### Before Requesting Help

Gather this diagnostic information:

```bash
# System environment
uname -a                          # Operating system info
claude --version 2>/dev/null || echo "Claude Code version not found"

# Configuration status
ls -la .claude/config/
cat .claude/config/business-context.yml | head -10

# Recent errors
tail -50 .claude/logs/errors.log 2>/dev/null || echo "No error log found"

# Agent status
ls -la .claude/agents/
head -5 .claude/agents/seo-strategist.md
```

#### Effective Bug Report Template

```markdown
## Issue Description
Brief description of the problem

## Steps to Reproduce
1. Step one
2. Step two  
3. Expected result vs actual result

## System Information
- OS: [Operating System and version]
- Claude Code Version: [Version number]
- SEOAgent Version: [Git commit or release]

## Configuration
- Business context configured: [Yes/No]
- API integrations enabled: [List]
- Recent configuration changes: [Description]

## Error Messages
```
[Paste error messages and logs here]
```

## Additional Context
Any additional information that might be helpful
```

## Emergency Recovery Procedures

### Complete System Reset

#### Full Reset (Last Resort)
```bash
# Backup current configuration
cp -r .claude/config .claude/config.backup.$(date +%Y%m%d)

# Reset to clean state
rm -rf .claude/agents/* .claude/missions/* .claude/config/* .claude/cache/* .claude/temp/*

# Reinstall from clean state
./scripts/install.sh

# Restore business configuration
cp .claude/config.backup.*/business-context.yml .claude/config/ 2>/dev/null || echo "No backup found"
```

#### Selective Recovery
```bash
# Reset only agents (keep configuration)
rm -rf .claude/agents/*
cp agents/* .claude/agents/

# Reset only missions (keep agents and config)  
rm -rf .claude/missions/*
cp missions/* .claude/missions/

# Reset only configuration (keep business context)
find .claude/config -name "*.yml" ! -name "business-context.yml" -delete
cp examples/seoagent-work-config.yml .claude/config/performance.yml
```

### Data Recovery

#### Configuration Backup and Restore
```bash
# Create backup
tar -czf seoagent-backup-$(date +%Y%m%d).tar.gz .claude/

# Restore from backup
tar -xzf seoagent-backup-YYYYMMDD.tar.gz

# Verify restored configuration
/validate config --fix-minor-issues
```

#### Mission State Recovery
```bash
# Check for recoverable mission state
ls -la .claude/temp/missions/

# Attempt mission recovery
@coordinator Attempt to recover incomplete mission [mission-id] from last checkpoint

# Manual mission reconstruction
@coordinator Recreate mission deliverables based on partial results:
[Paste available partial results]
```

## Frequently Asked Questions (FAQ)

### Setup and Configuration

**Q: Why aren't my agents loading properly?**
A: Check that agent files exist in `.claude/agents/` with proper syntax. Verify business context is configured in `.claude/config/business-context.yml`.

**Q: How do I know if my Google integrations are working?**
A: Use `@seo-analyst Test Google Search Console connection` and verify API credentials in `.claude/config/google-credentials.json`.

**Q: Can I run SEOAgent without third-party SEO tool APIs?**  
A: Yes, basic functionality works with Google services only. Third-party APIs enhance capabilities but aren't required.

### Mission Execution

**Q: Why do missions take longer than expected?**
A: Complex analysis requires time. Monitor resource usage and consider breaking large missions into smaller phases.

**Q: Can I run multiple missions simultaneously?**
A: Yes, but limit concurrent missions based on system resources. Default is 2 concurrent missions maximum.

**Q: What if a mission fails halfway through?**
A: Use mission recovery commands to resume from last checkpoint, or restart with reduced scope.

### Performance and Optimization

**Q: How can I improve agent response times?**
A: Optimize configuration settings, increase system memory allocation, reduce concurrent operations, and clear caches regularly.

**Q: What's the minimum system requirements?**
A: 8GB RAM minimum (16GB recommended), stable internet connection, and Claude Code latest version.

**Q: How often should I run comprehensive audits?**
A: Monthly comprehensive audits are recommended, with weekly focused audits for active optimization periods.

---

**Remember**: Most issues can be resolved through systematic troubleshooting and configuration optimization. When in doubt, start with the diagnostic checklist and work through solutions methodically.