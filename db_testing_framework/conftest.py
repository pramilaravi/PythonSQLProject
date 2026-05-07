import pytest
import sqlite3
from db.connection import get_connection,create_tables
@pytest.fixture
def db():
    conn =get_connection()
    create_tables(conn)
    yield conn
    conn.close()

@pytest.fixture
def db_with_data(db):
    cursor = db.cursor()
    cursor.executemany("INSERT INTO USERS (name,email,active) VALUES (?,?,?)",[("pram","ap@gmail.com","1"),
                                                                               ("manikandan","mani@gmail.com","1"),
                                                                               ("adi","adhi@gmail.com","0"),])
    db.commit()
    return db




