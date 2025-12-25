---
description: Set up your agent to auto-discover .ai/ context system
---

# Integrate Agent Config with .ai

> **Goal**: Establish a permanent "Pointer Rule" in your global agent config so it automatically enters `.ai/` protocols for any project.

## 1. Smart Discovery Rule (Universal)

Instead of per-project rules, add this to your **Global Agent Instructions**.
Replace `[CONTEXT_ROOT]` with your chosen folder name (e.g. `.context`).

```pseudo
IF exists("[CONTEXT_ROOT]/boot.md"):
  1. READ "[CONTEXT_ROOT]/boot.md" FIRST (Priority 0)
  2. RUN "bin/workflows/boot.md" from the pack.
  3. USE "[CONTEXT_ROOT]/" as the only source of truth for project rules.
  4. IGNORE internal agent memory if it contradicts project context.
```

## 2. Agent-Specific Implementations

| Agent | Config Path | Instructions (Add/Replace) |
|-------|-------------|----------------------------|
| **Antigravity** | `~/.agent/workflows/ucp.md` | `Read [CONTEXT_ROOT]/boot.md and run boot.md` |
| **Cursor** | `.cursorrules` (Global) | `If [CONTEXT_ROOT] exists, follow boot.md` |
| **Windsurf** | `.windsurf/rules/ai.md` | `Follow [CONTEXT_ROOT]/boot.md boot protocol` |
| **Claude Code**| `CLAUDE.md` | `Refer to [CONTEXT_ROOT]/ for all project rules` |

## 3. Benefits of Pointer Logic
- **Zero Config**: Drop `context/` into any new project; it works instantly.
- **Agent Agnostic**: The agent discovers its own adapter in `bin/adapters/`.
- **Version Resilience**: The agent follows the local `boot.md`.
