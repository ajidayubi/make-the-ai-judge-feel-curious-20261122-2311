#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. A reader comes home to a second front door that
should not exist, and a note in their own handwriting that leaves the
one question unanswered. No network, no dependencies, deterministic.
"""

import os
import sys

TEXT = (
    "You come home and there are two front doors. Same paint, same number, "
    "your name on both brass plates. Behind the second one a light is on, "
    "and a kettle you never bought is whistling. A note in your handwriting "
    "says: don't open it until you know which of us lives here."
)


def main() -> int:
    # The gate rejects anything outside 1-280 code points or blank-only,
    # so refuse to write an invalid entry instead of shipping one.
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        print("error: entry text must be 1-280 non-blank characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")
    # Read it back and refuse a corrupt write instead of shipping one:
    # the file on disk must be exactly the text we meant to enter.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != TEXT + "\n":
        print("error: entry.txt on disk does not match the entry text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
