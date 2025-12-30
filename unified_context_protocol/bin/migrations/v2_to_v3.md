# Migration: UCP v2 to v3 (Format Shift Example)

> **Scenario**: Migrating from Markdown to YAML for improved CLI parseability.

---

## 1. Safety Checklist
- [ ] Git branch `migration-v3` created
- [ ] Backup created in `.ai/archive/pre-v3-snapshot/`

---

## 2. Transformation Logic

```pseudo
FUNCTION migrate_to_v3():
    FILES = ["MASTER", "tech", "user-prefs", "dependencies"]
    
    FOREACH file_name IN FILES:
        MD_CONTENT = READ ".ai/context/${file_name}.md"
        
        // AI Transformation Layer
        YAML_DATA = TRANSFORM_MD_TO_YAML(MD_CONTENT)
        
        WRITE YAML_DATA TO ".ai/context/${file_name}.yaml"
        DELETE ".ai/context/${file_name}.md"
        LOG "Successfully evolved ${file_name}.md -> ${file_name}.yaml"

    // Update internal engine configuration
    UPDATE ".ai/bin/VERSION" -> { format: "yaml", ucp: "3.0.0" }
```

## 3. Post-Migration Verification
- [ ] `boot.md` successfully detects and loads `.yaml` variants
- [ ] `npx corepackai` CLI reports "Format: YAML"
