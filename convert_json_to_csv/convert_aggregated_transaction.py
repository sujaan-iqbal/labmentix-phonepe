import os
import json
import pandas as pd

BASE_DIR = r"C:\Users\iqbal\Downloads\pulse\pulse-master\data\aggregated\transaction\country\india"
OUTPUT_CSV = "aggregated_transaction_data.csv"

all_data = []

# Walk through all year and state folders
for dirpath, _, filenames in os.walk(BASE_DIR):
    for file in filenames:
        if file.endswith(".json"):
            file_path = os.path.join(dirpath, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    raw = json.load(f)
                    data = raw.get("data", {})
                    transactions = data.get("transactionData", [])

                    # Determine location from folder structure
                    parts = file_path.split(os.sep)
                    year = next((x for x in parts if x.isdigit()), None)
                    state = None
                    if "state" in parts:
                        state_index = parts.index("state") + 1
                        state = parts[state_index].lower()
                    else:
                        state = "india"

                    for entry in transactions:
                        name = entry.get("name", "")
                        instruments = entry.get("paymentInstruments", [])
                        for instrument in instruments:
                            row = {
                                "state": state,
                                "year": year,
                                "payment_category": name,
                                "type": instrument.get("type"),
                                "count": instrument.get("count"),
                                "amount": instrument.get("amount"),
                                "source_file": file_path
                            }
                            all_data.append(row)
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

# Convert to DataFrame and save
df = pd.DataFrame(all_data)
df.to_csv(OUTPUT_CSV, index=False)
print(f" Saved to {OUTPUT_CSV}")
