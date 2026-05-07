import sqlite3

def get_connection(db_path=":memory:"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables(conn):
    cursor =conn.cursor()
    cursor.execute("""
            CREATE TABLE users (
                id      INTEGER PRIMARY KEY,
                name    TEXT    NOT NULL,
                email   TEXT    UNIQUE,
                active  INTEGER DEFAULT 1
            )
        """)
    conn.commit()
