---
description: Non-destructive upgrade of .ai/ to latest UCP version
---

# Upgrade Workflow

> Upgrade your existing `.ai/` to the latest UCP version without losing data.

## When to Run

- New UCP version released
- Missing files detected
- Agent suggests upgrade during boot

---

## Steps

### 1. Check Current Version

```bash
cat .ai/VERSION
```

Note your current version. If no VERSION file exists, you're on v1.0.0 or earlier.

### 2. Review Release Notes

Read `.ai/CHANGELOG.md` (or get latest from UCP repo) to see what's new.

### 3. Add Missing Files (Non-Destructive)

For each file in latest UCP template:

| If file... | Action |
|------------|--------|
| Doesn't exist | ✅ Copy from template |
| Already exists | ⏭️ Skip (preserve user data) |

**Files added in v1.1.0:**
- `context/PRIORITY.md`
- `context/user-prefs.md`
- `context/dependencies.md`
- `knowledge/learnings.md`
- `knowledge/boundaries.md`
- `workflows/upgrade.md` (this file)
- `workflows/export.md`
- `VERSION`
- `CHANGELOG.md`

### 4. Update Existing Files (Careful!)

Some files may need new sections added:

| File | Check For |
|------|-----------|
| `.ai/README.md` | Context Priority section |
| `workflows/boot.md` | Tiered loading steps |
| `workflows/handoff.md` | learnings.md reference |
| Knowledge files | Tags field in templates |

**Rule: Add new sections, never overwrite existing content.**

### 5. Update VERSION

```yaml
version: "1.1.0"
installed: [keep original date]
last_upgrade: [today's date]
```

### 6. Verify

- [ ] All new files present
- [ ] VERSION updated
- [ ] Existing data preserved
- [ ] Boot protocol works

---

## Rollback

If something goes wrong:
1. Git revert (if .ai/ is committed)
2. Restore from archive/snapshot-*.md

---

## Future Upgrades

When v1.2.0 releases:
1. Read CHANGELOG.md for v1.2.0
2. Follow same process
3. Add only what's new
