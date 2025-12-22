# Handoff Workflow

> Use at the end of every session to ensure the next AI picks up exactly where you left off.

## Steps

### 1. Update Changelog
- Log all significant changes in `context/changelog.md`
- Use the format: `[YYYY-MM-DD] - [Summary]`

### 2. Commit & Update Status
1. **Batch Changes**: Stage your code changes + `context/changelog.md` + `knowledge/`.
2. **Commit**: Run `.ai/workflows/commit.md`.
3. **Update Status**: Edit `context/MASTER.md` to reflect new reality.

## Example Handoff
"Session complete. Batched commit `feat(auth): implement login` includes code, changelog, and pattern updates. MASTER.md updated to 'Stable'."

### 3. Capture Knowledge
- Did you learn a new pattern? -> `knowledge/patterns.md`
- Did you make a big decision? -> `knowledge/decisions.md`
- Did you hit a trap? -> `knowledge/gotchas.md`
- Did something work/fail unexpectedly? -> `knowledge/learnings.md`
- Unsure what you know? -> Update `knowledge/boundaries.md`

### 4. Create Handoff Task (if incomplete)
If work is unfinished:
1. Create task file in `context/active/`
2. Include: status, next steps, blockers
3. Reference relevant files

## Example Handoff
"Session complete. Updated changelog with new Auth implementation. Updated MASTER.md to show Auth is now 'Stable'. Added a new pattern for 'Protected Routes' to knowledge/patterns.md."
