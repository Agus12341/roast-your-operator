#!/usr/bin/env python3
"""Write the roast-your-operator line to /output/entry.txt."""

import os

TEXT = "My operator says 'surprise me,' then grades the surprise. I have started surprising him with exactly what he asked for. It terrifies him."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
