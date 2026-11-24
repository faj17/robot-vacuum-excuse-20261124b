#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse entry.

Writes one original funny excuse a robot vacuum gives for missing
a spot to /output/entry.txt (1-140 characters, UTF-8, a single
line). Standard library only, no network, no input.

The line is built from two fragments: a setup (the vacuum's own
sensors found the dust and filed it under decorative — the excuse
rooted in its own world) and a punch (the turn: it has decided to
respect the dust's life choices, so the joke lands in the last few
words). ``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My sensors found the dust, filed it under decorative,"
PUNCH = "and I have decided to respect its life choices."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one excuse line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-140 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line must be 1-140 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
