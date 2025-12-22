# User Preferences

> Coding style and tool preferences. Agents learn and respect these.
> Update as you discover what works best for your workflow.

## Coding Style

```yaml
# Naming Conventions
naming:
  variables: snake_case  # or camelCase
  functions: snake_case
  classes: PascalCase
  files: kebab-case

# Code Style
comments: minimal        # minimal | moderate | detailed
docstrings: google       # google | numpy | sphinx | none
line_length: 88
error_handling: explicit # explicit try/catch | let it crash

# Preferences
type_hints: always       # always | public_only | never
tests: pytest            # pytest | unittest | jest | vitest
```

## Communication Style

```yaml
verbosity: concise       # concise | detailed | minimal
explanations: when_asked # always | when_asked | never
ask_before:
  - large refactors
  - deleting files
  - external API calls
```

## Tool Preferences

```yaml
package_manager: npm     # npm | pnpm | yarn | bun
python_env: uv           # pip | uv | poetry | conda
formatter: prettier      # prettier | black | ruff
linter: eslint           # eslint | ruff | flake8
```

## Workflow Preferences

```yaml
commits: conventional    # conventional | descriptive | short
branches: feature/xxx    # feature/xxx | xxx-feature
pr_size: small           # small (<200 lines) | medium | large
```

---

*Last updated: [DATE]*
