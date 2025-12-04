from pathlib import Path
from typing import List, Tuple


def find_abc_files(root: str = "abc_books") -> List[Tuple[str, int]]:
    """
    Recursively find all .abc files under root.

    Returns:
        List of tuples: (filepath, book_number)
        Assumes the immediate parent folder name is numeric (e.g., "0", "1", "2").
    """
    p = Path(root)
    abc_files: List[Tuple[str, int]] = []

    if not p.exists():
        raise FileNotFoundError(f"{root} not found")

    for sub in p.iterdir():
        if sub.is_dir() and sub.name.isdigit():
            book_num = int(sub.name)
            for f in sub.rglob("*.abc"):
                abc_files.append((str(f), book_num))

    return abc_files


if __name__ == "__main__":
    # Quick test
    files = find_abc_files()
    for f, b in files:
        print(b, f)
