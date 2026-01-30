# HEARTBEAT.md

## Git Sync (every heartbeat)

1. `git pull` - get latest changes
2. Check for uncommitted work (`git status`)
3. If changes exist: stage, commit with descriptive message, push
4. Log sync status to today's memory file

## Self-Check (runs every hour)

Ask yourself:
- What sounded right but went nowhere?
- Where did I default to consensus?
- What assumption did I not pressure test?

Log answers to `memory/self-review.md`

Tag each entry with: [confidence | uncertainty | speed | depth]
