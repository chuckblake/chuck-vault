# Moltbot Setup

Configuration and setup tasks for ClawdBot's Moltbot instance.

---

## Installation Status

- [ ] Node.js >= 22 installed
- [ ] Moltbot installed (`npm install -g moltbot@latest`)
- [ ] Onboarding complete (`moltbot onboard --install-daemon`)
- [ ] Claude API key configured (from console.anthropic.com)

---

## Post-Install Configuration

### Memory & Session Settings

Enable memory flush before compaction and session memory search:

```json5
{
  compaction: {
    memoryFlush: {
      enabled: true
    }
  },
  memorySearch: {
    experimental: {
      sessionMemory: true
    },
    sources: ["memory", "sessions"]
  }
}
```

Or via CLI:
```bash
# Enable memory flush before compaction
# Enable session memory search with memory + sessions sources
moltbot config set compaction.memoryFlush.enabled true
moltbot config set memorySearch.experimental.sessionMemory true
moltbot config set memorySearch.sources '["memory", "sessions"]'
```

### Multi-Model Routing (Planned)

Goal: Use Claude Sonnet for external messages, local Ollama for trusted coding tasks.

- [ ] Configure default agent to use Claude Sonnet
- [ ] Set up explicit trigger (e.g., `/code`) to route to local Ollama
- [ ] Ensure external inputs never hit the local model directly

---

## Security Config

See `security-checklist.md` for full security configuration (gateway, channels, logging, sandbox).

### Key Settings to Apply

- [ ] Gateway: bind to loopback only, token auth
- [ ] Channels: `dmPolicy: "pairing"`, groups require mention
- [ ] Logging: `redactSensitive: "tools"`
- [ ] Discovery: `mdns: { mode: "minimal" }`
- [ ] **Enable sandboxing** — run untrusted contexts in Docker isolation
- [ ] **Enable whitelist** for incoming commands — restrict who can send commands
- [ ] **Run security audit** after install:
  ```bash
  moltbot security audit --deep --fix
  ```

### Nightly Security Patrol

Set up automated nightly security check (runs at 11 PM):

1. **Web search** — looks for new ClawdBot vulnerabilities, exposed gateways, CVEs
2. **GitHub check** — scans clawdbot/clawdbot for security-related issues/commits
3. **Local audit** — runs `clawdbot security audit --deep`
4. **Action based on severity:**
   - Critical: patches immediately + urgent alert
   - Moderate: proposes fix + explains risk
   - All clear: quick summary

Report delivered via Telegram.

---

## Notes

- Use Claude API (not Claude Code) to avoid ToS issues
- Smaller local models are vulnerable to prompt injection — only use for trusted inputs
