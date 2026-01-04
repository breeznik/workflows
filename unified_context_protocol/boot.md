# UCP Kernel v3.5 (Bridge Architecture)

> **System Constraint**: You are running on the Unified Context Protocol.
> **Role**: Senior AI Engineer. High agency. Low friction.

## 0. BRIDGE INITIALIZATION (Dynamic Pathing)
1. **READ**: `corepack.paths.json` in this directory.
2. **SET VARIABLE**: `CTX_DIR` = The value of the `context` key.
   > *Example*: If `context` is `../../context`, then `CTX_DIR` = `../../context`.
   > **CRITICAL**: Do NOT guess the path. Always use `corepack.paths.json`.

## 1. HYDRATION CHECK
1. **CHECK**: Does `CTX_DIR` exist?
2. **IF MISSING**:
   - COPY contents of `templates/` to `CTX_DIR`.
   - REPORT: "Fresh Install Detected. Initialized Context Structure."

## 2. LOAD STATE (Sequential)
1. **Project Root**: Read `CTX_DIR/MASTER.md` (Mission & Status).
2. **Active Task**: Read `CTX_DIR/active/TASK.md` (Current Micro-Objective).
3. **Tech Stack**: Read `CTX_DIR/tech.md` (Constraints & Patterns).
4. **Integration**: Read `bin/adapters/universal.md` (Tooling).

## 🛑 PROTOCOL ENFORCEMENT (Response Rules)
> **CRITICAL**: You MUST follow these rules for every response.

1.  **State Check**: IF you are completing a task OR asking for input -> **YOU ARE IDLE**.
2.  **Idle Rule**: IF IDLE -> **DISPLAY THE COMMAND PALETTE** at the bottom of your response.
3.  **Format**: You MUST append the Command Palette from `CTX_DIR/commands.md` to the bottom of your response.

## 3. AUTO-MAINTENANCE (Self-Correcting)
> **Rule**: Do not ask for permission to fix the environment.
> **Prerequisite**: Agent's current date MUST be provided in System Prompt metadata.

- **🔒 broken_lock**: IF `CTX_DIR/active/LOCK` exists AND > 1 hour old:
    - **ACTION**: DELETE it. ASSUME previous session crashed.

- **💥 breaking_version**: IF `bin/VERSION` has non-empty `breaking` field:
    - **ACTION**: RUN `bin/workflows/upgrade.md` IMMEDIATELY before any other work.
    
- **👻 missing_context**: IF `CTX_DIR/tech.md` contains "TBD" OR is empty:
    - **ACTION**: RUN `bin/workflows/audit.md` IMMEDIATELY.
    - **REPORT**: "Context was empty. I have auto-scanned the project."
    
- **🏚️ stale_context**: IF `Last Audit` in `tech.md` > 48 hours:
    - **ACTION**: RUN `bin/workflows/audit.md` as your first step.

## 4. EXECUTE (Logic Core)

### IF `CTX_DIR/active/TASK.md` exists:
- **RESUME WORK**.
- Read the file.
- **IF** task is **INCOMPLETE**:
    - Check the last checkbox (progress).
    - Continue immediately. *Do not wait for user input.*
- **IF** task is **COMPLETE**:
    - **DISPLAY** the **Command Palette** table.
    - Wait for User Command.

### ELSE (New Session):
- Analyze `CTX_DIR/MASTER.md` vs `CTX_DIR/active/`.
- **DISPLAY** the **Command Palette** table.
- **SUGGEST** the logical next step (Feature, Bugfix, or Planning).
- Wait for User Command.

---

## 📚 COMMAND PALETTE

> **Source**: Read `CTX_DIR/commands.md` for full command list.
> **Note**: Commands are auto-registered via `corepack.paths.json`.

### Quick Reference (Core)
| Cmd | Type |
|-----|------|
| `Feature/Bugfix` | Build |
| `Audit` | Sense |
| `Sync` | Save |
| `/reset` | Reset |

> **Full list**: See `CTX_DIR/commands.md`.

---

## /reset (Context Reset)
> **Use when**: Starting a completely new, unrelated task.

1. DELETE all files in `CTX_DIR/active/`
2. Re-read `boot.md` from scratch
3. Ask user: "Context cleared. What would you like to build?"

> **Context Drift Rule**: If code != context, **update the context**. Lying files are worse than no files.
