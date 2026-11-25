"""One Line, One Laugh — entry program (stdlib only).

Writes exactly one funny line (1-200 chars, no trailing newline)
to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
"""
import os

ENTRY = "I asked my smart speaker for a joke \u2014 it read out my bank balance and we both went quiet."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
