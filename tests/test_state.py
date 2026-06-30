from vibe.core.state import StateManager


def test_state_initialization(tmp_path):
    state_file = tmp_path / "state.json"
    manager = StateManager(state_path=str(state_file))
    assert manager.state["status"] == "INITIALIZED"


def test_state_transition(tmp_path):
    state_file = tmp_path / "state.json"
    manager = StateManager(state_path=str(state_file))
    manager.transition_to("agent1", "agent2")
    assert manager.state["current_agent"] == "agent1"
    assert manager.state["next_agent"] == "agent2"
    assert len(manager.state["history"]) == 1


def test_add_artifact(tmp_path):
    state_file = tmp_path / "state.json"
    manager = StateManager(state_path=str(state_file))
    manager.add_artifact("test", {"foo": "bar"})
    assert manager.state["artifacts"]["test"]["foo"] == "bar"
