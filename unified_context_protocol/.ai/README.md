# AI Context System

> **A drop-in documentation system for AI-assisted development.**
> Agents: Start here.

## 🧭 Navigation

**Where should you start?**

| If you are working on... | Read this first |
|--------------------------|-----------------|
| **The Core / Root Config / Specs** | `context/MASTER.md` |
| **A Specific Sub-Project** | `context/map.md` (finds your project context) |
| **A New Feature / Bugfix** | `workflows/README.md` (guides you) |
| **Picking up a shared task** | `context/active/README.md` (check for collisions) |

## 🚨 Agent Boot Protocol

**Every session MUST begin with these steps:**

1. `cat .ai/context/MASTER.md` — Load current project state
2. `ls .ai/context/active/` — Check for in-progress work
3. If resuming: Read the active task file and continue
4. If starting fresh: Read the relevant workflow in `workflows/`

**Before ending a session:**

1. Update `context/changelog.md` with changes made
2. Update `context/MASTER.md` status if significant
3. If work is incomplete, create a task file in `context/active/`

> 📘 See `workflows/boot.md` for the full boot protocol workflow.

---

## 🏗️ Structure

```
.ai/
├── context/          # State & Memory
│   ├── MASTER.md     # Global Root
│   ├── projects/     # Sub-Project Roots
│   └── active/       # Short-term Scratchpad
│
├── adapters/         # Agent Integration
│   ├── manifest.yaml # Detection rules
│   └── [agent].md    # Per-agent guides
│
├── workflows/        # Operating Procedures
├── knowledge/        # Learning Bank
└── archive/          # History
```

## 🔌 Agent Detection

Before starting work, identify yourself:

1. Check `adapters/manifest.yaml` for known agent types
2. If your config directory exists, read your adapter file:
   - Cursor: `adapters/cursor.md`
   - Windsurf: `adapters/windsurf.md`
   - Claude: `adapters/claude.md`
   - Antigravity: `adapters/antigravity.md`
   - Copilot: `adapters/copilot.md`
   - JetBrains: `adapters/jetbrains.md`
   - Aider: `adapters/aider.md`
   - Generic: `adapters/generic.md`
3. Follow the integration rules in your adapter file
4. Regardless of agent type, `.ai/` is the source of truth

---

## 🤖 Protocol

1. **Read First**: Always read the relevant `MASTER.md` before acting.
2. **Write Last**: Update `changelog.md` and `MASTER.md` before finishing.
3. **Respect Locks**: Check `active/` for conflicting work.
