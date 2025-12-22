# JetBrains

> Detect: `.aiassistant/rules/` + IDE

## Model

| System | Use |
|--------|-----|
| IDE | Syntax/refactor |
| `.ai/` | Strategy |

## Boot

```sh
cat .ai/context/MASTER.md
ls .ai/context/active/
```

## End

```sh
echo "changes" >> .ai/context/changelog.md
echo "refactor patterns" >> .ai/knowledge/patterns.md
```

## Setup

`.aiassistant/rules/context.md`:
```markdown
Read `.ai/context/MASTER.md` before work.
Update `.ai/knowledge/` with insights.
```

## Priority

MASTER → IDE state → .aiassistant/rules
