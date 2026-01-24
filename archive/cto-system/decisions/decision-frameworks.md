# Decision Frameworks

Reference guide for making better decisions.

## When to Use Which Framework

| Situation | Framework |
|-----------|-----------|
| Technical choice with long-term impact | ADR + DACI |
| Quick operational decision | Type 1 vs Type 2 |
| Hiring decision | Scorecard |
| Strategic direction | SWOT + Weighted Matrix |
| Conflict between options | Trade-off Matrix |
| Uncertain outcomes | Expected Value |

---

## Type 1 vs Type 2 Decisions (Amazon)

### Type 1 (One-way door)
- Irreversible or very costly to reverse
- Require careful analysis
- Should be made slowly and deliberately
- Examples: Major architecture choices, key hires, vendor commitments

### Type 2 (Two-way door)
- Reversible
- Should be made quickly
- Delegate when possible
- Examples: Feature flags, tool trials, process experiments

**Ask:** "What's the cost of reversing this decision?"

---

## DACI Framework

| Role | Person | Responsibility |
|------|--------|----------------|
| **D**river |  | Drives the decision process |
| **A**pprover |  | Makes the final call |
| **C**ontributors |  | Provide input |
| **I**nformed |  | Need to know the outcome |

Use for decisions that need clear ownership and input from multiple stakeholders.

---

## Weighted Decision Matrix

| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| Criterion 1 | x% |  |  |  |
| Criterion 2 | x% |  |  |  |
| Criterion 3 | x% |  |  |  |
| **Total** | 100% |  |  |  |

Score each option 1-5 for each criterion, multiply by weight.

---

## Expected Value Analysis

For decisions with uncertain outcomes:

```
Expected Value = (Probability of Success × Value of Success)
               - (Probability of Failure × Cost of Failure)
```

Example:
- 60% chance of $100K benefit
- 40% chance of $50K cost
- EV = (0.6 × $100K) - (0.4 × $50K) = $60K - $20K = $40K

---

## Pre-Mortem

Before committing to a decision, imagine it failed:

1. **Assume failure:** "It's 6 months later and this decision was a disaster."
2. **Generate reasons:** "What went wrong?"
3. **Address risks:** "How do we prevent these failure modes?"

Questions to ask:
- What would make this fail?
- What are we assuming that might be wrong?
- What could change that would invalidate this decision?
- What are we not seeing?

---

## Reversibility Test

Before deciding, ask:
1. Can we reverse this? At what cost?
2. Can we start small and expand?
3. Can we set a checkpoint to reassess?
4. What's the minimum commitment possible?

---

## The RAPID Framework

| Role | Description |
|------|-------------|
| **R**ecommend | Proposes a decision |
| **A**gree | Must agree for decision to proceed |
| **P**erform | Implements the decision |
| **I**nput | Consulted for input |
| **D**ecide | Makes the final call |

---

## Cognitive Bias Checklist

Before finalizing a decision, check for:

- [ ] **Confirmation bias** - Are we only looking at supporting evidence?
- [ ] **Sunk cost** - Are we continuing because of past investment?
- [ ] **Anchoring** - Are we over-weighted on the first option?
- [ ] **Availability** - Are we over-weighting recent/memorable events?
- [ ] **Groupthink** - Is everyone agreeing too easily?
- [ ] **Overconfidence** - Are our estimates realistic?

---

## Decision Documentation

Every significant decision should capture:

1. **Context** - Why we needed to decide
2. **Options** - What we considered
3. **Decision** - What we chose
4. **Rationale** - Why we chose it
5. **Consequences** - What we expect to happen
6. **Review date** - When we'll assess the outcome
