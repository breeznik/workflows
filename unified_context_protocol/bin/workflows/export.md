# Workflow: Knowledge Export

> **Trigger**: Migration || Team Sharing || Project Archive.

## 1. Aggregation Engine

```pseudo
FUNCTION compile_export():
  INITIALIZE "KNOWLEDGE_EXPORT.md"
  
  APPEND header: [Project Name], [Date], [UCP Version]
  
  // High-Priority Context
  APPEND from "MASTER.md": current_status, active_focus, warnings
  APPEND from "tech.md": stack, paths, patterns
  
  // Personalization
  APPEND from "user-prefs.md": style, tools, habits
  
  // Knowledge Base
  FOREACH file IN "[CONTEXT_ROOT]/knowledge/*.md":
    APPEND content AS section
  
  // Active Pipeline
  APPEND from "[CONTEXT_ROOT]/context/active/": all_task_summaries
```

## 2. Summary Generation

```pseudo
GENERATE executive_summary:
  CALCULATE project_health (warning_count)
  IDENTIFY key_recommendations (top_3_learnings)
  LIST outstanding_blockers (active_tasks)
```

## 3. Output Checklist

- [ ] Self-contained (no external links required)
- [ ] Exec Summary at top
- [ ] All knowledge sections included
