import json
import os
from datetime import datetime
import uuid
from typing import Dict, List, Any

class StateManager:
    def __init__(self, state_path: str = "artifacts/current/state.json"):
        self.state_path = state_path
        self.state = self._load_state()

    def _load_state(self) -> Dict[str, Any]:
        if os.path.exists(self.state_path):
            with open(self.state_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    pass

        now = datetime.utcnow().isoformat() + "Z"
        return {
            "project_id": "default",
            "run_id": str(uuid.uuid4()),
            "workflow_id": "default-workflow",
            "started_at": now,
            "updated_at": now,
            "current_stage": "idle",
            "current_agent": "idle",
            "next_agent": "00-creative-director",
            "status": "INITIALIZED",
            "completed_stages": [],
            "artifacts": {},
            "errors": [],
            "scores": {},
            "metrics": {},
            "history": []
        }

    def save_state(self):
        self.state["updated_at"] = datetime.utcnow().isoformat() + "Z"
        os.makedirs(os.path.dirname(self.state_path), exist_ok=True)
        with open(self.state_path, 'w') as f:
            json.dump(self.state, f, indent=2)

    def transition_to(self, agent_id: str, next_agent: str = None):
        entry = {
            "from": self.state["current_agent"],
            "to": agent_id,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        self.state["history"].append(entry)
        self.state["current_agent"] = agent_id
        self.state["current_stage"] = agent_id
        self.state["next_agent"] = next_agent
        if agent_id not in self.state["completed_stages"] and agent_id != "idle":
            self.state["completed_stages"].append(agent_id)
        self.save_state()

    def update_status(self, status: str):
        self.state["status"] = status
        self.save_state()

    def add_artifact(self, name: str, data: Any):
        self.state["artifacts"][name] = data
        self.save_state()

    def add_error(self, error: str):
        self.state["errors"].append(error)
        self.save_state()

    def update_score(self, key: str, value: float):
        self.state["scores"][key] = value
        self.save_state()
