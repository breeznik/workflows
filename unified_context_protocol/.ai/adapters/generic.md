# Generic LLM Integration Guide

## Detection

You are a generic LLM if:
- You don't have access to any agent-specific directories
- You're running via API, chat interface, or a tool without its own config system

## Integration Rules

You should use `.ai/` exclusively for all context management:

| Purpose | Location |
|---------|----------|
| Project state | `.ai/context/MASTER.md` |
| Change tracking | `.ai/context/changelog.md` |
| In-progress work | `.ai/context/active/` |
| Workflows | `.ai/workflows/` |
| Learnings | `.ai/knowledge/` |

## Session Protocol

### Start of Session

```bash
# Load project state
cat .ai/context/MASTER.md

# Check for in-progress work
ls .ai/context/active/
```

### During Session

- Follow workflows in `.ai/workflows/` for structured tasks
- Store any patterns or learnings in `.ai/knowledge/`
- Use `.ai/context/active/` for task tracking

### End of Session

```bash
# Update changelog
echo "## $(date)" >> .ai/context/changelog.md
echo "- [Your changes here]" >> .ai/context/changelog.md
```

1. Update `.ai/context/MASTER.md` if significant changes
2. If work is incomplete, create a task file in `.ai/context/active/`

## Tips for API Users

If you're using an LLM via API (OpenAI, Anthropic, etc.):

1. **Include context in system prompt**: Read `.ai/context/MASTER.md` and include it
2. **Persist changes**: After each session, update the relevant `.ai/` files
3. **Use structured output**: Ask the LLM to output changelog entries in a consistent format
