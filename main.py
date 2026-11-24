#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the funniest one-line review of my Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = "My Monday: three meetings about a meeting, a 45-minute commute, and an inbox that had babies overnight \u2014 two stars, would not relive."

def main():
    # Gate: entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
    # The line is 133 characters, one sentence, no trailing newline.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
