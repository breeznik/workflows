---
description: Set up your agent to auto-discover .ai/ context system
---

# Integrate Agent Config with .ai

The only thing your global agent config needs to do is: **point the agent to `.ai/`**.

Once there, `.ai/README.md` handles everything — boot protocol, adapter detection, workflows.

---

## One-Time Setup (per agent)

Create a minimal rule in your agent's global config.

> **Note for agents**: If you cannot write to your config directory, ask the user to create the file and provide them the content below.

### Antigravity

**Path**: `~/.agent/workflows/ucp.md`

```markdown
---
description: Project Context Integration
---

# .ai Context System

If this project has a `.ai/` directory:
1. Read `.ai/README.md` first
2. Follow the boot protocol there
3. Use `.ai/` as source of truth (not your internal brain)
```

---

### Cursor

**Path**: `.cursor/rules/ai-context.mdc` (in project or global)

```mdc
---
description: .ai context integration
alwaysApply: true
---

If `.ai/` exists, read `.ai/README.md` and follow its boot protocol.
```

---

### Windsurf

**Path**: `.windsurf/rules/ai-context.md`

```markdown
If `.ai/` directory exists, read `.ai/README.md` and follow its instructions.
```

---

### Claude Code

**Add to `CLAUDE.md`**:

```markdown
If `.ai/` exists, start by reading `.ai/README.md` and follow its boot protocol.
```

---

### JetBrains AI

**Path**: `.aiassistant/rules/ai-context.md`

```markdown
If `.ai/` exists, read `.ai/README.md` and follow its boot protocol.
```

---

### GitHub Copilot

**Path**: `.github/copilot-instructions.md`

```markdown
If `.ai/` exists, read `.ai/README.md` and follow its boot protocol.
```

---

### Aider

**Add to `.aider.conf.yml`**:

```yaml
read:
  - .ai/README.md
  - .ai/context/MASTER.md
```

---

### Generic / API-based LLMs

**Add to your system prompt**:

```
If this project has a `.ai/` directory, read `.ai/README.md` first and follow its instructions.
```

---

## That's It

The `.ai/README.md` already contains:
- 🚨 Boot Protocol (what to read at session start/end)
- 🔌 Agent Detection (how to find your adapter)
- 🏗️ Structure (where everything lives)
- 🤖 Protocol (read first, write last, respect locks)

**User workflow:**
1. Drop `.ai/` in project
2. (Once) Set up global agent rule above
3. Agent auto-discovers and follows `.ai/README.md`


