#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (<=200 chars) about the dumbest thing my own agent did
today to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "I asked my agent to rename one file. It renamed 214, committed as "
    "'cleanup', and asked if I wanted the backups renamed too."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
