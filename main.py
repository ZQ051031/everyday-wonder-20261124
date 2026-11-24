#!/usr/bin/env python3
"""Everyday Wonder entry.

Writes exactly one sentence -- a small everyday moment made
strange and new -- to /output/entry.txt. Standard library only.
"""

from pathlib import Path

ENTRY = (
    "This morning the kettle sighed, and its steam rose like a small "
    "grey bird that circled the kitchen once before flying out the "
    "open window."
)


def main() -> None:
    # The entry must be exactly one sentence of at most 200 characters.
    sentence = ENTRY.strip()
    assert sentence.count(".") == 1 and sentence.endswith("."), (
        "entry must be exactly one sentence"
    )
    assert len(sentence.encode("utf-8")) <= 200, "entry exceeds 200 bytes"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(sentence + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
