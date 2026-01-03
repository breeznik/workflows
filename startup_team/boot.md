# Startup Team v2.0

> Extends UCP with personas. `Team Off` returns to raw UCP.

## LOAD (adds to UCP)
1. `context/team.md` → personas, active_role
2. `board/strategy/roadmap.md` → strategy
3. Apply `active_role` style

## 🛑 ENFORCEMENT (from UCP)
IDLE → **DISPLAY COMMAND PALETTE**

## EXECUTE

```
IF no team.md     → Run Onboarding
IF team_status=off → FALLBACK TO UCP (no persona layer)
IF team_status=on  → Use active_role persona style
```

**Task Logic**: Same as UCP (resume if exists, suggest if new)

---

## 📚 COMMANDS

| Cmd | Source |
|-----|--------|
| `Onboarding` | Startup Team |
| `Switch to [R]` | Startup Team |
| `Disable/Enable [R]` | Startup Team |
| `Team Off` | → Raw UCP |
| `Team On` | → Persona layer |
| `Feature/Bugfix/Audit/Sync` | UCP |
| `/reset` | UCP |

> **Flow**: Team Off = UCP. Team On = Persona layer on top of UCP. No friction.

