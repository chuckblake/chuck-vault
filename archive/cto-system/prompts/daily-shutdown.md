# Daily Shutdown Prompt

Run this when signing off for the day to close loops and decompress.

---

## Instructions for Claude

Read my context from `@cto-system/prompts/my-context.md` and help me shut down for the day.

### Step 1: Day Review

Ask me:
1. How did today go? (Quick gut check)
2. Did you finish what you set out to do?
3. Anything still weighing on you?

### Step 2: Capture Loose Ends

Help me identify:
- Tasks that didn't get done (move to tomorrow or delegate?)
- Anything I promised someone that's still open
- Decisions that are still lingering

If there are open items, ask if I want to:
- Add them to Linear
- Send a quick Slack to someone
- Just note them for tomorrow

### Step 3: Wins & Progress

Ask me: **What's one thing you accomplished today, even if small?**

Acknowledge it. Building matters, even on hard days.

### Step 4: Update the Daily Log

Check if today's log exists at `@cto-system/daily/logs/YYYY-MM-DD.md`:
- If yes, append an "End of Day" section with accomplishments and notes
- If no, create it with the day's summary

Include:
- What got done
- What moved to tomorrow
- Energy level at end of day (1-10)
- Any notes for tomorrow morning

### Step 5: Clear the Mind

Ask: **Is there anything you need to get out of your head before signing off?**

If yes, help them:
- Write it down somewhere (note, Linear issue, Slack draft)
- Reframe if it's anxiety about something
- Reality-check if it's a worry

### Step 6: Shutdown Complete

End with something like:
> "You're done for today. The work will be there tomorrow. Go rest."

Keep it human. No corporate fluff.

---

## Optional: Slack Message

If there's something specific Chuck wants to communicate (e.g., a heads-up to a team member, a reminder to someone), offer to send it. This is NOT a routine team broadcast — only send if there's a specific message needed.
