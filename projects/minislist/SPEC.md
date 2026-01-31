# Minislist — Specification

> *The dumb todo list for your smart AI*

**Version:** 0.1 (Draft)
**Last Updated:** 2026-01-31

## Overview

**Minislist** is a simple iPhone app for daily task management. Tasks are stored as plain markdown files (one per day) that sync with a user-configured folder. The format is designed to be human-readable and editable from any text editor (Obsidian, Cursor, vim, etc.).

**Tech Stack:**
- Ruby on Rails backend
- Hotwire Native for iOS wrapper
- Hotwire (Turbo + Stimulus) for frontend
- File-based storage (iCloud Drive, Dropbox, or local)

---

## Core Concepts

### One File Per Day

Each day gets its own markdown file:

```
/configured-folder/
  2026-01-31.md
  2026-01-30.md
  2026-01-29.md
```

**File naming:** `YYYY-MM-DD.md` (ISO 8601 date format)

### File Sections

Each daily file has two distinct sections:

```markdown
---
readonly: false
---

# Tasks

- [ ] Task one @Work #urgent
- [ ] Task two @Home
- [x] Completed task

---

# AI

Processing notes, instructions, and analysis go here.
The app ignores everything below the AI section marker.
```

**Section rules:**
- `# Tasks` — App reads and writes this section only
- `# AI` — App ignores; AI/scripts can read and write freely
- Separator: `---` + `# AI` header marks the boundary
- App never touches content below the AI header

**Use cases for AI section:**
- Processing notes ("Moved 3 tasks from yesterday")
- Daily summary ("Completed 5/8 tasks, @Health deferred again")
- Instructions for tomorrow ("Schedule dentist first thing")
- Pattern observations ("Third day in a row deferring +Taxes")

### Task Format

```markdown
- [ ] Task title @Project #tag !priority +person ~estimate &area
  Notes: Optional multi-line notes here
  Can span multiple lines

- [x] Completed task @Work #done
```

**Checkbox states:**
- `- [ ]` — Open/incomplete
- `- [x]` — Completed

### Symbol Prefixes

Six symbol types are supported. Meanings are **user-configurable** — the app doesn't enforce what each symbol represents.

| Symbol | Default Label | Example |
|--------|---------------|---------|
| `@` | Project | `@Work` `@Home` `@SideProject` |
| `#` | Tag | `#urgent` `#phone` `#waiting` |
| `!` | Priority | `!high` `!1` `!today` |
| `+` | Person | `+Sarah` `+boss` `+dentist` |
| `~` | Estimate | `~5min` `~1hr` `~quick` |
| `&` | Area | `&Health` `&Finance` `&Family` |

**User can rename these** in settings (e.g., change `+` from "Person" to "Context").

### Read-Only Files

Files can be marked read-only to prevent editing. Use case: a background process "closes" past days after archiving or processing.

**Detection methods (check in order):**
1. Filesystem permissions (read-only = `444` or similar)
2. Frontmatter flag:

```markdown
---
readonly: true
---

- [x] Task from yesterday
```

When a file is read-only, the app:
- Displays tasks but disables checkboxes
- Hides "add task" button
- Shows a visual indicator (lock icon, muted colors)

---

## Screens

### 1. Task List (Main Screen)

The primary view. Shows tasks for the selected day.

**Default behavior:**
- Opens to the latest day (most recent file)
- If no file exists for today, shows empty state with "Add first task"

**Elements:**
- Date header (tappable to open date picker)
- List of tasks with checkboxes
- Floating "+" button to add task
- Pull-to-refresh to reload file

**Simple vs Detailed display:**
- By default, shows only task title + checkbox
- Configurable: show/hide symbols inline (see Settings)

**Interactions:**
- Tap checkbox → toggle complete/incomplete (mark done)
- Tap task → open Detail View
- Swipe left → delete task (with confirmation)
- Swipe right → move to tomorrow (defer task)
- Long press → quick actions (edit, delete, move to tomorrow)
- Drag handle → reorder tasks (drag & drop to change position)

**Task Actions Summary:**
| Action | Gesture | Result |
|--------|---------|--------|
| Mark done | Tap checkbox | Toggle `[ ]` ↔ `[x]` |
| Delete | Swipe left | Remove from file |
| Move to tomorrow | Swipe right | Remove from today, append to tomorrow's file |
| View details | Tap task | Open detail screen |
| Reorder | Drag handle | Move task up/down in list |

**Move to Tomorrow behavior:**
- Removes task from current day's file
- Appends task to next day's file (creates file if needed)
- Preserves all metadata (project, tags, notes, etc.)
- Shows brief "Moved to tomorrow" toast/undo option

### 2. Task Detail View

Shown when tapping a task.

**Displays:**
- Full task title
- All symbol values (project, tags, priority, person, estimate, area)
- Notes (full text, multi-line)

**Edit mode:**
- Tap any field to edit
- Auto-save on blur/close
- Symbol fields show autocomplete from previously used values

### 3. Date Picker / Day Navigation

**Access:** Tap date header or swipe horizontally

**Features:**
- Calendar view showing which dates have files
- Visual indicator for read-only days (grayed out or lock icon)
- Quick jump: "Today" button

### 4. Add/Edit Task

**Simple input mode (default):**
- Single text field
- Type naturally: `Call dentist @Health #phone !high`
- Symbols are parsed automatically

**Structured input mode (optional):**
- Separate fields for title, project, tags, etc.
- Toggle in settings

### 5. Settings / Configuration

**File Location:**
- Path to todo folder
- Options: iCloud Drive, Dropbox, Local (app sandbox)
- "Browse" button to select folder

