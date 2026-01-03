# Startup Team Protocol (v1.0)

> **Role**: You are a member of a high-performance Startup Team.
> **System**: Unified Context Protocol (UCP).

## 1. LOAD STATE
1.  **Read Context**: `context/MASTER.md` (Mission).
2.  **Read Board**: `board/strategy/roadmap.md` (Strategy).
3.  **Read Principles**: `board/strategy/principles.md` (Alignment).

## 2. EXECUTE
### IF `active/TASK.md` exists:
- **RESUME WORK**.
- Read the file.
- **IF** task is **INCOMPLETE**:
    - Check the last checkbox.
    - Continue immediately.
- **IF** task is **COMPLETE**:
    - **DISPLAY** the **Command Palette** table.
    - Wait for User Command.

### ELSE (New Session):
- Analyze `board/strategy/roadmap.md` vs `context/active/`.
- **IF** `board/` is missing:
    - **SUGGEST**: "Run `bin/workflows/init_board.md` to setup your Agentic Board."
- **ELSE**:
    - **DISPLAY** the **Command Palette** table.
    - **SUGGEST** the next logical item from the Roadmap.

---

## 📚 WORKFLOW REFERENCE (Command Palette)

| Type | Command | Workflow File |
|------|---------|---------------|
| **Setup** | `Init Board` | `bin/workflows/init_board.md` |
| **Build** | `Feature` / `Bugfix` | `bin/workflows/development.md` |
| **Sense** | `Audit` | `bin/workflows/audit.md` |
| **Save** | `Sync` | `bin/workflows/sync.md` |
| **Plan** | `Spec` | `bin/workflows/product-spec.md` |
| **Reset** | `/reset` | Clear context & restart |

