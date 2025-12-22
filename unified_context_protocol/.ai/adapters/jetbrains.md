# JetBrains AI Assistant Integration

> **Detection**: You have `.aiassistant/rules/` and run within IntelliJ/PyCharm/WebStorm

## Dual-System Model

| System | Scope | Use For |
|--------|-------|---------|
| **IDE State** (JetBrains) | Editor | Refactorings, autocomplete, file-specific hints |
| **`.ai/`** | Project | Global state, workflows, long-term knowledge |

**Relationship**: IDE optimizes code. `.ai/` tracks *why*.

## Boot Protocol

```sh
cat .ai/context/MASTER.md      # 1. Load project context
ls .ai/context/active/         # 2. Check pending tasks
# → IDE now understands project goals
```

> IDE knows syntax. `.ai/` knows strategy.

## End Protocol

1. Update `.ai/context/changelog.md`
2. Document refactoring patterns → `.ai/knowledge/patterns.md`
3. Incomplete → `.ai/context/active/`

## Recommended Setup

Create `.aiassistant/rules/context.md`:
```markdown
Read `.ai/context/MASTER.md` before work.
Update `.ai/knowledge/` with insights.
```

## Priority

1. `.ai/context/MASTER.md` → 2. IDE state → 3. `.aiassistant/rules/`
