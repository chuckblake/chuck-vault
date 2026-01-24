# Dashboard Checklist

## Essential Dashboards for a CTO

### 1. Real-Time Operations
**Purpose:** Know if things are on fire right now
**Refresh:** Real-time
**Alerts:** Yes

Must include:
- [ ] System health / uptime
- [ ] Error rates
- [ ] Latency percentiles
- [ ] Active incidents
- [ ] Deployment status
- [ ] On-call status

### 2. Engineering Velocity
**Purpose:** Track delivery performance
**Refresh:** Daily
**Alerts:** Weekly threshold

Must include:
- [ ] Sprint burndown/burnup
- [ ] Deployment frequency
- [ ] Lead time trend
- [ ] PR review time
- [ ] Blocked items
- [ ] WIP limits

### 3. Quality & Reliability
**Purpose:** Track system health over time
**Refresh:** Daily
**Alerts:** Threshold-based

Must include:
- [ ] DORA metrics
- [ ] Test coverage
- [ ] Bug trends
- [ ] Incident trends
- [ ] SLA compliance
- [ ] Security scan results

### 4. Team Health
**Purpose:** Track organizational health
**Refresh:** Weekly
**Alerts:** Quarterly review

Must include:
- [ ] Headcount vs plan
- [ ] Open positions & pipeline
- [ ] Attrition data
- [ ] 1:1 completion
- [ ] Survey results
- [ ] On-call load distribution

### 5. Cost & Efficiency
**Purpose:** Track spending and efficiency
**Refresh:** Daily for infra, monthly for others
**Alerts:** Budget threshold

Must include:
- [ ] Cloud spend by service
- [ ] Cost trends
- [ ] Budget vs actual
- [ ] Cost per transaction
- [ ] Idle resource alerts

### 6. Executive/Board View
**Purpose:** High-level metrics for non-technical stakeholders
**Refresh:** Weekly/Monthly
**Alerts:** None (curated updates)

Must include:
- [ ] Uptime summary
- [ ] Key deliverables status
- [ ] Team size
- [ ] Budget status
- [ ] Key risks
- [ ] OKR progress

## Dashboard Best Practices

### Design Principles
- Most important metrics top-left
- Use consistent color coding (red/yellow/green)
- Include trend indicators
- Show targets alongside actuals
- Link to drill-down details

### Common Mistakes
- Too many metrics (aim for 5-7 per dashboard)
- Vanity metrics that don't drive action
- Missing context (what's the target?)
- No historical comparison
- Stale data without timestamps

### Questions Each Dashboard Should Answer
1. Are we on track?
2. What needs attention?
3. What changed?
4. What action should I take?

## Tool Recommendations

| Use Case | Options |
|----------|---------|
| Real-time ops | Datadog, Grafana, New Relic |
| Project tracking | Jira, Linear, Asana |
| Custom dashboards | Looker, Tableau, Metabase |
| Team health | Lattice, Culture Amp, custom |
| Cost | CloudHealth, Spot, AWS Cost Explorer |
