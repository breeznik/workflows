---
description: "Synchronizes the Agent's internal memory/artifacts to the UCP repository state."
---

# Workflow: Context Sync (v3.0)

> **Purpose**: Persist "Brain State" (RAM) to "Project State" (Disk).
> **Trigger**: Task Completion || Session End

## 0. SETUP
1. Read `../../corepack.paths.json` -> Set `CTX_DIR`.

## 1. PROOF OF WORK (Validation Gate)
> **CRITICAL**: You may NOT mark a task as `[x]` in `PLAN.md` unless:
> 1. You have run a verifiable test command (e.g. `npm test`, `pytest`).
> 2. You have seen the output `SUCCESS` or `PASS`.
> 3. **OR** you have visually confirmed the feature works (screenshot/browser check).

## 2. SYNC PROTOCOL

### A. The Plan (`CTX_DIR/active/PLAN.md`)
- **READ** disk version first.
- **MERGE** your internal progress.
- **OVERWRITE** disk version.
- *Conflict Rule*: If disk version advanced while you were working, TRUST DISK but append your unique sub-tasks.

### B. The Changelog (`CTX_DIR/changelog.md`)
- **APPEND** only completed items.
- Format: `- [x] [Feat/Fix] Concise description (Files touched)`

### C. Knowledge (`CTX_DIR/knowledge/learnings.md`)
- **FILTER**: Do not log trivia (e.g., "Python uses indentation").
- **LOG**: Log architectural decisions, gotchas, or hidden dependencies.
- Format: `## [Date] Pattern: [Name]\n[Description]`

## 3. FINAL CHECK
- **Output**: "✅ Sync Complete. Plan updated. Handoff ready."
