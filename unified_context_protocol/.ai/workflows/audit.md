# Audit Workflow

> Use this for first session on a project or periodic health checks.

## Steps

### 1. Explore Structure
```
List root directory
List key subdirectories (src/, app/, lib/)
Identify entry points
```

### 2. Identify Tech Stack
- Framework (React, FastAPI, etc.)
- Database (if any)
- Auth system (if any)
- Key dependencies

### 3. Update Context
Update `context/tech.md` with findings:
- Frameworks and versions
- Key file paths
- Observed patterns

### 4. Assess State
Update `context/MASTER.md`:
- Current state table (working/broken/unknown)
- Any critical warnings
- Recent changes if visible in git

### 5. Document Knowledge
Add to `knowledge/` if discovered:
- Architecture decisions -> `decisions.md`
- Code patterns -> `patterns.md`
- Common gotchas -> `gotchas.md`
- What worked/failed -> `learnings.md`

## Output

After audit, the context files should be populated enough for any AI to understand the project quickly.
