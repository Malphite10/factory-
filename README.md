# Multi-Agent Deterministic Handoff System

**Owner**: @Malphite10
**Status**: Production Agent Operating System 🟢

A production-grade multi-agent orchestration framework with deterministic handoffs, a critical supply-chain gatekeeper, and a full-featured runtime execution engine.

## Quick Start

```bash
git clone https://github.com/@Malphite10/multi-agent-system.git
cd multi-agent-system
npm install
PYTHONPATH=. python3 runtime/orchestrator.py
```

## Core Components

### 1. Runtime State Machine
The `runtime/` engine manages the execution flow, state transitions, and artifact generation.
- `orchestrator.py`: Coordinates the multi-agent workflow.
- `state.py`: Manages global state persistence.
- `graph.py`: Defines the execution sequence.

### 2. Deterministic Handoffs
Every agent communicates via structured JSON packages validated against strict schemas in `agents/schemas/`.

### 3. Supply Chain Gatekeeper
Critical security gate in `.github/workflows/` enforcing:
- ✅ Dependency license scans
- ✅ SBOM generation (CycloneDX)
- ✅ SLSA provenance
- ✅ Signed releases

## Repository Structure

- `runtime/`: Execution engine and state management.
- `agents/`: Agent specifications, skills, and the central registry.
- `schemas/`: Global state and handoff definitions.
- `artifacts/`: Structured store for current runs, snapshots, and archives.
- `design-system/`: Registry and design tokens.
- `memory/`: Knowledge graph and marketplace intelligence.

## Success Metrics

- ✓ Zero supply-chain incidents.
- ✓ 100% Deterministic execution.
- ✓ Full audit traceability.

---Built with ❤️ by
███    ███  █████  ██      ██████  ██   ██ ██ ████████ ███████  ██████
████  ████ ██   ██ ██      ██   ██ ██   ██ ██    ██    ██      ██  ███
██ ████ ██ ███████ ██      ██████  ███████ ██    ██    █████   ██ ██ ██
██  ██  ██ ██   ██ ██      ██      ██   ██ ██    ██    ██      ████  ██
██      ██ ██   ██ ███████ ██      ██   ██ ██    ██    ███████  ██████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
