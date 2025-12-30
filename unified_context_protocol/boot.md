# AI Context System

> **A drop-in documentation system for AI-assisted development.**
> Agents: Start here.

## 🛠️ Tooling (Optional)
This protocol is designed to be **Agent-Agnostic**. You can manage these files manually, or use the **corepackai CLI** for automation.

### Using with corepackai CLI (Recommended)
If you are using the CLI (`corepackai`), it provides a suite of tools for auth, package management, and agent bridging.

#### Auth Commands
- `corepackai login`: Authenticate with CorePack AI via GitHub
- `corepackai whoami`: Show current logged in user
- `corepackai logout`: Log out and remove saved credentials

#### Core Commands
- `corepackai init`: Initialize a new .ai/ context in the current directory
- `corepackai install <package_name>`: Install a context package (e.g. npx corepackai install @username/pack)
- `corepackai update <package_name>`: Update/Re-install a context package
- `corepackai list`: List installed context packages
- `corepackai publish`: Publish a context package to the registry
- `corepackai doctor`: Check environment for issues
- `corepackai hook [agent]`: Manually bridge installed packs to a specific Agent/IDE
- `corepackai mcp`: Start Model Context Protocol server (stdio)

#### Agent Bridge Commands (Advanced)
- `corepackai write <file> [content]`: Write file and auto-log to changelog
- `corepackai read <file>`: Read file with context injection
- `corepackai patch <file> <search> <replace>`: Search and Replace content
- `corepackai run <command>`: Run shell command with auto-documentation

#### Deprecated
- `corepackai pull <slug>`: Use `install` instead

## 🧭 Navigation

**Where should you start?**

| If you are working on... | Read this first |
|--------------------------|-----------------|
| **The Core / Root Config / Specs** | `context/MASTER.md` |
| **A Specific Sub-Project** | `context/map.md` (finds your project context) |
| **First Time Setup** | `bin/workflows/onboarding.md` (The "Key") |
| **A New Feature / Bugfix** | `bin/workflows/README.md` (guides you) |
| **Committing Changes** | `bin/workflows/commit.md` (atomic commits) |
| **Saving Progress** | `bin/workflows/sync.md` (dump memory to disk) |
| **Picking up a shared task** | `context/active/README.md` (check for collisions) |

## 🚨 Agent Boot Protocol

**Every session MUST begin with these steps:**

1. `cat context/MASTER.md` — Load current project state
2. `ls context/active/` — Check for in-progress work
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
. (Pack Root)
├── bin/                  # THE CONTEXT ENGINE (Managed by CLI)
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
4. Regardless of agent type, the pack root is the source of truth

---

## 🤖 Protocol

1. **Read First**: Always read the relevant `MASTER.md` before acting.
2. **Write Last**: Update `changelog.md` and `MASTER.md` before finishing.
3. **Respect Locks**: Check `active/` for conflicting work.
