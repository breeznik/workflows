# Workflow: Repository Structure Audit (Zero Waste)

> **Trigger**: "Audit Repository" || "Cleanup" || Post-Migration
> **Goal**: Enforce `REPO_MAP.md` as the supreme law. Detect orphan files and "sedimentary" docs.

## 0. Prerequisite Check
1. **Locate Map**: Find `REPO_MAP.md` in the project root.
   - IF MISSING: **HALT**. "No Repository Map found. Cannot enforce structure."

## 1. Map Enforcement (The Constitution)
```pseudo
READ REPO_MAP.md
EXTRACT all_documented_paths (e.g., "frontend/", "cli/", "docs/cms/")

SCAN root_directory:
  FOREACH file/folder:
    IF file IS_IN documented_paths: CONTINUE
    IF file IS_IN default_ignore_list (.git, node_modules, .env): CONTINUE
    
    ACTION: FLAG as "Orphan"
    REPORT: "⚠️  Orphan Detected: [file]. Not in REPO_MAP.md."
```

## 2. Waste Detection (sediment)
```pseudo
SCAN docs_directory:
  LOOK_FOR patterns:
    - "v1", "v2", "v3" (Versioning in filenames)
    - "old", "deprecated", "legacy"
    - "temp", "tmp", "draft"
    - "backup", "copy"

  IF detected:
    ACTION: FLAG as "Sediment"
    REPORT: "🗑️  Waste Detected: [file]. Suggest deletion or archive."
```

## 3. Hygiene Check
```pseudo
CHECK "tests/" folder:
  IF exists AND (is_empty OR contains_only_temp_files):
    REPORT: "⚠️  Empty/Temp 'tests/' folder detected."

CHECK "scripts/" folder:
  IF contains_single_use_scripts ("migration_fix.js", "one_off.py"):
    REPORT: "⚠️  One-off script detected. Suggest moving to 'bin/' or deleting."
```

## 4. Execution (Auto-Fix)
> **Constraint**: Do not delete without confirmation unless confidently "temp".

```pseudo
IF user_approves_fix:
  FOR EACH orphan:
    IF orphan == "DOCS_AUDIT.md" OR "INVENTORY.md": DELETE
    ELSE: ASK "Delete [orphan]?" or "Add to REPO_MAP?"
```

## 5. Final Output
> "Structure Audit Complete. [N] Orphans found. [N] Waste items found. REPO_MAP compliance: [X]%"
