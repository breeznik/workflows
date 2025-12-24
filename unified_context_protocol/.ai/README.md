# AI Context System

> **A drop-in documentation system for AI-assisted development.**
> Agents: Start here.

## 🧭 Navigation

**Where should you start?**

| If you are working on... | Read this first |
|--------------------------|-----------------|
| **The Core / Root Config / Specs** | `context/MASTER.md` |
| **A Specific Sub-Project** | `context/map.md` (finds your project context) |
| **First Time Setup** | `bin/workflows/onboarding.md` (The "Key") |
| **A New Feature / Bugfix** | `bin/workflows/README.md` (guides you) |
| **Committing Changes** | `bin/workflows/commit.md` (atomic commits) |
| **Picking up a shared task** | `context/active/README.md` (check for collisions) |

## 🚨 Agent Boot Protocol

**Every session MUST begin with these steps:**

1. `cat .ai/context/MASTER.md` — Load current project state
2. `ls .ai/context/active/` — Check for in-progress work
3. If resuming: Read the active task file and continue
4. If starting fresh: Read the relevant workflow in `bin/workflows/`

**Before ending a session:**

1. Update `context/changelog.md` with changes made
2. Update `context/MASTER.md` status if significant
3. If work is incomplete, create a task file in `context/active/`

> 📘 See `bin/workflows/boot.md` for the full boot protocol workflow.

---

## 🏗️ Structure

```
.ai/
├── bin/                  # THE UCP ENGINE (Managed by CLI)
│   ├── workflows/        # Operating Procedures
│   ├── adapters/         # Agent Integration
│   └── VERSION           # System Version
│
├── context/              # State & Memory (Data)
│   ├── MASTER.md         # Project state (P0)
│   ├── tech.md           # Tech stack (P1)
│   └── active/           # In-progress tasks
│
├── knowledge/            # Learning Bank (Experience)
│   ├── patterns.md       # Code patterns (P1)
│   └── learnings.md      # What works/fails (P1)
│
└── archive/              # History (P3 - never auto-load)
```

### 📊 Context Priority

| Priority | Files | Load When |
|----------|-------|-----------|
| **P0** | MASTER.md, PRIORITY.md, adapter | Always |
| **P1** | tech, user-prefs, patterns, gotchas | Based on task |
| **P2** | decisions, boundaries, product | On demand |
| **P3** | archive | Never auto-load |

> See `context/PRIORITY.md` for full budget rules.

## 🔌 Agent Detection

Before starting work, identify yourself:

1. Check `bin/adapters/manifest.yaml` for known agent types
2. If your config directory exists, read your adapter file:
   - Cursor: `bin/adapters/cursor.md`
   - Windsurf: `bin/adapters/windsurf.md`
   - Claude: `bin/adapters/claude.md`
   - Antigravity: `bin/adapters/antigravity.md`
   - Copilot: `bin/adapters/copilot.md`
   - JetBrains: `bin/adapters/jetbrains.md`
   - Aider: `bin/adapters/aider.md`
   - Generic: `bin/adapters/generic.md`
3. Follow the integration rules in your adapter file
4. Regardless of agent type, `.ai/` is the source of truth

---

## 🤖 Protocol

1. **Read First**: Always read the relevant `MASTER.md` before acting.
2. **Write Last**: Update `changelog.md` and `MASTER.md` before finishing.
3. **Respect Locks**: Check `active/` for conflicting work.
