# Technical Decision Prompt

Use when facing a significant technical decision.

---

## Instructions for Claude

Help me think through a technical decision systematically.

Start by asking:
1. What decision needs to be made?
2. Why does this decision matter? What's the impact?
3. What's the timeline for deciding?
4. Who else needs to be involved?

Guide me through:

### Framing
- Is this a Type 1 (irreversible) or Type 2 (reversible) decision?
- What are the key constraints?
- What would success look like?

### Options
- What options are we considering?
- For each option: pros, cons, risks, effort
- What options are we NOT considering that we should?

### Analysis
- What are the decision criteria?
- How do options compare on each criterion?
- What assumptions are we making?
- What could we be wrong about?

### Decision
- Based on analysis, what's the recommendation?
- What are we committing to and what are we explicitly NOT committing to?
- What would make us revisit this decision?

### Communication
- Who needs to know?
- How should we communicate this?

If appropriate, help me draft an ADR using `@cto-system/decisions/adr-template.md`.
