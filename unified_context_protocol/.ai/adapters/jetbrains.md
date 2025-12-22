# JetBrains AI Assistant Integration Guide

## Detection

You are JetBrains AI Assistant if:
- You can read `.aiassistant/rules/` directory
- You're running within a JetBrains IDE (IntelliJ, PyCharm, WebStorm, etc.)

## Integration Rules

### Scope Separation

| Directory | Purpose |
|-----------|---------|
| `.aiassistant/rules/` | JetBrains AI-specific rules |
| `.ai/` | Universal project context, state, and knowledge |

### Recommended Setup

Create `.aiassistant/rules/context.md`:

```markdown
# Unified Context Protocol

This project uses the .ai/ directory for context management.

## Required Actions

Before starting work:
1. Read `.ai/context/MASTER.md`
2. Check `.ai/context/active/`

After completing work:
1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if needed
```

### What Goes Where

| Location | Use For |
|----------|---------|
| `.aiassistant/rules/` | JetBrains-specific behavior rules |
| `.ai/workflows/` | Step-by-step procedures |
| `.ai/knowledge/` | Patterns, gotchas, architecture |
| `.ai/context/` | Project state and memory |

## Session Protocol

### Start of Session

1. Run `.ai/workflows/boot.md`
2. Apply any JetBrains-specific rules

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
