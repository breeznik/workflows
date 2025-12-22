# Refactor Workflow

> Use when improving existing code without changing behavior.

## Steps

### 1. Identify Scope
- What needs improvement?
- Why is it important?
- What should NOT change?

### 2. Verify Current Behavior
- Understand what code does
- Note expected inputs/outputs
- Identify test coverage

### 3. Plan Changes
- Break into small steps
- Check `knowledge/patterns.md` for conventions
- Minimize blast radius

### 4. Implement
- Make incremental changes
- Verify behavior after each step
- Keep commits logical

### 5. Verify
- Ensure behavior unchanged
- Check for regressions
- Validate performance if relevant

### 6. Update Context
- Add to `changelog.md`
- Update `knowledge/patterns.md` if new patterns
- Document decision in `knowledge/decisions.md`
