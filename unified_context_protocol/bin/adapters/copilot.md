# Copilot

> Detect: `.github/copilot-instructions.md`

## Model

| System | Limit |
|--------|-------|
| Copilot | Tab context only |
| `[CONTEXT_ROOT]/` | Full project |

Reality: Copilot is stateless. `[CONTEXT_ROOT]/` fills gap.

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot

```sh
```sh
cat [CONTEXT_ROOT]/context/MASTER.md
```

## End

```sh
echo "changes" >> [CONTEXT_ROOT]/context/changelog.md
echo "patterns" >> [CONTEXT_ROOT]/knowledge/patterns.md
```

## Setup

`.github/copilot-instructions.md`:
```markdown
Read `[CONTEXT_ROOT]/context/MASTER.md` for state.
Update `[CONTEXT_ROOT]/context/changelog.md` after edits.
```

## Priority

MASTER → Open tabs → copilot-instructions
