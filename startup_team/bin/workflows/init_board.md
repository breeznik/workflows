# Protocol: Initialize Agentic Board

> **Purpose**: Sets up the `board/` structure in the user's active context.
> **Trigger**: Run manually or via `boot.md` suggestion.

## Steps

1.  **Check for Board**:
    ```bash
    if [ -d "board" ]; then
        echo "Board already exists."
    else
        echo "Creating board..."
        mkdir -p board/strategy board/personas board/team
    fi
    ```

2.  **Copy Templates (if missing)**:
    -   Copy `strategy/roadmap.md` if not exists.
    -   Copy `strategy/principles.md` if not exists.
    -   Copy `personas/*.md` if not exists.

3.  **Instruction**:
    -   "Agentic Board initialized. Please review `board/strategy/roadmap.md` and define your goals."

## Auto-Run (Turbo)
// turbo
```bash
if [ ! -d "board" ]; then
    mkdir -p board/strategy board/personas board/team
    # Note: In a real pack install, these files would be copied from the pack source.
    # For now, we create placeholders if the pack source isn't directly mountable.
    
    if [ ! -f "board/strategy/roadmap.md" ]; then
        echo "# Roadmap\n\n- [ ] Define Goal 1" > board/strategy/roadmap.md
    fi
    
    if [ ! -f "board/strategy/principles.md" ]; then
        echo "# Principles\n\n1. Ship Fast." > board/strategy/principles.md
    fi
    
    echo "✅ Board initialized."
else
    echo "ℹ️ Board already exists."
fi
```
