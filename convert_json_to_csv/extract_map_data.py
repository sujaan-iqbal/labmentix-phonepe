import os
import json
import pandas as pd

BASE_PATH = r"C:\Users\iqbal\Downloads\pulse\pulse-master\data\map"
CATEGORIES = ["transaction", "user", "insurance"]
OUTPUT_DIR = "./map_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_state_level(path, category):
    records = []
    for year_folder in os.listdir(path):
        year_path = os.path.join(path, year_folder)
        if not os.path.isdir(year_path): continue

        for file in os.listdir(year_path):
            if not file.endswith(".json"): continue
            quarter = file.replace(".json", "")
            file_path = os.path.join(year_path, file)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f).get("data", {})
                    if category == "user":
                        hover_data = data.get("hoverData", {})
                        for region, metrics in hover_data.items():
                            records.append({
                                "level": "state",
                                "region": region,
                                "year": year_folder,
                                "quarter": quarter,
                                "registeredUsers": metrics.get("registeredUsers"),
                                "appOpens": metrics.get("appOpens"),
                                "source": file_path
                            })
                    else:
                        hover_list = data.get("hoverDataList", [])
                        for item in hover_list:
                            metric = item.get("metric", [{}])[0]
                            records.append({
                                "level": "state",
                                "region": item.get("name"),
                                "year": year_folder,
                                "quarter": quarter,
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                                "source": file_path
                            })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return records

def extract_district_level(path, category):
    records = []
    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        if not os.path.isdir(state_path): continue

        for year_folder in os.listdir(state_path):
            year_path = os.path.join(state_path, year_folder)
            if not os.path.isdir(year_path): continue

            for file in os.listdir(year_path):
                if not file.endswith(".json"): continue
                quarter = file.replace(".json", "")
                file_path = os.path.join(year_path, file)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f).get("data", {})
                        if category == "user":
                            hover_data = data.get("hoverData", {})
                            for region, metrics in hover_data.items():
                                records.append({
                                    "level": "district",
                                    "state": state,
                                    "region": region,
                                    "year": year_folder,
                                    "quarter": quarter,
                                    "registeredUsers": metrics.get("registeredUsers"),
                                    "appOpens": metrics.get("appOpens"),
                                    "source": file_path
                                })
                        else:
                            hover_list = data.get("hoverDataList", [])
                            for item in hover_list:
                                metric = item.get("metric", [{}])[0]
                                records.append({
                                    "level": "district",
                                    "state": state,
                                    "region": item.get("name"),
                                    "year": year_folder,
                                    "quarter": quarter,
                                    "count": metric.get("count"),
                                    "amount": metric.get("amount"),
                                    "source": file_path
                                })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return records

for category in CATEGORIES:
    print(f" Processing category: {category}")
    state_path = os.path.join(BASE_PATH, category, "hover", "country", "india")
    district_path = os.path.join(state_path, "state")

    state_records = extract_state_level(state_path, category)
    district_records = extract_district_level(district_path, category)

    df = pd.DataFrame(state_records + district_records)
    out_file = os.path.join(OUTPUT_DIR, f"map_{category}.csv")
    df.to_csv(out_file, index=False)
    print(f" Saved: {out_file} (Rows: {len(df)})")
