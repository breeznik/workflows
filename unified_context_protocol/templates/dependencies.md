# External Dependencies

> Quick reference for external services, APIs, and critical packages.
> Helps agents understand integrations without reading docs.

## 🌐 External APIs

| Service | Purpose | Docs | Rate Limits | Auth |
|---------|---------|------|-------------|------|
| *e.g., Stripe* | *Payments* | *https://stripe.com/docs* | *100 req/sec* | *API Key* |
| *e.g., Clerk* | *Auth* | *https://clerk.com/docs* | *Unlimited* | *Publishable Key* |

## 🔑 Environment Variables

| Variable | Service | Required |
|----------|---------|----------|
| *e.g., `STRIPE_SECRET_KEY`* | *Stripe* | *Yes* |
| *e.g., `CLERK_PUBLISHABLE_KEY`* | *Clerk* | *Yes* |

## 📦 Pinned Dependencies

> Packages that MUST stay at specific versions.

| Package | Version | Reason |
|---------|---------|--------|
| *e.g., next* | *14.0.4* | *Breaking changes in 15.x* |

## ⚠️ Integration Gotchas

> Known issues with external services.

<!-- Add entries:
### [Service Name]
- Issue description
- Workaround
-->

*Add gotchas above this line.*
