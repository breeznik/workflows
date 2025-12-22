# Cursor Integration

> **Detection**: You have `.cursor/rules/` and Composer features

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **Cursor Rules** (`.cursor/rules/`) | File-level | Syntax rules, model hints, tool-specific behavior |
| **`.ai/`** | Project-level | State, workflows, knowledge base |

**Relationship**: `.cursor/rules/` defines *how* to code. `.ai/` defines *what* to build.

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # 1. Load project state
cat .cursor/rules/*.mdc        # 2. Load syntax preferences
ls .ai/context/active/         # 3. Check pending work
```

> `.ai/` tracks project evolution. Cursor tracks coding style.

## End Protocol

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` (if significant)
3. Incomplete work → `.ai/context/active/`
4. New patterns → `.ai/knowledge/patterns.md`

## Recommended Bridge

Create `.cursor/rules/ai-bridge.mdc`:
```mdc
---
alwaysApply: true
---
Read `.ai/context/MASTER.md` at session start.
Update `.ai/context/changelog.md` at session end.
```

## Priority

1. `.ai/context/MASTER.md` → 2. `.cursor/rules/` → 3. `.ai/workflows/`
