# Workflow: Context Refinement (Learning)

> **Trigger**: End of Session || Major Milestone

## 1. Scan Logic

```pseudo
FOREACH interaction IN session_history:
  IF user.msg CONTAINS ("No", "Don't", "Incorrect") OR user.action == REJECT_PLAN:
    state.trigger = CORRECTION
  IF diff(agent_code, user_final_code).exists():
    state.trigger = STYLE_PREF_IMPLICIT
  IF user.msg CONTAINS ("Use X", "I prefer Y", "Change architecture"):
    state.trigger = EXPLICIT_DECISION
```

## 2. Update Routing

| Trigger Type | Observation | Target File | Action |
|--------------|-------------|-------------|--------|
| `STYLE_PREF` | Syntax preference (e.g., arrows) | `.ai/context/user-prefs.md` | Add to `## Coding Style` |
| `CORRECTION` | Rejected library/pattern | `.ai/context/user-prefs.md` | Add to `## 🚫 Anti-Patterns` |
| `CORRECTION` | General lesson ("Auth is flaky") | `.ai/knowledge/learnings.md` | Add to `## ✅ What Works` / `## ❌ What Failed` |
| `DECISION` | New library added | `.ai/context/tech.md` | Add to relevant section |
| `DECISION` | Feature completed | `.ai/context/product/roadmap.md` | Mark as `[x]` |
| `DECISION` | Arch change | `.ai/context/MASTER.md` | Update `## Current State` |

## 3. Commit Gates

```pseudo
FUNCTION commit_rule(rule):
  // Guardrails against bad data
  MATCH rule:
    CASE contradicts(existing_rules): ASK user
    CASE is_one_off_event(): DISCARD
    CASE default: WRITE to target_file
```

## 4. Execution Prompt

> "Analyze session history using the Scan Logic. For established patterns, run the Commit Gates. If valid, update the Target Files defined in the Routing table."
