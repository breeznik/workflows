# Unified Context Protocol

This directory contains the **Unified Context Protocol**, a system for orchestrating AI development across complex, multi-project environments.

## Purpose

The Standard `.ai` structure defined here is not just a template; it is a **Protocol** for:

1.  **Multi-Project Orchestration**: Managing context across monorepos (e.g., `projects/frontend`, `projects/backend`) while maintaining a unified vision.
2.  **State Unification**: Bringing together architectural decisions, technical constraints, and active task states into a single, queryable interface.
3.  **Agent Governance**: Defining standardized workflows (`workflows/audit.md`, `workflows/refactor.md`) to ensure consistent AI behavior.

## Contents

- **`.ai/`**: The implementation of the protocol.
    - **`context/projects/`**: The dedicated space for scoped sub-project contexts.
    - **`context/active/`**: A synchronization layer for locking active tasks to prevent agent collisions.
    - **`workflows/`**: Standard Operating Procedures (SOPs) ensuring repeatable success.

## Usage

To adopt this protocol:

1.  **Deploy**: Copy `.ai` to your root.
2.  **Configure**: adapting `context/map.md` to define your project boundaries.
3.  **Orchestrate**: Use the defined workflows to guide agents through complex, multi-step tasks.

## Documentation

For a deep dive into the protocol's mechanics, see the [User Guide](USER_GUIDE.md).

