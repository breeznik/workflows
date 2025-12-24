---
description: Set up your agent to auto-discover .ai/ context system
---

# Integrate Agent Config with .ai

> **Goal**: Establish a permanent "Pointer Rule" in your global agent config so it automatically enters `.ai/` protocols for any project.

## 1. Smart Discovery Rule (Universal)

Instead of per-project rules, add this to your **Global Agent Instructions**:

```pseudo
IF exists(".ai/README.md"):
  1. READ ".ai/README.md" FIRST (Priority 0)
  2. RUN ".ai/bin/workflows/boot.md"
  3. USE ".ai/" as the only source of truth for project rules.
  4. IGNORE internal agent memory if it contradicts project context.
```

## 2. Agent-Specific Implementations

| Agent | Config Path | Instructions (Add/Replace) |
|-------|-------------|----------------------------|
| **Antigravity** | `~/.agent/workflows/ucp.md` | `Read .ai/README.md and run boot.md` |
| **Cursor** | `.cursorrules` (Global) | `If .ai exists, follow .ai/README.md` |
| **Windsurf** | `.windsurf/rules/ai.md` | `Follow .ai/README.md boot protocol` |
| **Claude Code**| `CLAUDE.md` | `Refer to .ai/ for all project rules` |

## 3. Benefits of Pointer Logic
- **Zero Config**: Drop `.ai/` into any new project; it works instantly.
- **Agent Agnostic**: The agent discovers its own adapter in `.ai/adapters/`.
- **Version Resilience**: The agent follows the local `boot.md`, ensuring it uses the correct v1.1, v1.2, or future protocols.
