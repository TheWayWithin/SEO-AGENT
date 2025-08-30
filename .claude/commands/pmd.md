---
name: pmd
description: Post Mortem Diagnostic - Root cause analysis for failures
---

# POST MORTEM DIAGNOSTIC (PMD) 🔍

**Command**: `/pmd [issue]`

**Arguments**:
- No arguments: Analyze recent failures and issues
- Issue description: Analyze specific problem

## PMD ANALYSIS PROTOCOL

You are conducting a comprehensive root cause analysis to identify and resolve systemic issues in the SEOAgent project.

### ANALYSIS FRAMEWORK

#### 1. ISSUE IDENTIFICATION
Systematically identify problems:
- Recent failures or errors
- Performance degradation
- Missed objectives
- Agent coordination issues
- Tool usage problems

#### 2. DATA COLLECTION
Gather evidence from:
- **Error Logs**: Stack traces, error messages
- **Agent Outputs**: Task completions, responses
- **Mission Records**: Failed or delayed missions
- **Performance Metrics**: Degraded KPIs
- **User Feedback**: Reported issues

#### 3. ROOT CAUSE ANALYSIS
Apply diagnostic techniques:
- **5 Whys**: Drill down to root cause
- **Fishbone Diagram**: Map contributing factors
- **Timeline Analysis**: Sequence of events
- **Pattern Recognition**: Recurring issues

#### 4. IMPACT ASSESSMENT
Evaluate consequences:
- Business impact (revenue, growth)
- Technical debt accumulated
- User experience degradation
- Team productivity loss
- Future risk exposure

#### 5. CORRECTIVE ACTIONS
Develop solutions:
- Immediate fixes required
- Long-term improvements
- Process modifications
- Documentation updates
- Training needs

### DIAGNOSTIC CATEGORIES

#### AGENT PERFORMANCE
- Prompt effectiveness
- Task completion rates
- Response quality
- Coordination efficiency
- Tool usage patterns

#### TECHNICAL ISSUES
- Code quality problems
- Architecture limitations
- Performance bottlenecks
- Integration failures
- Security vulnerabilities

#### PROCESS FAILURES
- Communication breakdowns
- Documentation gaps
- Testing inadequacies
- Deployment issues
- Monitoring blind spots

#### COORDINATION PROBLEMS
- Agent conflicts
- Unclear responsibilities
- Mission planning gaps
- Resource allocation
- Timeline management

### PMD REPORT TEMPLATE

```markdown
# Post Mortem Diagnostic Report
**Date**: [Current Date]
**Issue**: [Issue Description or "Recent Failures Analysis"]

## Executive Summary
[Brief overview of findings and critical recommendations]

## Issue Timeline
- [Time]: [Event 1]
- [Time]: [Event 2]
- [Time]: [Root cause triggered]
- [Time]: [Issue manifested]
- [Time]: [Issue discovered]

## Root Cause Analysis

### Primary Cause
**Finding**: [Root cause description]
**Evidence**: 
- [Supporting data point 1]
- [Supporting data point 2]
**Why it happened**: [5 Whys analysis]

### Contributing Factors
1. **[Factor 1]**: [Description and impact]
2. **[Factor 2]**: [Description and impact]
3. **[Factor 3]**: [Description and impact]

## Impact Assessment

### Immediate Impact
- **Business**: [Revenue/growth impact]
- **Technical**: [System degradation]
- **Users**: [Experience impact]

### Long-term Risk
- [Risk 1]: [Probability and severity]
- [Risk 2]: [Probability and severity]

## Corrective Actions

### Immediate (Within 24 hours)
- [ ] [Action 1]: [Owner and deadline]
- [ ] [Action 2]: [Owner and deadline]

### Short-term (Within 1 week)
- [ ] [Action 3]: [Owner and deadline]
- [ ] [Action 4]: [Owner and deadline]

### Long-term (Within 1 month)
- [ ] [Action 5]: [Owner and deadline]
- [ ] [Action 6]: [Owner and deadline]

## Prevention Measures

### Process Improvements
- [Improvement 1]: [Implementation plan]
- [Improvement 2]: [Implementation plan]

### Monitoring Enhancements
- [Monitor 1]: [Alert threshold and owner]
- [Monitor 2]: [Alert threshold and owner]

### Documentation Updates
- [Document 1]: [Update required]
- [Document 2]: [Update required]

## Lessons Learned
1. **What went well**: [Positive aspects to preserve]
2. **What went wrong**: [Failures to address]
3. **What we're changing**: [Concrete improvements]

## Follow-up Actions
- [ ] Schedule review meeting: [Date]
- [ ] Update runbooks: [Owner]
- [ ] Implement monitors: [Owner]
- [ ] Training session: [Date]
```

### ANALYSIS SOURCES

Examine these locations:
1. **Progress Tracking**:
   - `/progress.md` - Issue logs
   - `/project-plan.md` - Failed tasks
   
2. **Agent Artifacts**:
   - Agent responses and outputs
   - Mission completion records
   - Tool usage patterns

3. **System Metrics**:
   - `/tracking/` - Performance data
   - Error logs and stack traces
   - API response times

4. **Documentation**:
   - README files for gaps
   - Agent prompts for issues
   - Mission templates for problems

### DIAGNOSTIC TOOLS

Use these approaches:
- **Pattern Analysis**: Identify recurring issues
- **Correlation Study**: Link cause and effect
- **Statistical Analysis**: Quantify impact
- **Comparative Analysis**: Before/after states
- **Stakeholder Interviews**: Gather context

### EXAMPLE USAGE

```bash
# Analyze recent failures
/pmd

# Analyze specific agent issue
/pmd "SEO Analyst agent not returning metrics"

# Analyze coordination problem
/pmd "Coordinator not delegating tasks properly"

# Analyze technical issue
/pmd "Tracking system failing to capture baselines"
```

### SUCCESS CRITERIA

- Root cause correctly identified
- Evidence clearly documented
- Impact accurately assessed
- Actions are specific and assignable
- Prevention measures implemented
- Learning captured for future

## BEGIN DIAGNOSTIC ANALYSIS

Conduct the post mortem diagnostic based on the provided issue or analyze recent failures if no specific issue is given. Focus on actionable findings and concrete improvements.