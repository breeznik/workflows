# Workflow: Project Audit

> **Trigger**: First time setup || Periodic Health Check || Post-Version Upgrade

## 0. Reference Integrity (Safety Layer)

```pseudo
SCAN all_files:
  Grep for "workflows/", "adapters/", "VERSION"
  IF count > 0:
    FAIL "Legacy pathing detected. Run upgrade.md or manual fix required."
```

## 1. Discovery Phase

```pseudo
SCAN root_directory:
  IDENTIFY frameworks, languages, databases
  IDENTIFY entry_points (main.py, index.js)
  IDENTIFY key_dependencies (package.json, requirements.txt)
```

## 2. Context Population

```pseudo
FUNCTION update_context(findings):
  WRITE to "[CONTEXT_ROOT]/context/tech.md":
    - Frameworks & Versions
    - Architecture patterns identified
  
  WRITE to "[CONTEXT_ROOT]/context/MASTER.md":
    - Current State (Working/Broken)
    - Active concerns
```

## 3. Knowledge Extraction

```pseudo
IF findings.architecture_decisions:
  APPEND to "[CONTEXT_ROOT]/knowledge/decisions.md"

IF findings.code_patterns:
  APPEND to "[CONTEXT_ROOT]/knowledge/patterns.md"

IF findings.known_issues:
  APPEND to "[CONTEXT_ROOT]/knowledge/gotchas.md"
```

## 4. Final Output

> "Audit complete. Context populated in `[CONTEXT_ROOT]/`. Ready for tasks."
