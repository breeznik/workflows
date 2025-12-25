# Cursor

> Detect: `.cursor/rules/` + Composer

## Model

| System | Use |
|--------|-----|
| `.cursor/rules/` | File syntax rules |
| `[CONTEXT_ROOT]/` | Project state |

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot

```sh
cat [CONTEXT_ROOT]/context/MASTER.md
cat .cursor/rules/*.mdc
ls [CONTEXT_ROOT]/context/active/
```

## End

```sh
echo "changes" >> [CONTEXT_ROOT]/context/changelog.md
# Update MASTER if significant
```

## Bridge

`.cursor/rules/ai.mdc`:
```mdc
---
alwaysApply: true
---
---
Read `[CONTEXT_ROOT]/context/MASTER.md` on boot.
```

## Priority

MASTER → .cursor/rules → workflows
