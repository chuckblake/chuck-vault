# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## 1Password

- CLI: `~/.local/bin/op` (v2.32.0)
- Auth: Service account token via `OP_SERVICE_ACCOUNT_TOKEN` env var
- Skill: `/Users/gomez/clawd/skills/1password/SKILL.md`

## qmd (Markdown Search)

- CLI: `~/.bun/bin/qmd`
- Skill: `/Users/gomez/clawd/skills/qmd-external/SKILL.md`
- Index: `~/.cache/qmd/index.sqlite`
- Collections:
  - **chuck-vault**: `/Users/gomez/clawd` (`**/*.md`) — Chuck's personal knowledge base, notes, to-dos, and project info
- Usage: `export PATH="$HOME/.bun/bin:$PATH" && qmd search "query" -c chuck-vault`

## MTA R Train Times

- Script: `/Users/gomez/clawd/scripts/mta_train_times.py`
- **"Heading to work"** → `python3 scripts/mta_train_times.py work` (4th Ave-9th St → Manhattan)
- **"Heading home"** → `python3 scripts/mta_train_times.py home` (Cortlandt St → Brooklyn)

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
