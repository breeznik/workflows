# Windsurf

> Detect: Cascade + `.windsurf/rules/`

## Model

| System | Use |
|--------|-----|
| Cascade | Session flow |
| `.ai/` | Permanent state |

Flow: `.ai/` → Cascade → `.ai/`

## Boot

```sh
cat .ai/context/MASTER.md
ls .ai/context/active/
# Cascade now grounded
```

## End

```sh
# Extract session learnings
echo "insights" >> .ai/knowledge/learnings.md
echo "changes" >> .ai/context/changelog.md
```

## Rule

`.windsurf/rules`:
```
ON BOOT: Read .ai/context/MASTER.md
ON END: Sync to .ai/knowledge/
```

## Priority

MASTER → Cascade → .windsurf/rules
