# Compress Workflow

> Reduce context bloat. Run monthly or when stats.md shows warnings.

## When to Run

- `stats.md` shows file size warnings
- Knowledge files exceed 1KB
- Duplicate entries suspected
- Before major releases

## Steps

### 1. Measure Current State

```sh
# Check file sizes
ls -la .ai/context/*.md
ls -la .ai/knowledge/*.md

# Update stats.md with current counts
```

### 2. Archive Old Entries

```sh
# Move entries older than 30 days to archive
# Format: archive/[file]-[date].md

# From learnings.md → archive/learnings-2025-12.md
# From changelog.md → archive/changelog-2025-12.md
```

**Keep in active file**: Last 10 entries or 30 days, whichever is less.

### 3. Merge Duplicates

Check for overlap between:
- `patterns.md` ↔ `learnings.md`
- `gotchas.md` ↔ `learnings.md`
- `decisions.md` ↔ `patterns.md`

**Rule**: If same concept appears twice, keep in most specific file.

### 4. Compress Verbose Entries

Before:
```markdown
### Pattern: Error Handling
We discovered that when dealing with API errors, the best approach
is to always wrap calls in try-catch and log the full error object
including the stack trace for debugging purposes.
```

After:
```markdown
### Error Handling
API calls: try-catch + log full error w/ stack.
```

### 5. Update stats.md

```yaml
last_compress: [DATE]
before:
  total_bytes: [X]
after:
  total_bytes: [Y]
savings: [X-Y] bytes ([%]%)
```

## Output

- Archived files in `archive/`
- Leaner knowledge files
- Updated `stats.md`
