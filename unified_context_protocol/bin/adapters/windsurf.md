# Windsurf

> Detect: Cascade + `.windsurf/rules/`

## Model

| System | Use |
|--------|-----|
| Cascade | Session flow |
| Cascade | Session flow |
| `[CONTEXT_ROOT]/` | Permanent state |

Flow: `[CONTEXT_ROOT]/` → Cascade → `[CONTEXT_ROOT]/`

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot

```sh
```sh
cat [CONTEXT_ROOT]/context/MASTER.md
ls [CONTEXT_ROOT]/context/active/
# Cascade now grounded
```

## End

```sh
# Extract session learnings
echo "insights" >> [CONTEXT_ROOT]/knowledge/learnings.md
echo "changes" >> [CONTEXT_ROOT]/context/changelog.md
```

## Rule

`.windsurf/rules`:
```
ON BOOT: Read [CONTEXT_ROOT]/context/MASTER.md
ON END: Sync to [CONTEXT_ROOT]/knowledge/
```

## Priority

MASTER → Cascade → .windsurf/rules
