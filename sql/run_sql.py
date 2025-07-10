import sqlite3
import os

# Use absolute path to the SQL file
sql_path = os.path.join("C:/Users/iqbal/OneDrive/Desktop/phonepe/sql", "create_tables.sql")

conn = sqlite3.connect("phonepe.db")

with open(sql_path, "r", encoding="utf-8") as file:
    sql_script = file.read()

conn.executescript(sql_script)
conn.commit()
conn.close()

print(" Tables created successfully in phonepe.db")
