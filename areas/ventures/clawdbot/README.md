# ClawdBot (Moltbot)

**Status:** Active — Running
**Started:** January 2026

Self-hosted personal AI assistant running on dedicated Mac Mini. Uses Moltbot (formerly ClawdBot) framework with Claude as the underlying model.

## Goal

24/7 personal AI assistant accessible via messaging apps (WhatsApp, iMessage, etc.) that can execute tasks, manage calendar, control smart home, and act as a productivity multiplier.

## Current State

- ✅ Core system running (Jan 30)
- ✅ Claude Max OAuth subscription key configured
- ✅ 1Password integration (dedicated account for ClawdBot)
- ✅ Gmail integration tested and working
- 🔲 Tailscale gateway setup needs refinement

## Architecture

- **Hardware:** Mac Mini (dedicated)
- **Framework:** Moltbot (open source, MIT license)
- **Model:** Claude via Anthropic API
- **Channels:** TBD (WhatsApp, iMessage candidates)

## Resources

- [Moltbot Docs](https://docs.molt.bot/)
- [Moltbot Security Docs](https://docs.molt.bot/gateway/security)
- [GitHub: moltbot/moltbot](https://github.com/moltbot/moltbot)

## Related Files

- [Security Setup Checklist](./security-checklist.md)
