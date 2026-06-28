import json
from runtime.registry import AgentRegistry
from runtime.graph import ExecutionGraph

def test_execution_order(tmp_path):
    reg_file = tmp_path / "registry.json"
    data = {
        "A": {"next": "B"},
        "B": {"next": "C"},
        "C": {"next": None}
    }
    with open(reg_file, 'w') as f:
        json.dump(data, f)

    registry = AgentRegistry(registry_path=str(reg_file))
    graph = ExecutionGraph(registry)
    order = graph.get_execution_order("A")
    assert order == ["A", "B", "C"]
