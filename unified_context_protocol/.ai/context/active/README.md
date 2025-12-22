# Active Tasks & Scratchpad

> **External Memory for Agents**
> Use this folder to "write off" context or lock files during execution.

## 📂 Namespacing (Traffic Control)

To prevent collisions between agents working on different projects, **use sub-folders**:

- Global tasks: `active/task-[name].md`
- Project tasks: `active/[project-name]/task-[name].md`

**Example:**
- Agent A (Twitter Bot) -> `active/twitter-bot/task-fix-login.md`
- Agent B (Watcher) -> `active/watcher/task-update-api.md`

## Protocol

### 1. Start a Task
Check if `active/[project]/` exists. If not, create it.
Create your task file: `active/[project]/task-[slug].md`.

### 2. Dumping Memory (The "Write Off")
If you are hitting context limits, **dump your state here**:

```markdown
# Task: Auth Migration
**Scope**: Twitter Bot > Backend
**Status**: In Progress
**Current Step**: 3 of 5

## Context Dump
- Modified `user.py`
- Pending: `alembic upgrade head`

## Next Agent Instructions
1. Run migration
2. Verify login
```

### 3. Completion
1. Update project-specific changelog: `context/projects/[project]/changelog.md`
2. Update project status: `context/projects/[project]/MASTER.md`
3. Delete the task file in `active/[project]/`.
