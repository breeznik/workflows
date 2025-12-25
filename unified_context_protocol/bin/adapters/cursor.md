# Cursor

> Detect: `.cursor/rules/` + Composer

## Model

| System | Use |
|--------|-----|
| `.cursor/rules/` | File syntax rules |
| `.ai/` | Project state |

## Boot

```sh
cat .ai/context/MASTER.md
cat .cursor/rules/*.mdc
ls .ai/context/active/
```

## End

```sh
echo "changes" >> .ai/context/changelog.md
# Update MASTER if significant
```

## Bridge

`.cursor/rules/ai.mdc`:
```mdc
---
alwaysApply: true
---
Read `.ai/context/MASTER.md` on boot.
```

## Priority

MASTER → .cursor/rules → workflows
