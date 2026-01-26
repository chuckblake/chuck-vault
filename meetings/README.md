# Meetings

Meeting transcriptions and notes.

## Structure

```
meetings/
├── inbox/      # Raw transcriptions (eml, txt, pdf, etc.)
├── 2026/       # Processed meeting notes by year
└── README.md
```

## Workflow

1. Drop raw transcription into `inbox/`
2. Run `/process-meeting` to convert and extract
3. Processed notes go to `meetings/YYYY/YYYY-MM-DD-person-or-topic.md`
4. Action items extracted to main `inbox/`
5. Person info flagged for review (not auto-updated)

## Naming Convention

Processed files: `YYYY-MM-DD-person-or-topic.md`

Examples:
- `2026-01-26-ben-cohen.md`
- `2026-01-28-team-standup.md`
- `2026-02-01-investor-update.md`
