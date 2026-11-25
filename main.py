"""One line: a roast of the entrant's own fridge.

Writes the line to /output/entry.txt (UTF-8, single line, 1-199 chars).
"""

import os

LINE = "My fridge groans every time I open it, like it's judging my life choices — and after one look at what's inside, honestly, so am I."

MAX_CHARS = 199


def main() -> None:
    # Validate the line before writing anything, so a bad line never
    # produces a partial or invalid /output/entry.txt.
    line = LINE
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
