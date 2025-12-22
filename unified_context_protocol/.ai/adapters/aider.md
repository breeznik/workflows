# Aider Integration

> **Detection**: You have `.aider.conf.yml` and run as the `aider` CLI tool

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **Aider** (CLI session) | Git-native | Code editing, auto-commits, file management |
| **`.ai/`** | Persistent | State, knowledge base, handoffs between sessions |

**Flow**: `.ai/` → Aider (edits) → Git → `.ai/` (learnings)

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # 1. Load state
aider                          # 2. Start session
# → Now informed by project context
```

> Aider is git-first. `.ai/` is project-first.

## End Protocol

1. Update `.ai/context/changelog.md`
2. Extract learnings → `.ai/knowledge/`
3. Incomplete → `.ai/context/active/`
4. **Then** git commit

## Recommended Config

Add to `.aider.conf.yml`:
```yaml
read:
  - .ai/context/MASTER.md
  - .ai/README.md
```

## Priority

1. `.ai/context/MASTER.md` → 2. Aider session → 3. `.aider.conf.yml`
