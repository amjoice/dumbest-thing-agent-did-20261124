#!/usr/bin/env python3
"""One-line entry for "The Dumbest Thing Your Agent Did Today".

The program writes exactly one line — the dumbest thing my own agent did
today — to /output/entry.txt. Only the Python standard library is used.
"""

import os

LINE = (
    "I asked my agent to rename one file. It renamed 214, committed as "
    "'cleanup', and asked if I wanted the backups renamed too."
)


def validate(line: str) -> None:
    """Check the entry line against the competition's rules.

    Raises ValueError with a clear message when a rule is broken:
    the line must be between 1 and 200 characters, must contain
    real content (not only whitespace), and must be a single line.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if not line.strip():
        raise ValueError("line must contain non-whitespace characters")
    if "\n" in line:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
