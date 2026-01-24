# CTO Command Center

Your personal Claude Code-powered system for world-class technical leadership.

## Quick Start

Run these commands based on your current need:

```bash
# Morning briefing
claude "Review my @cto-system/daily/morning-briefing.md and help me start my day"

# Weekly planning
claude "Let's do my weekly review using @cto-system/weekly/review-template.md"

# Before a board meeting
claude "Help me prepare using @cto-system/communication/board-update-template.md"

# Making a technical decision
claude "Guide me through a decision using @cto-system/decisions/adr-template.md"
```

## System Structure

```
cto-system/
├── daily/           # Daily standups, priorities, blockers
├── weekly/          # Weekly reviews, 1:1 prep, planning
├── monthly/         # Monthly retrospectives, metrics review
├── quarterly/       # OKR planning, roadmap updates
├── strategic/       # Vision, long-term planning, market analysis
├── team/            # Hiring, performance, org design, culture
├── technical/       # Architecture, tech debt, code quality
├── communication/   # Board updates, stakeholder comms, team announcements
├── metrics/         # KPIs, dashboards, health indicators
├── prompts/         # Claude Code workflow prompts
├── decisions/       # ADRs, decision logs, frameworks
└── personal/        # Your growth, learning, time management
```

## Recommended Rhythms

### Daily (5-10 min)
- Morning briefing: Review priorities, calendar, blockers
- End of day: Capture wins, update tomorrow's priorities

### Weekly (30-60 min)
- Monday: Week planning, team sync prep
- Friday: Week review, metrics check, next week setup

### Monthly (2-3 hours)
- Team health assessment
- Technical debt review
- Metrics deep dive
- Personal reflection

### Quarterly (half day)
- OKR review and planning
- Roadmap alignment
- Org structure assessment
- Strategic initiatives review

## Getting Started

1. **Customize your context** - Edit `prompts/my-context.md` with your company, team, and current priorities
2. **Run your first briefing** - Use the morning briefing prompt
3. **Build the habit** - Start with daily, then add weekly rhythms

## Key Prompts

| Need | Command |
|------|---------|
| Start my day | `claude "@cto-system/prompts/daily-start.md"` |
| Prepare for 1:1 | `claude "@cto-system/prompts/one-on-one-prep.md [name]"` |
| Technical decision | `claude "@cto-system/prompts/tech-decision.md"` |
| Write board update | `claude "@cto-system/prompts/board-update.md"` |
| Review architecture | `claude "@cto-system/prompts/architecture-review.md"` |
| Hiring decision | `claude "@cto-system/prompts/hiring-decision.md"` |
| Incident postmortem | `claude "@cto-system/prompts/postmortem.md"` |
| Strategic planning | `claude "@cto-system/prompts/strategic-planning.md"` |

## Files to Maintain

These files should be kept updated for best results:

- `prompts/my-context.md` - Your current situation, company, team
- `metrics/current-kpis.md` - Your key metrics and targets
- `team/org-chart.md` - Current team structure
- `strategic/current-okrs.md` - Active OKRs
- `decisions/decision-log.md` - Record of key decisions
