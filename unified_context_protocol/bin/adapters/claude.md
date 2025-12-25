# Claude

> Detect: Artifacts + conversation

## Model

| System | Use |
|--------|-----|
| Conversation | Thinking |
| `[CONTEXT_ROOT]/` | Memory |

Flow: `[CONTEXT_ROOT]/` → Chat → `[CONTEXT_ROOT]/`

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot

```sh
```sh
cat [CONTEXT_ROOT]/context/MASTER.md
ls [CONTEXT_ROOT]/context/active/
```

## End

```sh
# Distill permanent insights
echo "learnings" >> [CONTEXT_ROOT]/knowledge/learnings.md
echo "changes" >> [CONTEXT_ROOT]/context/changelog.md
```

## Setup

`CLAUDE.md`:
```markdown
Read `[CONTEXT_ROOT]/context/MASTER.md` on boot.
Write learnings to `[CONTEXT_ROOT]/knowledge/`.
```

## Priority

MASTER → Conversation → CLAUDE.md
