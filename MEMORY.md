# MEMORY.md - Long-Term Memory

## Chuck-Vault Structure

When Chuck asks about people, personal info, or vault content, look here first:

| Content Type | Location |
|-------------|----------|
| **People profiles** | `people/` — individual files per person |
| **About Chuck** | `me/about.md` — background, work style, values |
| **Chuck's goals** | `me/goals.md` — 2026 goals, quarterly OKRs |
| **Chuck's focus** | `me/focus.md` — current priorities |
| **Chuck's network** | `me/people.md` — key relationships |
| **Events/research** | `archive/cto-system/personal/` — Silicon Alley profiles, etc. |
| **Journal entries** | `journal/2026/01/` — daily logs |
| **Meeting notes** | `meetings/2026/` — processed meeting summaries |
| **Weekly focus** | `focus/2026/` — weekly and monthly priorities |
| **Decisions** | `decisions/` — decision log and frameworks |
| **Projects** | `projects/` — active project tracking |
| **Recipes** | `recipes/` — cooking reference |
| **Templates** | `templates/` — reusable templates |
| **Prompts** | `prompts/` — Claude prompts for various tasks |

## Search Tips

- Use `qmd search "query" -c chuck-vault` for fast keyword search
- For semantic search: `qmd vsearch "query"` (slower, use if keywords fail)
- 150 files indexed as of 2026-01-30

## Key Learnings

- 2026-01-30: Merged chuck-vault master branch with full vault content (147 files)
- 2026-01-30: Set up qmd for local markdown search
