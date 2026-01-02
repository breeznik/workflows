---
description: "Synchronizes the Agent's internal memory/artifacts to the UCP repository state."
---

# Workflow: Context Sync (v3.0)

> **Purpose**: Persist "Brain State" (RAM) to "Project State" (Disk).
> **Trigger**: Task Completion || Session End

## 1. PROOF OF WORK (Validation Gate)
> **CRITICAL**: You may NOT mark a task as `[x]` in `PLAN.md` unless:
> 1. You have run a verifiable test command (e.g. `npm test`, `pytest`).
> 2. You have seen the output `SUCCESS` or `PASS`.

## 2. SYNC PROTOCOL

### A. The Plan (`context/active/PLAN.md`)
- **READ** disk version first.
- **MERGE** your internal progress.
- **OVERWRITE** disk version.
- *Conflict Rule*: If disk version advanced while you were working, TRUST DISK but append your unique sub-tasks.

### B. The Changelog (`context/changelog.md`)
- **APPEND** only completed items.
- Format: `- [x] [Feat/Fix] Concise description (Files touched)`

### C. Knowledge (`knowledge/learnings.md`)
- **FILTER**: Do not log trivia (e.g., "Python uses indentation").
- **LOG**: Log architectural decisions, gotchas, or hidden dependencies.
- Format: `## [Date] Pattern: [Name]\n[Description]`

## 3. FINAL CHECK
- **Output**: "✅ Sync Complete. Plan updated. Handoff ready."
