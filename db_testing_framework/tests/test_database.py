import sqlite3
import sys
import logging
from db.connection import get_connection, create_tables

logger = logging.getLogger(__name__)

def test_user_table_exists():

    logger.info("test_user_table_exists Test started")
    conn = get_connection()
    create_tables(conn)
    cursor =conn.cursor()
    cursor.execute("""select name from sqlite_master 
    where type ='table' and name ='users'""")
    result = cursor.fetchone()
    assert result is not None,"users table doesn't exist"
    logger.info("test_user_table_exists Test completed")
    conn.close()

def test_insert_user():
    conn = get_connection()
    create_tables(conn)
    cursor =conn.cursor()
    cursor.execute("insert into users (name, email) values (?, ?)",
    ("pramila","pramila@gmail.com"))
    conn.commit()

    cursor.execute("select * from users where email =?",("pramila@gmail.com",))
    user =cursor.fetchone()
    assert user["name"]=="pramila"
    assert user["active"]==1
    assert user["email"]=="pramila@gmail.com"
    conn.close()


