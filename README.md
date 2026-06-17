# Multi-Agent Deterministic Handoff System

Production-grade multi-agent workflow orchestration for product development. Every agent communicates through structured handoff packages. Zero human-readable prose. Zero ambiguity.

## Core Philosophy

**Problem**: Multi-agent systems fail when agents communicate ambiguously, skip fields, or make implicit assumptions.

**Solution**: 
1. Every agent outputs the same structure: `INPUTS | TASKS | OUTPUTS | HANDOFF | BLOCKERS`
2. Every handoff is validated against a strict JSON schema
3. Agents cannot modify upstream packages (immutable)
4. If required information is missing, agent returns `BLOCKED` (stops workflow)
5. The GitHub Supply Chain Agent is the critical gatekeeper — nothing reaches production without explicit supply-chain validation

## System Architecture

```
Creative Director
    ↓ (Opportunity Report)
Research Agent
    ↓ (Research Package)
Product Agent
    ↓ (Product Spec)
Design Agent
    ↓ (Design Package)
    ↓ + Dependencies declared
GitHub Supply Chain ← CRITICAL GATEKEEPER
    ↓ (GitHub Approval)
    ├─ Security audit
    ├─ License validation
    ├─ Maintenance scoring
    ├─ SBOM generation
    └─ Version pinning
    ↓ (GitHub Package: approved or BLOCKED)
Builder Agent
    ↓ (Build Package)
Integration Agent
    ↓ (Integration Package)
QA Agent (parallel with Email Agent)
    ↓ (QA Sign-Off)
Launch Agent
    ↓ (Live + Monitoring)
```

## The GitHub Supply Chain Agent: Why It Matters

The GitHub Supply Chain Agent is the single point of control that prevents:
- ❌ Unknown dependencies sneaking into production
- ❌ Security vulnerabilities from abandoned packages
- ❌ License conflicts
- ❌ Bundle bloat from unused packages
- ❌ Supply-chain attacks via malicious dependencies
- ❌ Dependency hell from unpinned versions

**No code, component, or SDK reaches Builder without GitHub Supply Chain approval.**

## Repository Structure

```
agents/
├── schemas/
│   ├── opportunity-report.json
│   ├── research-package.json
│   ├── product-spec.json
│   ├── design-package.json
│   ├── github-package.json
│   ├── build-package.json
│   └── launch-package.json
│
├── 00-creative-director.md
├── 01-research.md
├── 02-product.md
├── 03-design.md
├── 04-content.md
├── 05-github-supply-chain.md (CRITICAL)
├── 06-builder.md
├── 07-integration.md
├── 08-qa.md
├── 09-email.md
└── 10-launch.md

.github/workflows/
├── 01-research-pipeline.yml
├── 02-product-spec-validation.yml
├── 03-design-package-approval.yml
├── 05-github-supply-chain-gate.yml (CRITICAL)
├── 06-builder-stage.yml
└── 08-qa-sign-off.yml

config/
├── approved-sources.json (registry of all allowed packages)
├── design-system-versions.json
└── cms-schemas.json

.env.example
.gitignore
package.json
README.md (this file)
```

## Handoff Package Structure (Universal)

Every agent, regardless of role, outputs this JSON structure:

```json
{
  "agent": "agent-name",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z",
  
  "inputs": {
    "upstream_package": { "...": "..." },
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
    "next_agent": "next-agent-name",
    "required_approvals": [],
    "sla": "4 hours"
  },
  
  "blockers": [
    { "issue": "...", "action": "..." }
  ]
}
```

If `blockers` is non-empty, the workflow stops. Next agent cannot proceed until issues are resolved upstream.

## Quick Start

### 1. Install

```bash
git clone https://github.com/org/multi-agent-system.git
cd multi-agent-system
npm install

# Copy environment template
cp .env.example .env
# Edit .env with your API keys, GitHub tokens, etc.
```

### 2. Validate Schema

```bash
npm run validate-schemas
```

This checks:
- All JSON schemas are valid
- All agent markdown files declare required rules
- All handoff packages conform to schema

### 3. Run a Workflow

```bash
# Trigger via GitHub webhook (on PR or manual trigger)
# Or run locally:
npm run test-workflow -- agents/03-design.md < sample-input.json

# The output will be a JSON handoff package
```

### 4. Deploy

```bash
# Validate all sources before deploying
npm run validate-sources

# Build
npm run build

# Deploy (CI/CD pipelines defined in .github/workflows/)
npm run deploy
```

## The Critical Rules

Every agent markdown file MUST include this exact text:

```
You do not communicate with humans.

You communicate only through structured handoff packages.

You may not skip required fields.

You may not modify upstream packages.

You may only consume approved inputs.

If required information is missing, return BLOCKED.
```

These rules are non-negotiable. They enforce determinism.

## Approved Sources Registry

Maintain a single source of truth for all approved packages:

```json
{
  "npm_packages": [
    "react@18.2.0",
    "@shadcn/ui@0.8.1",
    "framer-motion@10.16.4"
  ],
  "github_repositories": [
    "owner/design-system#v1.2.0"
  ],
  "framer_plugins": [
    "framer-plugin-uuid-123"
  ],
  "wix_extensions": [
    "wix-extension-id-456"
  ],
  "excluded_forever": [
    "random-experimental-lib"
  ]
}
```

**Why this matters**: Builder Agent validates every dependency against this list. Anything not approved → BLOCKED.

## GitHub Actions Workflows

### `05-github-supply-chain-gate.yml` (Critical)

Runs when Design Package is submitted:

