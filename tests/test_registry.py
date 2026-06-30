import json
from vibe.core.registry import AgentRegistry


def test_registry_load(tmp_path):
    reg_file = tmp_path / "registry.json"
    data = {"agent1": {"next": ["agent2"]}}
    with open(reg_file, "w") as f:
        json.dump(data, f)

    registry = AgentRegistry(registry_path=str(reg_file))
    assert registry.get_next_agents("agent1") == ["agent2"]


def test_get_agent_info(tmp_path):
    reg_file = tmp_path / "registry.json"
    data = {"agent1": {"id": "agent1", "name": "Agent 1"}}
    with open(reg_file, "w") as f:
        json.dump(data, f)
    registry = AgentRegistry(registry_path=str(reg_file))
    assert registry.get_agent_info("agent1")["name"] == "Agent 1"
