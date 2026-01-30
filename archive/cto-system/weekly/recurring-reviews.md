# Recurring Reviews

Reviews that should happen on a regular cadence. Claude checks this during daily planning.

## Active Reviews

| Review | Cadence | Preferred Day | Last Completed | Next Due |
|--------|---------|---------------|----------------|----------|
| Vantaa Review | Weekly | Wednesday | 2026-01-21 | 2026-01-28 |

## How It Works

During daily planning, Claude should:
1. Check if any review's **Next Due** date is today or past
2. If overdue, remind at the start of prioritization
3. Keep reminding daily until completed
4. After completing a review, update **Last Completed** to today and **Next Due** to +7 days (for weekly)

## Cadence Reference

| Cadence | Next Due Calculation |
|---------|---------------------|
| Weekly | Last Completed + 7 days |
| Biweekly | Last Completed + 14 days |
| Monthly | Last Completed + 30 days |

## Adding New Reviews

Add rows with:
- **Review:** Short name
- **Cadence:** Weekly / Biweekly / Monthly
- **Preferred Day:** Day you'd ideally do it (for planning)
- **Last Completed:** Date (YYYY-MM-DD)
- **Next Due:** Calculated from cadence
