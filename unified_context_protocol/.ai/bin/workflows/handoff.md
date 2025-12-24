# Workflow: Session Handoff

> **Trigger**: End of every session.

## 1. Documentation Update

```pseudo
FUNCTION sync_documentation():
  APPEND to ".ai/context/changelog.md": [YYYY-MM-DD] - Summary of changes
  UPDATE ".ai/context/MASTER.md": current_state, focus, warnings
```

## 2. Knowledge Capture

```pseudo
MATCH observation:
  CASE new_habit: UPDATE ".ai/context/user-prefs.md"
  CASE new_lesson: UPDATE ".ai/knowledge/learnings.md"
  CASE new_pattern: UPDATE ".ai/knowledge/patterns.md"
  CASE new_decision: UPDATE ".ai/knowledge/decisions.md"
  CASE new_trap: UPDATE ".ai/knowledge/gotchas.md"
```

## 3. Commit Cycle

```pseudo
RUN ".ai/bin/workflows/commit.md" // Batch code + context + knowledge
```

## 4. Handoff Task (If Incomplete)

```pseudo
IF work_is_unfinished:
  CREATE ".ai/context/active/handoff-[task].md"
  WRITE status, next_steps, blockers, relative_file_paths
```

## 5. Exit Message

> "Session complete. [Summary of commits]. [Link to handoff task if created]."
