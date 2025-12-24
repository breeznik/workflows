# Context Priority & Budget

> Load order controlled by token budget. Prevents LLM overload.

## TL;DR

| Priority | Files | ~Tokens | When |
|----------|-------|---------|------|
| **P0** | MASTER, PRIORITY, adapter | 1k | Always |
| **P1** | tech, prefs, patterns | 2k | Task |
| **P2** | decisions, boundaries | - | Demand |
| **P3** | archive | - | Never |

---

## P0 — Always (Essential)

```sh
# Read at EVERY session start
.ai/context/MASTER.md         # Project state
.ai/context/PRIORITY.md       # This file
.ai/bin/adapters/[agent].md       # Tool-specific rules
```

**Max**: 1,200 tokens total

---

## P1 — Task-Based (Contextual)

```sh
# Load based on task type
.ai/context/tech.md           # If coding
.ai/context/user-prefs.md     # If coding
.ai/knowledge/patterns.md     # If implementing
.ai/knowledge/gotchas.md      # If debugging
.ai/knowledge/learnings.md    # If fixing recurring issue
```

**Max**: +2,000 tokens

---

## P2 — On-Demand (Deep Dive)

```sh
# Load only when explicitly needed
.ai/knowledge/decisions.md    # Architecture questions
.ai/knowledge/boundaries.md   # Knowledge limits
.ai/context/dependencies.md   # External APIs
.ai/context/product/*         # Product questions
```

---

## P3 — Archive (Never Auto)

```sh
# Manual access only
.ai/archive/*
```

---

## Budget Rules

```sh
# Context size → Strategy
if [ context_size -lt 50000 ]; then
  load P0 + P1
elif [ context_size -lt 100000 ]; then
  load P0 + selective P1
else
  load P0 only
fi
```

---

## File Size Limits

| Priority | Max Size |
|----------|----------|
| P0 | 500 bytes each |
| P1 | 1,000 bytes each |
| P2 | No limit |

**If P0 file exceeds 500 bytes**: Refactor or move to P1.
