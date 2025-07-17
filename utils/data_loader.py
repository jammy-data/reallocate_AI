import os
import json

def load_all_pilots(data_dir="data/pilots"):
    pilots = []
    for filename in os.listdir(data_dir):
        if filename.startswith("pilot_") and filename.endswith(".json"):
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                pilot_data = json.load(f)
                pilots.append(pilot_data)
    return pilots
