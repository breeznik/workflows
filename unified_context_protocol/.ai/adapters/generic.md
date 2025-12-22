# Generic LLM Integration

> **Detection**: No agent-specific config. Running via API, chat, or simple CLI.

## System Model

**Reality**: You are stateless. `.ai/` is your only memory.

| System | Scope |
|--------|-------|
| **You** | This session only |
| **`.ai/`** | Forever |

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # Load truth
ls .ai/context/active/         # Check handoffs
```

> You forget. `.ai/` remembers.

## End Protocol

1. Update `.ai/context/changelog.md`
2. Save insights → `.ai/knowledge/learnings.md`
3. Incomplete → `.ai/context/active/handoff-[date].md`

## For API Users

If integrating via API:
1. **System prompt**: Include `.ai/context/MASTER.md`
2. **After session**: Write back to `.ai/`
3. **Structured output**: Request changelog format

## Priority

1. `.ai/context/MASTER.md` → 2. `.ai/workflows/` → 3. Session input
