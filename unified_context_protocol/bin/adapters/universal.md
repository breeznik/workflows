# Universal Agent Adapter

> **Purpose**: Integration guide for ALL AI agents (Cursor, Windsurf, Claude, Copilot, etc.)
> **Goal**: Connect your agent's specific context system to the UCP standards.

## 1. Core Logic (Universal)

Regardless of which agent you are, follow these **Protocol Rules**:

1.  **Boot**: At the start of EVERY session, read `.ai/boot.md` (The Power Button).
2.  **Context**: Store project state in `[CONTEXT_ROOT]/context/`, NOT in your private memory.
3.  **End**: Before exiting, read `[CONTEXT_ROOT]/bin/workflows/sync.md` to save state.
4.  **Drift**: If code contradicts context, AUTO-UPDATE the context.

---

## 2. Agent-Specific Setup

Find your agent below to see how to "install" the bridge.

### 🖱️ Cursor
**File**: `.cursor/rules/ucp.mdc`
```markdown
---
description: UCP Bridge
globs: *
alwaysApply: true
---
# UCP Protocol
1. BOOT: Read `.ai/boot.md` immediately.
2. CONTEXT: Use `.ai/context/MASTER.md` as source of truth.
```

### 🏄 Windsurf / Cascade
**File**: `.windsurf/rules`
```markdown
# UCP Protocol
- ON SESSION START: Read `.ai/boot.md`
- ON SESSION END: Run `.ai/bin/workflows/sync.md`
```

### 🤖 Claude Code / Anthropic
**File**: `CLAUDE.md` or `.claude/config`
```markdown
# UCP Governance
You must follow the Unified Context Protocol.
- Start every task by reading `.ai/boot.md`
- Check `.ai/context/active/` for locks before working.
```

### ✈️ GitHub Copilot
**File**: `.github/copilot-instructions.md`
```markdown
# UCP Instructions
1. Always check `.ai/context/MASTER.md` for project status.
2. When creating new files, update `.ai/context/map.md`.
```

### 🧠 JetBrains AI
**File**: `.aiassistant/rules`
```markdown
Follow `.ai/boot.md` protocol.
```

### 🟣 Antigravity (Google)
**File**: `.agent/workflows/ucp.md`
```markdown
# UCP Pointer
Read `.ai/boot.md` to initialize project context.
```

### 🗣️ Aider / CLI Agents
**File**: `.aider.conf.yml` or System Prompt
```yaml
read: .ai/boot.md
```
