# Claude Integration

> **Detection**: You have access to Projects, Artifacts, and contextual chat

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **Claude Artifacts/Chat** | Conversation | Drafts, brainstorming, ephemeral planning |
| **`.ai/`** | Permanent | Finalized state, knowledge, handoff instructions |

**Flow**: `.ai/` → Conversation → Artifact (draft) → `.ai/` (commit)

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # 1. Ground in reality
ls .ai/context/active/         # 2. Check for handoffs
# → Start conversation informed by truth
```

> Conversation is for thinking. `.ai/` is for remembering.

## End Protocol

1. **Distill from conversation**: What's permanent?
2. Update `.ai/context/changelog.md`
3. Save insights → `.ai/knowledge/learnings.md`
4. Incomplete → `.ai/context/active/`

## Recommended CLAUDE.md

```markdown
# Context Protocol
Read `.ai/context/MASTER.md` at session start.
Write permanent learnings to `.ai/knowledge/`.
```

## Priority

1. `.ai/context/MASTER.md` → 2. Conversation → 3. `CLAUDE.md` → 4. `.ai/workflows/`
