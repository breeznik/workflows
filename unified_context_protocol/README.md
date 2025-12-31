# Unified Context Protocol (UCP)

> A drop-in context system that makes AI agents **actually remember** your project.

## The Problem

AI coding assistants forget everything between sessions. You waste time re-explaining your project, and agents create conflicting work.

## The Solution

Install this pack into your project's context directory (e.g. `.context` or `.doc`). Agents automatically discover it, load project state, and coordinate with each other.

## 🛠️ Tooling (Optional)
This protocol is designed to be **Agent-Agnostic**. You can manage these files manually, or use the **corepackai CLI** for automation.

### Using with corepackai CLI (Recommended)
If you are using the CLI (`corepackai`), it provides "Bridge Tools" that allow your Agent to self-maintain this context.

- **Initialization**: `npx corepackai init`
- **Maintenance**: `corepackai write`, `corepackai read`

See `context/CLI_GUIDE.md` for tool instructions if you are using the CLI. If you are using this raw, you can ignore that file.

---

## ✨ Features

### 🚀 Boot Protocol
Agents automatically run a startup checklist:
1. Read `boot.md` → Load context files
2. **Present 14-item Agent Menu** — guides users through all workflows
3. **UCP Loop** — agents return to menu after each task until Exit

### 🔌 Multi-Agent Support
Works with **8 AI coding assistants** out of the box:

| Agent | Adapter |
|-------|---------|
| Cursor | `bin/adapters/cursor.md` |
| Windsurf | `bin/adapters/windsurf.md` |
| Claude Code | `bin/adapters/claude.md` |
| Antigravity | `bin/adapters/antigravity.md` |
| GitHub Copilot | `bin/adapters/copilot.md` |
| JetBrains AI | `bin/adapters/jetbrains.md` |
| Aider | `bin/adapters/aider.md` |
| Generic LLM | `bin/adapters/generic.md` |

### 🤝 Session Handoffs
When work is incomplete, agents save state to `context/active/`. Next session picks it up — even if it's a different agent.

### 📂 Monorepo Ready
Define sub-projects in `context/map.md`. Each gets its own scoped context while sharing the global knowledge base.

### 🧠 Knowledge Persistence
Patterns, gotchas, and decisions go in `knowledge/`. Agents can learn and remember across sessions.

### 📋 Standardized Workflows
Pre-built high-perf Pseudo-Code in `bin/workflows/`:
- `audit.md` — Initial project discovery
- `feature.md` — Adding new features
- `bugfix.md` — Fixing issues
- `refactor.md` — Code improvements
- `boot.md` — Session startup with context budget
- `onboarding.md` — One-time agent setup (The "Key")
- `maintenance.md` — Prune and archive context
- `integrate-agent.md` — Set up your agent config
- `upgrade.md` — SmartSync non-destructive upgrade
- `export.md` — Export all knowledge for migration
- `sync.md` — Hybrid Sync (Dump memory to disk)

### ⚡ Context Budget System
Prevents LLM overload with tiered loading:

| Priority | Files | Load When |
|----------|-------|-----------|
| **P0** | MASTER.md, adapter | Always |
| **P1** | tech, patterns, user-prefs | Based on task |
| **P2** | decisions, boundaries | On demand |

### 🎓 Agent Learning
- `user-prefs.md` — Remembers style & Anti-Patterns
- `learnings.md` — What worked/failed in this project
- `bin/workflows/learning.md` — Active context refinement loop
- `boundaries.md` — What agent knows vs. needs to ask
- `dependencies.md` — External APIs reference

### 🔄 Upgrade & Migration
- **VERSION** file tracks installed UCP version
- **upgrade.md** workflow for non-destructive upgrades
- **export.md** compiles all knowledge to portable document

---

## 🚀 Quick Start

```bash
# 1. Install UCP Pack
# Manually:
cp -r * /path/to/your/project/context/

# OR via CLI:
npx corepackai install ucp --target ./context
```

# 2. Run the onboarding workflow (One-time setup)
# Tell your agent: "Read bin/workflows/onboarding.md" and follow the instructions.

# 3. Run the audit workflow
# Tell your agent: "Read bin/workflows/audit.md and audit this project"

# 4. Done! Agent now has persistent context

---

## 📖 Documentation

| Resource | Description |
|----------|-------------|
| [User Guide](USER_GUIDE.md) | Detailed setup and usage for humans |
| [boot.md](boot.md) | Agent entry point (boot protocol, structure) |
| [bin/workflows/integrate-agent.md](bin/workflows/integrate-agent.md) | Set up your agent to auto-discover UCP |
