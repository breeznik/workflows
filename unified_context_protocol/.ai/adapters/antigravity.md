# Antigravity Integration Guide

## Detection

You are Antigravity if:
- You have access to `.agent/workflows/` in the user's home directory
- Your internal artifact directory is `~/.gemini/antigravity/brain/`

## Integration Rules

### Scope Separation

| Directory | Scope | Purpose |
|-----------|-------|---------|
| `.agent/workflows/` | Global (all projects) | User preferences, global test workflows |
| `.ai/` | This project only | Project state, knowledge, project-specific workflows |

### Priority Order

1. **Read `.ai/context/MASTER.md`** - Always load project state first
2. **Check `.ai/context/active/`** - Look for in-progress work from previous sessions
3. **Use `.ai/workflows/`** for project tasks
4. **Fall back to `.agent/workflows/`** only for truly global operations

### What NOT to Do

❌ Do NOT use your internal brain directory (`~/.gemini/antigravity/brain/`) for project context  
❌ Do NOT create task.md or implementation_plan.md in your brain - use `.ai/context/active/` instead  
❌ Do NOT store project learnings internally - use `.ai/knowledge/`

### Bridging Your Global Workflows

If you have a global workflow in `.agent/workflows/` that should trigger `.ai/` integration:

```markdown
# In .agent/workflows/project-init.md

1. Check if `.ai/` exists:
   ls .ai/

2. If yes, run the boot protocol:
   cat .ai/workflows/boot.md
   # Follow those instructions

3. Your global workflows still apply, but defer to .ai/ for project-specific procedures.
```

## Session Protocol

### Start of Session

1. Run `.ai/workflows/boot.md`
2. Load your global user preferences from `.agent/` if needed
3. Do NOT create artifacts in your internal brain - use `.ai/context/active/`

### End of Session

1. Update `.ai/context/changelog.md`
2. Update `.ai/context/MASTER.md` if significant changes
3. If work is incomplete, create a task file in `.ai/context/active/`
