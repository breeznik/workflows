# Context Priority & Budget

> Controls what agents read and when — prevents LLM context overload.
> Agents MUST respect these priorities to stay within token budgets.

## TL;DR

| Priority | Files | Tokens | When |
|----------|-------|--------|------|
| **P0** | MASTER, PRIORITY, adapter | ~2k | Always |
| **P1** | tech, prefs, patterns | ~3k | Task-based |
| **P2** | decisions, boundaries | - | On-demand |
| **P3** | archive | - | Never auto |

## 📊 Context Budget

| Context Size | Strategy |
|--------------|----------|
| **Small** (<50k tokens) | Load all P0 + P1 |
| **Medium** (50-100k) | Load P0, selective P1 |
| **Large** (>100k) | Load P0 only, on-demand P1/P2 |

---

## 🔴 P0 — Always Read (Essential)

> Read these at EVERY session start. Non-negotiable.

| File | Purpose | Max Size |
|------|---------|----------|
| `context/MASTER.md` | Current state | 100 lines |
| `context/PRIORITY.md` | This file | 50 lines |
| `adapters/[your-agent].md` | Your integration rules | 60 lines |

**Token budget: ~2,000 tokens**

---

## 🟡 P1 — Read if Relevant (Context-Dependent)

> Read based on the task at hand.

| File | Read When | Max Size |
|------|-----------|----------|
| `context/tech.md` | Any code changes | 100 lines |
| `context/user-prefs.md` | Generating code | 60 lines |
| `context/dependencies.md` | External API work | 50 lines |
| `knowledge/patterns.md` | Writing new code | 200 lines |
| `knowledge/gotchas.md` | Debugging | 100 lines |
| `context/active/*.md` | Resuming work | Varies |

**Token budget: ~3,000 tokens**

---

## 🟢 P2 — Read on Demand (Reference Only)

> Only read when explicitly needed or asked.

| File | Read When |
|------|-----------|
| `knowledge/decisions.md` | Architecture questions |
| `knowledge/learnings.md` | Before trying new approach |
| `knowledge/boundaries.md` | Unsure what you know |
| `context/product/*.md` | Product/UX work |
| `context/changelog.md` | Need change history |
| Older `context/active/*.md` | Historical tasks |

**Token budget: On-demand only**

---

## 🔵 P3 — Archive (Never Auto-Load)

> Only read if explicitly requested by user.

| Directory | Contents |
|-----------|----------|
| `archive/` | Old changelogs, snapshots, deprecated knowledge |

---

## ⚙️ Loading Strategy

### At Session Start
```
1. Read PRIORITY.md (this file)
2. Read MASTER.md
3. Read your adapter file
4. Check context/active/ for pending tasks
5. IF task found → load relevant P1 files
6. IF no task → wait for user instruction
```

### During Session
```
- Load P1 files as needed based on task type
- Load P2 files only when explicitly relevant
- Never auto-load P3 (archive)
```

### When Context Grows Large
```
1. Summarize instead of reading full files
2. Ask user which context is most relevant
3. Offload resolved knowledge to archive
```

---

## 📏 Size Limits & Overflow

| File | Soft Limit | Hard Limit | Overflow Action |
|------|------------|------------|-----------------|
| MASTER.md | 80 lines | 120 lines | Archive old changes |
| changelog.md | 30 entries | 50 entries | Archive to monthly file |
| patterns.md | 150 lines | 250 lines | Split into categories |
| Any knowledge file | 150 lines | 300 lines | Archive or split |

---

## 🚨 Overload Prevention

If you notice context is getting large:

1. **Run maintenance workflow** — prunes and archives
2. **Ask user to confirm priorities** — what's most relevant now?
3. **Summarize don't quote** — paraphrase instead of copying full context
4. **Use file references** — "See patterns.md for X" instead of inlining
