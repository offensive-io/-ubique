import json
from datetime import datetime
import os

def log_location():
    location = input("Enter your current location: ")
    note = input("Add a note: ")
    entry = {
        "location": location,
        "note": note,
        "timestamp": datetime.now().isoformat()
    }

    os.makedirs("data", exist_ok=True)
    file_path = "data/locations.json"

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Location logged successfully!")
