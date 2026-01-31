# MinisList — Specification

> *The dumb todo list for your smart AI*

**Version:** 0.2 (Draft)
**Last Updated:** 2026-01-31

## Overview

**MinisList** is a simple iPhone app for daily task management. Tasks are stored as plain markdown files (one per day) that sync with a user-configured folder. The format is designed to be human-readable and editable from any text editor (Obsidian, Cursor, vim, etc.).

**Tech Stack:**
- Ruby on Rails backend
- Hotwire Native for iOS wrapper
- Hotwire (Turbo + Stimulus) for frontend
- File-based storage (iCloud Drive)

---

## Folder Structure

The app syncs to a configured root folder. Inside that folder:

```
/MinisList/                    ← Root folder (user configures this)
  /daily/                      ← Daily task files
    2026-01-31.md
    2026-01-30.md
    2026-01-29.md
  /configuration/              ← App + AI config
    app.yaml                   ← App configuration
    AGENT.md                   ← AI/agent instructions
```

### /daily/
Where all daily task files live. One file per day, named `YYYY-MM-DD.md`.

### /configuration/app.yaml
App configuration file. The app reads this to configure behavior. Can be edited in-app or manually.

### /configuration/AGENT.md
Instructions for AI agents (Claude Code, Codex, etc.) explaining how to interact with this folder structure, edit tasks, and understand the format. This file is for AI consumption, not the app.

---

## Daily File Format

Each daily file has two sections:

```markdown
---
status: active
---

# Tasks

- [ ] Open task @Project #tag
- [x] Completed task
- [-] Cancelled task
- [>] Moved to another day

---

# AI

Processing notes, instructions, and analysis go here.
The app ignores everything below the AI section marker.
```

### Frontmatter

```yaml
---
status: active | readonly
---
```

- `active` — File can be edited by app (default)
- `readonly` — File is locked; app shows tasks but disables editing

### Task Section
App reads and writes this section only.

### AI Section
App ignores; AI/scripts can read and write freely.

---

## Task States

Tasks use markdown checkbox syntax with single-character states:

| State | Syntax | Meaning |
|-------|--------|---------|
| Open | `- [ ]` | Ready to be done |
| Done | `- [x]` | Completed |
| Cancelled | `- [-]` | Dropped/skipped/deleted |
| Moved | `- [>]` | Moved to another day |

**Examples:**
```markdown
- [ ] Call dentist @Health #phone
- [x] Buy groceries
- [-] Meeting cancelled
- [>] Moved to tomorrow → 2026-02-01
```

When a task is moved via swipe-right:
1. Original task marked `- [>]` with note of destination
2. Task appended to destination day's file as `- [ ]`

---

## Task Format

```markdown
- [ ] Task name @Project #tag #another-tag !priority +person
  Notes go here, indented with 2 spaces
  Can span multiple lines
```

### Labels (Tags)

Labels are **always prefixed with a symbol**. This makes parsing unambiguous.

| Symbol | Default Label | Example |
|--------|---------------|---------|
| `@` | Project | `@Work` `@Home` |
| `#` | Tag | `#urgent` `#phone` |
| `!` | Priority | `!high` `!low` |
| `+` | Person | `+Sarah` `+boss` |
| `~` | Estimate | `~5min` `~1hr` |
| `&` | Area | `&Health` `&Finance` |

**Rules:**
- Symbol + word (no space): `@Project` ✓
- Words after symbols are labels: `#my-tag` ✓
- Plain words are part of the task name, not labels
- Labels can appear anywhere after task name
- Label names: alphanumeric + hyphens, case-insensitive

**Configuration:** The display name for each symbol is configurable in `app.yaml`. The symbols themselves are fixed.

### Notes

Indented lines (2+ spaces) after a task are notes:

```markdown
- [ ] Review proposal @Work !high
  Important: CEO wants this by Friday
  Include Q4 projections
```

---

## Configuration

### /configuration/app.yaml

```yaml
# MinisList App Configuration

# What day to show on launch
# - "latest": Show most recent day with tasks
# - "today": Always show today (create if needed)
default_view: today

# Whether to auto-create today's file if missing
auto_create_today: true

# Symbol display names (customize these)
symbols:
  "@": "Project"
  "#": "Tag"
  "!": "Priority"
  "+": "Person"
  "~": "Estimate"
  "&": "Area"

# Which labels to show in list view (vs detail only)
show_in_list:
  - "@"  # Project
  - "#"  # Tags
  - "!"  # Priority

# Theme (future)
# theme: light | dark | system
```

### /configuration/AGENT.md

```markdown
# MinisList Agent Instructions

This folder contains daily task lists managed by the MinisList app.

## Folder Structure
- `/daily/` — One markdown file per day (YYYY-MM-DD.md)
- `/configuration/` — App and agent config

## File Format
Each daily file has two sections:
1. `# Tasks` — The app manages this section
2. `# AI` — You can freely read/write this section

## Task Syntax
- `- [ ]` — Open task
- `- [x]` — Done
- `- [-]` — Cancelled
- `- [>]` — Moved to another day

