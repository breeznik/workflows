# Workflow: Project Audit

> **Trigger**: First time setup || Periodic Health Check || Post-Version Upgrade

## 0. Reference Integrity (Safety Layer)

```pseudo
SCAN all_files:
  Grep for ".ai/workflows/", ".ai/adapters/", ".ai/VERSION"
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
  WRITE to ".ai/context/tech.md":
    - Frameworks & Versions
    - Architecture patterns identified
  
  WRITE to ".ai/context/MASTER.md":
    - Current State (Working/Broken)
    - Active concerns
```

## 3. Knowledge Extraction

```pseudo
IF findings.architecture_decisions:
  APPEND to ".ai/knowledge/decisions.md"

IF findings.code_patterns:
  APPEND to ".ai/knowledge/patterns.md"

IF findings.known_issues:
  APPEND to ".ai/knowledge/gotchas.md"
```

## 4. Final Output

> "Audit complete. Context populated in `.ai/`. Ready for tasks."