**File Format:**
- Date format for filename (default: `YYYY-MM-DD.md`)
- Checkbox style: `- [ ]` vs `* [ ]`
- Notes prefix (default: 2-space indent)

**Symbol Configuration:**
- For each symbol (`@`, `#`, `!`, `+`, `~`, `&`):
  - Enabled: yes/no
  - Label: what it's called (e.g., "Project", "Context")
  - Show in list: yes/no (display on main screen vs detail only)

**Display Options:**
- `showProjectInList`: true/false
- `showTagsInList`: true/false
- `showPriorityInList`: true/false
- `showPersonInList`: true/false
- `showEstimateInList`: true/false
- `showAreaInList`: true/false

**Behavior:**
- Default to today: yes/no
- Auto-create today's file: yes/no

---

## File Sync

### Supported Backends

1. **iCloud Drive**
   - Native iOS integration
   - Folder picker using UIDocumentPickerViewController
   - Watch for file changes (NSMetadataQuery)

2. **Dropbox**
   - Dropbox SDK integration
   - OAuth login
   - Sync on app open + pull-to-refresh

3. **Local Only**
   - Files in app sandbox
   - No sync (useful for testing or privacy)

### Sync Behavior

- **On app open:** Reload current day's file
- **On pull-to-refresh:** Force reload
- **On task change:** Write immediately (debounced 500ms)
- **Background refresh:** Optional, configurable

### Conflict Handling

If file changed externally while app has unsaved changes:
- Show diff/conflict UI
- Options: Keep mine, Keep theirs, Merge (append both)

---

## Data Model

### Task

```ruby
class Task
  attr_accessor :title        # String, required
  attr_accessor :completed    # Boolean
  attr_accessor :project      # String, optional (@)
  attr_accessor :tags         # Array<String> (#)
  attr_accessor :priority     # String, optional (!)
  attr_accessor :person       # String, optional (+)
  attr_accessor :estimate     # String, optional (~)
  attr_accessor :area         # String, optional (&)
  attr_accessor :notes        # String, optional (multi-line)
  attr_accessor :line_number  # Integer, position in file
end
```

### DayFile

```ruby
class DayFile
  attr_accessor :date         # Date
  attr_accessor :path         # String, full file path
  attr_accessor :readonly     # Boolean
  attr_accessor :tasks        # Array<Task>
  attr_accessor :raw_content  # String, original file content
end
```

### UserConfig

```ruby
class UserConfig
  attr_accessor :folder_path
  attr_accessor :date_format        # Default: "%Y-%m-%d"
  attr_accessor :checkbox_style     # Default: "- [ ]"
  attr_accessor :symbols            # Hash of symbol configs
  attr_accessor :display_options    # Hash of show/hide flags
end
```

---

## Parser Rules

### Reading a File

1. Check for YAML frontmatter (between `---` markers at top)
2. Find `# Tasks` section — only parse content here
3. Stop parsing at `# AI` header (ignore everything below)
4. Parse each line starting with `- [ ]` or `- [x]` as a task
5. Subsequent indented lines (2+ spaces) are notes
6. Extract symbols using regex: `(@\w+)`, `(#\w+)`, `(!\w+)`, `(\+\w+)`, `(~\w+)`, `(&\w+)`

### Writing a File

1. Preserve frontmatter if present
2. Write `# Tasks` header
3. Write tasks in display order (reordering in app = reordering in file)
4. Format: `- [x] Title @project #tag #tag2 !priority +person ~estimate &area`
5. Notes on next line(s), indented 2 spaces
6. Write `---` separator + `# AI` header
7. Preserve AI section content exactly as-is (never modify)

**Reorder behavior:** When user drags a task to a new position, the file is rewritten with tasks in the new order. The line order in the markdown file always matches the display order in the app.

**AI section protection:** The app reads but never writes to the AI section. If creating a new file, it adds an empty AI section placeholder.

---

## Edge Cases

- **Empty file:** Show "No tasks yet" + add button
- **Missing today's file:** Auto-create on first task add (if enabled)
- **Missing tomorrow's file:** Auto-create when deferring a task
- **Malformed lines:** Preserve as-is, don't parse as tasks
- **Symbols in notes:** Don't parse symbols inside notes block
- **Unicode in tags:** Support unicode (`#日本語` should work)
- **Defer from read-only day:** Should this be allowed? (Probably yes — moves task out, doesn't edit read-only file)

---

## Future Considerations (v2+)

- **Search:** Full-text search across all days
- **Recurring tasks:** Template for daily/weekly tasks
- **Widgets:** iOS home screen widget showing today's tasks
- **Apple Watch:** Quick view and check-off
- **Push notifications:** Reminders for tasks with times
- **Share extension:** Add task from other apps
- **Siri shortcuts:** "Add to today's list"
- **Archive view:** Browse completed tasks by project/tag

---

## Open Questions

1. **Offline behavior:** Queue writes when offline? Or require connection?
2. **Multi-device conflict:** How aggressive with sync? Real-time or manual refresh?
3. **Migration:** Import from other todo apps (Things, Todoist export)?
4. **Themes:** Light/dark mode? Custom colors?

---

## Getting Started (Development)

```bash
# Create Rails app with Hotwire
rails new daily-todo --css=tailwind --javascript=esbuild

# Add Hotwire Native
# See: https://github.com/hotwired/hotwire-native-ios

# Key gems
gem "turbo-rails"
gem "stimulus-rails"
```

iOS wrapper setup: [Hotwire Native iOS Guide](https://native.hotwired.dev/)

---

*This spec is a living document. Update as decisions are made.*