## Labels
Labels are prefixed with symbols:
- `@` — Project
- `#` — Tag
- `!` — Priority
- `+` — Person
- `~` — Estimate
- `&` — Area

## What You Can Do
- Read any file to understand tasks
- Write to the `# AI` section (notes, summaries, patterns)
- The app preserves your AI section content
- Do NOT edit the `# Tasks` section directly (app manages it)

## Example Workflow
1. User adds tasks via app
2. You read tasks, analyze patterns
3. You write insights to `# AI` section
4. User sees your notes when they view the file
```

---

## Screens

### 1. Task List (Main Screen)

**Default behavior (configurable):**
- `default_view: today` — Opens to today's date, creates file if missing
- `default_view: latest` — Opens to most recent day with tasks

**Elements:**
- Date header (tappable to open date picker)
- List of tasks with checkboxes
- Floating "+" button to add task
- Pull-to-refresh to reload file

**Display:**
- Task name + checkbox always shown
- Labels shown based on `show_in_list` config
- Tap task to see all details

**Interactions:**
| Gesture | Action |
|---------|--------|
| Tap checkbox | Toggle open ↔ done |
| Tap task | Open detail view |
| Swipe left | Mark cancelled (or delete) |
| Swipe right | Move to tomorrow |
| Drag handle | Reorder tasks |

**Move to Tomorrow:**
- Marks original as `- [>] Task → 2026-02-01`
- Appends `- [ ] Task` to tomorrow's file
- Creates tomorrow's file if needed
- Shows undo toast

### 2. Task Detail View

Shows full task information:
- Task name (editable)
- All labels (editable, with autocomplete)
- Notes (editable, multi-line)
- Task state indicator

### 3. Add Task

Single text field input:
- Type naturally: `Call dentist @Health #phone !high`
- Symbols parsed automatically into labels
- Press enter to add

### 4. Edit Task

Same as detail view, but focused for editing:
- Tap any field to edit
- Auto-save on close

### 5. Date Picker

**Access:** Tap date header

**Features:**
- Calendar view
- Dots on dates with files
- Lock icon on readonly dates
- "Today" quick button

### 6. Settings

- **Folder path:** Browse to select root folder (iCloud Drive)
- **Default view:** Today vs Latest
- **Symbol labels:** Customize what each symbol is called
- **List display:** Which labels show in list view

---

## File Sync

### iCloud Drive Only (v1)

- Native iOS UIDocumentPickerViewController for folder selection
- Watch for file changes via NSMetadataQuery
- Sync behavior:
  - On app open: Reload current file
  - On pull-to-refresh: Force reload
  - On change: Write immediately (debounced 500ms)

### Conflict Handling

If file changed externally while app has unsaved changes:
- Show conflict dialog
- Options: Keep mine, Keep theirs, Merge

---

## Parser Rules

### Reading a File

1. Parse YAML frontmatter (between `---` markers)
2. Find `# Tasks` section
3. Stop at `# AI` header (ignore rest)
4. Parse lines starting with `- [ ]`, `- [x]`, `- [-]`, `- [>]`
5. Extract labels: `(@[\w-]+)`, `(#[\w-]+)`, `(![\w-]+)`, `(\+[\w-]+)`, `(~[\w-]+)`, `(&[\w-]+)`
6. Indented lines (2+ spaces) after task = notes

### Writing a File

1. Write frontmatter
2. Write `# Tasks` header
3. Write tasks in display order
4. Write `---` separator
5. Write `# AI` header
6. Preserve AI section content exactly

---

## Data Model

### Task

```ruby
class Task
  attr_accessor :title        # String, required
  attr_accessor :state        # :open, :done, :cancelled, :moved
  attr_accessor :labels       # Hash of symbol => Array<String>
  attr_accessor :notes        # String, optional
  attr_accessor :moved_to     # Date, if state == :moved
end
```

### DayFile

```ruby
class DayFile
  attr_accessor :date         # Date
  attr_accessor :status       # :active, :readonly
  attr_accessor :tasks        # Array<Task>
  attr_accessor :ai_content   # String, preserved
end
```

---

## Edge Cases

- **Empty file:** Show "No tasks yet" + add button
- **Missing today's file:** Auto-create if `auto_create_today: true`
- **Missing tomorrow's file:** Auto-create when moving task
- **Readonly file:** Show tasks, disable editing, show lock icon
- **Moving from readonly:** Allowed (marks as moved, doesn't edit content)
- **Malformed lines:** Preserve as-is, don't parse
- **Symbols in notes:** Don't parse (notes are indented)
- **Unicode in labels:** Supported (`#日本語`)

---

## Future Considerations (v2+)

- **Search:** Full-text search across all days
- **Widgets:** iOS home screen widget
- **Apple Watch:** Quick view and check-off
- **Share extension:** Add task from other apps
- **Siri shortcuts:** "Add to today's list"
- **Archive view:** Browse by project/tag
- **Themes:** Light/dark mode

---

## Open Questions

1. **Swipe left behavior:** Delete entirely or mark cancelled `- [-]`?
2. **Moved task display:** Show moved tasks grayed out or hide them?
3. **Label autocomplete:** Source from current file or all files?

---

*This spec is a living document. Update as decisions are made.*
