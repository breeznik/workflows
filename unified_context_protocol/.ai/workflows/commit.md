---
description: Standard protocol for creating atomic, meaningful git commits
---

# Commit Workflow

> Use this to ensure history remains clean and context updates are batched with their related code changes.

## Rules

1.  **Atomic Context**: NEVER commit `.ai/` files in isolation unless it is a specific documentation task.
2.  **Batching**: Always stash/stage context updates (`CHANGELOG.md`, `MASTER.md`, `knowledge/`) together with the code changes they describe.
3.  **Conventions**: Use [Conventional Commits](https://www.conventionalcommits.org/).

---

## Steps

### 1. Review Staged Changes
```bash
git status
```
- Are there code changes?
- Is the relevant context updated? (`changelog.md` entry, `MASTER.md` status)
- Are there any accidental files?

### 2. Stage Everything
```bash
git add .
```

### 3. Craft the Commit Message
Format: `type(scope): description`

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `chore`: Maintenance, dependencies, version bumps
- `refactor`: Code change that neither fixes a bug nor adds a feature

**Scope:**
- `ucp`: for .ai/ improvements
- `auth`, `api`, `ui`: for project components

**Description:**
- Imperative, lower case (e.g., "add auth middleware", not "added..." or "Adding...")

### 4. Commit
```bash
git commit -m "type(scope): description"
```

## Examples

### ✅ Good (Batched)
```bash
git add src/auth.ts .ai/context/changelog.md .ai/knowledge/patterns.md
git commit -m "feat(auth): add jwt middleware and document security pattern"
```

### ❌ Bad (Fragmented)
```bash
git add src/auth.ts
git commit -m "add middleware"
# ... 2 minutes later ...
git add .ai/context/changelog.md
git commit -m "update docs"
```
