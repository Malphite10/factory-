# Security Policy

- All handoff packages must be validated against their JSON schema.
- Secrets must never be committed to the repository; use environment variables.
- The GitHub Supply Chain Agent is the final gatekeeper for all production-bound code.

## Network Access Control (Firewall)

The firewall system implements a whitelist-based approach for all agent activities and MCP servers:

1. **Default Allowlist**: Common package registries (npm, PyPI) and Git providers (GitHub) are allowed by default.
2. **Custom Allowlist**: Organizations can add approved domains in `config/network-policy.json`.
3. **Denylist**: Explicitly blocked domains in `config/network-policy.json` take precedence over allowlists.
4. **Pattern Matching**: Supports wildcards (e.g., `*.company.com`) for flexible policy enforcement.
5. **MCP Server Isolation**: Each MCP server is restricted to its own network allowlist as defined in its configuration.

## Secret Management

1. **Environment Variables**: Sensitive configuration must be managed via environment variables. Never hardcode secrets.
2. **Secret Scanning**: Automatic scanning of all changes for accidentally committed secrets is enforced via Gitleaks in CI.
3. **MCP Server Secrets**: MCP servers access repository secrets through environment variables injected at runtime.
