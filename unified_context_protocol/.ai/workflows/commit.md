# Workflow: Commit Protocol

> **Trigger**: Ready to commit code changes.

## 1. Pre-Commit Checks

```pseudo
ASSERT tests_pass == TRUE
ASSERT lint_errors == 0
ASSERT no_secrets_in_code == TRUE
```

## 2. Message Generation

```pseudo
FUNCTION generate_commit_message(diff):
  // Format: <type>(<scope>): <subject>
  MATCH change_type:
    CASE new_feature: TYPE = "feat"
    CASE bug_fix: TYPE = "fix"
    CASE docs: TYPE = "docs"
    CASE refactor: TYPE = "refactor"
  
  SET SCOPE = filename_or_module
  SET SUBJECT = concise_summary(diff)
  
  RETURN "${TYPE}(${SCOPE}): ${SUBJECT}"
```

## 3. Execution

```pseudo
RUN "git add ."
RUN "git commit -m '${generated_message}'"
```
