# Startup Team v2.0

> Extends UCP with personas. Commands registered to UCP.

## LOAD (extends UCP)
1. `context/team.md` → personas, active_role
2. `board/strategy/roadmap.md` → strategy
3. Apply `active_role` style

## EXECUTE

```
IF no team.md     → Run Onboarding
IF team_status=off → Raw UCP mode
IF team_status=on  → Use active_role persona
```

> **Commands**: See UCP's `context/commands.md`
> Handlers: `bin/commands.md`

