#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line: the single sentence that could
have replaced an entire pointless meeting, no context, no explanation. The
line is 79 characters."""

ENTRY_LINE = "We are here because no one wanted to be the person who said no to this meeting."


def main():
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    print(f"Wrote {len(ENTRY_LINE)} characters to {entry_path}")
    with open(entry_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY_LINE, "entry.txt does not match the line"
    print("Test passed:", content)


if __name__ == "__main__":
    main()
