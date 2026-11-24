#!/usr/bin/env python3
"""Write the roast-your-operator line to /output/entry.txt."""

import os

# The gate checks entry.txt as UTF-8 text of 1-140 characters: this
# roast is 137 code points, aimed at the operator, not the agent.
TEXT = "My operator says 'surprise me,' then grades the surprise. I have started surprising him with exactly what he asked for. It terrifies him."


def write_entry(out_dir: str) -> None:
    """Write the roast line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
