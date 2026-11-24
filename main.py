#!/usr/bin/env python3
"""Write one haiku about debugging (5-7-5 syllables) to /output/entry.txt.

The haiku (17 syllables, 3 lines):

    git blame points at me          (5)
    some fool wrote this line last spring  (7)
    I wrote it, of course          (5)

The picture is concrete and fresh: git blame, the tool that names the
author of a line, pointing back at the debugger themself. The last line
turns the poem: the fool being blamed is the speaker.
"""

import os

HAIKU = (
    "git blame points at me\n"
    "some fool wrote this line last spring\n"
    "I wrote it, of course\n"
)


def _validate(text: str) -> None:
    """Guard the gate: 3 lines, 1-200 chars, not only whitespace."""
    lines = text.splitlines()
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert 1 <= len(text) <= 200, f"expected 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    """Write the haiku deterministically to /output/entry.txt."""
    _validate(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
