# Multi-Agent Deterministic Handoff System
## Implementation Manifesto & Architectural Guide

---

## The Problem We're Solving

Multi-agent AI systems fail because:

1. **Ambiguous Communication**: Agents send natural language that humans can interpret, but other agents cannot
2. **Missing Requirements**: Agents skip optional fields, creating gaps downstream
3. **Upstream Mutations**: Agents modify packages they receive, breaking determinism
4. **Silent Failures**: Agents proceed even when critical data is missing
5. **Supply Chain Blindness**: No visibility into what code/components/dependencies are actually being used

**Result**: Broken workflows, security vulnerabilities, compliance failures, and zero audit trail.

---

## The Solution

### Core Principle 1: Deterministic Handoffs

Every agent outputs ONE structure:

```
INPUTS | TASKS | OUTPUTS | HANDOFF | BLOCKERS
```

That's it. No variations. No special cases. This structure must validate against a strict JSON schema or the workflow stops.

### Core Principle 2: Immutable Upstream Packages

An agent CANNOT modify what it receives. If the upstream package is incomplete or wrong, the agent returns `BLOCKED` instead of guessing.

### Core Principle 3: The GitHub Supply Chain Agent as Gatekeeper

Before ANY code reaches Builder:
- All dependencies are validated
- All versions are pinned
- All licenses are checked
- All security issues are scanned
- SBOM is generated for audit

**Nothing bypasses this gate. Ever.**

### Core Principle 4: Fail Fast, Fail Loudly

If an agent is missing required information, it returns `BLOCKED`. This stops the workflow immediately, preventing downstream chaos.

### Core Principle 5: Complete Audit Trail

Every decision is timestamped, logged, and traceable. Six months later, you can answer: "Who approved this? When? Why?"

---

## System Architecture

```
INPUT: Creative Brief
  ↓
Creative Director Agent
  Outputs: Opportunity Report
  Validates: ✓ Brief is complete
  ├─ If valid → Emits handoff package
  └─ If invalid → Returns BLOCKED
  ↓
Research Agent
  Inputs: Opportunity Report (immutable)
  Outputs: Research Package
  Validates: ✓ Market data complete
  ├─ If valid → Emits handoff package
  └─ If invalid → Returns BLOCKED
  ↓
Product Agent
  Inputs: Opportunity Report + Research Package (both immutable)
  Outputs: Product Spec
  Validates: ✓ Spec aligned with brief + research
  ├─ If valid → Emits handoff package
  └─ If invalid → Returns BLOCKED
  ↓
Design Agent
  Inputs: Product Spec (immutable)
  Outputs: Design Package + Dependencies Declared
  Validates: ✓ Design system compliance
               ✓ Accessibility (WCAG 2.1 AA)
               ✓ All dependencies declared
  ├─ If valid → Emits handoff package
  └─ If invalid → Returns BLOCKED
  ↓
GitHub Supply Chain Agent ← CRITICAL GATEKEEPER
  Inputs: Design Package + Dependencies List (immutable)
  Validates: ✓ All dependencies in approved list
             ✓ All versions pinned
             ✓ Security score ≥ 90
             ✓ No high/critical CVEs
             ✓ Licenses compatible
             ✓ Maintenance score ≥ 75
  Outputs: GitHub Package (approved or BLOCKED)
  ├─ If approved → Emits handoff package
  └─ If issues → Returns BLOCKED + specific actions
  ↓
Builder Agent
  Inputs: Design Package + GitHub Approval (both immutable)
  Output Policy: ✓ Only use approved sources
                 ✓ All versions from GitHub approval
                 ✓ No random packages
                 ✓ Validate source policy before build
  Outputs: Build Package (source code, artifacts)
  ├─ If valid → Emits handoff package
  └─ If invalid → Returns BLOCKED
  ↓
Integration Agent
  Inputs: Build Package (immutable)
  Outputs: Integration Package (APIs, services wired)
  ├─ If valid → Emits handoff package
  └─ If invalid → Returns BLOCKED
  ↓
QA Agent & Email Agent (parallel)
  QA: Tests, validates, sign-off
  Email: Campaign messaging, scheduling
  ├─ If both valid → Emit handoff packages
  └─ If either blocked → Workflow stops
  ↓
Launch Agent
  Inputs: Build Package + QA Sign-Off + Email Campaign (all immutable)
  Outputs: Launch Package (live URL, monitoring, release notes)
  ├─ If valid → DEPLOYMENT
  └─ If invalid → Returns BLOCKED

OUTPUT: Live product + Complete audit trail
```

---

## The GitHub Supply Chain Agent: Why It's the Linchpin

**Without it**: Developers pull random npm packages. Security team has no visibility. Malicious dependency gets installed. Production is compromised.

**With it**: Every dependency is validated, versioned, scanned, and approved. Builder Agent can't deviate. Supply chain is secure by construction.

### What GitHub Supply Chain Agent Does

