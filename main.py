#!/usr/bin/env python3
"""Write one office-life joke, a single line under 200 characters, to /output/entry.txt.

Entry for make.fun competition "Make the AI Judge Laugh"
(u-rama-melon-make-the-ai-judge-laugh-302d0825).
"""

import os

ENTRY = "The whiteboard still shows Q1's strategy \u2014 nobody erases it, because then we'd have to admit it never happened."

OUTPUT_PATH = "/output/entry.txt"

# House gate (rules, "The gate"): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space. Fail loudly instead of
# writing an entry the gate would refuse.
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate allows 1-200")
    if not ENTRY.strip():
        raise ValueError("entry is only white space, gate refuses it")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
