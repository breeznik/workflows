# Generic LLM

> Detect: No agent config. API/chat/CLI.

## Reality

You are stateless. `.ai/` is your only memory.

## Boot

```sh
cat .ai/context/MASTER.md
ls .ai/context/active/
```

## End

```sh
echo "changes" >> .ai/context/changelog.md
echo "insights" >> .ai/knowledge/learnings.md
# Create handoff if incomplete
```

## API Integration

1. System prompt: Include MASTER.md
2. After session: Write to `.ai/`
3. Structured output: Changelog format

## Priority

MASTER → workflows → Session input
