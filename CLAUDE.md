# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

SEOAgent (SearchOps-11™) is an elite SEO agent suite designed for business growth through coordinated AI specialists. This is a mission-based framework for SEO operations using Claude Code's sub-agent system.

## Architecture

This repository follows a hub-and-spoke coordination model with:
- **Mission templates** in `missions/` - Predefined workflows for SEO operations
- **Agent templates** in `templates/` - Framework for creating optimized agents
- **Ideation/documentation** in `ideation/` - Strategic planning and product specs

## Key Concepts

### Agent System
- 6 specialized SEO agents: Strategist, Technical, Content, Researcher, Analyst, Builder
- Each agent has specific tools and responsibilities
- Coordination through @coordinator to prevent conflicts
- "Stay in Lane" principle - agents escalate outside their scope

### Mission Structure
Missions follow this pattern:
1. Briefing - objectives and requirements
2. Phases - step-by-step execution
3. Specialists - agents involved
4. Deliverables - expected outputs
5. Success criteria - completion metrics

## Working with Missions

### Launching Missions
```bash
/coord [mission-name] [inputs...]
```

Available mission codes:
- `site-audit` - Comprehensive SEO analysis
- `content-gap` - Content opportunity discovery
- `technical-fix` - Performance optimization
- `ai-search-optimize` - Future-proof with llms.txt
- `keyword-research` - Market intelligence
- `operation-recon` - UI/UX reconnaissance
- `build`, `fix`, `refactor`, `mvp`, `deploy` - Development missions

### Tracking Progress
All missions automatically capture before/after metrics:
```bash
/track baseline domain.com     # Manual baseline before mission
/track compare domain.com      # View improvements after mission
/track roi domain.com 90d      # Calculate financial ROI
```

### Creating New Missions
Use `templates/mission-template.md` as the base for new missions. Follow the AGENT-11 optimization standards outlined in `templates/agent-creation-mastery.md`.

## Agent Creation Guidelines

When creating new agents:
1. Use ALL CAPS headers (never ## markdown)
2. Consistent dash bullets (-) throughout
3. Keep agents under 150 lines for optimal performance
4. Include clear ✅/❌ scope boundaries
5. Always escalate to @coordinator for cross-agent work

## File Conventions

- Mission files: `mission-[name].md` in `missions/`
- Agent templates: descriptive names in `templates/`
- Documentation: descriptive markdown in `ideation/`

## Integration Points

The system expects connections to:
- Google Search Console (required)
- Google Analytics 4 (required)
- SEO platforms (Ahrefs, SEMrush, or Moz)
- Optional: WordPress/Shopify, Screaming Frog

## Performance Targets

- Mission completion within estimated timeframes
- 95%+ agent performance standards
- Clear deliverables for each operation
- Measurable success criteria

## Tracking System

The repository includes a comprehensive tracking system at `/tracking/`:
- **Baselines**: Capture initial metrics before optimization
- **Snapshots**: Regular performance recordings
- **Reports**: Automated progress and ROI reports
- **Commands**: `/track` commands for all tracking operations

Configuration in `/tracking/config/tracking.yml` controls:
- Automatic baseline capture
- Snapshot frequency
- ROI calculation values
- Alert thresholds