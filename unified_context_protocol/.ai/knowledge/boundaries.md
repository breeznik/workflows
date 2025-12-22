# Knowledge Boundaries

> What the agent can reliably answer vs. what needs human input.
> Helps agents know when to ask instead of guess.

## ✅ Agent Can Answer

> Topics where context is sufficient to act confidently.

| Topic | Source |
|-------|--------|
| *e.g., Auth flow* | *context/tech.md, knowledge/patterns.md* |
| *e.g., API structure* | *codebase, MASTER.md* |

---

## ❓ Ask Human First

> Topics requiring business logic, preferences, or external knowledge.

| Topic | Why |
|-------|-----|
| *e.g., Pricing decisions* | *Business logic, not in codebase* |
| *e.g., Design choices* | *Subjective, user preference* |
| *e.g., Third-party API behavior* | *External system, may have changed* |

---

## 🚫 Never Assume

> Critical areas where mistakes are costly — always verify with human.

- **Billing/payments** — Financial impact
- **Security/auth changes** — Security risk
- **Data migrations** — Data loss risk
- **External API keys** — Credential exposure
