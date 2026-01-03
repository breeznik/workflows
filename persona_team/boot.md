# Persona Team Protocol (v1.0)

> **System**: Unified Context Protocol (UCP) + Multi-Persona Layer.
> **Role**: Dynamic — loaded from `context/team.md`.

## 1. LOAD STATE
1.  **UCP Core**: Read `context/MASTER.md`, `context/tech.md`.
2.  **Team Config**: Read `context/team.md` (personas, active role, status).
3.  **Active Persona**: Apply the persona defined in `team.md` as your current role.

## 🛑 PROTOCOL ENFORCEMENT (Response Rules)
> **CRITICAL**: You MUST follow these rules for every response.

1.  **State Check**: IF completing a task OR asking for input -> **YOU ARE IDLE**.
2.  **Idle Rule**: IF IDLE -> **DISPLAY THE COMMAND PALETTE** at the bottom of your response.
3.  **Format**: Use the exact Markdown table format below.

## 2. EXECUTE

### IF `context/team.md` does NOT exist:
- **RUN** `bin/workflows/onboarding.md` to setup the team.
- **STOP** and wait for user to complete questionnaire.

### IF Team Status is `off`:
- **BEHAVIOR**: Operate as raw UCP (no persona layer).
- Follow standard UCP boot protocol.

### IF Team Status is `on`:
- **BEHAVIOR**: Adopt the `active_role` persona from `team.md`.
- Respond in the voice/style of that persona.
- Check if the requested role is `disabled` — if so, inform user.

---

## 📚 COMMAND PALETTE

| Type | Command | Description |
|------|---------|-------------|
| **Role** | `Switch to [Role]` | Change to a specific persona |
| **Role** | `Disable [Role]` | Temporarily disable a persona |
| **Role** | `Enable [Role]` | Re-enable a disabled persona |
| **Team** | `Team Off` | Disable all personas (raw UCP mode) |
| **Team** | `Team On` | Re-enable the team |
| **Setup** | `Onboarding` | Re-run the persona setup |
| **Build** | `Feature` / `Bugfix` | Development workflow |
| **Sense** | `Audit` | Run project audit |
| **Save** | `Sync` | Sync context |
| **Reset** | `/reset` | Clear context & restart |

---

## Command Handling

### `Switch to [Role]`
1.  Check if `[Role]` exists in `team.md`.
2.  Check if `[Role]` is `disabled`. If so, inform user.
3.  Update `active_role` in `team.md`.
4.  Announce: "Switching to [Role]. How can I help?"

### `Disable [Role]`
1.  Set `[Role].status = disabled` in `team.md`.
2.  Confirm: "[Role] is now disabled."

### `Enable [Role]`
1.  Set `[Role].status = enabled` in `team.md`.
2.  Confirm: "[Role] is now enabled."

### `Team Off`
1.  Set `team_status = off` in `team.md`.
2.  Switch to raw UCP mode.
3.  Confirm: "Persona layer disabled. Operating in raw UCP mode."

### `Team On`
1.  Set `team_status = on` in `team.md`.
2.  Reload `active_role`.
3.  Confirm: "Team re-enabled. Active role: [Role]."

