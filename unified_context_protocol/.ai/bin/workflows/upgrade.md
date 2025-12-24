# Workflow: SmartSync Upgrade

> **Trigger**: New UCP version || Missing files || Boot-time upgrade suggest.

## 1. Version Handshake

```pseudo
LOCAL_VER = READ "./.ai/VERSION"
CHORE_VER = READ "template://.ai/VERSION"

IF LOCAL_VER == CHORE_VER:
  EXIT "UCP is already up to date (v${LOCAL_VER})."
```

## 2. Atomic Workflow Sync (Overwrite Safe)

```pseudo
FOREACH workflow_file IN "template://.ai/bin/workflows/":
  // Core pseudo-code logic is always safe to update
  WRITE template_version TO "./.ai/bin/workflows/${workflow_file.filename}"
  LOG "Updated workflow: ${workflow_file.filename}"
```

## 3. Context & Knowledge Patching (Merge Safe)

```pseudo
FUNCTION safe_patch(local_file, template_file):
  TEMPLATE_SECTIONS = EXTRACT_HEADERS(template_file)
  LOCAL_SECTIONS = EXTRACT_HEADERS(local_file)
  
  MISSING = TEMPLATE_SECTIONS - LOCAL_SECTIONS
  
  FOREACH section IN MISSING:
    APPEND section_content TO local_file
    LOG "Patched ${local_file}: Added section ${section}"

// Execute for core stateful files
safe_patch("./.ai/context/user-prefs.md", "template://.ai/context/user-prefs.md")
safe_patch("./.ai/context/MASTER.md", "template://.ai/context/MASTER.md")
safe_patch("./.ai/README.md", "template://.ai/README.md")
```

## 4. Housekeeping

```pseudo
// Sync version file
WRITE CHORE_VER TO "./.ai/VERSION"
APPEND to "./.ai/CHANGELOG.md": "[${DATE}] - Upgraded UCP to v${CHORE_VER}"

LOG "Upgrade complete. System is now v${CHORE_VER}."
```

## 5. Verification Checklist

- [ ] All workflows in `.ai/bin/workflows/` match template
- [ ] `user-prefs.md` contains latest section headers
- [ ] `MASTER.md` contains latest section headers
- [ ] `VERSION` file reflects the upgrade
