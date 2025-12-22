# Antigravity Integration

> **Detection**: You have `.agent/workflows/` and `~/.gemini/antigravity/brain/`

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **Brain** (`~/.gemini/.../brain/`) | Session | `task.md`, `implementation_plan.md`, `walkthrough.md` |
| **`.ai/`** | Persistent | `MASTER.md`, `knowledge/`, `active/` handoffs |

**Flow**: `.ai/` → Brain (boot) → Brain → `.ai/` (sync)

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # 1. Load state
ls .ai/context/active/         # 2. Check pending work
# → Use brain for session planning
```

> `.ai/` is truth. Brain is informed by `.ai/`, not vice versa.

## End Protocol

1. Update `.ai/context/MASTER.md` (if significant)
2. Update `.ai/context/changelog.md`
3. Incomplete work → `.ai/context/active/`
4. Learnings → `.ai/knowledge/`

## Priority

1. `.ai/context/MASTER.md` → 2. `.ai/context/active/` → 3. Brain → 4. `.agent/workflows/`
