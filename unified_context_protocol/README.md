# Unified Context Protocol (UCP)

**A drop-in context system that makes AI coding assistants *actually remember* your project.**

## 🎯 The Problem

AI coding assistants forget everything between sessions. You waste time re-explaining your project architecture, coding standards, and past decisions—and agents often create conflicting or inconsistent work.

## 💡 The Solution

UCP is a **standardized governance layer** that sits between your codebase and AI agents. It provides a file-system-based protocol for persistent context, enabling agents to:
- **Read** project state and history
- **Write** learnings and decisions
- **Coordinate** across sessions and tools

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **🚀 Boot Protocol** | Agents run a startup checklist to load context automatically |
| **🔌 Multi-Agent Support** | Works with 8+ AI assistants (Cursor, Claude, Copilot, Windsurf, Aider, and more) |
| **🤝 Session Handoffs** | Incomplete work is saved—next session picks it up, even with a different agent |
| **📂 Monorepo Ready** | Define sub-projects with scoped contexts |
| **🧠 Knowledge Persistence** | Patterns, gotchas, and decisions survive across sessions |
| **📋 Pre-Built Workflows** | High-performance pseudo-code for audits, features, bugfixes, refactoring, and maintenance |
| **⚡ Context Budget System** | Tiered loading prevents LLM context overload |
| **🎓 Agent Learning** | Tracks user preferences, what worked/failed, and external dependencies |

## 🔧 Supported AI Assistants

See [Universal Adapter](bin/adapters/universal.md).

Cursor • Windsurf • Claude Code • GitHub Copilot • JetBrains AI • Aider • Gemini Antigravity • Generic LLMs

## 📂 What's Included

```text
unified_context_protocol/
├── boot.md           # Agent entry point
├── context/          # Project state (MASTER.md, tech.md, changelog.md...)
├── knowledge/        # Persistent learnings & decisions
├── bin/
│   ├── workflows/    # audit, development, maintenance...
│   └── adapters/     # Per-agent integration guides
└── archive/          # Historical context storage
```

## 🚀 Quick Start

### 1. Install
**Via CLI (Recommended):**
```bash
npx corepackai install ucp
```

**Or Manual:**
Copy the pack into your project's context directory (e.g., `.context/` or `.ai/`).

### 2. Initialize
Tell your agent:
> "Read bin/workflows/onboarding.md"

### 3. Audit
Tell your agent:
> "Read bin/workflows/audit.md and audit this project"

**Done!** Your agents now have persistent, coordinated context.

## 🏆 Why UCP?

- **Escape vendor lock-in**: Your context lives in version-controlled files, not proprietary cloud systems
- **Tool-agnostic**: Switch between AI assistants without losing context
- **Human-readable**: All files are markdown—you can edit them directly
- **Version-controlled**: Commit your context alongside your code

## 📖 Documentation

| Resource | Description |
|----------|-------------|
| [User Guide](USER_GUIDE.md) | Detailed setup and usage for humans |
| [boot.md](boot.md) | Agent entry point (boot protocol, structure) |
| [CLI Guide](context/CLI_GUIDE.md) | Automation tool instructions |
