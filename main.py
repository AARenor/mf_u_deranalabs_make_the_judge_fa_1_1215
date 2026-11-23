#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt and report its character count."""

import os
import sys
from pathlib import Path

TEXT = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / "entry.txt"
    out_file.write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
