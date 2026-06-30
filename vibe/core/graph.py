from vibe.core.registry import AgentRegistry


class ExecutionGraph:
    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    def get_execution_order(self, start_node: str = "strategy") -> list[str]:
        order = []
        visited = set()
        stack = [start_node]

        while stack:
            current = stack.pop(0)
            if current and current not in visited:
                order.append(current)
                visited.add(current)
                next_agents = self.registry.get_next_agents(current)
                if next_agents:
                    stack.extend(next_agents)
        return order
