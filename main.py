#!/usr/bin/env python3
"""Entry for make.fun bounty: One Sentence, One Journey.

Writes a single one-sentence journey story to entry.txt inside
MAKEFUN_OUTPUT_DIR (falling back to /output).
"""

import os
import stat
from pathlib import Path

TEXT = (
    "For eleven hours Mara drove her father's ashes north in a dented "
    "thermos, his road atlas open beside her, past diesel and pine resin "
    "and the tollbooth where he once paid for strangers, until at the "
    "grey pier in Tobermory she tipped him into the wind and drove home "
    "empty-handed, singing aloud"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT + ".", encoding="utf-8")
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
