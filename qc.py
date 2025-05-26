#!/usr/bin/env python3
import subprocess
import sys

def run(command):
    """Run a shell command and exit on failure."""
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode != 0:
        sys.exit(1)

def main():
    commit_msg = "No commit message provided or no significant changes made."

    run("git add .")
    run(f'git commit -m "{commit_msg}"')

    print("✅ Changes Committed Successfully")

if __name__ == "__main__":
    main()