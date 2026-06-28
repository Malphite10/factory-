import json
import os
from typing import Dict, Any, List, Optional, Union

class AgentRegistry:
    def __init__(self, registry_path: str = "agents/registry.json"):
        self.registry_path = registry_path
        self.registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        if os.path.exists(self.registry_path):
            with open(self.registry_path, 'r') as f:
                return json.load(f)
        return {}

    def get_agent_info(self, agent_id: str) -> Dict[str, Any]:
        return self.registry.get(agent_id, {})

    def get_next_agents(self, agent_id: str) -> List[str]:
        nxt = self.get_agent_info(agent_id).get("next")
        if nxt is None:
            return []
        if isinstance(nxt, list):
            return nxt
        return [nxt]

    def get_next_agent(self, agent_id: str) -> Optional[str]:
        agents = self.get_next_agents(agent_id)
        return agents[0] if agents else None
