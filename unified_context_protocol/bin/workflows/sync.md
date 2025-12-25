---
description: "Synchronizes the Agent's internal memory/artifacts to the UCP repository state."
---

# Workflow: Context Sync (Hybrid Checkpoint)

> **Trigger**: Phase Completion || Session End || User Correction
> **Purpose**: Persist your internal "Fast RAM" state to the project's "Hard Drive".

## 1. The Mapping Protocol (Concept -> File)

You must extract the following concepts from your internal memory (Artifacts, Chat History, Graph) and write them to the Repo.

| Concept | Target File | Action |
|---------|-------------|--------|
| **The Plan** | `[CONTEXT_ROOT]/context/active/PLAN.md` | **OVERWRITE** with current detailed plan & status. |
| **Progress** | `[CONTEXT_ROOT]/context/changelog.md` | **APPEND** completed steps since last sync. |
| **Learnings** | `[CONTEXT_ROOT]/knowledge/learnings.md` | **APPEND** new facts, patterns, or user preferences. |

## 2. Execution Logic

```pseudo
FUNCTION sync_state():
  # 1. Capture the Brain
  INTERNAL_STATE = GET_INTERNAL_MEMORY()

  # 2. Persist the Plan (Safety Check)
  CURRENT_DISK_PLAN = READ_FILE "[CONTEXT_ROOT]/context/active/PLAN.md"
  IF CURRENT_DISK_PLAN differs significantly from INTERNAL_STATE.original_read:
     PRINT "⚠️ Conflict: PLAN.md changed externally. Merging changes..."
     MERGED_PLAN = SMART_MERGE(CURRENT_DISK_PLAN, INTERNAL_STATE.current_plan)
     WRITE_FILE "[CONTEXT_ROOT]/context/active/PLAN.md" CONTENT = MERGED_PLAN
  ELSE:
     WRITE_FILE "[CONTEXT_ROOT]/context/active/PLAN.md" CONTENT = INTERNAL_STATE.current_plan

  # 3. Log Progress
  IF INTERNAL_STATE.has_new_completed_items:
    APPEND_FILE "[CONTEXT_ROOT]/context/changelog.md":
      CONTENT = "- [x] " + INTERNAL_STATE.just_completed_items

  # 4. Save Knowledge
  IF INTERNAL_STATE.learned_something_new:
    APPEND_FILE "[CONTEXT_ROOT]/knowledge/learnings.md":
      CONTENT = "## [Date] New Insight\n" + INTERNAL_STATE.insight

  PRINT "✅ Context Synced to Disk."
```

## 3. Verification
- open `[CONTEXT_ROOT]/context/active/PLAN.md` -> Does it match your internal plan?
