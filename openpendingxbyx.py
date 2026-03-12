#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_JSON_PATH = SCRIPT_DIR / "connections" / "followers_and_following" / "pending_follow_requests.json"

# How many tabs to open per Enter
BATCH_SIZE = 30


def load_pending_usernames(json_path: Path) -> list[str]:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    usernames = []
    for e in data.get("relationships_follow_requests_sent", []):
        for s in e.get("string_list_data", []):
            if "value" in s:
                usernames.append(s["value"].strip())
                break
    return usernames


def main():
    import argparse
    p = argparse.ArgumentParser(description="Open pending profiles in Chrome in batches.")
    p.add_argument("--json", type=Path, default=DEFAULT_JSON_PATH, help="Path to pending_follow_requests.json")
    p.add_argument("--batch", type=int, default=BATCH_SIZE, help=f"Tabs to open per Enter (default: {BATCH_SIZE})")
    args = p.parse_args()
    batch = max(1, args.batch)

    if not args.json.exists():
        print(f"Error: File not found: {args.json}")
        sys.exit(1)

    usernames = load_pending_usernames(args.json)
    total = len(usernames)
    print(f"Total {total} profiles. Opening {batch} tabs per Enter.\n")

    start = 0
    batch_num = 0
    while start < total:
        chunk = usernames[start : start + batch]
        urls = [f"https://www.instagram.com/{u}/" for u in chunk]
        batch_num += 1
        print(f"  → Opening {len(chunk)} tabs (profiles {start + 1}-{start + len(chunk)} / {total})...")
        subprocess.run(["open", "-a", "Google Chrome"] + urls, check=False)
        start += len(chunk)
        if start < total:
            input(f"  Press Enter to open next {min(batch, total - start)} tabs... ")
        print()

    print("Done. All profiles opened.")


if __name__ == "__main__":
    main()
