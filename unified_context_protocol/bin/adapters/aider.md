# Aider

> Detect: `.aider.conf.yml` + CLI

## Model

| System | Use |
|--------|-----|
| Aider | Git-native edits |
| `[CONTEXT_ROOT]/` | Project memory |

Flow: `[CONTEXT_ROOT]/` → Aider → Git → `[CONTEXT_ROOT]/`

> **Note**: `[CONTEXT_ROOT]` refers to your installation directory (e.g. `.ai`, `.context`).

## Boot

```sh
cat [CONTEXT_ROOT]/context/MASTER.md
aider
```

## End

```sh
echo "changes" >> [CONTEXT_ROOT]/context/changelog.md
echo "learnings" >> [CONTEXT_ROOT]/knowledge/learnings.md
# Then git commit
```

## Config

`.aider.conf.yml`:
```yaml
read:
  - [CONTEXT_ROOT]/context/MASTER.md
  - [CONTEXT_ROOT]/boot.md
```

## Priority

MASTER → Aider session → .aider.conf.yml
