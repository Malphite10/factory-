# Multi-Agent Deterministic Handoff System Architecture

**Core Principle**: Every agent communicates only through structured handoff packages. No human-readable prose in agent outputs. Production is secure by construction.

## Repository Structure

```
agents/
├── _shared/           # Mandatory Agent Communication Contract
├── XX-agent-name/     # Individual Agent Directories
│   ├── agent.md       # Agent definition and rules
│   └── skill.md       # Agent capabilities and output formats
└── schemas/           # JSON schemas for all handoff packages

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

## Agent Pipeline

1. **00-creative-director**: Vision and Strategy.
2. **01-research**: Market Intelligence.
3. **02-product**: IA and Feature Specs.
4. **03-design**: Design Systems and Tokens.
5. **04-content**: High-converting Copy and SEO.
6. **05-github-supply-chain**: Security and Dependency Gatekeeper.
7. **06-builder**: Implementation and Build Artifacts.
8. **07-integration**: API and Service Connectivity.
9. **08-qa**: Final Quality Gate and Validation.
10. **09-email**: Lifecycle Communication Assets.
11. **10-launch**: Marketplace Distribution and Release.

## Critical Rules (Defined in `agents/_shared/agent-contract.md`)

1. You do not communicate with humans.
2. You communicate only through structured handoff packages.
3. You may not skip required fields.
4. You may not modify upstream packages.
5. You may only consume approved inputs.
6. If required information is missing, return BLOCKED.
