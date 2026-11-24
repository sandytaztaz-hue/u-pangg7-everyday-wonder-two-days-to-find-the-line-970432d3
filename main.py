"""Everyday Wonder entry: one sentence, at most 200 characters.

Writes the entry to /output/entry.txt (no trailing newline, so the file
holds exactly the judged sentence) and prints it to stdout.
"""

from pathlib import Path

ENTRY = "The key sticks in the lock for three seconds every winter morning, as if the door needs that long to decide whether I still live here."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
