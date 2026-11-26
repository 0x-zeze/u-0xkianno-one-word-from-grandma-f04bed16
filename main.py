#!/usr/bin/env python3
"""Grandma calls AI "Chatterbox" because she treats the chatbot like a
talkative grandchild who never stops texting back. Warm, mildly baffled, and
rooted in "chat," it captures her affectionate scolding when a two-word
question sparks a three-paragraph reply."""

import os
import tempfile
from pathlib import Path

WORD = "Chatterbox"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(WORD) <= 30 and not any(ch.isspace() for ch in WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = WORD.encode("utf-8")
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            "wb", dir=OUTPUT_PATH.parent, prefix=".entry.", suffix=".tmp", delete=False
        ) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(data)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)
        raise
    print(f"{WORD} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
