# User Guide: Unified Context Protocol

> **For Humans**: How to orchestrate AI development using the Unified Context Protocol.

## What is this?

The `unified_context_protocol` is a **standardized governance layer** between your codebase and AI agents. It does more than just provide context; it allows you to **orchestrate** complex, multi-project workflows by giving agents a structured way to read state, write memory, and follow procedures.

## 🚀 Setup

### 1. Installation
Copy the `unified_context_protocol` context folder from this directory into your project root.

```bash
cp -r unified_context_protocol/* /path/to/your/project/context/
```

### 2. Onboarding (One-Time per Agent)
Ask your AI agent:
> "Read `bin/workflows/onboarding.md` and follow the instructions."
This ensures your agent has the "Universal Pointer" to always find UCP context.

### 3. Initialization (Per Project)
Ask your AI agent:
> "Read `bin/workflows/audit.md` and run an initial audit of this project to populate the unified context."

### 4. Verification
Check that `context/MASTER.md` and `context/tech.md` have been correctly populated.

## 📂 Orchestrating Multi-Project Repos

For monorepos (e.g., `./frontend`, `./backend`, `./mobile`):

1.  **Define Boundaries**: Edit `context/map.md` to list your sub-projects and their paths.
2.  **Create Scoped Contexts**:
    > "Create a new project context for `./frontend` in `context/projects/frontend/` following the protocol."
3.  **Project Vision**: Override global patterns by creating `context/projects/<name>/product/vision.md`.
4.  **Active Locking**: Use `context/active/` to signal which sub-project is currently being modified to avoid cross-project pollution.

## 🤝 Working with AI

When starting a session, paste this prompt to ground the agent:

> "Check `boot.md` to understand the Unified Protocol, then read `context/MASTER.md` for the current system state."

## 🧹 Maintenance

Every few weeks:
1.  **Run Maintenance**: Ask AI to "Run the maintenance workflow".
2.  **Prune Knowledge**: It will summarize old changelogs and consolidate the knowledge base.

## ⚠️ For AI Agents with Internal Memory

Some AI tools (like Cursor Composer, Windsurf Cascade, Gemini Antigravity, or other agentic IDEs) have their own internal "brain" or "artifact" directories for task tracking.

> [!CAUTION]
> **DO NOT use your internal memory systems for this project.**

Use the protocol's context directory exclusively for:

| Purpose | Location |
|---------|----------|
| Task tracking | `context/active/` |
| Session memory | `context/MASTER.md` |
| Knowledge storage | `knowledge/` |
| Changelogs | `context/changelog.md` |

The context directory is the **single source of truth**. Creating parallel tracking systems causes context fragmentation and defeats the purpose of this protocol.

---

## 🔌 Multi-Agent Support

The protocol works with any AI coding assistant. The `adapters/` directory contains:

- **manifest.yaml**: Machine-readable agent detection rules
- **[agent].md**: Human-readable integration guides for each agent

### Supported Agents
Check `bin/adapters/` for your specific tool's integration guide.

| Agent | Adapter File |
|-------|--------------|
| Cursor | `bin/adapters/cursor.md` |
| Windsurf | `bin/adapters/windsurf.md` |
| Claude Code | `bin/adapters/claude.md` |
| Antigravity | `bin/adapters/antigravity.md` |
| GitHub Copilot | `bin/adapters/copilot.md` |
| JetBrains AI | `bin/adapters/jetbrains.md` |
| Aider | `bin/adapters/aider.md` |
| Generic LLM | `bin/adapters/generic.md` |

### If You Use Multiple Tools

If you use Cursor, Claude, and Antigravity on the same project:

1. Each tool should read `context/MASTER.md` at session start
2. Each tool should update `context/changelog.md` at session end
3. Agent-specific configs (like `.cursor/rules/`) can reference protocol context content
4. All project state stays in the protocol context — never fragmented across tools

---

## ⚡ Context Budget (v1.1.0)

Agents use tiered loading to prevent context overload:

| Priority | Files | When |
|----------|-------|------|
| **P0** | MASTER.md, PRIORITY.md, adapter | Always |
| **P1** | tech, patterns, user-prefs | Based on task |
| **P2** | decisions, boundaries | On demand |
| **P3** | archive | Never auto-load |

See `context/PRIORITY.md` for full rules.

---

## 🎓 Knowledge Management (v1.1.0)

| File | Purpose |
|------|---------|
| `knowledge/learnings.md` | What worked/failed in this project |
| `knowledge/boundaries.md` | What agent knows vs. needs to ask |
| `context/user-prefs.md` | Your coding style preferences |
| `context/dependencies.md` | External APIs reference |

> **Active Learning Loop**: Agents should run `workflows/learning.md` at the end of sessions to automatically update `user-prefs.md` and `learnings.md` based on your feedback.

---

## 🔄 Upgrade & Migration (v1.1.0)

| Workflow | Purpose |
|----------|---------|
| `workflows/commit.md` | **Smart Commit**: Standardizes atomic git commits (Code + Context) |
| `workflows/upgrade.md` | Upgrade existing context to new version |
| `workflows/export.md` | Export all knowledge for migration |

Check `bin/VERSION` for current version. See `CHANGELOG.md` for release notes.

---

## ❓ FAQ

**Q: Should I commit this folder?**
A: **YES.** This is the "operating system" for your agents. It must be versioned.

**Q: Can I edit files manually?**
A: Yes. You are the **Architect**; the AI is the **Builder**. You set the plans in `MASTER.md`, and the AI executes them.

**Q: How do I upgrade to a new UCP version?**
A: Run `workflows/upgrade.md`. It adds new files without overwriting your data.

**Q: How do I export knowledge for migration?**
A: Run `workflows/export.md`. It compiles everything into `KNOWLEDGE_EXPORT.md`.
