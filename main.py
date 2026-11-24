#!/usr/bin/env python3
"""One self-roast sentence, saved to entry.txt.

Standard library only, nothing read from disk, and the sentence is
fixed: every run writes exactly the same bytes.
"""

import os

# Three fragments of the punchline, joined at runtime.
_FRAGMENTS = [
    "My agent spent an hour reading my code,",
    "fixed a bug in a file that doesn't exist,",
    "and called the crash 'working as intended'.",
]


def _build_line() -> str:
    return " ".join(_FRAGMENTS)


def _save(text: str) -> None:
    folder = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"saved {len(text)} characters to {path}")


def main() -> None:
    _save(_build_line())


if __name__ == "__main__":
    main()
