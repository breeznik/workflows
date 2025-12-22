# Handoff Workflow

> Use at the end of every session to ensure the next AI picks up exactly where you left off.

## Steps

### 1. Update Changelog
- Log all significant changes in `context/changelog.md`
- Use the format: `[YYYY-MM-DD] - [Summary]`

### 2. Update Status
- Update `context/MASTER.md`
- Mark completed tasks as ✅
- Update "Active Focus" if the goal posts moved

### 3. Capture Knowledge
- Did you learn a new pattern? -> `knowledge/patterns.md`
- Did you make a big decision? -> `knowledge/decisions.md`
- Did you hit a trap? -> `knowledge/gotchas.md`

### 4. Leave a Note (Optional)
If there is unfinished work, add a `TODO` section to `context/MASTER.md` for the next agent.

## Example Handoff
"Session complete. Updated changelog with new Auth implementation. Updated MASTER.md to show Auth is now 'Stable'. Added a new pattern for 'Protected Routes' to knowledge/patterns.md."
