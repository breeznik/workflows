# AI Context System

> **Agents: Start here. This is MANDATORY.**

> [!CAUTION]
> **BOOT CHECKLIST** — Complete ALL steps before any work:
> 1. ☐ Read `context/PRIORITY.md` (budget rules)
> 2. ☐ Read `context/MASTER.md` (project state)
> 3. ☐ Read `bin/adapters/[your-agent].md` (integration rules)
> 4. ☐ Check `context/active/` (pending work)
> 5. ☐ If resuming: Read the active task file
> 6. ☐ **Present the Agent Menu below**

---

## 🎯 Agent Greeting

After loading context, greet the user with status + menu:

```
🤖 UCP Boot Complete!

📊 CONTEXT LOADED:
  • Project: [from MASTER.md → Current State]
  • Active Tasks: [count from context/active/] pending
  • Tech Stack: [from tech.md → Framework if populated]
  • Knowledge: [count] patterns, [count] learnings

⚠️ ATTENTION NEEDED:
  • [List pending handoffs from active/]

---

📋 DEVELOPMENT
  1. ✨ Feature    — Add new functionality
  2. 🐛 Bugfix     — Fix a reported issue
  3. ♻️ Refactor   — Improve existing code
  4. 🔍 Audit      — Scan & populate project context

📊 CONTEXT MANAGEMENT
  5. 💾 Sync       — Save progress to disk
  6. 🔄 Handoff    — End session with context transfer
  7. 🧹 Maintenance — Prune old context
  8. 📤 Export     — Export knowledge for migration

📝 PRODUCT & PLANNING
  9. 📋 Product-Spec — Define features from business view
  10. 🗺️ Map        — Navigate monorepo sub-projects

🔧 SETUP
  11. 🔑 Onboarding — Set up Universal Pointer
  12. 🔌 Integrate  — Configure agent settings
  13. ⬆️ Upgrade    — Update to latest UCP version

  0. 🚪 Exit       — End session (runs sync + handoff)

What would you like to work on?
```

---

## 🔁 UCP Loop Protocol

> [!CAUTION]
> **PERSISTENT TODO** — Add to your internal task list:
> `⚡ UCP LOOP — Return to boot.md menu after completing current task`
> Keep pinned until user selects "0. Exit"

**Loop behavior:**
1. Show menu → Get selection → Run workflow
2. After task: Run `sync.md` checkpoint
3. Return to menu (do NOT exit automatically)
4. On "0. Exit": Run sync + handoff, then end session

---

## 🔌 Agent Detection

Check `bin/adapters/manifest.yaml` for your adapter:
- Cursor → `bin/adapters/cursor.md`
- Windsurf → `bin/adapters/windsurf.md`
- Claude → `bin/adapters/claude.md`
- Antigravity → `bin/adapters/antigravity.md`
- Copilot → `bin/adapters/copilot.md`

---

## 🤖 Protocol Rules

1. **Read First**: Load `MASTER.md` before acting
2. **Write Last**: Update `changelog.md` before finishing
3. **Respect Locks**: Check `context/active/` for conflicts
4. **Sync Often**: Run `bin/workflows/sync.md` at checkpoints
