"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one word, the word my ex would use to describe me.
# One word, 8 characters — inside the 1-24 character gate.
# Revision note: "avoidant" lands instantly, stings with recognition, and
# needs no explanation — the judge brief's own test for the winning word.
import os

TEXT = "avoidant"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
