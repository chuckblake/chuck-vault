# People

Personal CRM - one file per person in my life.

## How It Works

Each person has a markdown file with YAML frontmatter for structured data and a body for notes, history, and context.

**File naming:** `firstname-lastname.md` (lowercase, hyphenated)

## Structure

```yaml
---
name: Full Name
tags: [family, friend, colleague, collaborator, investor, customer, misc]
# ... structured fields
---

# Notes, history, relationship context
```

## Tags

| Tag | Use For |
|-----|---------|
| `family` | Family members |
| `friend` | Personal friends |
| `colleague` | Current coworkers (LEA team) |
| `collaborator` | People I work with outside LEA |
| `investor` | Investors, board members |
| `customer` | Customer contacts |
| `mentor` | Mentors and advisors |
| `misc` | Everyone else |

Multiple tags allowed (e.g., `[friend, collaborator]`).

## Using with Claude

Claude will automatically recognize when people are mentioned and can:
- Create new person files when you meet someone
- Update existing files with new information
- Surface relevant context before meetings
- Track contact history when requested

Just mention someone naturally:
- "I met Sarah Chen at the conference yesterday..."
- "Update Brenton's file - he mentioned he's moving to Austin"
- "When did I last talk to [person]?"

## Template

See `_template.md` for the full template structure.
