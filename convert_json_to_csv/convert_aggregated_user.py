import os
import json
import pandas as pd

BASE_DIR = r"C:\Users\iqbal\Downloads\pulse\pulse-master\data\aggregated\user\country\india"
OUTPUT_CSV = "aggregated_user_data.csv"

all_data = []

for dirpath, _, filenames in os.walk(BASE_DIR):
    for file in filenames:
        if file.endswith(".json"):
            file_path = os.path.join(dirpath, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    raw = json.load(f)
                    data = raw.get("data", {})
                    aggregated = data.get("aggregated", {})
                    users_by_device = data.get("usersByDevice", [])

                    parts = file_path.split(os.sep)
                    year = next((x for x in parts if x.isdigit()), None)
                    state = None
                    if "state" in parts:
                        state = parts[parts.index("state") + 1]
                    else:
                        state = "india"

                    for device in users_by_device:
                        row = {
                            "state": state,
                            "year": year,
                            "brand": device.get("brand"),
                            "count": device.get("count"),
                            "percentage": device.get("percentage"),
                            "registered_users": aggregated.get("registeredUsers"),
                            "app_opens": aggregated.get("appOpens"),
                            "source_file": file_path
                        }
                        all_data.append(row)
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

df = pd.DataFrame(all_data)
df.to_csv(OUTPUT_CSV, index=False)
print(f" Saved to {OUTPUT_CSV}")
