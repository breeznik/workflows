---
description: Session startup checklist for AI agents
---

# Agent Boot Protocol

This workflow MUST be executed at the start of every AI session. It ensures the agent is grounded in the project's current state before taking any action.

// turbo-all

---

## 🎯 Context Budget

> Respect priority loading to prevent context overload.

| Priority | When to Load | Budget |
|----------|--------------|--------|
| **P0** | Always | ~2k tokens |
| **P1** | Based on task | ~3k tokens |
| **P2** | On demand | As needed |

See `context/PRIORITY.md` for full priority matrix.

---

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
3. **If still uncertain, ask the user**
4. Read your adapter file from `adapters/[agent].md`
5. If unknown/other, use `adapters/generic.md`

---

### 1. Load P0 Context (Always)

```bash
cat .ai/context/PRIORITY.md   # Understand what to load
cat .ai/context/MASTER.md     # Current project state
```

---

### 2. Check for Active Work

```bash
ls .ai/context/active/
```

- If task file exists → Read it, continue from where last agent stopped
- If empty → Ready for new work

---

### 3. Load P1 Context (Based on Task)

| If task involves... | Load these P1 files |
|---------------------|---------------------|
| Code changes | `context/tech.md`, `knowledge/patterns.md` |
| Debugging | `knowledge/gotchas.md`, `knowledge/learnings.md` |
| New feature | `context/user-prefs.md`, `workflows/feature.md` |
| External APIs | `context/dependencies.md` |

---

### 4. Load P2 Context (Only if Needed)

- `knowledge/decisions.md` — For architecture questions
- `knowledge/boundaries.md` — When unsure what you know
- `context/product/*.md` — For product/UX work

**Do NOT auto-load P2. Wait until explicitly needed.**

---

## Session End Protocol

Before ending your session:

1. **Update changelogs**
   - Add entry to `context/changelog.md`
   - Update `context/MASTER.md` if status changed

2. **Record learnings** (if any)
   - Add to `knowledge/learnings.md` what worked/failed

3. **Handoff incomplete work**
   - Create task file in `context/active/` using `workflows/handoff.md`

---

## ⚠️ Context Overload Prevention

If you notice context is getting large:

1. **Summarize, don't inline** — Reference files instead of copying
2. **Ask user** — "Which context is most relevant right now?"
3. **Run maintenance** — `workflows/maintenance.md` prunes and archives

