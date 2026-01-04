# Context Priority & Budget

> [!CAUTION]
> **MANDATORY**: Read this BEFORE loading any other context.

## TL;DR

| Priority | Files | Max Size | When |
|----------|-------|----------|------|
| **P0** | MASTER, PRIORITY, adapter | 500B | Always |
| **P1** | tech, prefs, patterns | 1KB | Task-based |
| **P2** | decisions, boundaries, product | - | On demand |
| **P3** | archive | - | Never auto |

---

## Loading Rules

```
P0: Always load (MASTER.md, PRIORITY.md, adapter)
P1: Load if coding/debugging (tech.md, patterns.md)
P2: Load on explicit need (decisions.md, boundaries.md)
P3: Manual access only (archive/*)
```

## Size Enforcement

> [!WARNING]
> If any P0 file exceeds **500 bytes** or P1 exceeds **1000 bytes**:
> Run `bin/workflows/maintenance.md` to prune.

---
*See `bin/workflows/maintenance.md` for pruning.*
