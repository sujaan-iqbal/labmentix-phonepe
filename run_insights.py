import sqlite3
import os

DB_PATH = "phonepe.db"
INSIGHTS_PATH = "sql/insights"

def execute_query(file_path):
    try:
        with open(file_path, "r") as f:
            query = f.read()
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            results = cursor.execute(query).fetchall()
            print(f"\n[RESULTS] {os.path.basename(file_path)}")
            for row in results:
                print(row)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to execute: {file_path}\n{e}")

if __name__ == "__main__":
    for i in range(1, 6):
        sql_file = os.path.join(INSIGHTS_PATH, f"q{i}_*.sql".replace("*", ""))
        matching = [f for f in os.listdir(INSIGHTS_PATH) if f.startswith(f"q{i}_")]
        if matching:
            execute_query(os.path.join(INSIGHTS_PATH, matching[0]))
        else:
            print(f"[ERROR] SQL file for Q{i} not found.")
