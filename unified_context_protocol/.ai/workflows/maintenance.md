# Maintenance Workflow

> Keep context lean and efficient. Run when triggered or every ~20 sessions.

---

## 🚨 Auto-Triggers

Run this workflow when ANY of these apply:

| Trigger | Threshold |
|---------|-----------|
| Changelog entries | > 30 entries |
| MASTER.md lines | > 100 lines |
| Any knowledge file | > 200 lines |
| User says "context feels slow" | Immediately |
| Last maintenance | > 30 days ago |
| `stats.md` shows warnings | Immediately |

> **Tip**: Check `context/stats.md` first. If warnings exist, run `workflows/compress.md`.

---

## Steps

### 1. Audit Context Sizes

Check each file against limits:

| File | Soft Limit | Hard Limit | Action |
|------|------------|------------|--------|
| MASTER.md | 80 lines | 120 lines | Archive Recent Changes |
| changelog.md | 30 entries | 50 entries | Archive old entries |
| Each knowledge file | 150 lines | 250 lines | Split or archive |
| Each active task | - | 7 days old | Complete or archive |

### 2. Archive Old Changelog

```
1. Move entries older than 30 days to archive/changelog-YYYY-MM.md
2. Keep only last 15 entries in main changelog
3. Add summary line: "See archive/ for older entries"
```

### 3. Prune MASTER.md

- Remove resolved warnings
- Collapse old "Recent Changes" into one-liner
- Keep only currently relevant state
- Target: < 80 lines

### 4. Prune Knowledge Files

| File | Action |
|------|--------|
| `patterns.md` | Merge duplicates, archive unused |
| `gotchas.md` | Remove fixed gotchas |
| `decisions.md` | Archive superseded decisions |
| `learnings.md` | Move "Superseded" to archive |
| `boundaries.md` | Update with current state |

### 5. Validate Learnings

For each entry in `learnings.md`:

```
- Is it still accurate? → Keep
- Is it outdated? → Move to "Superseded" section
- Is it now a pattern? → Move to patterns.md
```

### 6. Clean Active Tasks

```bash
ls .ai/context/active/
```

For each task file:
- Older than 7 days? → Archive or complete it
- Still relevant? → Keep
- Blocked? → Note in MASTER.md warnings

### 7. Create Snapshot

Before destructive changes, save:

```bash
cp context/MASTER.md archive/snapshot-YYYY-MM-DD.md
```

---

## Archive Structure

```
archive/
├── changelog-2024-12.md      # Monthly changelogs
├── changelog-2025-01.md
├── snapshot-2025-01-15.md    # Point-in-time MASTER.md
├── deprecated-patterns.md    # Old patterns
├── superseded-decisions.md   # Old decisions
└── resolved-gotchas.md       # Fixed gotchas
```

---

## Post-Maintenance Checklist

- [ ] All files under soft limits
- [ ] MASTER.md current and concise
- [ ] No stale active tasks
- [ ] Learnings validated
- [ ] Snapshot saved if major pruning

