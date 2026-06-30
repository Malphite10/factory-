import argparse
import json
import os

def load_config():
    config_path = "vibe.config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Mistral Vibe - Main Assistant CLI")
    parser.add_argument("command", nargs="?", help="Command to run")
    args = parser.parse_args()

    config = load_config()
    agent_name = config.get("agent_name", "Main Assistant")
    mode = config.get("mode", "cloud")

    print(f"[{agent_name}] running in {mode} mode.")
    if not args.command:
        parser.print_help()
        return

    print(f"Executing command: {args.command}")

if __name__ == "__main__":
    main()
