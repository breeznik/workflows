# Aider

> Detect: `.aider.conf.yml` + CLI

## Model

| System | Use |
|--------|-----|
| Aider | Git-native edits |
| `.ai/` | Project memory |

Flow: `.ai/` → Aider → Git → `.ai/`

## Boot

```sh
cat .ai/context/MASTER.md
aider
```

## End

```sh
echo "changes" >> .ai/context/changelog.md
echo "learnings" >> .ai/knowledge/learnings.md
# Then git commit
```

## Config

`.aider.conf.yml`:
```yaml
read:
  - .ai/context/MASTER.md
  - .ai/README.md
```

## Priority

MASTER → Aider session → .aider.conf.yml
