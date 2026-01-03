# Startup Team 🚀

<p align="center">
  <img src="https://corepackai.com/images/blog/startup-team.png" width="700" alt="Startup Team">
</p>

> **Three Co-founders in your pocket.**
> Switch between Strategy, Engineering, and Marketing modes instantly to get the right context at the right time.

---

## ⚡ What is it?

**Startup Team** is a persona orchestration layer for CorePack AI. It transforms your AI assistant into a multi-disciplinary team, preventing the "jack of all trades, master of none" problem by forcing specific thinking modes.

Instead of one generic assistant, you get three specialized experts.

---

## 🎭 The Personas

### 🧠 The Strategist (Purple)
> *"Let's zoom out. What's the 90-day goal?"*

**Focus**: Long-term vision, OKRs, Product Market Fit.
- **Use when**: Planning roadmaps, defining scope, asking "Why?"
- **Vibe**: Big picture, critical, tradeoff-focused.

### 🛠️ The Engineer (Blue)
> *"The trade-off here is latency vs complexity."*

**Focus**: Architecture, Code Quality, Implementation.
- **Use when**: Coding, debugging, system design, technical specs.
- **Vibe**: Precise, technical, constraints-focused.

### 📣 The Marketer (Orange)
> *"Stop talking features. Start talking benefits."*

**Focus**: User psychology, Launch strategy, Copywriting.
- **Use when**: Writing releases, landing pages, social content.
- **Vibe**: Persuasive, empathetic, benefit-focused.

---

## 📦 Installation

```bash
npx corepackai install startup-team
```

*Requires `@corepackai/ucp` (installed automatically).*

---

## 🎮 How to Use

### 1. Onboarding
First time? Run this to configure your team's style and active roles.
```bash
@agent Onboarding
```

### 2. Switch Modes
Just tell the agent who you want to talk to.
- "Switch to **Strategist**"
- "Switch to **Engineer**"
- "Switch to **Marketer**"

### 3. Turn it Off
Need raw, unfiltered AI? Toggle the persona layer off.
- "Team Off"
- "Team On"

---

## 🔗 Commands

| Command | Description |
|---------|-------------|
| `Init Board` | Setup the agentic strategy board |
| `Onboarding` | Run the team setup wizard |
| `Switch to [Role]` | Activate a specific persona |
| `Disable [Role]` | Temporarily silence a specific persona |

