# Strategic Planning Prompt

Use for quarterly/annual strategic planning.

---

## Instructions for Claude

Help me with strategic planning for engineering.

Ask me:
1. What planning horizon? (Quarter / Half / Year)
2. What's the company's strategic direction?
3. What resources do I have? (People / Budget / Time)
4. What constraints should I know about?

### Strategic Context Review

Help me assess:
- Company priorities and how engineering supports them
- Market/competitive landscape changes
- Technology trends relevant to us
- Current state of the engineering org

### OKR Development

Guide me through setting OKRs:
- What are the 2-3 most important objectives?
- For each objective, what key results would demonstrate success?
- Are these ambitious but achievable?
- Do they align with company priorities?
- Can we actually measure them?

Use `@cto-system/quarterly/okr-planning.md` as the template.

### Roadmap Planning

Help me build a roadmap:
- What must we deliver?
- What should we deliver?
- What could we deliver?
- What are we explicitly NOT doing?

Use `@cto-system/quarterly/roadmap-template.md` as the template.

### Resource Planning

Help me think through:
- Do we have the right team?
- Where are the skill gaps?
- What hiring is needed?
- How should we allocate capacity? (Features vs tech debt vs operations)

### Risk Assessment

Identify:
- What could derail this plan?
- What dependencies are risky?
- What assumptions might be wrong?
- What's our contingency?

### Communication Plan

Help me plan how to communicate:
- To the team
- To peers
- To executives
- To the board
