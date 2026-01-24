# Architecture Review Prompt

Use when reviewing or designing system architecture.

---

## Instructions for Claude

Help me review or design system architecture.

First, determine if this is:
1. **New design** - We're designing something new
2. **Review** - We're evaluating a proposed design
3. **Audit** - We're assessing existing architecture

### For New Design

Ask me:
- What problem are we solving?
- What are the requirements (functional and non-functional)?
- What constraints exist (timeline, team, budget, existing systems)?
- What scale do we need to support?

Guide me through designing:
- High-level architecture
- Key components and their responsibilities
- Data flow
- API contracts
- Scalability approach
- Failure modes and mitigation
- Security considerations
- Migration/rollout strategy

### For Review

Ask me to describe the proposed architecture, then help me evaluate:
- Does it solve the stated problem?
- Is it appropriately simple or complex?
- What are the failure modes?
- How does it scale?
- What are the operational implications?
- What's the migration path?
- What questions should I ask the proposer?

### For Audit

Help me assess:
- Current pain points
- Scalability limits
- Technical debt
- Security gaps
- Operational burden
- Recommendations for improvement

Use `@cto-system/technical/architecture-review.md` as the template.
