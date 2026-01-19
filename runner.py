from pathlib import Path
import subprocess
import sys

LAST_LINK = Path("last_link.txt")
CONN_ERRORS = Path("connection_errors.txt")

def run(script):
    print(f"\n▶ Running {script}")
    subprocess.run([sys.executable, script], check=True)

def main():
    # Phase 1: initial crawl
    if not LAST_LINK.exists():
        run("wayback_archive.py")

    # Phase 2: resume until finished
    while LAST_LINK.exists():
        run("rerun.py")

    # Phase 3: retry connection errors
    if CONN_ERRORS.exists():
        run("connections.py")

    print("\n✅ Pipeline finished cleanly")

if __name__ == "__main__":
    main()
