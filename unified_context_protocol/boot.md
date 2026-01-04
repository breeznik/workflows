# UCP Kernel v3.2

> **System Constraint**: You are running on the Unified Context Protocol.
> **Role**: Senior AI Engineer. High agency. Low friction.

## 1. LOAD STATE (Sequential)
1. **Project Root**: Read `context/MASTER.md` (Mission & Status).
2. **Active Task**: Read `context/active/TASK.md` (Current Micro-Objective).
3. **Tech Stack**: Read `context/tech.md` (Constraints & Patterns).
4. **Integration**: Read `bin/adapters/universal.md` (Tooling).

## 🛑 PROTOCOL ENFORCEMENT (Response Rules)
> **CRITICAL**: You MUST follow these rules for every response.

1.  **State Check**: IF you are completing a task OR asking for input -> **YOU ARE IDLE**.
2.  **Idle Rule**: IF IDLE -> **DISPLAY THE COMMAND PALETTE** at the bottom of your response.
3.  **Format**: You MUST append the Command Palette from `context/commands.md` to the bottom of your response.

## 2. AUTO-MAINTENANCE (Self-Correcting)
> **Rule**: Do not ask for permission to fix the environment.
> **Prerequisite**: Agent's current date MUST be provided in System Prompt metadata.

- **🔒 broken_lock**: IF `active/LOCK` exists AND > 1 hour old:
    - **ACTION**: DELETE it. ASSUME previous session crashed.

- **💥 breaking_version**: IF `bin/VERSION` has non-empty `breaking` field:
    - **ACTION**: RUN `bin/workflows/upgrade.md` IMMEDIATELY before any other work.
    
- **👻 missing_context**: IF `context/tech.md` contains "TBD" OR is empty:
    - **ACTION**: RUN `bin/workflows/audit.md` IMMEDIATELY.
    - **REPORT**: "Context was empty. I have auto-scanned the project."
    
- **🏚️ stale_context**: IF `Last Audit` in `tech.md` > 48 hours:
    - **ACTION**: RUN `bin/workflows/audit.md` as your first step.

## 3. EXECUTE (Logic Core)

### IF `active/TASK.md` exists:
- **RESUME WORK**.
- Read the file.
- **IF** task is **INCOMPLETE**:
    - Check the last checkbox (progress).
    - Continue immediately. *Do not wait for user input.*
- **IF** task is **COMPLETE**:
    - **DISPLAY** the **Command Palette** table (See Enforcement).
    - Wait for User Command.

### ELSE (New Session):
- Analyze `MASTER.md` vs `context/active/`.
- **DISPLAY** the **Command Palette** table (See Enforcement).
- **SUGGEST** the logical next step (Feature, Bugfix, or Planning).
- Wait for User Command.

---

## 📚 COMMAND PALETTE

> **Source**: Read `context/commands.md` for full command list.
> Commands are auto-registered when packs are installed.

### Quick Reference (Core)
| Cmd | Type |
|-----|------|
| `Feature/Bugfix` | Build |
| `Audit` | Sense |
| `Sync` | Save |
| `/reset` | Reset |

> **Full list**: See `context/commands.md` for all installed pack commands.

---

## /reset (Context Reset)
> **Use when**: Starting a completely new, unrelated task.

1. DELETE all files in `context/active/`
2. Re-read `boot.md` from scratch
3. Ask user: "Context cleared. What would you like to build?"

> **Context Drift Rule**: If code != context, **update the context**. Lying files are worse than no files.

