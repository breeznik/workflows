# Workflow: Project Audit

> **Trigger**: First time setup || Periodic Health Check || Post-Version Upgrade

## 0. Reference Integrity (Safety Layer)

```pseudo
SCAN all_files:
  Grep for "workflows/", "adapters/", "VERSION"
  IF count > 0:
    FAIL "Legacy pathing detected. Run upgrade.md or manual fix required."
```

## 1. Discovery Phase (Eagle View)

```pseudo
SCAN root_directory:
  IDENTIFY frameworks, languages, databases
  IDENTIFY entry_points (main.py, index.js, App.tsx)
  IDENTIFY key_dependencies (package.json, requirements.txt)
  IDENTIFY project_structure (monorepo vs polyrepo)
```

## 2. Deep Analysis (Logic & Flow)

```pseudo
SELECT 3-5 key_files (Entry point, Core Controller, Main Data Model)
READ content of selected_files
TRACE Execution Flow:
  Start at [Entry Point] -> Follow to [Core Logic] -> End at [Data/Output]
IDENTIFY Design Patterns (MVC, Singleton, Adapter, etc.)
```

## 3. Context Synthesis

```pseudo
FUNCTION update_context(findings):
  WRITE to "[CONTEXT_ROOT]/context/tech.md":
    - UPDATE "Last Audit" timestamp to TODAY
    - Frameworks & Versions
    - "Architecture & Data Flow": Summarize the execution trace from Step 2
  
  WRITE to "[CONTEXT_ROOT]/context/map.md":
    - Fill "Logic & Architecture" with identified patterns
    - Fill "Component Relations" (who calls whom)
    - Map key directories to business features
  
  WRITE to "[CONTEXT_ROOT]/knowledge/patterns.md":
    - Document specific code patterns found (e.g. "Uses Factory for Auth")

  WRITE to "[CONTEXT_ROOT]/context/MASTER.md":
    - Current State (Working/Broken)
    - Summary of "What this app actually does" (high-level functional)
```

## 4. Feature Extraction

```pseudo
IF context/product/vision.md exists:
  EXTRACT observed_features from code
  COMPARE with vision.md
  UPDATE "Current Features" list in vision.md or MASTER.md
```

## 5. Final Output

> "Deep Audit complete. Context populated in `[CONTEXT_ROOT]/`. Architecture and Logic Flow recorded."
