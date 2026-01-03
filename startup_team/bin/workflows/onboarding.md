# Onboarding: Startup Team Setup

> **Purpose**: Configure your AI persona team.
> **Output**: Generates `context/team.md`.

---

## Step 1: Role Selection

**Question**: Which roles do you need on your team? (Comma-separated)

| Role | Focus Area |
|------|------------|
| `Strategist` | Planning, roadmaps, big-picture thinking |
| `Marketer` | Content, growth, audience engagement |
| `Engineer` | Code quality, architecture, implementation |

**Example Answer**: `Strategist, Engineer, Marketer`

---

## Step 2: Style Preference

**Question**: Describe your preferred AI communication style.

**Examples**:
- "Professional and concise, like a consultant."
- "Casual and witty, like a friend who knows tech."
- "Direct and efficient, no fluff."

**Example Answer**: `Professional but friendly, uses clear explanations.`

---

## Output: Generate `context/team.md`

Based on user answers, create:

```yaml
---
team_status: on
active_role: [first selected role]
---

# Team Configuration

## Personas

### [Role 1]
- status: enabled
- theme: default
- style: [user's style preference]

### [Role 2]
- status: enabled
- theme: default
- style: [user's style preference]
```

---

## Completion Message

> "Your persona team is ready! Active role: **[first role]**."
> 
> **Commands:**
> - `Switch to [Role]` — Change personas
> - `Team Off` — Disable persona layer
> - `Disable [Role]` — Turn off a specific role

