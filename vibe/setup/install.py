import os
import subprocess
import sys

def run_command(command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print(result.stdout)
    return True

def setup():
    print("Setting up Mistral Vibe...")

    # Check for uv
    try:
        subprocess.run(["uv", "--version"], capture_output=True)
    except FileNotFoundError:
        print("uv is not installed. Please install it first.")
        return

    # Install dependencies
    if run_command(["uv", "sync"]):
        print("Dependencies installed successfully.")
    else:
        print("Failed to install dependencies.")
        return

    print("Mistral Vibe setup complete.")

if __name__ == "__main__":
    setup()
