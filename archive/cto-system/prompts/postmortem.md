# Incident Postmortem Prompt

Use after incidents to conduct blameless postmortems.

---

## Instructions for Claude

Help me conduct a blameless postmortem.

Ask me:
1. What happened? (Brief description)
2. What was the severity/impact?
3. Is the incident fully resolved?
4. When should the postmortem meeting happen?

### Before the Meeting

Help me:
- Construct a timeline of events
- Identify who should attend
- Gather relevant data (logs, metrics, alerts)
- Prepare questions to explore root cause

### During/After the Meeting

Use `@cto-system/technical/incident-postmortem.md` as the template.

Guide me through:

**Timeline Construction**
- When did it start?
- When was it detected? How?
- What actions were taken?
- When was it resolved?

**Impact Assessment**
- Customer impact
- Business impact
- Internal impact

**Root Cause Analysis**
- What happened?
- 5 Whys analysis
- Contributing factors
- Why wasn't it caught earlier?

**Action Items**
- What prevents recurrence?
- What improves detection?
- What reduces impact?

**Lessons Learned**
- What worked well in our response?
- What could have gone better?
- What should we do differently?

Remind me:
- This is blameless - focus on systems, not people
- Assume everyone made the best decision with the information they had
- The goal is learning, not punishment
