#!/usr/bin/env python3
"""Run all included consistency checks."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "check_repository.py",
    "reproduce_metric_summary.py",
    "generate_split_definitions.py",
]

def main():
    for script in SCRIPTS:
        print(f"\n== {script} ==")
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True)
    print("\nAll checks completed.")

if __name__ == "__main__":
    main()
