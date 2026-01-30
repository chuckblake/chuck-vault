# Weekly Review

GTD-style weekly review covering all areas of life.

**Best time:** Sunday afternoon/evening
**Duration:** 30-60 minutes

---

## Instructions for Claude

See `.claude/skills/weekly-review.md` for full process.

### Setup

1. Get current date and week number:
   ```bash
   date '+%Y-%m-%d %A (Week %V)'
   ```

2. Read context files:
   - Current week's focus file
   - `focus/2026/yearly.md`
   - `me/focus.md`
   - Recent journal entries

3. Check what week we're closing and what week we're setting up

---

## Conversation Flow

### Opening

Start with:
- "Ready for your weekly review?"
- Confirm energy level and time available
- If low energy/time: offer quick review option

### Phase 1: Get Clear

Walk through:
1. "Let's process your inbox first" - review `inbox/` items
2. "Anything floating in your head to capture?"
3. Quick capture, then move on

### Phase 2: Get Current

**Review last week:**
- Read the closing week's file
- "What got done this week?"
- "What didn't happen? Any patterns?"
- "Any wins to celebrate?"

**Check waiting-on:**
- Review all waiting items
- "Any follow-ups needed?"
- Update statuses

**Area by area:**
- Work: "How did LEA go this week? What's the focus for next week?"
- Ventures: "Any progress on side projects?"
- Personal: "How's health/personal stuff? Anyone to reach out to?"

### Phase 3: Get Creative

- "Let's zoom out - how are we tracking on Q1 goals?"
- "What would make next week great?"
- "Anything in someday/maybe to activate?"

### Phase 4: Set Up Next Week

1. Create new weekly file together
2. Confirm top 3 priorities
3. Note any known commitments
4. Update monthly file and dashboard

### Closing

- Create review file in `reviews/weekly/`
- Summarize: "Here's your week ahead..."
- Mindset: "You're set up. Enjoy the rest of Sunday."

---

## Quick Review (15 min version)

If short on time:

1. "What got done this week?" (2 min)
2. "What's the #1 thing for next week?" (2 min)
3. "Any waiting-on follow-ups?" (2 min)
4. Create next week file with top 3 (5 min)
5. Done

---

## Output Files

1. **Review notes:** `reviews/weekly/YYYY-WXX.md`
2. **Next week:** `focus/2026/WXX.md`
3. **Updated:** `me/focus.md`, monthly file
