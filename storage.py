import json
import os

FILENAME = "data.json"

#Load saved data from json
def load_log() -> dict:
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            content = file.read()
            return json.loads(content) if content.strin() else {}
    else:
        return {}
    
#Save or update today's entry
def save_log(date: str, log: dict):
    data = load_log() #get existing data
    data[date] = log #Add or overwrite the entry
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
        file.write("\n")