#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — entry program.

Writes exactly one sentence pitching a ridiculous invention that fixes
a tiny everyday annoyance to /output/entry.txt and prints exactly the
same text to stdout. Deterministic: no input, no randomness, no time,
no network.
"""

import os

ENTRY = "A toaster that apologizes in advance for burning your toast, then burns it anyway out of professional pride."

# The gate allows 1 to 220 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 220, f"entry length {len(ENTRY)} outside 1-220"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
