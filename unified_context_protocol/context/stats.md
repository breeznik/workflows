# Context Statistics

> Auto-updated by agents. Check for warnings before boot.

## Current State

```yaml
last_audit: [DATE]
version: 1.1.0

token_estimate:
  P0: ~1000
  P1: ~2000
  P2: ~1500
  total: ~4500

file_sizes:
  MASTER.md: [X] bytes
  PRIORITY.md: [X] bytes
  tech.md: [X] bytes
  learnings.md: [X] bytes
  patterns.md: [X] bytes
  gotchas.md: [X] bytes
```

## Warnings

```yaml
# Auto-populated when issues detected
warnings: []

# Examples:
# - learnings.md exceeds 1000 bytes (run compress)
# - 3+ entries older than 30 days (archive needed)
# - Duplicate pattern detected in patterns.md and gotchas.md
```

## Health Score

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| P0 Load | <1200 tokens | - | 🔲 |
| Knowledge Files | <1KB each | - | 🔲 |
| Entries Age | <30 days | - | 🔲 |
| Duplicates | 0 | - | 🔲 |

## Actions

- ⚠️ Warnings present → Run `workflows/compress.md`
- ✅ All green → No action needed

---

*Updated: [DATE]*
