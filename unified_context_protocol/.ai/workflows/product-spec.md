# Product Spec Workflow

> Use when defining a new feature from a BUSINESS perspective (before coding).

## Steps

### 1. Goal Definition
- Which **Persona** is this for? (See `context/product/users.md`)
- Which **Metric** does this move? (See `context/product/vision.md`)
- What is the **Sales Narrative**? (See `context/product/vision.md`)

### 2. Requirements Gathering
- Must-have features (MVP)
- Nice-to-have features
- "Anti-goals" (what we will NOT do)

### 3. Drafting the Spec
Create a file in `context/product/specs/` (create folder if needed):
```markdown
# Spec: [Feature Name]
**Driver**: [User Persona]
**Goal**: [Business Goal]

## User Story
"As a [Role], I want to [Action], so that [Benefit]."

## Acceptance Criteria
- [ ] User can do X...
- [ ] System responds with Y...
```

### 4. Review
- Check against `brand.md` for tone.
- Check against `roadmap.md` for timing alignment.
