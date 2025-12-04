import sqlite3
from typing import Dict, List, Optional

DB_PATH = "tunes.db"


def create_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    """
    Create and return a SQLite connection.
    """
    return sqlite3.connect(db_path)


def create_table(conn: sqlite3.Connection) -> None:
    """
    Create the tunes table if it does not already exist.
    """
    sql = """
    CREATE TABLE IF NOT EXISTS tunes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book INTEGER,
        filename TEXT,
        X TEXT,
        T TEXT,
        M TEXT,
        K TEXT,
        R TEXT,
        body TEXT
    );
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def insert_tune(conn: sqlite3.Connection, tune: Dict) -> int:
    """
    Insert a single tune dictionary into the database.
    Returns the new row id.
    """
    sql = """
    INSERT INTO tunes (book, filename, X, T, M, K, R, body)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    cur = conn.cursor()
    cur.execute(
        sql,
        (
            tune.get("book"),
            tune.get("filename"),
            tune.get("X"),
            tune.get("T"),
            tune.get("M"),
            tune.get("K"),
            tune.get("R"),
            tune.get("body"),
        ),
    )
    conn.commit()
    return cur.lastrowid


def insert_many(conn: sqlite3.Connection, tunes: List[Dict]) -> None:
    """
    Insert a list of tunes into the database.
    """
    for t in tunes:
        insert_tune(conn, t)


def clear_table(conn: sqlite3.Connection) -> None:
    """
    Delete all rows from the tunes table.
    """
    cur = conn.cursor()
    cur.execute("DELETE FROM tunes;")
    conn.commit()


if __name__ == "__main__":
    # Quick manual test
    conn = create_connection()
    create_table(conn)
    conn.close()
    print("DB initialized.")
