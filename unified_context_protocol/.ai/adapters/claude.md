# Claude

> Detect: Artifacts + conversation

## Model

| System | Use |
|--------|-----|
| Conversation | Thinking |
| `.ai/` | Memory |

Flow: `.ai/` → Chat → `.ai/`

## Boot

```sh
cat .ai/context/MASTER.md
ls .ai/context/active/
```

## End

```sh
# Distill permanent insights
echo "learnings" >> .ai/knowledge/learnings.md
echo "changes" >> .ai/context/changelog.md
```

## Setup

`CLAUDE.md`:
```markdown
Read `.ai/context/MASTER.md` on boot.
Write learnings to `.ai/knowledge/`.
```

## Priority

MASTER → Conversation → CLAUDE.md
