# Multi-Agent Deterministic Handoff System

**Core Principle**: Every agent communicates only through structured handoff packages. No exceptions. No human-readable prose in agent outputs.

## Repository Structure

```
agents/
├── schemas/           # JSON schemas for all handoff packages
├── 00-creative-director.md
├── 01-research.md
├── 02-product.md
├── 03-design.md
├── 04-content.md
├── 05-github-supply-chain.md
├── 06-builder.md
├── 07-integration.md
├── 08-qa.md
├── 09-email.md
└── 10-launch.md

.github/workflows/
├── 01-research-pipeline.yml
├── 02-product-spec-validation.yml
├── 03-design-package-approval.yml
├── 05-github-supply-chain-gate.yml
├── 06-builder-stage.yml
└── 08-qa-sign-off.yml

.env.example          # Template for required environment variables
README.md             # Setup and usage documentation
```

## Critical Rules (Enforce in Every Agent)

Every `.md` file must include:

```
You do not communicate with humans.

You communicate only through structured handoff packages.

You may not skip required fields.

You may not modify upstream packages.

You may only consume approved inputs.

If required information is missing, return BLOCKED.
```

## Execution Flow

1. **Creative Director** → Opportunity Report
2. **Research** → Research Package
3. **Product** → Product Spec
4. **Design** → Design Package
5. **GitHub Supply Chain** ← Validates all dependencies
   - ✓ Approved → Passes to Builder
   - ✗ Issues → Returns to Design with BLOCKED status
6. **Builder** → Build Package
7. **Integration** → Integration Package
8. **QA** → QA Sign-Off
9. **Email** → Campaign Package (parallel to QA)
10. **Launch** → Launch Package

## Handoff Package Structure (Universal)

Every agent output follows this structure:

```json
{
  "agent": "agent-name",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z",
  "inputs": {
    "upstream_agent": "agent-name",
    "package_version": "1.0.0",
    "validated": true
  },
  "tasks": [
    "task 1 completed",
    "task 2 completed"
  ],
  "outputs": {
    "primary_deliverable": "...",
    "metadata": {}
  },
  "handoff": {
    "next_agent": "agent-name",
    "required_approvals": [],
    "sla": "4 hours",
    "package_version": "1.0.0"
  },
  "blockers": []
}
```

## Source Policy (Builder Agent Enforces)

**Approved Sources**:
- Internal design system
- Approved GitHub package list (validated by GitHub Supply Chain)
- Approved asset library
- Approved CMS schema

**Forbidden**:
- Random npm packages
- Unreviewed GitHub repositories
- CDN imports (unvetted)
- Unpinned dependencies
- Unverified Framer plugins
- Unauthorized Wix extensions

## Success Metrics

1. **Zero agent communication errors** - all handoffs pass validation
2. **Zero supply chain surprises** - no production incidents from missing dependency review
3. **Deterministic deployment** - same input → same output every time
4. **Audit trail** - every decision logged with reasoning

---

**Next**: Start with `/agents/README.md` for agent-by-agent documentation.