1. Parse design dependencies
2. Run security audit (npm audit, SNYK)
3. Check maintenance score (commits, releases)
4. Verify version pinning
5. Generate SBOM
6. Validate license compatibility
7. Approve or BLOCK

**If BLOCKED**: Workflow stops. Returns to Design Agent with specific action items.

**If APPROVED**: Emits GitHub Package handoff. Builder Agent can proceed.

### `06-builder-stage.yml`

Runs when GitHub Package is approved:

1. Parse GitHub Package
2. Validate source policy (only approved sources)
3. Install dependencies (pinned versions from lockfile)
4. Build
5. Run tests
6. Generate build artifacts
7. Emit Build Package handoff

**Source Policy Check** (non-negotiable):

```javascript
const approved = require('./config/approved-sources.json');
const pkg = require('./package.json');

for (const [name, version] of Object.entries(pkg.dependencies)) {
  const entry = `${name}@${version}`;
  if (!approved.npm_packages.includes(entry)) {
    throw new Error(`BLOCKED: ${entry} not in approved list`);
  }
}
```

## Validation & Testing

### Run Schema Validation

```bash
npm run validate-schemas
```

Checks:
- All schemas are valid JSON Schema v7
- No required fields are missing
- All agent markdown files include the critical rules

### Validate Handoff Package

```bash
npm run validate-handoff -- <output-file.json>
```

Checks:
- All required fields present
- All values conform to schema
- No upstream package modification detected
- Agent name is valid

### Audit Approved Sources

```bash
npm run audit-approved-sources
```

Runs:
- npm audit on all approved packages
- SNYK scan
- License check
- Maintenance scoring

## Operational Runbook

### When a Workflow is BLOCKED

1. **Identify the blocker**: Check the `blockers` array in the handoff package
2. **Root cause**: Each blocker includes `issue`, `requirement`, and `action`
3. **Resolution**: Take action as specified (usually re-run upstream agent)
4. **Re-validate**: Run validation script again
5. **Re-submit**: Previous agent re-emits handoff package
6. **Proceed**: Next agent resumes workflow

### Example: BLOCKED by GitHub Supply Chain

```json
{
  "blockers": [
    {
      "package": "some-experimental-lib",
      "reason": "Not in APPROVED_SOURCES registry",
      "requirement": "Remove dependency or request approval review",
      "action": "Contact security team for review, or remove from design package"
    }
  ]
}
```

**What happens**: Design Agent must either:
- Remove the dependency from Figma/design package, OR
- Request formal review (creates GitHub issue for security team)

Once resolved, Design Agent re-submits package.

### Deployment Checklist

Before deploying to production:

- [ ] All workflows completed without BLOCKED status
- [ ] Build artifacts validated (bundle size, performance)
- [ ] QA sign-off obtained
- [ ] Email campaign approved (if applicable)
- [ ] Rollback procedure documented
- [ ] Monitoring dashboards ready
- [ ] Health checks passing

## Monitoring & Observability

Each handoff package includes:
- `timestamp`: When agent completed its work
- `tasks`: What was done
- `blockers`: If any issues arose

Aggregate these across the entire workflow to get:
- Total time from Creative Director → Launch
- Bottleneck identification (which agent takes longest)
- Blocker frequency (which agent most likely to BLOCK)
- Success rate (% of workflows that complete vs. BLOCKED)

### Success Metrics

- ✓ **Zero supply-chain incidents**: No unknown dependencies in production
- ✓ **Deterministic deployment**: Same input → same output every time
- ✓ **100% audit traceability**: Every decision logged with reasoning
- ✓ **No rework**: Workflows complete on first attempt (no re-runs due to mistakes)

## Troubleshooting

### "Agent returned BLOCKED"

Check the `blockers` array for the specific issue. Common causes:

- **GitHub Supply Chain**: Unapproved dependency → Request review or remove
- **Builder**: Source policy violation → Ensure all dependencies are approved
- **QA**: Test failure → Fix bug and re-run Builder
- **Design**: Accessibility issue → Fix in Figma and re-export

### "Workflow stuck in pending"

Check GitHub Actions logs for:
- API rate limiting
- Missing environment variables
- Network connectivity issues

### "Dependency version mismatch"

Cause: Package.json has unpinned version (uses `^` or `*`).

Fix: Pin exact version in lockfile. Regenerate lockfile and commit.

## Success Stories

**Scenario 1**: Design Agent declares dependency on experimental lib. GitHub Supply Chain validates, finds it's abandoned. BLOCKED. Design Agent removes it. Workflow resumes. Zero issues in production.

**Scenario 2**: Builder Agent attempts to use unreviewed npm package. Source policy validation fails. BLOCKED. Build fails to start. Design must re-request approval through proper channel.

**Scenario 3**: All agents complete without blockers. Code deploys to production with complete audit trail. Six months later, security audit is trivial — every decision is documented.

## Contributing

When adding a new agent:

1. Create `NN-agent-name.md` in `agents/` directory
2. Include the critical rules at the top
3. Define input schema in `agents/schemas/`
4. Create corresponding GitHub Actions workflow in `.github/workflows/`
5. Update `approved-sources.json` with any new dependencies
6. Run validation: `npm run validate-schemas`
7. Test with sample input: `npm run test-workflow -- agents/NN-agent-name.md < sample.json`
8.

## License & Support

This repository is the single source of truth for all multi-agent workflows. Questions? Check the agent markdown files — they document everything.

CO-Auth--https://github.com/Malphite10/factory-.git
---

**The key insight**: When agents can only communicate through immutable, validated handoff packages, failures are caught early, workflows are deterministic, and production is secure by construction.
