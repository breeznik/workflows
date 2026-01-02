# Universal Development Workflow

> **Triggers**: user asks for "Feature", "Bugfix", or "Refactor".
> **Usage**: `MODE=[Feature|Bugfix|Refactor] dev_loop(goal)`

## 1. Safety Checks (ALL MODES)

```pseudo
CHECK context/active/:
  IF locked by another task: FAIL "Lock file exists"
  
CHECK bin/VERSION:
  IF breaking changes pending: WARN USER
```

## 2. Mode Selection & Planning

### MODE: ✨ Feature
> Adding new functionality.
- **Goal**: Implement new requirement $X.
- **Focus**: Integration, User Experience, Edge Cases.
- **Check**: `context/product/vision.md` (Does this align?)

### MODE: 🐛 Bugfix
> Fixing broken behavior.
- **Goal**: Restore expected behavior $Y.
- **Focus**: Root Cause Analysis, Regression Testing.
- **Check**: `knowledge/gotchas.md` (Is this a known issue?)
- **Action**: CREATE REPLICATION CASE first.

### MODE: ♻️ Refactor
> Improving code without changing behavior.
- **Goal**: Optimize structure/performance.
- **Focus**: Maintainability, Test Coverage.
- **Check**: `knowledge/patterns.md` (Align with standards).
- **Constraint**: NO behavior changes allowed.

## 3. Execution Loop

```pseudo
WHILE task_incomplete:
  read_relevant_files()
  
  IF MODE == "Bugfix":
    reproduce_failure()
    
  create_plan()
  write_code()
  
  verify_fix_or_feature()
  
  IF failed:
    update_learnings("What went wrong")
    retry()
```

## 4. Documentation & Commit

```pseudo
FUNCTION finalize():
  UPDATE "context/tech.md":
    - New dependencies?
    - Architecture changes?
    
  UPDATE "context/map.md":
    - New file relationships?

  UPDATE "knowledge/learnings.md":
    - "Tried X, failed, used Y instead"

  UPDATE "CHANGELOG.md":
    - "[Type] Description of change"
    
  RUN "bin/workflows/commit.md"
```
