# User Guide: Unified Context Protocol

> **For Humans**: How to orchestrate AI development using the Unified Context Protocol.

## What is this?

The `unified_context_protocol` (implemented via the `.ai/` directory) is a **standardized governance layer** between your codebase and AI agents. It does more than just provide context; it allows you to **orchestrate** complex, multi-project workflows by giving agents a structured way to read state, write memory, and follow procedures.

## 🚀 Setup

### 1. Installation
Copy the `.ai/` folder from this directory into your project root.

```bash
cp -r workflows/unified_context_protocol/.ai /path/to/your/project/
```

### 2. Initialization
Ask your AI agent:
> "Read `.ai/workflows/audit.md` and run an initial audit of this project to populate the unified context."

### 3. Verification
Check that `context/MASTER.md` and `context/tech.md` have been correctly populated.

## 📂 Orchestrating Multi-Project Repos

For monorepos (e.g., `./frontend`, `./backend`, `./mobile`):

1.  **Define Boundaries**: Edit `.ai/context/map.md` to list your sub-projects and their paths.
2.  **Create Scoped Contexts**:
    > "Create a new project context for `./frontend` in `.ai/context/projects/frontend/` following the protocol."
3.  **Project Vision**: Override global patterns by creating `context/projects/<name>/product/vision.md`.
4.  **Active Locking**: Use `context/active/` to signal which sub-project is currently being modified to avoid cross-project pollution.

## 🤝 Working with AI

When starting a session, paste this prompt to ground the agent:

> "Check `.ai/README.md` to understand the Unified Protocol, then read `.ai/context/MASTER.md` for the current system state."

## 🧹 Maintenance

Every few weeks:
1.  **Run Maintenance**: Ask AI to "Run the maintenance workflow".
2.  **Prune Knowledge**: It will summarize old changelogs and consolidate the knowledge base.

## ⚠️ For AI Agents with Internal Memory

Some AI tools (like Cursor Composer, Windsurf Cascade, Gemini Antigravity, or other agentic IDEs) have their own internal "brain" or "artifact" directories for task tracking.

> [!CAUTION]
> **DO NOT use your internal memory systems for this project.**

Use `.ai/` exclusively for:

| Purpose | Location |
|---------|----------|
| Task tracking | `.ai/context/active/` |
| Session memory | `.ai/context/MASTER.md` |
| Knowledge storage | `.ai/knowledge/` |
| Changelogs | `.ai/context/changelog.md` |

The `.ai/` directory is the **single source of truth**. Creating parallel tracking systems causes context fragmentation and defeats the purpose of this protocol.

---

## 🔌 Multi-Agent Support

The `.ai/` system works with any AI coding assistant. The `adapters/` directory contains:

- **manifest.yaml**: Machine-readable agent detection rules
- **[agent].md**: Human-readable integration guides for each agent

### Supported Agents

| Agent | Adapter File |
|-------|--------------|
| Cursor | `.ai/adapters/cursor.md` |
| Windsurf | `.ai/adapters/windsurf.md` |
| Claude Code | `.ai/adapters/claude.md` |
| Antigravity | `.ai/adapters/antigravity.md` |
| GitHub Copilot | `.ai/adapters/copilot.md` |
| JetBrains AI | `.ai/adapters/jetbrains.md` |
| Aider | `.ai/adapters/aider.md` |
| Generic LLM | `.ai/adapters/generic.md` |

### If You Use Multiple Tools

If you use Cursor, Claude, and Antigravity on the same project:

1. Each tool should read `.ai/context/MASTER.md` at session start
2. Each tool should update `.ai/context/changelog.md` at session end
3. Agent-specific configs (like `.cursor/rules/`) can reference `.ai/` content
4. All project state stays in `.ai/` — never fragmented across tools

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

---

## 🔄 Upgrade & Migration (v1.1.0)

| Workflow | Purpose |
|----------|---------|
| `workflows/upgrade.md` | Upgrade existing .ai/ to new version |
| `workflows/export.md` | Export all knowledge for migration |

Check `.ai/VERSION` for current version. See `.ai/CHANGELOG.md` for release notes.

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
