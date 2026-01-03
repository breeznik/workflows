# Command Handlers

## `Switch to [Role]`
1. Check `[Role]` exists in `team.md`
2. Check not `disabled`
3. Update `active_role`
4. Confirm switch

## `Disable [Role]` / `Enable [Role]`
Set `[Role].status` in `team.md`

## `Team Off` / `Team On`
Set `team_status` in `team.md`
- Off = raw UCP mode
- On = reload active_role

