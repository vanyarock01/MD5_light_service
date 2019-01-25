import sqlite3
import os

DB_NAME = 'tasks.db'
package_dir = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(package_dir, 'tasks.db')


def db_up():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, email text, url text, status INTEGER, MD5 text)")
    conn.commit()
    conn.close()


def db_execute(query, values):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(query, values)
    last_row_id = c.lastrowid
    conn.commit()
    conn.close()
    return last_row_id


def db_select(query, values):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    result = c.execute(query, values).fetchone()
    conn.close()

    return result
