# Feature Workflow

> Use when adding new functionality.

## Steps

### 1. Understand Requirements
- What should the feature do?
- Who uses it?
- Any constraints?

### 2. Plan Implementation
- Identify affected files
- Check existing patterns in `context/tech.md`
- Consider edge cases

### 3. Implement
- Follow existing code patterns
- Add appropriate error handling
- Include comments for complex logic

### 4. Test
- Verify feature works
- Check for regressions
- Test edge cases

### 5. Finalize & Commit
1. **Batch Updates**: Stage code changes AND context updates (`tech.md`, `changelog.md`, `learnings.md`) together.
2. **Review**: Ensure no context files are missing.
3. **Commit**: Run `.ai/bin/workflows/commit.md`.

