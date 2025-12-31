# Workflow: Session Boot

> **Trigger**: Start of every session.

## 0. Pre-Flight Validation (MANDATORY)

```pseudo
// ASSERT these are complete before ANY work
ASSERT READ("context/PRIORITY.md") == true
ASSERT READ("context/MASTER.md") == true
ASSERT READ("bin/adapters/[SELF].md") == true

IF any_assertion_failed:
  HALT "❌ Boot incomplete. Read required files first."
```

## 1. Load State

```pseudo
LOAD "context/PRIORITY.md"   // Budget rules
LOAD "context/MASTER.md"     // Project state
LOAD "bin/adapters/[SELF].md" // Your integration
```

## 2. Active Work Check

```pseudo
IF exists("context/active/*.md"):
  READ active_task_file
  RESUME from_last_checkpoint
ELSE:
  READY for_new_instruction
```

## 3. Context Loading (P1 - Task-Based)

```pseudo
MATCH task_type:
  CASE "coding": LOAD "context/tech.md", "knowledge/patterns.md"
  CASE "debugging": LOAD "knowledge/gotchas.md", "knowledge/learnings.md"
  CASE "feature": LOAD "context/user-prefs.md"
  CASE "external_api": LOAD "context/dependencies.md"
```

## 4. Work Execution

> You may use internal memory for speed.
> **MUST** run `bin/workflows/sync.md` at checkpoints.

## 5. Session End Protocol

```pseudo
FUNCTION end_session():
  UPDATE "context/changelog.md"
  IF work_complete:
    UPDATE "context/MASTER.md"
    RUN "bin/workflows/learning.md"
  ELSE:
    RUN "bin/workflows/handoff.md"
```
