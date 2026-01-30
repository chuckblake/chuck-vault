# 1Password Skill

Access secrets from 1Password vaults using the `op` CLI.

## Setup

- CLI location: `~/.local/bin/op`
- Token stored in: `~/.clawdbot/.env` as `OP_SERVICE_ACCOUNT_TOKEN`

## Running Commands

Source the token before running op commands:

```bash
export OP_SERVICE_ACCOUNT_TOKEN=$(grep OP_SERVICE_ACCOUNT_TOKEN ~/.clawdbot/.env | cut -d'=' -f2-) && ~/.local/bin/op <command>
```

Or use this shorthand pattern in scripts:
```bash
OP=$(grep OP_SERVICE_ACCOUNT_TOKEN ~/.clawdbot/.env | cut -d'=' -f2-) ~/.local/bin/op <command>
```

## Common Commands

```bash
# List vaults
~/.local/bin/op vault list

# List items in a vault
~/.local/bin/op item list --vault "Vault Name"

# Get a specific item
~/.local/bin/op item get "Item Name" --vault "Vault Name"

# Get a specific field (e.g., password)
~/.local/bin/op item get "Item Name" --fields password --vault "Vault Name"

# Get username and password
~/.local/bin/op item get "Item Name" --fields username,password --vault "Vault Name"

# Read a secret reference (op:// URI)
~/.local/bin/op read "op://Vault/Item/Field"
```

## Secret References

Use `op://` URIs for direct field access:
- `op://Vault/Item/username`
- `op://Vault/Item/password`
- `op://Vault/Item/Section/Field`

## Notes

- Service account tokens are scoped to specific vaults
- Token must be set in environment before commands work
- Use `--format json` for programmatic parsing
