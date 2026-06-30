# Open Design Template Factory

Deterministic AI-powered production system for marketplace-ready website templates. Powered by **Mistral Vibe**.

## Overview

Open Design Template Factory transforms market opportunities, design systems, and component libraries into production-ready template releases through a structured, multi-agent workflow.

## Architecture

Built on the **Mistral Vibe** engine:
- `vibe/core`: Orchestration, State Management, and Agent Execution.
- `vibe/cli`: Interactive management interface.
- `vibe/acp`: Agent Client Protocol bridge.

### Agent Pipeline

1. **Strategy Agent**: Market analysis and product planning.
2. **Open Design Core Agent**: Design ingestion and platform adaptation.
3. **Production Agent**: Template assembly and quality assurance.

## Repository Structure

```
open-design-template-factory/
├── vibe/               # Mistral Vibe Core Engine
│   ├── core/           # Orchestration & Logic
│   ├── cli/            # TUI Components
│   ├── acp/            # Protocol Bridge
│   └── setup/          # Configuration Wizards
├── agents/             # Agent definitions & schemas
├── design-system/      # Canonical design tokens & components
├── memory/             # Knowledge graph & analytics
├── workflows/          # Structured process definitions
├── references/         # Standards & policies
├── projects/           # Active template projects
└── AGENTS.md           # Engineering conventions
```

## Getting Started

### Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

### Installation
```bash
uv sync
```

### Running the Orchestrator
```bash
uv run python -m vibe.core.orchestrator --dry-run
```

## Engineering Standards

We follow strict Mistral Vibe conventions. See [AGENTS.md](AGENTS.md) for details on:
- Command usage via `uv`
- Python 3.12+ style (match/case, modern type hints)
- Absolute imports
- Pydantic for data validation

---

Built with by @Malphite10
