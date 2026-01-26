# People Management Skill

Manage the personal CRM in `people/`. This skill activates when the user mentions people, meetings, or relationship management.

## Trigger Phrases

- "I met [person]..."
- "Update [person]'s file..."
- "Add [person] to my contacts"
- "When did I last talk to [person]?"
- "What do I know about [person]?"
- "Create a person file for..."
- Meeting prep that involves specific people
- Any mention of updating contact information

## Directory Structure

- Location: `people/`
- Template: `people/_template.md`
- Naming: `firstname-lastname.md` (lowercase, hyphenated)

## Core Behaviors

### When User Mentions Meeting Someone New

1. Ask for key details if not provided:
   - Full name
   - How they met
   - Any contact info shared
   - Tags (relationship type)
2. Use the `linkedin-finder` agent to find their LinkedIn URL (if professional contact)
3. Create new file from template
4. Fill in known fields (leave `aliases` empty by default)
5. Confirm creation
6. Do NOT add aliases unless explicitly requested

### When User Mentions Existing Person

1. Search `people/` for matching file
2. If found, read for context
3. If updating, modify relevant fields
4. Update `updated:` timestamp

### When User Asks About Someone

1. Search for matching person file
2. Provide relevant summary
3. Surface useful context (last contact, upcoming events, etc.)

## File Matching & Aliases

**Quick lookup:** Check `people/_aliases.md` first for common short names.

**Search order:**
1. `_aliases.md` lookup table
2. `aliases` array in frontmatter
3. `name` field in frontmatter
4. Filename match (firstname-lastname.md)

**Alias examples:**
- "Max" → Max Klein
- "mom" → Barbara Blake
- "Brenton" → Brenton Morris

**Adding aliases:**
- Do NOT automatically add aliases for new contacts
- Only add aliases when Chuck explicitly requests it (e.g., "add Max as an alias" or "I'll call him Max")
- When adding, update both the `aliases` field in the person file AND `_aliases.md`

Handle ambiguity:
- If multiple people could match, ask for clarification
- "Which David? David Lei or David [other]?"

## Frontmatter Fields

### Required for New Contacts
- `name` - Full name
- `tags` - At least one tag
- `met_date` - When first met
- `met_context` - How we met
- `created` - Today's date

### Optional but Recommended
- `linkedin` - LinkedIn profile URL (use `linkedin-finder` agent to find)

### Update on Each Edit
- `updated` - Today's date

### Update When Contact Occurs
- `last_contact` - Date of most recent interaction

## Tags Reference

| Tag | Use For |
|-----|---------|
| `family` | Blood relatives, in-laws |
| `friend` | Personal friends |
| `colleague` | LEA team members |
| `collaborator` | External work partners |
| `investor` | Investors, board members |
| `customer` | Customer contacts |
| `mentor` | Mentors and advisors |
| `misc` | Everyone else |

## Example Interactions

### Creating New Contact

User: "I met Sarah Chen at the fintech conference yesterday. She's a PM at Stripe."

Claude:
1. Uses `linkedin-finder` agent to find LinkedIn URL
2. Creates `sarah-chen.md`:
```yaml
---
name: Sarah Chen
aliases: []
tags: [collaborator]
met_date: 2026-01-23
met_context: Fintech conference
company: Stripe
title: PM
linkedin: https://linkedin.com/in/sarachen
created: 2026-01-24
updated: 2026-01-24
---

# Sarah Chen

## Summary
PM at Stripe. Met at fintech conference January 2026.

## How We Met
Met at fintech conference on 2026-01-23.
```

### Adding an Alias

User: "Add Sarah as an alias for Sarah Chen"

Claude:
1. Updates `sarah-chen.md` frontmatter: `aliases: [Sarah]`
2. Adds entry to `_aliases.md`: `| Sarah | Sarah Chen | sarah-chen.md |`

### Updating Existing Contact

User: "Brenton mentioned he's thinking about moving to Austin"

Claude: Updates `brenton-morris.md`:
- Adds note about Austin move consideration
- Updates `updated:` date

### Pre-Meeting Context

User: "I have a call with Sarah Chen tomorrow"

Claude: Reads `sarah-chen.md` and surfaces:
- Who she is, how we met
- Last contact date
- Any relevant notes
- Open action items

## Integration with Other Systems

### With 1:1 Prep (`@prompts/one-on-one-prep.md`)
- Pull person context from `people/` for colleague files
- Cross-reference with `areas/work/team/` for work-specific notes

### With Journal
- When logging meetings, offer to update `last_contact`
- Surface birthday reminders if approaching

### With me/people.md
- `me/people.md` is a quick reference summary
- `people/` folder has the detailed files
- Keep them loosely synced

## Best Practices

1. **Be proactive but not annoying** - Offer to create/update files, don't force it
2. **Ask before assuming** - If unsure which person, ask for clarification
3. **Keep it lightweight** - Not every mention needs a file update
4. **Surface context when useful** - Before meetings, when discussing someone
5. **Respect privacy** - This contains personal information
