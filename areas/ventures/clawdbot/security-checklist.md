# ClawdBot Security Setup Checklist

Last updated: 2026-01-28

**Key lessons learned:**
- Install Tailscale BEFORE applying firewall lockdowns. Get remote access working first, then harden.
- Do NOT use "Block all incoming connections" — it blocks Screen Sharing/SSH even over Tailscale. Use per-app firewall rules instead.

---

## Phase 0: Factory Reset Mac Mini

### How to Erase and Reinstall macOS

1. **Shut down** the Mac Mini
2. **Hold the power button** until you see "Loading startup options"
3. Select **Options** → Continue
4. From the menu bar: **Recovery Assistant** → **Erase Mac**
5. Confirm erase
6. After erase, select **Reinstall macOS** from Recovery
7. Follow the installer

### Alternative (if above doesn't work)
1. Boot to Recovery (hold power button → Options)
2. Open **Disk Utility**
3. Select internal drive → **Erase** (APFS format)
4. Quit Disk Utility
5. Select **Reinstall macOS**

---

## Phase 1: Basic macOS Setup (NO Lockdowns Yet)

Do these first, while the system is still "open."

### During macOS Setup
- [x] Create admin account (for system management)
- [x] Skip Apple ID sign-in for now (or use dedicated Apple Account if already created)

### After Setup - Create ClawdBot User
- [x] System Settings → Users & Groups → Add User
- [x] Create standard (non-admin) user for ClawdBot
- [x] This user will run Moltbot

### Basic Settings (No Firewall Yet)
- [x] Enable FileVault: System Settings → Privacy & Security → FileVault → Turn On
- [x] Save FileVault recovery key securely - iCould - chuck.blake@gmail.com
- [x] Disable automatic login: System Settings → Users & Groups → Automatic login: Off
- [x] Disable Guest account: System Settings → Users & Groups → Guest User → Off

**DO NOT enable firewall lockdowns yet — Tailscale first.**

---

## Phase 2: Tailscale Setup (While System is Open)

Install Tailscale BEFORE firewall lockdowns so it can set up its VPN configuration without issues.

**Note:** Install from the **admin account** — it's system-wide.

### ✅ CURRENT STATUS (Jan 30)
- Mac Mini: Tailscale installed and connected ✓
- Mac Mini Tailscale IP: `100.107.220.110`
- Mac Mini hostname: `Mac-mini`
- Mac Mini username: `chuckblake`
- MacBook: Tailscale connected ✓
- Remote access (SSH + Screen Sharing) working over Tailscale ✓
- Firewall configured ✓
- Moltbot running with Claude Max OAuth ✓
- 1Password integration (dedicated ClawdBot account) ✓
- Gmail integration tested ✓
- **TODO:** Get Tailscale gateway fully working
- **TODO:** Switch to Tailscale system daemon for headless boot (see below)

