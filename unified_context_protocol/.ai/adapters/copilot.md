# GitHub Copilot Integration

> **Detection**: You have `.github/copilot-instructions.md` or `AGENTS.md`

## System Model

| System | Scope | Limitation |
|--------|-------|------------|
| **Copilot** | File/Tab | Context from *open files only* |
| **`.ai/`** | Project-wide | Persistent, full codebase context |

**Reality**: Copilot is mostly stateless. `.ai/` fills the gap.

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # Load project state
# → Copilot now has project-level awareness
```

> Copilot sees files. `.ai/` sees the *project*.

## End Protocol

1. Update `.ai/context/changelog.md`
2. Document patterns → `.ai/knowledge/patterns.md`
3. Incomplete → `.ai/context/active/`

## Recommended Setup

Add to `.github/copilot-instructions.md`:
```markdown
Always read `.ai/context/MASTER.md` for project state.
Update `.ai/context/changelog.md` after edits.
```

## Priority

1. `.ai/context/MASTER.md` → 2. Open tabs → 3. `.github/copilot-instructions.md`
