# Copilot

> Detect: `.github/copilot-instructions.md`

## Model

| System | Limit |
|--------|-------|
| Copilot | Tab context only |
| `.ai/` | Full project |

Reality: Copilot is stateless. `.ai/` fills gap.

## Boot

```sh
cat .ai/context/MASTER.md
```

## End

```sh
echo "changes" >> .ai/context/changelog.md
echo "patterns" >> .ai/knowledge/patterns.md
```

## Setup

`.github/copilot-instructions.md`:
```markdown
Read `.ai/context/MASTER.md` for state.
Update `.ai/context/changelog.md` after edits.
```

## Priority

MASTER → Open tabs → copilot-instructions
