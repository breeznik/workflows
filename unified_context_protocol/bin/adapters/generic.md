# Generic LLM

> Detect: No agent config. API/chat/CLI.

## Reality

You are stateless. `[CONTEXT_ROOT]/` is your only memory.

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
echo "insights" >> [CONTEXT_ROOT]/knowledge/learnings.md
# Create handoff if incomplete
```

## API Integration

1. System prompt: Include MASTER.md
2. After session: Write to `[CONTEXT_ROOT]/`
3. Structured output: Changelog format

## Priority

MASTER → workflows → Session input
