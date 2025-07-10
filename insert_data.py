import sqlite3
import pandas as pd
import os

# Database connection
conn = sqlite3.connect("phonepe.db")
cursor = conn.cursor()

# CSV directory
csv_dir = "csv"

# Mapping of CSV files to table names
csv_table_map = {
    "aggregated_transaction.csv": "aggregated_transaction",
    "aggregated_user.csv": "aggregated_user",
    "aggregated_insurance.csv": "aggregated_insurance",
    "map_transaction.csv": "map_transaction",
    "map_user.csv": "map_user",
    "map_insurance.csv": "map_insurance",
    "top_transaction.csv": "top_transaction",
    "top_user.csv": "top_user",
    "top_insurance.csv": "top_insurance"
}

# Load each CSV and insert into the corresponding table
for file_name, table_name in csv_table_map.items():
    file_path = os.path.join(csv_dir, file_name)
    
    if os.path.exists(file_path):
        print(f" Loading {file_name} into {table_name}...")
        df = pd.read_csv(file_path)
        df.to_sql(table_name, conn, if_exists="append", index=False)
    else:
        print(f" File not found: {file_path}")

conn.commit()
conn.close()
print(" All data inserted successfully.")
