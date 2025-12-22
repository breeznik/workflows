# Cursor Integration Guide

## Detection

You are Cursor if:
- You can read `.cursor/rules/*.mdc` files
- You have access to Cursor-specific features (composer, etc.)

## Integration Rules

### Scope Separation

| Directory | Purpose |
|-----------|---------|
| `.cursor/rules/` | Cursor-specific rule files (file globs, model hints) |
| `.ai/` | Universal project context, state, and knowledge |

### Recommended Setup

Create a bridge rule in `.cursor/rules/ai-context.mdc`:

```mdc
---
description: Bridge to .ai context system
alwaysApply: true
---

At the start of every session:
1. Read `.ai/context/MASTER.md` to understand project state
2. Check `.ai/context/active/` for in-progress work
3. Before ending, update `.ai/context/changelog.md`

Use `.ai/knowledge/` for storing patterns and gotchas discovered during this session.
```

### What Goes Where

| Location | Use For |
|----------|---------|
| `.cursor/rules/` | File-pattern-specific rules (e.g., "for *.tsx files, use...") |
| `.ai/workflows/` | Step-by-step procedures for features, bugfixes, refactors |
| `.ai/knowledge/` | Patterns, gotchas, architecture decisions |
| `.ai/context/` | Project state and memory |

## Session Protocol

### Start of Session

1. Run `.ai/workflows/boot.md`
2. Apply any Cursor-specific rules from `.cursor/rules/`

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
