import sqlite3

DB = "students.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT NOT NULL,
                department TEXT NOT NULL,
                level TEXT NOT NULL,
                state TEXT NOT NULL,
                age INTEGER NOT NULL,
                image TEXT NOT NULL,
                admission_status TEXT DEFAULT 'Pending'
            )
        """)
