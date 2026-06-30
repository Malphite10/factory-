import sys
import argparse
from runtime.state import StateManager
from runtime.registry import AgentRegistry
from runtime.graph import ExecutionGraph
from runtime.executor import AgentExecutor

class Orchestrator:
    def __init__(self, dry_run=False):
        self.state_manager = StateManager()
        self.registry = AgentRegistry()
        self.graph = ExecutionGraph(self.registry)
        self.executor = AgentExecutor(self.state_manager, dry_run=dry_run)
        self.dry_run = dry_run

    def run(self):
        mode = "DRY-RUN" if self.dry_run else "PRODUCTION"
        print(f"Starting Orchestrator in {mode} mode...")
        self.state_manager.update_status(f"RUNNING_{mode}")

        execution_order = self.graph.get_execution_order()

        current_input = {}
        for agent_id in execution_order:
            agent_info = self.registry.get_agent_info(agent_id)
            if not agent_info:
                print(f"Error: Agent {agent_id} not found in registry.")
                break

            result = self.executor.execute(agent_id, current_input, agent_info)
            if result.get("status") != "SUCCESS":
                print(f"Agent {agent_id} failed. Stopping.")
                self.state_manager.add_error(f"{agent_id} failed")
                self.state_manager.update_status("FAILED")
                return
            current_input = result

        self.state_manager.update_status("COMPLETED")
        print("Workflow completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    orchestrator = Orchestrator(dry_run=args.dry_run)
    orchestrator.run()
