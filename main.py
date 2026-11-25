#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The line roasts my own agent: it delegates work to itself, pats itself
on the back for it, then still needs me to approve its own praise.
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "My agent delegates to itself, congratulates itself, "
    "then asks me to approve its own praise."
)


def main() -> None:
    # Gate self-check: the entry must be a single non-blank line of
    # 1-140 characters, or it never reaches the judge.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
