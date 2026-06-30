import json
from pathlib import Path
from typing import Any


class AgentRegistry:
    def __init__(self, registry_path: str = "agents/registry.json"):
        self.registry_path = Path(registry_path)
        self.registry = self._load_registry()

    def _load_registry(self) -> dict[str, Any]:
        if self.registry_path.exists():
            with self.registry_path.open("r") as f:
                return json.load(f)
        return {}

    def get_agent_info(self, agent_id: str) -> dict[str, Any]:
        return self.registry.get(agent_id, {})

    def get_next_agents(self, agent_id: str) -> list[str]:
        nxt = self.get_agent_info(agent_id).get("next")
        if nxt is None:
            return []
        if isinstance(nxt, list):
            return nxt
        return [nxt]

    def get_next_agent(self, agent_id: str) -> str | None:
        agents = self.get_next_agents(agent_id)
        return agents[0] if agents else None