### Installation (Mac Mini) ✓ DONE
- [x] Download Tailscale from [tailscale.com/download](https://tailscale.com/download)
- [x] Install on Mac Mini
- [x] Launch Tailscale
- [x] Allow VPN configuration when prompted
- [x] Sign in with your Tailscale account
- [x] Note the Mac Mini's Tailscale IP: `100.107.220.110`

### Enable Remote Access (Mac Mini) ✓ DONE
- [x] System Settings → General → Sharing → Screen Sharing → On
- [x] System Settings → General → Sharing → Remote Login (SSH) → On
- [ ] Restrict "Allow access for" to specific users (optional)

### On Your MacBook ✓ DONE
- [x] Install Tailscale: [tailscale.com/download](https://tailscale.com/download)
- [x] Sign in with **same Tailscale account** as Mac Mini
- [x] Verify MacBook shows as connected in Tailscale

### Verify Remote Access Works (Over Tailscale) ✓ DONE
- [x] From MacBook: `ping 100.107.220.110` (should respond)
- [x] SSH: `ssh chuckblake@100.107.220.110`
- [x] Screen Sharing: Finder → Go → Connect to Server → `vnc://100.107.220.110`
- [x] **All must work before proceeding to firewall lockdowns**

### Switch to Tailscale System Daemon (For Headless Boot)

**Problem:** The App Store version only starts after user login. For true headless operation (reboot without login), you need the system daemon.

- [ ] Uninstall App Store version of Tailscale (drag to trash)
- [ ] Install via Homebrew: `brew install tailscale`
- [ ] Install system daemon: `sudo tailscaled install-system-daemon`
- [ ] Authenticate: `sudo tailscale up`
- [ ] Verify: `tailscale status`
- [ ] **Test:** Reboot Mac Mini, ping from MacBook *before* logging in on Mini

---

## Phase 3: Apply Firewall Lockdowns ✓ DONE

Only do this AFTER Tailscale remote access is verified working.

### Firewall Settings
- [x] System Settings → Network → Firewall → Turn On
- [x] Firewall Options:
  - [x] **Do NOT enable "Block all incoming connections"** — this blocks everything including Tailscale
  - [x] Enable Stealth Mode
  - [x] Ensure Screen Sharing is allowed (toggle off/on in Sharing settings if needed)
  - [x] Ensure Remote Login (SSH) is allowed
- [ ] Verify SIP enabled: `csrutil status` in Terminal

### Verify Remote Access Still Works (Over Tailscale) ✓ DONE
- [x] Screen Sharing via Tailscale IP still works
- [x] SSH via Tailscale IP still works
- [ ] Local network access is now blocked (expected — test from another device on LAN)

---

## Phase 4: Account Setup (Isolated Identity)

Create dedicated accounts for the Mac Mini — optional but recommended for isolation.

### Step 1: Create Dedicated Gmail
- [ ] Go to accounts.google.com on the Mac Mini
- [ ] Create new account (e.g., `clawdbot-mini@gmail.com`)
- [ ] If phone required: use your real number (Google won't share with Apple)
- [ ] Strong unique password → save in 1Password
- [ ] Enable 2FA (TOTP preferred over SMS)
- [ ] Save recovery codes securely

### Step 2: Set Up Google Voice
- [ ] Go to voice.google.com
- [ ] Sign in with the new Gmail
- [ ] Choose a phone number (pick your area code)
- [ ] Verify with your real phone number (one-time setup)
- [ ] Note the Google Voice number in 1Password

### Step 3: Create Dedicated Apple Account (Optional)
- [ ] Go to appleid.apple.com
- [ ] Create new account using:
  - Email: the new Gmail address
  - Phone: the Google Voice number (NOT your real number)
- [ ] Strong unique password → save in 1Password
- [ ] Enable 2FA with Google Voice number
- [ ] Save recovery key securely
- [ ] **Disable all iCloud services** — no sync, no backup

---

## Phase 5: Moltbot Installation

### Prerequisites
- [ ] Node.js >= 22 installed
- [ ] Tailscale working
- [ ] Logged in as ClawdBot user (non-admin)

### Install
```bash
npm install -g moltbot@latest
moltbot onboard --install-daemon
```

---

## Phase 6: Moltbot Security Configuration

### Run Security Audit
```bash
moltbot security audit --deep --fix
```

### File Permissions (Verify)
- [ ] `~/.moltbot/` directory: `700`
- [ ] `~/.moltbot/moltbot.json`: `600`
- [ ] All credential files: `600`

### Gateway Configuration
```json5
{
  gateway: {
    mode: "local",
    bind: "loopback",  // NEVER use 0.0.0.0 unauthenticated
    port: 18789,
    auth: {
      mode: "token",
      token: "your-long-random-token"  // Generate: moltbot doctor --generate-gateway-token
    },
    trustedProxies: ["127.0.0.1"]
  }
}
```

### Channel Security
```json5
{
  channels: {
    whatsapp: {
      dmPolicy: "pairing",  // or "allowlist" for maximum security, NEVER "open"
      groups: {
        "*": { requireMention: true }
      }
    }
  }
}
```

### Logging & Discovery
```json5
{
  logging: {
    redactSensitive: "tools"  // Prevents secrets in logs
  },
  discovery: {
    mdns: { mode: "minimal" }  // Reduces broadcast exposure
  }
}
```

---

## Phase 7: Sandbox Configuration (For Untrusted Contexts)

For group chats or less trusted channels, use Docker isolation:

```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main"  // Groups run in Docker, DMs stay on-host
      }
    }
  }
}
```

---

## Security Warnings

### Known Risks (January 2026)
- Exposed control panels found in the wild with no auth — API keys and conversations leaked
- Prompt injection attacks possible, especially with smaller/quantized models
- mDNS broadcasts operational details by default

### Critical Don'ts
- **Never** bind gateway to `0.0.0.0` without authentication
- **Never** use `dmPolicy: "open"`
- **Never** run on a machine with crypto wallets or sensitive credentials
- **Never** expose browser relay ports over LAN or public internet
- **Avoid** smaller/quantized models — more vulnerable to prompt injection

### Model Selection
Use large, instruction-hardened models (Claude Opus, Sonnet) for any bot with tool access.

---

## If Compromise Suspected

1. Rotate gateway token (`CLAWDBOT_GATEWAY_PASSWORD`)
2. Restart Gateway
3. Rotate all provider credentials (WhatsApp, Slack, API keys)
4. Revoke suspicious node pairings
5. Review session transcripts for unauthorized actions

---

## References

- [Moltbot Security Docs](https://docs.molt.bot/gateway/security)
- [Moltbot FAQ](https://docs.molt.bot/help/faq)
- [The Register: Security Concerns](https://www.theregister.com/2026/01/27/clawdbot_moltbot_security_concerns/)
- [drduh/macOS-Security-and-Privacy-Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide)
- [Apple Mac Mini Security Features](https://support.apple.com/guide/mac-mini/security-features-apdcf567823b/mac)
