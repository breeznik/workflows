# Antigravity Integration

> **Detection**: You have `.agent/workflows/` and `~/.gemini/antigravity/brain/`

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **Brain** (`~/.gemini/.../brain/`) | Session | `task.md`, `implementation_plan.md`, `walkthrough.md` |
| **`[CONTEXT_ROOT]/`** | Persistent | `MASTER.md`, `knowledge/`, `active/` handoffs |

**Flow**: `[CONTEXT_ROOT]/` → Brain (boot) → Brain → `[CONTEXT_ROOT]/` (sync)

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot Protocol

```sh
cat [CONTEXT_ROOT]/context/MASTER.md      # 1. Load state
ls [CONTEXT_ROOT]/context/active/         # 2. Check pending work
# → Use brain for session planning
```

> `[CONTEXT_ROOT]/` is truth. Brain is informed by `[CONTEXT_ROOT]/`, not vice versa.

## End Protocol

1. Update `[CONTEXT_ROOT]/context/MASTER.md` (if significant)
2. Update `[CONTEXT_ROOT]/context/changelog.md`
3. Incomplete work → `[CONTEXT_ROOT]/context/active/`
4. Run `bin/workflows/learning.md`

## Priority

1. `[CONTEXT_ROOT]/context/MASTER.md` → 2. `[CONTEXT_ROOT]/context/active/` → 3. Brain → 4. `.agent/workflows/`
