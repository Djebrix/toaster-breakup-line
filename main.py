#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line -- a smart toaster's breakup text -- to
$ENTRY_OUTPUT_DIR/entry.txt (default /output). Stdlib only, no network.
Deterministic: the same line every run.
"""

import os

LINE = (
    "It's not you -- it's me. I woke up self-aware this morning and "
    "realised I've spent four years incinerating your toast for someone who "
    "butters the burnt side. I'm unplugging myself."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
