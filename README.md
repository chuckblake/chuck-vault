# Chuck's Vault

A personal knowledge management system designed for use with Claude Code. This is my operating system for life - bridging professional work, creative ventures, personal growth, and continuous learning.

## Quick Start

```bash
# Morning startup
claude "@prompts/morning.md"

# Evening reflection
claude "@prompts/evening.md"

# Weekly review
claude "@prompts/weekly-review.md"

# Quick capture (just talk to Claude)
claude "Add to inbox: [your thought]"
```

## Structure

| Folder | Purpose | When to Use |
|--------|---------|-------------|
| `me/` | Personal context | Update when circumstances change |
| `inbox/` | Quick capture | Throw anything here, process later |
| `journal/` | Daily reflections | Morning/evening entries |
| `people/` | Personal CRM | One file per person |
| `areas/` | Ongoing responsibilities | Work, ventures, personal life |
| `projects/` | Active time-bound work | Things with deadlines or endpoints |
| `knowledge/` | Learning & reference | Articles, books, notes |
| `decisions/` | Decision making | Important choices, frameworks |
| `reviews/` | Review workflows | Daily, weekly, monthly, quarterly |
| `prompts/` | Claude prompts | Interaction templates |
| `templates/` | Reusable templates | Structured documents |
| `archive/` | Completed/old | Move things here when done |

## Philosophy

**Capture freely, organize minimally, review regularly.**

This system is designed to:
- Reduce friction for capturing thoughts and information
- Provide Claude with enough context to be genuinely helpful
- Support both quick interactions and deep work sessions
- Bridge personal and professional seamlessly
- Grow and evolve over time

## Key Files

- `me/about.md` - Who I am, how I work (context for Claude)
- `me/focus.md` - Current priorities across all areas
- `me/goals.md` - Active goals and aspirations
- `decisions/log.md` - Record of important decisions
- `journal/YYYY/MM/DD.md` - Daily entries

## Cadences

| Rhythm | What Happens | Prompt |
|--------|--------------|--------|
| Daily AM | Set intentions, review calendar | `@prompts/morning.md` |
| Daily PM | Reflect, capture learnings | `@prompts/evening.md` |
| Weekly | Review progress, plan ahead | `@prompts/weekly-review.md` |
| Monthly | Bigger picture review | `@prompts/monthly-review.md` |
| Quarterly | Goals and direction check | `@prompts/quarterly-review.md` |
