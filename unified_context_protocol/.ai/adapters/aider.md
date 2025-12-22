# Aider Integration Guide

## Detection

You are Aider if:
- You can read `.aider.conf.yml` in the project or home directory
- You're running as the `aider` CLI tool

## Integration Rules

### Scope Separation

| Directory | Scope | Purpose |
|-----------|-------|---------|
| `.aider.conf.yml` | Project | Project-specific Aider settings |
| `~/.aider.conf.yml` | Global | User-wide Aider preferences |
| `.ai/` | Project | Universal project context, state, and knowledge |

### Recommended Setup

Add to your `.aider.conf.yml`:

```yaml
# Aider Configuration

# Read files at startup
read:
  - .ai/context/MASTER.md
  - .ai/README.md

# Reminder to update context
auto-commits: false  # So you can update .ai/ before committing
```

### What Goes Where

| Location | Use For |
|----------|---------|
| `.aider.conf.yml` | Aider-specific settings (model, API keys, etc.) |
| `.ai/workflows/` | Step-by-step procedures |
| `.ai/knowledge/` | Patterns, gotchas, architecture |
| `.ai/context/` | Project state and memory |

## Session Protocol

### Start of Session

1. Aider auto-reads files from `read:` config
2. Manually check `.ai/context/active/` for in-progress work

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
4. Then commit your changes
