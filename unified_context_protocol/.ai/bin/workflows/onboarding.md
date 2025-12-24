---
description: "Generates the Universal Pointer configuration for new agents/users."
---

# UCP Onboarding: The "Keys to the Kingdom"

## Welcome
You have installed the Unified Context Protocol (UCP). To ensure your AI agent (Cursor, Windsurf, etc.) can **always** find the context it needs, you must give it a "Universal Pointer".

Think of this as a key. You only need to put this key in your agent's pocket *once*, and it will be able to unlock the context for any UCP-enabled project you work on.

## The Universal Pointer
Copy the following text and add it to your agent's **global** system instructions (e.g., `.cursorrules` or `Global Custom Instructions`).

```text
# Universal Context Pointer (UCP)
# -------------------------------
# This project uses the Unified Context Protocol (UCP).
# The source of truth for ALL context is the ".ai/" directory.
#
# RULE:
# Before starting ANY task, you MUST check for the existence of ".ai/boot.md".
# If it exists, read it immediately. It contains the instructions,
# workflows, and architectural context for this project.
#
# Do NOT rely on hardcoded prompt settings for this project.
# Delegate all logic to the protocol defined in ".ai/".
```

## Verification
Once you have added this to your global settings, testing it is easy:
1. Open a new chat in this project.
2. Typle "boot" or "help".
3. The agent should immediately identify the UCP structure and offer the correct commands.

---
**Note:** This is a one-time setup per agent. You do not need to do this for every project.
