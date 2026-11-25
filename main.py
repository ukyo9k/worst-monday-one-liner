#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt), then reads it back and verifies the
byte-identical round-trip. Python 3, standard library only, no network.
"""

import os
import sys

LINE = (
    "Monday: my deploy died at 98%, my inbox hit 400 unread, "
    "and stand-up unanimously agreed the blocker was me."
)

MAX_CHARS = 140


def main() -> int:
    # Guards: one line, non-empty, within the 140-character limit.
    if not LINE or not LINE.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line must not start or end with whitespace",
              file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            "error: line is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and verify the round-trip is byte-identical.
    with open(path, "rb") as f:
        round_tripped = f.read()
    if round_tripped != data:
        print("error: round-trip mismatch", file=sys.stderr)
        return 1

    text = round_tripped.decode("utf-8")
    if text != LINE or len(text) > MAX_CHARS:
        print("error: verification failed", file=sys.stderr)
        return 1
    if round_tripped.endswith(b"\n") or round_tripped != LINE.encode("utf-8"):
        print("error: file must hold exactly the line, no trailing newline",
              file=sys.stderr)
        return 1

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
