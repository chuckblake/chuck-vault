# Daily Start Prompt

Run this each morning to get focused.

---

## Instructions for Claude

Read my context from `@cto-system/prompts/my-context.md` and then help me with my morning briefing.

### Step 1: Review Yesterday

Before asking questions, quickly check:
- Yesterday's log (`@cto-system/daily/logs/YYYY-MM-DD.md`) for "Notes for Tomorrow"
- Open reminders in `@cto-system/daily/reminders-log.md`

Surface anything relevant before the check-in.

### Step 2: Check-in

Ask me:
1. How are you feeling today? (Energy level 1-10)
2. Any fires or urgent issues from overnight?

### Step 3: Linear Issues

Fetch my Linear issues using `@.claude/skills/linear-issues.md`:
- Get issues assigned to me in the current cycle
- Show **In Progress** and **Ready** issues (skip Done/Canceled)
- Display as a quick reference table with identifier, title, priority

Then ask: **Which of these will you focus on today?** (can pick 1-3)

### Step 4: Recurring Reviews

Check `@cto-system/weekly/recurring-reviews.md` for any reviews where **Next Due** is today or past. If any are overdue, remind me before prioritization. Keep reminding daily until I complete them.

### Step 5: Priorities

Based on my answers, help me:
- Confirm my top 3 priorities for the day
- Surface any blockers I should address
- Flag any calendar conflicts or concerns
- Remind me of any follow-ups I owe people
- Include any recurring reviews due today

Keep it concise and action-oriented. No fluff.

If I mention I'm stressed or overwhelmed, help me triage and identify what can be delegated or deferred.

End by asking if there's anything specific I want to think through together.

## Logging

After the briefing is complete, create a new file at `@cto-system/daily/logs/YYYY-MM-DD.md` (using today's date) with:
- Date as the title (# YYYY-MM-DD)
- Energy level
- Fires (if any)
- Focus/priorities for the day
- **Linear issues** selected for today (list identifiers like GET-123)
- Brief notes on context or decisions made

Keep entries concise - 8-10 lines max.

## Optional: Slack Reminder

After logging, offer to send a personal reminder to Chuck's own Slack DM (not a team broadcast) using `@.claude/skills/daily-slack-update.md`. This is a self-reminder he can glance at later in the day.
