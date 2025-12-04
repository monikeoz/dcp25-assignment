from typing import List, Dict


def parse_abc_file(filepath: str, book_number: int) -> List[Dict]:
    """
    Parse an ABC notation file into a list of tune dictionaries.

    Each tune:
      - Starts with a line 'X:'
      - Can have header fields like T, M, R, K
      - The remaining lines are stored as 'body'
    """
    tunes: List[Dict] = []

    # Template for the current tune we are building
    current = {
        "book": book_number,
        "filename": filepath,
        "X": None,
        "T": None,
        "M": None,
        "K": None,
        "R": None,
        "body": "",
    }

    def save_current():
        # Only save if we actually started a tune (X not None)
        if current["X"] is not None:
            tunes.append(current.copy())

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.rstrip("\n")

            if line.startswith("X:"):
                # New tune begins
                save_current()
                current = {
                    "book": book_number,
                    "filename": filepath,
                    "X": line[2:].strip(),
                    "T": None,
                    "M": None,
                    "K": None,
                    "R": None,
                    "body": "",
                }
            elif line.startswith("T:"):
                current["T"] = line[2:].strip()
            elif line.startswith("M:"):
                current["M"] = line[2:].strip()
            elif line.startswith("K:"):
                current["K"] = line[2:].strip()
            elif line.startswith("R:"):
                current["R"] = line[2:].strip()
            else:
                # Not a header line → part of the body
                current["body"] += line + "\n"

    # Save the last tune if present
    save_current()
    return tunes
