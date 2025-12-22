# AI Context System

> **A drop-in documentation system for AI-assisted development.**
> Agents: Start here.

## 🧭 Navigation

**Where should you start?**

| If you are working on... | Read this first |
|--------------------------|-----------------|
| **The Core / Root Config / Specs** | `context/MASTER.md` |
| **A Specific Sub-Project** | `context/map.md` (finds your project context) |
| **A New Feature / Bugfix** | `workflows/README.md` (guides you) |
| **Picking up a shared task** | `context/active/README.md` (check for collisions) |

## 🏗️ Structure

```
.ai/
├── context/          # State & Memory
│   ├── MASTER.md     # Global Root
│   ├── projects/     # Sub-Project Roots
│   └── active/       # Short-term Scratchpad
│
├── workflows/        # Operating Procedures
├── knowledge/        # Learning Bank
└── archive/          # History
```

## 🤖 Protocol

1. **Read First**: Always read the relevant `MASTER.md` before acting.
2. **Write Last**: Update `changelog.md` and `MASTER.md` before finishing.
3. **Respect Locks**: Check `active/` for conflicting work.
