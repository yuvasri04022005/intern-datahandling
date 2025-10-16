import sqlite3
import pandas as pd

# Step 1: Connect to SQLite (creates db if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Step 2: Create table & insert data
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
"""
)
cursor.execute("INSERT INTO student (name, marks) VALUES ('Yuva', 89)")
cursor.execute("INSERT INTO student (name, marks) VALUES ('Riya', 92)")
conn.commit()

# Step 3: Read data
df_sql = pd.read_sql_query("SELECT * FROM student", conn)
print(df_sql)
