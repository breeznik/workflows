# Maintenance Workflow

> Use periodically (every ~20 sessions) to keep context lean.

## When to Run
- Changelog exceeds 50 entries
- MASTER.md feels cluttered
- Knowledge files are getting long

## Steps

### 1. Archive Old Changelog
Move entries older than 30 days to `archive/changelog-YYYY-MM.md`
Keep only the last 10-15 entries in main changelog.

### 2. Compress MASTER.md
- Remove resolved warnings
- Summarize old "Recent Changes" into one line
- Keep only currently relevant state

### 3. Prune Knowledge Files
- Merge duplicate patterns
- Archive obsolete gotchas
- Keep only actively-used decisions

### 4. Create Snapshot
Save current MASTER.md to `archive/snapshot-YYYY-MM-DD.md` before major changes.

## Context Size Guidelines

| File | Target Size | Action if Exceeded |
|------|-------------|-------------------|
| MASTER.md | < 100 lines | Summarize or archive |
| changelog.md | < 50 entries | Archive old entries |
| Each knowledge file | < 200 lines | Split or archive |

## Archive Naming

```
archive/
├── changelog-2024-12.md
├── changelog-2025-01.md
├── snapshot-2025-01-15.md
└── deprecated-patterns.md
```
