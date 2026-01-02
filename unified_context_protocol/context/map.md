# Codebase Map (Token-Optimized)

> **Purpose**: Quick navigation index for Agents.
> **Preferred I/O**: `corepackai` CLI (if available).

## 🔑 Key Files
- `bin/workflows/`: Agent Meta-Instructions
- `bin/ops/`: Project Procedures (Test, Deploy)

## 📂 Directories
- `context/active/`: Volatile State (Lock file)
- `knowledge/`: Persistent Wisdom

## 🏗️ Logic & Architecture
- **Pattern**: *[e.g. Monolith / Microservices / Next.js Pages]*
- **Key Logic Flows**:
  - *[e.g. User Login: AuthProvider -> LoginScreen -> API]*
  - *[e.g. Data Sync: Webhook -> Parser -> DB]*

## 🧩 Component Relations
> Map how major parts talk to each other.
- `[Component A]` dependencies: `[Comp B]`, `[Comp C]`
- `[Component B]` triggers: `[Event X]`
