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

## ❓ FAQ

**Q: Should I commit this folder?**
A: **YES.** This is the "operating system" for your agents. It must be versioned.

**Q: Can I edit files manually?**
A: Yes. You are the **Architect**; the AI is the **Builder**. You set the plans in `MASTER.md`, and the AI executes them.
