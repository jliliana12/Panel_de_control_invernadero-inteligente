import sqlite3

def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS variables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL,
            humedad REAL,
            ph REAL
        )
    """)
    conn.commit()
    conn.close()
