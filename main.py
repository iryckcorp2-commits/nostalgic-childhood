#!/usr/bin/env python3
"""Write one childhood memory, at most 280 characters, to entry.txt.

Deterministic: the same entry is written on every run, byte for byte.
Uses only the Python 3 standard library and needs no network.
"""

import os

ENTRY = (
    "I still hear the ice cream cart bell from three streets away, and I can "
    "feel the coins sweating in my palm as I ran barefoot down the hot "
    "pavement, certain the whole summer would wait for me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
