# AI Context System

> **Agents: Start here. This is MANDATORY.**

> [!CAUTION]
> **BOOT CHECKLIST** — Complete ALL steps before any work:
> 0. ☐ Check `bin/VERSION` → if `breaking` field is not empty, **ALERT USER FIRST**
> 1. ☐ Read `context/PRIORITY.md` (budget rules)
> 2. ☐ Read `context/MASTER.md` (project state)
> 3. ☐ Read `bin/adapters/[your-agent].md` (integration rules)
> 4. ☐ Check `context/active/` (pending work)
> 5. ☐ If resuming: Read the active task file
> 6. ☐ **Present the Agent Menu below**

---

## 🎯 Agent Greeting

After loading context, greet the user with status + menu:

```text
╔═══════════════════════════════════════════════════════════════╗
║  🤖 UCP Boot Complete!                                        ║
╚═══════════════════════════════════════════════════════════════╝

📊 CONTEXT LOADED:
   • Project: [from MASTER.md → Current State]
   • Active Tasks: [count from context/active/] pending
   • Tech Stack: [from tech.md → Framework if populated]
   • Knowledge: [count] patterns, [count] learnings

⚠️ ATTENTION NEEDED:
   • [List pending handoffs from active/]

💡 SUGGESTED NEXT:
   → [#] [Action Name] — [Reason based on context analysis]

═══════════════════════════════════════════════════════════════

📋 DEVELOPMENT
   1. ✨ Feature      — Add new functionality (runs development.md)
   2. 🐛 Bugfix       — Fix a reported issue (runs development.md)
   3. ♻️ Refactor     — Improve existing code (runs development.md)
   4. 🔍 Audit        — Scan & populate project context

📊 CONTEXT MANAGEMENT
   5. 💾 Sync         — Save progress to disk
   6. 🔄 Handoff      — End session with context transfer
   7. 🧹 Maintenance  — Prune old context
   8. 📤 Export       — Export knowledge for migration

📝 PRODUCT & PLANNING
   9. 📋 Product-Spec — Define features from business view
  10. 🗺️ Map          — Navigate monorepo sub-projects

🔧 SETUP
  11. 🔑 Onboarding   — Set up Universal Pointer
  12. 🔌 Integrate    — Configure agent settings
  13. ⬆️ Upgrade      — Update to latest UCP version

   0. 🚪 Exit         — End session (runs sync + handoff)

═══════════════════════════════════════════════════════════════
What would you like to work on? [Enter number or command]
```

---

## 💡 Suggestion Logic

Agents MUST analyze context and provide ONE smart suggestion. Use this priority:

| Priority | Condition | Suggested Action |
|----------|-----------|------------------|
| 1 | `context/active/PLAN.md` has incomplete tasks | **Continue**: `1. Feature` or `2. Bugfix` |
| 2 | `context/active/` has handoff files | **Resume**: Link to handoff task |
| 3 | `MASTER.md` is empty or minimal | **Setup**: `4. Audit` — project needs scanning |
| 4 | `context/changelog.md` has many unsaved changes | **Save**: `5. Sync` — checkpoint progress |
| 5 | Long session detected (>10 tool calls) | **Checkpoint**: `5. Sync` — save work |
| 6 | `bin/VERSION` shows new version available | **Upgrade**: `13. Upgrade` |
| 7 | No roadmap in `context/product/roadmap.md` | **Plan**: `9. Product-Spec` |
| 8 | Default fallback | **Ask**: "What would you like to build today?" |

**Example suggestions:**
```text
💡 SUGGESTED NEXT:
   → 4. Audit — MASTER.md is empty, let's scan your project first

💡 SUGGESTED NEXT:
   → 1. Feature — Continue: "Add user authentication" (from active/PLAN.md)

💡 SUGGESTED NEXT:
   → 5. Sync — 15 changes pending, checkpoint your progress
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

Check `bin/adapters/manifest.yaml` or just read:
- **`bin/adapters/universal.md`** (All Agents)

---

## 🤖 Protocol Rules

1. **Read First**: Load `MASTER.md` before acting
2. **Write Last**: Update `changelog.md` before finishing
3. **Respect Locks**: Check `context/active/` for conflicts
4. **Sync Often**: Run `bin/workflows/sync.md` at checkpoints
6. **🛡️ Stale Check**:
   > Verify `Last Audit` date in `context/tech.md`.
   > **IF** > 48 hours old: WARN "⚠️ Context Stale — Run Audit"
