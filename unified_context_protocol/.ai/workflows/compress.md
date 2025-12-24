# Workflow: Context Compression

> **Trigger**: `stats.md` warnings || Knowledge files > 1KB || Subscription to lean context.

## 1. Metrics Audit

```pseudo
SCAN ".ai/context/*.md", ".ai/knowledge/*.md":
  RECORD file_sizes
  COMPARE against thresholds in "maintenance.md"
```

## 2. Archival Logic

```pseudo
FOREACH context_file:
  IF entries > 30 OR age > 30_days:
    MOVE old_entries TO ".ai/archive/[file]-YYYY-MM.md"
    RETAIN last_10_entries IN active_file
```

## 3. Deduplication

```pseudo
MATCH overlap:
  CASE pattern IN learnings: MOVE to "patterns.md", DELETE from "learnings.md"
  CASE gotcha IN learnings: MOVE to "gotchas.md", DELETE from "learnings.md"
  CASE decision IN patterns: MOVE to "decisions.md", DELETE from "patterns.md"
```

## 4. Verbosity Pruning

```pseudo
FOREACH entry:
  TRANSFORM prose TO bullet_points
  REMOVE conversational_fluff
```

## 5. Stats Update

```pseudo
WRITE to "stats.md": last_compress, bytes_saved, %_reduction
```
