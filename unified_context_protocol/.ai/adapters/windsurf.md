# Windsurf Integration

> **Detection**: You have Cascade memory and `.windsurf/rules/`

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **Cascade** (Windsurf memory) | Session | Real-time flow, chat history, ephemeral insights |
| **`.ai/`** | Persistent | Permanent state, knowledge base, handoffs |

**Flow**: `.ai/` → Cascade (work) → Cascade → `.ai/` (commit learnings)

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # 1. Load project truth
ls .ai/context/active/         # 2. Check for handoffs
# → Cascade now has full context
```

> Cascade is brilliant for the session. `.ai/` is the transcript.

## End Protocol

1. **Extract from Cascade**: What did I learn?
2. Update `.ai/context/changelog.md`
3. Update `.ai/knowledge/learnings.md` (session insights)
4. Incomplete → `.ai/context/active/`

## Recommended Rule

Add to `.windsurf/rules`:
```
ON BOOT: Read .ai/context/MASTER.md
ON END: Sync learnings to .ai/knowledge/
```

## Priority

1. `.ai/context/MASTER.md` → 2. Cascade → 3. `.windsurf/rules/` → 4. `.ai/workflows/`
