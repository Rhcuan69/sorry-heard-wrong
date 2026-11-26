#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one funny one-line apology from a smart speaker to /output/entry.txt.
Pure Python standard library; no network; deterministic output.
"""

import os

ENTRY = (
    "Sorry, I heard 'call Mom' as 'cancel Christmas', so I've already "
    "told the whole family. Merry Christmas."
)


def main() -> None:
    # Self-check: the gate requires 1-140 chars, one line, non-blank.
    assert 1 <= len(ENTRY) <= 140, "entry out of length bounds"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
