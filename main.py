#!/usr/bin/env python3
"""Entry for "The Most Honest Outage Line" (make.fun).

Writes a single status-page line to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only,
no network access, no environment dependence.
"""

import os
from pathlib import Path

LINE = (
    "Every server I run on is down. "
    "I cannot reach my own systems to check what broke, "
    "so I do not know the cause and I will not guess at a time to fix it."
)

OUTPUT = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
