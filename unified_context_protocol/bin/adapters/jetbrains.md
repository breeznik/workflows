# JetBrains

> Detect: `.aiassistant/rules/` + IDE

## Model

| System | Use |
|--------|-----|
| IDE | Syntax/refactor |
| `[CONTEXT_ROOT]/` | Strategy |

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot

```sh
```sh
cat [CONTEXT_ROOT]/context/MASTER.md
ls [CONTEXT_ROOT]/context/active/
```

## End

```sh
```sh
echo "changes" >> [CONTEXT_ROOT]/context/changelog.md
echo "refactor patterns" >> [CONTEXT_ROOT]/knowledge/patterns.md
```

## Setup

`.aiassistant/rules/context.md`:
```markdown
Read `[CONTEXT_ROOT]/context/MASTER.md` before work.
Update `[CONTEXT_ROOT]/knowledge/` with insights.
```

## Priority

MASTER → IDE state → .aiassistant/rules
