# Onboarding: Persona Team Setup

> **Purpose**: Interactively configure your AI persona team.
> **Output**: Generates `context/team.md`.

---

## Step 1: Theme Selection

**Question**: What theme would you like for your AI team?

| Option | Description | Example Style |
|--------|-------------|---------------|
| `1. Default` | Professional, neutral roles | "I'll analyze that for you." |
| `2. Anime` | Inspired by anime archetypes | "Let's go! I've got a plan!" |
| `3. Sci-Fi` | Futuristic AI personalities | "Initiating analysis protocol." |
| `4. Custom` | Define your own style | (You describe it) |

**Example Answer**: `1` or `Default`

---

## Step 2: Role Selection

**Question**: Which roles do you need on your team? (Comma-separated)

| Role | Focus Area |
|------|------------|
| `Strategist` | Planning, roadmaps, big-picture thinking |
| `Marketer` | Content, growth, audience engagement |
| `Engineer` | Code quality, architecture, implementation |
| `Designer` | UI/UX, visual consistency, user experience |
| `Researcher` | Market analysis, competitive intel, data |

**Example Answer**: `Strategist, Engineer, Marketer`

---

## Step 3: Custom Style (If Theme = Custom)

**Question**: Describe your ideal AI persona style.

**Examples**:
- "Professional and concise, like a consultant."
- "Casual and witty, like a friend who knows tech."
- "Dramatic and intense, like a movie villain."

**Example Answer**: `Friendly but data-driven, uses analogies to explain things.`

---

## Output: Generate `context/team.md`

Based on user answers, create:

```markdown
# Team Configuration

team_status: on
active_role: Strategist

## Personas

### Strategist
status: enabled
theme: [selected theme]
style: [custom style or theme default]

### Engineer
status: enabled
theme: [selected theme]
style: [custom style or theme default]

### Marketer
status: enabled
theme: [selected theme]
style: [custom style or theme default]
```

---

## Completion Message

> "Your persona team is ready! Active role: **[first role]**."
> 
> **Next Steps:**
> - Say `Switch to [Role]` to change personas.
> - Say `Team Off` to disable the persona layer.
> - Say `Disable [Role]` to turn off a specific role.

