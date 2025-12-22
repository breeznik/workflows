---
description: Session startup checklist for AI agents
---

# Agent Boot Protocol

This workflow MUST be executed at the start of every AI session. It ensures the agent is grounded in the project's current state before taking any action.

// turbo-all

## Steps

### 0. Self-Identification (if uncertain)

If you don't know which AI agent you are:

1. Check your system prompt for identifiers (e.g., "You are Cursor", "You are Antigravity")
2. Check for agent-specific directories:
   - `.cursor/rules/` → Cursor
   - `.windsurf/rules/` → Windsurf
   - `.agent/workflows/` → Antigravity
   - `CLAUDE.md` → Claude Code
   - `.github/copilot/` → GitHub Copilot
3. **If still uncertain, ask the user:**
   > "I need to know which AI assistant I am to follow the correct integration rules. Are you using Cursor, Windsurf, Claude Code, Antigravity, Copilot, or something else?"
4. Read your adapter file from `.ai/adapters/[agent].md`
5. If unknown/other, use `.ai/adapters/generic.md`

---

### 1. Read the current project status:
```bash
cat .ai/context/MASTER.md
```

### 2. Check for in-progress tasks:
```bash
ls .ai/context/active/
```

### 3. Resume or Start:
- If there's an active task file, read it and continue from where the previous agent left off.
- If starting fresh, read the appropriate workflow based on your task:
  - New feature: `.ai/workflows/feature.md`
  - Bug fix: `.ai/workflows/bugfix.md`
  - Refactor: `.ai/workflows/refactor.md`
  - Audit: `.ai/workflows/audit.md`

## Session End Protocol

Before ending your session:

1. Update `context/changelog.md` with changes made
2. Update `context/MASTER.md` status if significant progress was made
3. If work is incomplete, create a task file in `context/active/` using the handoff workflow
