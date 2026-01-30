# Prompts

Claude interaction prompts for different workflows. Invoke with `@prompts/filename.md`.

## Daily

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| `morning.md` | Start the day | Morning routine |
| `evening.md` | End the day | Evening wind-down |

## Reviews

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| `weekly-review.md` | Weekly review and planning | End of week |
| `monthly-review.md` | Monthly reflection | End of month |
| `quarterly-review.md` | Quarterly goals check | End of quarter |

## Work

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| `decision.md` | Help with decisions | Important choices |
| `one-on-one-prep.md` | Prepare for 1:1s | Before 1:1 meetings |
| `project-kickoff.md` | Start a new project | New project |

## Usage

```bash
# Morning startup
claude "@prompts/morning.md"

# With additional context
claude "@prompts/decision.md" "Should we use Postgres or MongoDB?"
```
