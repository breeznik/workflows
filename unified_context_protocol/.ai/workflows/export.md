---
description: Compile all project knowledge into a portable handoff document
---

# Knowledge Export Workflow

> Create a standalone document containing all accumulated project knowledge.
> Use when migrating, sharing with teams, or archiving.

---

## Output

Creates `KNOWLEDGE_EXPORT.md` in project root (or specified location).

---

## Steps

### 1. Create Export Header

```markdown
# [Project Name] Knowledge Export

**Generated:** YYYY-MM-DD  
**UCP Version:** [from VERSION file]  
**Export Type:** Full / Partial
```

### 2. Compile Project State

From `context/MASTER.md`:
- Current status table
- Active focus
- Critical warnings

### 3. Compile Tech Stack

From `context/tech.md`:
- Frameworks and versions
- Key file paths
- Observed patterns

### 4. Compile User Preferences

From `context/user-prefs.md`:
- Coding style
- Tool preferences
- Workflow preferences

### 5. Compile External Dependencies

From `context/dependencies.md`:
- External APIs with docs links
- Pinned packages with reasons
- Integration gotchas

### 6. Compile All Knowledge

From `knowledge/`:

| File | Section Title |
|------|---------------|
| patterns.md | Code Patterns |
| gotchas.md | Known Issues & Gotchas |
| decisions.md | Architecture Decisions |
| learnings.md | What Works / What Failed |
| boundaries.md | Knowledge Boundaries |

### 7. Compile Open Tasks

From `context/active/`:
- List all active task files
- Include status and next steps

### 8. Generate Executive Summary

At the top, add:
- Project health (based on warnings count)
- Key recommendations
- Outstanding issues

---

## Export Template

```markdown
# [Project Name] Knowledge Export

**Generated:** YYYY-MM-DD  
**UCP Version:** 1.1.0

---

## Executive Summary

**Health:** 🟢 Good / 🟡 Needs Attention / 🔴 Critical Issues

**Key Points:**
- [3-5 most important things about this project]

**Outstanding:**
- [Open tasks or issues]

---

## Project State

[Content from MASTER.md]

---

## Tech Stack

[Content from tech.md]

---

## Code Patterns

[Content from patterns.md]

---

## Known Issues & Gotchas

[Content from gotchas.md]

---

## Architecture Decisions

[Content from decisions.md]

---

## Learnings

### What Works
[From learnings.md]

### What Failed
[From learnings.md]

---

## User Preferences

[Content from user-prefs.md]

---

## External Dependencies

[Content from dependencies.md]

---

## Open Tasks

[List from context/active/]

---

## Knowledge Boundaries

[Content from boundaries.md]

---

*Export complete. This document is self-contained.*
```

---

## Use Cases

| Scenario | Export Type |
|----------|-------------|
| Migrating to new system | Full |
| Sharing with contractor | Full minus user-prefs |
| End of project archive | Full |
| Team onboarding doc | Partial (patterns + tech) |
