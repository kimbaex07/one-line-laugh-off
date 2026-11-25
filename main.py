"""One-Line Laugh-Off entry.

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python stdlib only. Gate (from the kit RULES): entry.txt must be
UTF-8 text of 1-200 characters, a single line, not only whitespace.
"""

import os

LINE = (
    "My Roomba just filed for divorce \u2014 apparently moving the couch "
    "every week and blaming it for the dust counts as emotional abuse."
)


def main() -> None:
    # Gate guard: the entry must be a single non-blank line of 1-200 chars.
    if not (1 <= len(LINE) <= 200):
        raise ValueError(
            f"entry must be 1-200 characters, got {len(LINE)}"
        )
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(out_path, 0o644)

    # Post-write guard: re-read what was written and re-check the gate
    # against the file itself, so a stray newline or encoding slip fails
    # loudly instead of shipping a bad entry.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written entry differs from the intended line")
    if not (1 <= len(written) <= 200) or "\n" in written or "\r" in written:
        raise ValueError("written entry fails the 1-200 char single-line gate")


if __name__ == "__main__":
    main()
