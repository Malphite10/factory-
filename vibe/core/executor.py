from typing import Any
import time
from vibe.core.state import StateManager


class AgentExecutor:
    def __init__(self, state_manager: StateManager, dry_run: bool = False):
        self.state_manager = state_manager
        self.dry_run = dry_run

    def execute(self, agent_id: str, input_data: dict[str, Any]) -> dict[str, Any]:
        print(f"[{'DRY-RUN' if self.dry_run else 'EXEC'}] Agent: {agent_id}")

        # We need next_agent info here, or handled by orchestrator
        # For simplicity in this mock, we'll just transition
        self.state_manager.transition_to(agent_id)

        if self.dry_run:
            time.sleep(0.1)
            handoff = {"status": "SUCCESS", "mode": "dry-run"}
        else:
            # Simulate real execution
            handoff = {
                "status": "SUCCESS",
                "agent": agent_id,
                "output": f"Mock output from {agent_id}",
                "timestamp": time.time(),
            }

        self.state_manager.add_artifact(f"{agent_id}_handoff", handoff)
        return handoff
