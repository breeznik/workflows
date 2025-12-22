# Bugfix Workflow

> Use when fixing a reported bug.

## Steps

### 1. Understand the Bug
- What is the expected behavior?
- What is the actual behavior?
- Steps to reproduce?

### 2. Locate the Code
- Search for relevant files
- Check `context/tech.md` for patterns
- Check `knowledge/gotchas.md` for known issues

### 3. Identify Root Cause
- Trace the code path
- Check for similar patterns in codebase
- Verify assumptions

### 4. Implement Fix
- Make minimal changes
- Follow existing patterns
- Add comments if non-obvious

### 5. Verify
- Test the fix
- Check for regressions
- Confirm expected behavior

### 6. Finalize & Commit
1. **Batch Updates**: Stage fix + `changelog.md` + `knowledge/`.
2. **Commit**: Run `.ai/workflows/commit.md`.

