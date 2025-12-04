from file_loader import find_abc_files
from parser import parse_abc_file
from db_manager import create_connection, create_table, insert_tune, clear_table


def build_db(root: str = "abc_books", db_path: str = "tunes.db", wipe: bool = False) -> None:
    """
    Build (or rebuild) the tunes database from all ABC files under `root`.
    """
    conn = create_connection(db_path)
    create_table(conn)
    if wipe:
        clear_table(conn)

    files = find_abc_files(root)
    total = 0

    for filepath, book in files:
        tunes = parse_abc_file(filepath, book)
        for t in tunes:
            insert_tune(conn, t)
            total += 1

    conn.close()
    print(f"Inserted {total} tunes from {len(files)} files.")


if __name__ == "__main__":
    build_db(root="abc_books", wipe=True)
