# Claude Corrections Log

Mistakes I've made and what I learned. Reference this to avoid repeating errors.

---

## 2026-01-24

**Category:** Process
**Error:** Assumed the system-provided date was accurate for Chuck's timezone
**Correction:** Chuck is in EST - the system date may be in UTC and off by a day. Always trust Chuck's stated day over the system date.
**Fix:** Updated `.claude/skills/daily-routines.md` with timezone note

---

## 2026-01-24

**Category:** Factual
**Error:** Called it "Claude Bot"
**Correction:** It's "ClawdBot" (with a 'w')
**Fix:** None needed - just remember the name

---

## 2026-01-24

**Category:** Factual
**Error:** Thought Monday was Jan 27 when it's actually Jan 26
**Correction:** Today is Saturday Jan 24, so Monday = Jan 26
**Fix:** Updated `.claude/skills/daily-routines.md` with proper date handling:
- Use `date '+%Y-%m-%d %A'` to get correct local date
- Use `date -v+monday` for date math instead of calculating manually
- Never rely solely on system prompt date

---
