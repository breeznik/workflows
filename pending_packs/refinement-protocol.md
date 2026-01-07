# Pack Concept: `@corepackai/refinement-protocol`

**"The Automated QA & Polish Lead"**

> **Status**: Pending / Conceptual
> **Goal**: To codify the rigorous "Audit & Polish" workflow into a reusable Agent Protocol.

## 1. The Insight
The most valuable part of our "Technical Noir" session wasn't the specific style, but the **Visual Integrity Workflow** we followed.
We found that "functional" code often has:
-   Inconsistent design tokens (Light mode leaks).
-   Weak typography/copy.
-   Unbalanced spacing.

The "Refinement Protocol" is the discipline of fixing these unseen issues before shipping.

## 2. The Pack Proposal
A **Workflow Pack** that turns an Agent into a relentless QA Engineer.

**Package Name**: `@corepackai/refinement-protocol`
**Tagline**: "Shipping is just the beginning of refinement."

### Content (The Strategy)

#### A. `audit-logic.md` (The "Grep" Heuristics)
Teaches the agent *how* to look for inconsistencies:
-   **Leak Detection**: "If the project is Dark Mode, grep for `bg-white`, `zinc-50`, `gray-100` and flag them."
-   **Token consistency**: "Check if `border-white/10` is used alongside `border-zinc-800`. Flag the inconsistency."
-   **Type Safety**: "Scan for `any` types or ignored TS errors."

#### B. `copy-sharpening.md` (The Editor)
Teaches the agent how to refine UI text:
-   **Conciseness**: "Shorten labels. 'The Marketplace for...' -> 'Marketplace'."
-   **Hierarchy**: "Ensure H1/H2/H3 use consistent tracking (e.g., `tracking-tight` vs `tracking-widest`)."
-   **Voice**: "Switch passive voice to active voice in buttons/CTAs."

#### C. `interaction-sanity.md` (The UX Check)
A checklist for the Agent to simulate:
-   "Does the clickable element have `cursor-pointer`?"
-   "Does it have a hover state?"
-   "Is the click target at least 44px (mobile friendly)?"

## 3. Future Expansion (The QA Suite)
This Protocol is the foundation for a much larger **Quality Assurance Suite**:
-   **E2E Testing Generators**: Automatically generating Playwright tests for every interactive element found.
-   **Accessibility Audits**: Automated ARIA label checks and contrast ratio verification.
-   **Performance budgets**: Checking bundle sizes and image optimization.

## 4. Usage Scenario
**User**: "I'm done building the Settings page. Run the `@corepackai/refinement-protocol`."

**Agent Action**:
1.  **Scans Types**: "Found 3 `any` types in `Settings.tsx`."
2.  **Scans Visuals**: "Found a rogue `bg-white` in the dark theme modal."
3.  **Scans Copy**: "The 'Save Changes' button could just be 'Save'."
4.  **Auto-Fixes**: "I have patched the `bg-white` and updated the copy."

## 5. Why This Matters
It decouples **Implementation** (building the feature) from **Excellence** (making it ship-ready).
It allows developers to build "messy" first drafts, knowing the Refinement Protocol will catch the details they missed.
