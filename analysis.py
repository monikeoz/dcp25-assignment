import sqlite3
from typing import Optional

import pandas as pd

DB_PATH = "tunes.db"


def load_df(db_path: str = DB_PATH) -> pd.DataFrame:
    """
    Load the entire tunes table from the SQLite database into a pandas DataFrame.
    """
    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql("SELECT * FROM tunes", conn)
    finally:
        conn.close()
    return df


def get_tunes_by_book(df: pd.DataFrame, book_number: int) -> pd.DataFrame:
    """
    Return all tunes from a specific book.
    """
    return df[df["book"] == book_number].copy()


def get_tunes_by_type(df: pd.DataFrame, tune_type: str) -> pd.DataFrame:
    """
    Return all tunes matching a given tune type (matches the R column, case-insensitive).
    """
    # match in R column (case-insensitive)
    return df[df["R"].str.contains(tune_type, case=False, na=False)].copy()


def search_tunes(df: pd.DataFrame, search_term: str) -> pd.DataFrame:
    """
    Search tunes by title (T column), case-insensitive.
    """
    return df[df["T"].str.contains(search_term, case=False, na=False)].copy()