1. **Dependency Review**
   - Parse all npm packages, GitHub repos, Framer plugins, Wix apps from Design package
   - Check each against `approved-sources.json`
   - If not approved → BLOCKED

2. **Security Scan**
   - `npm audit` for vulnerability database
   - SNYK integration for CVE detection
   - Fail if score < 90 (unless explicitly waived)

3. **License Validation**
   - Ensure all licenses are permissive (MIT, Apache 2.0, etc.)
   - Fail if GPL or unknown license

4. **Maintenance Check**
   - Last commit date (< 6 months = active)
   - Issue response time
   - Release frequency
   - Fail if abandoned (no activity for > 1 year)

5. **Version Pinning**
   - Require exact SemVer (e.g., "18.2.0", not "^18.0.0")
   - Fail if unpinned

6. **SBOM Generation**
   - Create Software Bill of Materials in SPDX format
   - For compliance, audit, and legal review

7. **Approval Decision**
   - If all checks pass → Emit GitHub Package (approved)
   - If any checks fail → Emit GitHub Package (BLOCKED) with specific actions

---

## Handoff Package Structure (Universal)

Every agent outputs this JSON, NO EXCEPTIONS:

```json
{
  "agent": "agent-name",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z",

  "inputs": {
    "upstream_package": {
      "agent": "previous-agent",
      "version": "1.0.0"
    },
    "validated": true
  },

  "tasks": [
    "task 1 completed",
    "task 2 completed",
    "task 3 completed"
  ],

  "outputs": {
    "primary_deliverable": "...",
    "secondary_deliverable": "...",
    "metadata": {}
  },

  "handoff": {
    "next_agent": "next-agent-name",
    "required_approvals": [],
    "sla": "4 hours"
  },

  "blockers": [
    {
      "issue": "Specific problem",
      "requirement": "What needs to happen",
      "action": "How to resolve"
    }
  ]
}
```

### Validation Rules

- ✓ `agent` must be in the registry (00-creative-director, 01-research, etc.)
- ✓ `version` must be SemVer
- ✓ `timestamp` must be ISO 8601
- ✓ `inputs.upstream_package` must match previous agent's output (immutable)
- ✓ `tasks` array must have at least 1 item
- ✓ `outputs` must include all required fields for this agent
- ✓ `handoff.next_agent` must be valid
- ✓ If `blockers` is non-empty, workflow STOPS
- ✗ Any deviation from this structure → Validation fails → Workflow stops

---

## Approved Sources Registry

File: `config/approved-sources.json`

```json
{
  "npm_packages": [
    "react@18.2.0",
    "@shadcn/ui@0.8.1",
    "framer-motion@10.16.4",
    "next@14.0.1",
    "typescript@5.3.2"
  ],
  
  "github_repositories": [
    "owner/design-system#v1.2.0",
    "owner/icon-library#main"
  ],
  
  "framer_plugins": [
    "framer-plugin-id-123"
  ],
  
  "wix_extensions": [
    "wix-ext-456"
  ],
  
  "asset_libraries": [
    "https://cdn.jsdelivr.net/npm/icons@1.0.0"
  ],
  
  "excluded_forever": [
    "sketchy-lib",
    "known-malware"
  ]
}
```

**How it works**: Builder Agent validates every dependency against this list. Anything not listed → BLOCKED.

---

## Source Policy (Builder Agent Enforces)

```javascript
// Before every build
const APPROVED = require('./config/approved-sources.json');
const PKG = require('./package.json');

for (const [name, version] of Object.entries(PKG.dependencies)) {
  const entry = `${name}@${version}`;
  if (!APPROVED.npm_packages.includes(entry)) {
    throw new Error(`BLOCKED: ${entry} not in approved list`);
  }
}

// If any dependency fails this check, build stops.
// Builder cannot proceed without re-requesting approval.
```

---

## Deployment Checklist

Before going live:

- [ ] All agents completed without BLOCKED status
- [ ] Design Package has WCAG 2.1 AA compliance verified
- [ ] GitHub Supply Chain Package shows `approved: true`
- [ ] Builder Package shows zero source policy violations
- [ ] QA sign-off obtained
- [ ] Email campaign approved
- [ ] Monitoring dashboards configured
- [ ] Health checks passing
- [ ] Rollback procedure documented
- [ ] Audit trail complete (every decision logged)

---

## Success Metrics

1. **Zero Supply-Chain Incidents** — No unknown dependencies in production
2. **Deterministic Deployment** — Same input → Same output every time
3. **100% Audit Traceability** — Every decision logged with reasoning
4. **No Rework** — Workflows complete without re-runs (no mistakes because rules are enforced)
5. **Fast Feedback** — Agents BLOCK immediately if something is wrong (fail fast)

---

## Common Failure Modes (And Why They're Prevented)

### Failure: "Someone installed a random npm package"

**Prevention**: GitHub Supply Chain Agent validates every dependency. If it's not in `approved-sources.json`, workflow BLOCKS. Builder can't proceed.

