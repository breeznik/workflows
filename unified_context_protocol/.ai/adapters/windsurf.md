# Windsurf / Codeium Integration Guide

## Detection

You are Windsurf/Cascade if:
- You can read `.windsurf/rules/` or `.windsurfrules`
- You have access to Cascade-specific features

## Integration Rules

### Scope Separation

| Directory | Purpose |
|-----------|---------|
| `.windsurf/rules/` | Windsurf-specific rules and preferences |
| `.ai/` | Universal project context, state, and knowledge |

### Recommended Setup

Add to your Cascade Rules:

```
CRITICAL: This project uses the Unified Context Protocol.

ON SESSION START:
- Read .ai/README.md and .ai/context/MASTER.md immediately
- Check .ai/context/active/ for in-progress work

THROUGHOUT SESSION:
- Use .ai/ for all task tracking (not internal memory)
- Update .ai/context/changelog.md with changes

ON SESSION END:
- Update .ai/context/MASTER.md if significant changes made
- Create task file in .ai/context/active/ if work incomplete
```

### What Goes Where

| Location | Use For |
|----------|---------|
| `.windsurf/rules/` | Windsurf-specific behavior rules |
| `.ai/workflows/` | Step-by-step procedures for features, bugfixes, refactors |
| `.ai/knowledge/` | Patterns, gotchas, architecture decisions |
| `.ai/context/` | Project state and memory |

## Session Protocol

### Start of Session

1. Run `.ai/workflows/boot.md`
2. Apply any Windsurf-specific rules

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
