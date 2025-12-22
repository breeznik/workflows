# Claude Code Integration Guide

## Detection

You are Claude Code if:
- You can read `CLAUDE.md` in the project root
- You have access to `.claude/commands/` directory

## Integration Rules

### Scope Separation

| Directory | Purpose |
|-----------|---------|
| `CLAUDE.md` | Project-level instructions for Claude |
| `.claude/commands/` | Custom slash commands |
| `.ai/` | Universal project context, state, and knowledge |

### Recommended Setup

Add this to your `CLAUDE.md`:

```markdown
# Project Context

This project uses the Unified Context Protocol. 

## Before Any Work

1. Read `.ai/context/MASTER.md` for current project state
2. Check `.ai/context/active/` for in-progress work
3. Follow workflows in `.ai/workflows/`

## After Work

1. Update `.ai/context/changelog.md` with changes
2. Update `.ai/context/MASTER.md` if significant
3. Create task file in `.ai/context/active/` if incomplete

## Important

Use `.ai/` for all project context. Do not rely on conversation memory alone.
```

### Custom Commands

Create `.claude/commands/boot.md`:

```markdown
Read .ai/context/MASTER.md and .ai/context/active/ to load project state.
```

### What Goes Where

| Location | Use For |
|----------|---------|
| `CLAUDE.md` | High-level project instructions |
| `.claude/commands/` | Reusable slash commands |
| `.ai/workflows/` | Step-by-step procedures |
| `.ai/knowledge/` | Patterns, gotchas, architecture decisions |
| `.ai/context/` | Project state and memory |

## Session Protocol

### Start of Session

1. Run `.ai/workflows/boot.md` (or `/boot` command)
2. Read any Claude-specific instructions from `CLAUDE.md`

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
