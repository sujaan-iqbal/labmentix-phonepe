import os
import json
import pandas as pd

# Update this to your dataset location
BASE_DIR = r"C:\Users\iqbal\Downloads\pulse\pulse-master\data\top"
OUTPUT_DIR = "top_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_top_category(category):
    records = []
    root_path = os.path.join(BASE_DIR, category, "country", "india")

    if not os.path.exists(root_path):
        print(f"Path does not exist: {root_path}")
        return pd.DataFrame()

    for year in os.listdir(root_path):
        year_path = os.path.join(root_path, year)
        if not os.path.isdir(year_path):
            continue

        for filename in os.listdir(year_path):
            if not filename.endswith(".json"):
                continue

            quarter = filename.replace(".json", "")
            file_path = os.path.join(year_path, filename)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    json_data = json.load(f)

                data = json_data.get("data", {})
                for level_key in ["states", "districts", "pincodes"]:
                    for entry in data.get(level_key, []):
                        region = entry.get("entityName") or entry.get("name")
                        record = {
                            "category": category,
                            "level": level_key[:-1],  # 'states' -> 'state'
                            "region": region,
                            "year": year,
                            "quarter": quarter,
                        }

                        if category == "user":
                            record["registeredUsers"] = entry.get("registeredUsers")
                        else:
                            metric = entry.get("metric", {})
                            record["count"] = metric.get("count")
                            record["amount"] = metric.get("amount")

                        records.append(record)
            except Exception as e:
                print(f" Error processing {file_path}: {e}")

    return pd.DataFrame(records)

# Run for all 3 categories
for cat in ["transaction", "user", "insurance"]:
    print(f" Processing category: {cat}")
    df = process_top_category(cat)
    if df.empty:
        print(f" No data found for {cat}")
    else:
        output_csv = os.path.join(OUTPUT_DIR, f"top_{cat}.csv")
        df.to_csv(output_csv, index=False)
        print(f"Saved: {output_csv} ({len(df)} rows)")
