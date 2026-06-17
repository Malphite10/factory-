# Quick Start Guide

Your multi-agent deterministic handoff system is ready to deploy.

## What You Have

A production-grade multi-agent orchestration framework with:

- ✓ **GitHub Supply Chain Agent** as the critical gatekeeper (prevents supply-chain attacks)
- ✓ **Deterministic handoffs** (same input → same output every time)
- ✓ **Immutable upstream packages** (agents can't mutate what they receive)
- ✓ **Fail-fast blocking** (workflow stops immediately if data is missing)
- ✓ **Complete audit trail** (every decision logged and traceable)
- ✓ **JSON schema validation** (all handoffs validated against strict schemas)
- ✓ **GitHub Actions workflows** (ready to deploy to GitHub)

## File Manifest

```
multi-agent-system/
├── README.md                          ← START HERE
├── MANIFESTO.md                       ← Philosophy & architecture
├── ARCHITECTURE.md                    ← System overview
├── QUICKSTART.md                      ← This file
├── package.json                       ← Dependencies & npm scripts
├── .env.example                       ← Configuration template
├── .gitignore                         ← Git configuration
│
├── agents/
│   ├── 03-design.md                  ← Design Agent spec
│   ├── 05-github-supply-chain.md     ← GitHub gatekeeper (critical)
│   ├── 06-builder.md                 ← Builder Agent spec
│   └── schemas/
│       └── handoff-schemas.json      ← JSON schemas for all handoffs
│
└── .github/workflows/
    └── 05-github-supply-chain-gate.yml ← Critical workflow
```

## The Key Innovation: GitHub Supply Chain Agent

This agent is the single point of control that prevents:
- ❌ Unknown dependencies reaching production
- ❌ Security vulnerabilities from abandoned packages
- ❌ License conflicts
- ❌ Supply-chain attacks

**No code reaches Builder without GitHub Supply Chain approval.**

## Getting Started (5 Steps)

### 1. Initialize Repository

```bash
cd multi-agent-system
git init
git add .
git commit -m "Initial multi-agent system setup"
git remote add origin https://github.com/YOUR_ORG/YOUR_REPO.git
git push -u origin main
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your:
#   - GITHUB_TOKEN
#   - SNYK_TOKEN
#   - Slack webhook
#   - API keys
```

### 4. Validate Schema

```bash
npm run validate-schemas
```

This verifies:
- All JSON schemas are valid
- All agent markdown files have required rules
- No configuration errors

### 5. Test Workflow

```bash
npm run test-workflow -- agents/03-design.md < sample-input.json
```

Output: Handoff package (JSON) with all required fields.

## How It Works (The Flow)

```
Design Agent
  ↓ (Design Package + Dependencies Declared)
GitHub Supply Chain Agent ← CRITICAL GATE
  ├─ Validates all dependencies
  ├─ Runs security audit
  ├─ Checks licenses
  ├─ Pins versions
  ├─ Generates SBOM
  └─ Approves or BLOCKS
    ↓ (GitHub Package: approved)
Builder Agent
  ├─ Checks source policy (only approved sources)
  ├─ Builds code
  ├─ Generates artifacts
  └─ Emits Build Package
    ↓ (to Integration, QA, Launch)
```

## The Core Rule

Every agent outputs this structure:

```json
{
  "agent": "agent-name",
  "inputs": { "upstream_package": {...}, "validated": true },
  "tasks": ["task 1", "task 2"],
  "outputs": { "deliverable": "..." },
  "handoff": { "next_agent": "..." },
  "blockers": []
}
```

If `blockers` is non-empty, workflow stops.

## Critical Files to Update

1. **config/approved-sources.json** — List of all approved packages (doesn't exist yet, you create it)
   ```json
   {
     "npm_packages": [
       "react@18.2.0",
       "@shadcn/ui@0.8.1"
     ]
   }
   ```

2. **.env** — Your API keys and configuration

3. **agents/** — Add more agent specs for your workflow (01-research, 02-product, etc.)

## Deployment to GitHub

1. Push to GitHub
2. Go to repository settings → Actions → Enable workflows
3. GitHub Actions will run on:
   - Pull requests (design package submitted)
   - Manual trigger (for testing)
4. Workflow validates design → GitHub Supply Chain → Build → Deploy

## Success Indicators

After first workflow run:

- ✓ All agents complete without BLOCKED status
- ✓ GitHub Supply Chain shows `approved: true`
- ✓ Build artifacts generated
- ✓ Audit trail logged
- ✓ Handoff packages validated

## Common Next Steps

1. **Add more agents** — Create 01-research.md, 02-product.md, etc.
2. **Integrate with Figma** — Design Agent queries Figma API for component specs
3. **Integrate with GitHub** — Builder Agent pushes to GitHub, creates PRs
4. **Set up monitoring** — Track workflow times, blockers, success rate
5. **Configure notifications** — Slack alerts when workflows complete/block

## Troubleshooting

### "npm run validate-schemas fails"

Check that all JSON files are valid JSON (use a linter).

### "GitHub Actions workflow not running"

- Verify `.github/workflows/` has the `.yml` file
- Enable Actions in repository settings
- Check branch name matches workflow trigger

### "SNYK_TOKEN not set"

Optional. GitHub Supply Chain agent skips SNYK if not configured (still runs npm audit).

## Success Story

**Scenario**: Your team adds a design dependency on an experimental package. GitHub Supply Chain Agent validates, finds security issues, BLOCKS workflow with specific action: "Package has unresolved CVE, remove or request approval."

Design Agent removes it → GitHub agent approves → Builder proceeds. **Zero issues in production.**

Without this system? The package gets installed, security vulnerability ships, compliance violation later.

## Next: Read These Files

1. **README.md** — Full documentation
2. **MANIFESTO.md** — Philosophy and architecture
3. **agents/05-github-supply-chain.md** — How the critical gatekeeper works
4. **agents/06-builder.md** — How Builder enforces source policy

## Questions?

Each agent markdown file documents its role, responsibilities, and exact output format.

The JSON schemas (agents/schemas/handoff-schemas.json) are the source of truth for all handoff structure.

GitHub Actions workflow (05-github-supply-chain-gate.yml) shows how to implement the gatekeeper in CI/CD.

---

**You're ready. Build secure, deterministic, audit-friendly systems.**
