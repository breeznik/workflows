# Workflow: Maintenance

> **Trigger**: `context/stats.md` warning || explicit user request || > 20 sessions

## 1. Safety Check

```pseudo
SNAPSHOT "[CONTEXT_ROOT]/context/MASTER.md" TO "[CONTEXT_ROOT]/archive/snapshot-YYYY-MM-DD.md"
```

## 2. Pruning Logic

```pseudo
FOREACH file IN context:
  MATCH file:
    CASE "MASTER.md":
      IF lines > 80: ARCHIVE "Recent Changes" TO history
      REMOVE resolved_warnings
    
    CASE "changelog.md":
      IF entries > 30: MOVE old_entries TO "[CONTEXT_ROOT]/archive/changelog-YYYY-MM.md"
    
    CASE "knowledge/*.md":
      IF lines > 200: SPLIT or ARCHIVE old_sections
    
    CASE "active/*.md":
      IF age > 48_hours: ARCHIVE or COMPLETE
```

## 3. Learning & Audit

```pseudo
FUNCTION validate_learnings():
  FOREACH entry IN "[CONTEXT_ROOT]/knowledge/learnings.md":
    IF entry.is_outdated: MOVE TO archive
    IF entry.is_pattern: MOVE TO "[CONTEXT_ROOT]/knowledge/patterns.md"

FUNCTION validate_prefs():
  SCAN "[CONTEXT_ROOT]/context/user-prefs.md"
  IF contradiction_found: ASK user
```

## 4. Final Output

> "Maintenance complete. All files within prompt limits. Learning validated."
