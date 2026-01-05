# Unified Context Protocol (UCP)

**The Standard Kernel for Agent-Native Development.**

## 🎯 The Problem

Agents without architecture are just chatbots. They "forget" technical decisions, ignore conventions, and drift off-course. Prompting them repeatedly is fragile and unscalable.

## 💡 The Solution

UCP is a **Behavioral Architecture** that installs directly into your project. It acts as an operating system for your AI agents, providing:
- **Memory**: A structured file system for project state.
- **governance**: Strict protocols for decision making.
- **Coordination**: A shared language for multi-agent collaboration.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **🧠 Smart Kernel v3.1** | High-speed boot with auto-fix for stale context |
| **🔌 Universal Adapter** | Run the same behavior on Cursor, Windsurf, or Claude |
| **🤝 Session Persistence** | "Save Game" for your codebase—never explain context twice |
| **📂 Monorepo Ready** | Scoped contexts for complex projects |
| **⚡ Context Budgeting** | Tiered loading prevents LLM overload |

## 🚀 Quick Start

### 1. Install
**Via CLI:**
```bash
npx corepackai install @corepackai/ucp
```

### 2. Boot
Tell your agent:
> "Read .ai/boot.md and follow the instructions."

## 📂 Architecture

```text
unified_context_protocol/
├── boot.md           # The Kernel Entry Point
├── context/          # Mutable Project State (MASTER.md)
├── knowledge/        # Immutable Learnings
└── bin/              # Workflows & Protocols
```

## 🏆 Why UCP?

- **Agent-Native**: Designed for LLMs, not just humans.
- **Vendor Agnostic**: Works with any AI model or IDE.
- **Zero Lock-in**: It's just Markdown files in your repo.
- **Version Controlled**: Your agent's brain lives in git.

## 📖 Documentation

| Resource | Description |
|----------|-------------|
| [User Guide](USER_GUIDE.md) | Detailed usage instructions |
| [boot.md](boot.md) | Kernel Protocol |
