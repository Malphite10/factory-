# Review Policy

- Blocked handoffs require manual intervention and a re-run of the blocking agent.
- High-risk dependencies require a secondary manual sign-off in the `approved-sources.json`.

## Validation Pipeline

All agent-created changes must go through the following validation pipeline:

1. **CodeQL**: Static analysis for security vulnerabilities (JavaScript, Python).
2. **AI-Powered Review**: Automated code quality review for best practices.
3. **Secret Scanning**: Detection of credentials and sensitive data (Gitleaks).
4. **Dependency Checks**: Vulnerability scanning and license compliance for all new dependencies (Supply Chain Gate).
