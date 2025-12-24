# Workflow: Session Boot

> **Trigger**: Start of every session.

## 0. Format Detection (Evolution Layer)

```pseudo
// Support future format shifts (e.g., .yaml, .json)
CONFIG_EXT = SCAN_FOR_EXTENSION(".ai/context/MASTER.*")
IF CONFIG_EXT != ".md":
  LOG "🔄 Evolution format detected: ${CONFIG_EXT}"
  SET state.format = CONFIG_EXT
ELSE:
  SET state.format = ".md"
```

## 1. Load State

```pseudo
// Always load these first
LOAD ".ai/context/PRIORITY.md"
LOAD ".ai/context/MASTER.md"
```

## 2. Active Work Check

```pseudo
IF exists(".ai/context/active/*.md"):
  READ active_task_file
  RESUME work_from_last_checkpoint
ELSE:
  READY for_new_instruction
```

## 3. Work Execution

> **Rule**: You may use your internal memory/artifacts for speed.
> **Constraint**: You MUST run `bin/workflows/sync.md` at key checkpoints (Plan Finished, Session End).

## 4. Context Loading (P1)

```pseudo
MATCH task_type:
  CASE "coding":
    LOAD ".ai/context/tech.md"
    LOAD ".ai/knowledge/patterns.md"
  CASE "debugging":
    LOAD ".ai/knowledge/gotchas.md"
    LOAD ".ai/knowledge/learnings.md"
  CASE "feature":
    LOAD ".ai/context/user-prefs.md"
    LOAD ".ai/bin/workflows/feature.md"
  CASE "external_api":
    LOAD ".ai/context/dependencies.md"
```

## 4. Context Loading (P2 - On Demand)

```pseudo
// DO NOT AUTO-LOAD
IF need_architecture: READ ".ai/knowledge/decisions.md"
IF need_product_specs: READ ".ai/context/product/*.md"
IF uncertainty > high: READ ".ai/knowledge/boundaries.md"
```

## 5. Session End Protocol

```pseudo
FUNCTION end_session():
  UPDATE ".ai/context/changelog.md"
  IF work_complete:
    UPDATE ".ai/context/MASTER.md"
    RUN ".ai/bin/workflows/learning.md" // Crucial: Capture learnings
  ELSE:
    RUN ".ai/bin/workflows/handoff.md"
```
