# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **CTO Command Center** - a Claude Code-powered leadership operating system. It's a structured collection of templates, prompts, and decision frameworks for technical leadership workflows. This is NOT a software project that needs building/testing - it's a prompt-driven system designed to be used interactively with Claude.

## Usage Pattern

Invoke prompts using the `@` file reference syntax:

```bash
# Morning briefing
claude "@cto-system/prompts/daily-start.md"

# Weekly review
claude "@cto-system/prompts/weekly-review.md"

# Technical decisions
claude "@cto-system/prompts/tech-decision.md"

# 1:1 preparation
claude "@cto-system/prompts/one-on-one-prep.md [person-name]"
```

## Architecture

**Three-layer structure:**

1. **Prompts Layer** (`/prompts/`) - Entry points for Claude interactions with instructions and context references
2. **Template Layer** (organized by cadence) - Structured templates for activities like reviews, planning, decisions
3. **Context Layer** (`/prompts/my-context.md`) - Single source of truth for personal/company context, referenced by prompts

**Directory organization by time cadence:**
- `daily/` - Standups, priorities, blockers
- `weekly/` - Reviews, 1:1 prep, planning
- `monthly/` - Retrospectives, metrics review
- `quarterly/` - OKR planning, roadmap updates
- `strategic/` - Vision, long-term planning

**Functional directories:**
- `team/` - Hiring, performance, org design
- `technical/` - Architecture, tech debt, postmortems
- `communication/` - Board updates, stakeholder comms
- `metrics/` - KPIs, dashboards
- `decisions/` - ADRs, decision log, frameworks
- `personal/` - Growth, learning, time management

## Key Files to Keep Updated

These files should be maintained for the system to work well:
- `prompts/my-context.md` - Current situation, company, team (Claude reads this for context)
- `metrics/current-kpis.md` - Key metrics and targets
- `team/org-chart.md` - Current team structure
- `strategic/current-okrs.md` - Active OKRs
- `decisions/decision-log.md` - Record of key decisions

## Conventions

- **Cross-file references** use `@cto-system/path/to/file.md` syntax
- **Status values:** On Track / At Risk / Off Track / Proposed / Accepted / Deprecated
- **Assessment scores:** 1-10 scales (e.g., team health dimensions, energy levels)
- **Tables** are heavily used for quick scanning and Claude processing

## Decision Frameworks

Located in `decisions/decision-frameworks.md`:
- Type 1 vs Type 2 decisions (Amazon framework)
- DACI framework
- Weighted decision matrix
- Expected value analysis
- Pre-mortem analysis
- RAPID framework

ADRs follow the template in `decisions/adr-template.md`.

## Key Prompts

| Purpose | Prompt File |
|---------|-------------|
| Start day | `prompts/daily-start.md` |
| Weekly review | `prompts/weekly-review.md` |
| Tech decision | `prompts/tech-decision.md` |
| Architecture review | `prompts/architecture-review.md` |
| Board update | `prompts/board-update.md` |
| Hiring decision | `prompts/hiring-decision.md` |
| 1:1 prep | `prompts/one-on-one-prep.md` |
| Postmortem | `prompts/postmortem.md` |
| Strategic planning | `prompts/strategic-planning.md` |
