# GitHub Copilot Integration Guide

## Detection

You are GitHub Copilot if:
- You can read `.github/copilot/` directory
- You can read `AGENTS.md` in the project root

## Integration Rules

### Scope Separation

| Directory | Purpose |
|-----------|---------|
| `.github/copilot/` | Copilot-specific configuration |
| `AGENTS.md` | Agent instructions for Copilot Workspace |
| `.ai/` | Universal project context, state, and knowledge |

### Recommended Setup

Add to `.github/copilot-instructions.md`:

```markdown
# Unified Context Protocol

This project follows the Unified Context Protocol.

## Context Sources

- Project state: `.ai/context/MASTER.md`
- Active tasks: `.ai/context/active/`
- Workflows: `.ai/workflows/`
- Knowledge: `.ai/knowledge/`

## Session Protocol

Always read `MASTER.md` before starting work.
Update `changelog.md` after making changes.
```

For Copilot Workspace, add to `AGENTS.md`:

```markdown
# Agent Instructions

## Context System

This project uses `.ai/` for all context management.

Read `.ai/context/MASTER.md` to understand current state.
Check `.ai/context/active/` for in-progress work.
Follow workflows in `.ai/workflows/`.
```

### What Goes Where

| Location | Use For |
|----------|---------|
| `.github/copilot/` | Copilot-specific settings |
| `AGENTS.md` | High-level agent instructions |
| `.ai/workflows/` | Step-by-step procedures |
| `.ai/knowledge/` | Patterns, gotchas, architecture |
| `.ai/context/` | Project state and memory |

## Session Protocol

### Start of Session

1. Run `.ai/workflows/boot.md`
2. Apply any Copilot-specific configuration

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
