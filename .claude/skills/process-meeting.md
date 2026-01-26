# Skill: Process Meeting

Converts raw meeting transcriptions into structured notes, extracts action items, and flags person info updates.

## Trigger

User says `/process-meeting` or asks to process a meeting transcription.

## Workflow

### 1. Find Raw Transcription

Check `meetings/inbox/` for unprocessed files. If multiple files exist, list them and ask which to process. Supported formats:
- `.eml` (email exports)
- `.txt` (plain text)
- `.md` (markdown)
- `.pdf` (if readable)
- Other text-based formats

### 2. Parse and Extract

Read the raw transcription and extract:
- **Date** of meeting
- **Attendees** (names, roles if mentioned)
- **Topic/purpose** of meeting
- **Key discussion points**
- **Decisions made**
- **Action items** (who, what, when)
- **Person info** worth noting (new contacts, updated info about existing people)

### 3. Create Meeting Notes

Create processed meeting notes at `meetings/YYYY/YYYY-MM-DD-person-or-topic.md`:

```markdown
---
date: YYYY-MM-DD
attendees: [Name1, Name2]
type: [1:1, team, external, interview, etc.]
---

# Meeting: [Topic/Person] - [Date]

## Summary

[2-3 sentence overview]

## Key Points

- Point 1
- Point 2

## Decisions

- Decision 1

## Action Items

- [ ] @Chuck: Task description (by date if mentioned)
- [ ] @Other: Task description

## Notes

[Any additional context, quotes, or details worth preserving]
```

### 4. Extract Action Items

For each action item assigned to Chuck:
- Create a quick capture in main `inbox/` folder with context
- Format: `YYYY-MM-DD-meeting-action-[brief-desc].md`

### 5. Create/Update Person Files

For each person mentioned in the meeting:

1. Check if they exist in `people/` directory
2. If **new person**:
   - Use `linkedin-finder` agent to find their LinkedIn URL
   - Create person file following `people-management.md` skill conventions
   - Include: name, company, title, linkedin, met_date, met_context, tags
   - Set `met_context` to reference the meeting
3. If **existing person**:
   - Update `last_contact` date
   - Add any new information learned (company changes, new projects, etc.)
   - Flag significant updates in the summary

See `.claude/skills/people-management.md` for file format and field conventions.

### 6. Clean Up

After successful processing:
- Move the original file to `meetings/processed/` (create folder if needed)
- Confirm what was created and flagged

## Output

After processing, summarize:
1. Meeting notes created at: `meetings/YYYY/...`
2. Action items extracted: X items
3. Person files created/updated: list new files and updates made

## Notes

- Meeting notes should be **complete** - capture everything relevant
- When in doubt about what to include, include it
- Action items should have clear ownership (who does what)
- Always create person files for new contacts met in meetings
- Use `linkedin-finder` agent proactively for new professional contacts
