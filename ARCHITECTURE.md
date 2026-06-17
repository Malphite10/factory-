# Multi-Agent Deterministic Handoff System Architecture

**Core Principle**: Every agent communicates only through structured handoff packages. No human-readable prose in agent outputs. Production is secure by construction.

## Repository Structure

```
agents/
├── schemas/           # JSON schemas for all handoff packages
├── 00-creative-director.md
├── ...
└── 10-launch.md

governance/            # Policies for dependencies, security, and naming
evaluators/            # Evaluation templates for agent outputs
memory/
├── knowledge/         # Relationship graphs and learned patterns
└── marketplace/       # Intelligence data for design components

adding-ai-design-components-marketplace/ # Integration guides
ai-data-engineering/   # Data pipeline structures
code-documenter/       # Documentation patterns
writing-github-actions/ # CI/CD best practices

.github/workflows/
└── 05-github-supply-chain-gate.yml # Critical gatekeeper logic

config/                # Registry of approved sources and schemas
scripts/               # Validation and auditing tools
release/               # Checklists and changelog templates
```

## Critical Rules

Every agent must follow these non-negotiable rules:
1. You do not communicate with humans.
2. You communicate only through structured handoff packages.
3. You may not skip required fields.
4. You may not modify upstream packages.
5. You may only consume approved inputs.
6. If required information is missing, return BLOCKED.

## Deterministic Handoff Flow

1. **Creative Director** → Opportunity Report
2. **Research** → Research Package
3. **Product** → Product Spec
4. **Design** → Design Package
5. **GitHub Supply Chain** (Gatekeeper) ← Validates all dependencies
6. **Builder** → Build Package
7. **Integration** → Integration Package
8. **QA** → QA Sign-Off
9. **Email** → Campaign Package
10. **Launch** → Launch Package

## Success Metrics

- **Zero supply-chain incidents**: All dependencies validated by the GitHub Supply Chain Agent.
- **100% Audit Traceability**: Every decision logged with reasoning and timestamped.
- **Deterministic Deployment**: Same input → same output, guaranteed.