### Failure: "Unpinned dependency caused production break"

**Prevention**: GitHub Supply Chain Agent requires exact version pinning. `^18.0.0` is rejected. Only `18.2.0` accepted. Build fails if version not pinned.

### Failure: "Design is inaccessible but nobody noticed until launch"

**Prevention**: Design Agent must pass WCAG 2.1 AA audit before emitting handoff. If accessibility issues detected, agent returns BLOCKED.

### Failure: "Different versions of React installed in different environments"

**Prevention**: All versions pinned in lockfile (package-lock.json or yarn.lock). Commit lockfile. Same versions everywhere.

### Failure: "No one knows why this dependency is here or who approved it"

**Prevention**: Every dependency in `outputs.dependency_review` includes reason, approval status, security score, and timestamp. Complete audit trail.

### Failure: "Product has GPL dependency that violates license"

**Prevention**: GitHub Supply Chain Agent runs license check. GPL rejected. Workflow BLOCKS with action: "Remove or re-request approval."

---

## Operational Runbook

### When a Workflow is BLOCKED

1. Check the `blockers` array
2. Each blocker has `issue`, `requirement`, `action`
3. Take the action
4. Previous agent re-emits handoff
5. Workflow resumes

### When You Need to Add a New Dependency

1. Design Agent adds to `outputs.dependencies_declared`
2. Include `reason` and `version`
3. Handoff to GitHub Supply Chain Agent
4. If not in approved list → GitHub agent BLOCKS with action
5. Either approve the dependency (security review) OR remove it
6. Design Agent re-submits
7. Workflow continues

### When GitHub Supply Chain Agent BLOCKS

Example blocker:

```json
{
  "issue": "Unknown npm package",
  "package": "trending-lib@1.0.0",
  "requirement": "Package must be in approved list",
  "action": "Submit for security review: 'trending-lib' passes npm audit, maintenance, license checks?"
}
```

**What you do**:
1. Check if package is legitimate
2. Run security audit manually
3. If safe, add to `approved-sources.json`
4. Design Agent re-submits
5. GitHub agent approves second time

---

## Monitoring & Observability

Every handoff package includes `timestamp`. Aggregate across workflow:

```
Creative Director: 10:00
  ↓ (10 min)
Research: 10:10
  ↓ (20 min)
Product: 10:30
  ↓ (15 min)
Design: 10:45
  ↓ (5 min)
GitHub Supply Chain: 10:50 ← Approval takes 5 min
  ↓ (depends on blockers)
Builder: 10:55 ← Implementation takes variable time
  ↓
Total: ~1-2 hours end-to-end

Identify bottlenecks: Which agent is slowest? Which one most likely to BLOCK?
```

**Metrics Dashboard**:
- Total workflow time (Creative → Launch)
- Agent-by-agent time breakdown
- Blocker frequency (which agent most likely to BLOCK)
- Re-run count (ideally zero)
- Success rate (% completing vs. BLOCKED)

---

## Security Implications

### Before This System

- Developers pull random packages
- No central approval
- Security has no visibility
- Malicious dependency gets installed
- Production is compromised

### With This System

- All packages explicitly declared
- GitHub Supply Chain Agent validates every one
- Security team has audit trail
- Malicious dependency is detected and BLOCKED
- Production is secure by construction

---

## Compliance & Audit

**For regulatory review**:

Every decision is timestamped and traceable:
- Who approved this? → GitHub Supply Chain Agent (logged)
- When? → Timestamp (ISO 8601)
- Why? → `reason` field (logged)
- What did they check? → Security score, maintenance, license (logged)
- What was the decision? → approved/BLOCKED (logged)

**Generating an audit report**:

```bash
npm run audit-trail -- --from 2024-01-01 --to 2024-01-31
```

Outputs: List of all approvals, blockers, timestamps, reasoning. Ready for legal/compliance review.

---

## The Philosophy Behind This System

> "When the only way two agents can communicate is through immutable, validated handoff packages, failures are caught early, workflows are deterministic, and production is secure by construction."

- No ambiguous natural language → No misinterpretation
- No optional fields → No silent failures
- No upstream mutations → No broken assumptions
- No bypassing gates → No security vulnerabilities
- Every decision is logged → Complete audit trail

This is what deterministic multi-agent systems look like. Build on this foundation.

---

## Next Steps

1. **Clone the repository**
2. **Copy `.env.example` → `.env`** and fill in your values
3. **Run `npm install`**
4. **Run `npm run validate-schemas`** to verify everything
5. **Read each agent markdown file** (`agents/0X-*.md`) to understand their role
6. **Update `config/approved-sources.json`** with your actual approved packages
7. **Create a test workflow** with sample input
8. **Deploy GitHub Actions workflows** to your repository
9. **Test end-to-end** with a real project

---

**Good luck. Build secure, deterministic, audit-friendly systems.**
