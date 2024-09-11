import sqlite3
import os

# Dapatkan path direktori saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))
schema_path = os.path.join(current_dir, 'schema.sql')

conn = sqlite3.connect(os.path.join(current_dir, 'database.db'))
with open(schema_path) as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
