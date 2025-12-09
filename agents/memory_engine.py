import json
import os

MEMORY_PATH = "database/memory.json"

def save_memory(key, value):
    if not os.path.exists(MEMORY_PATH):
        json.dump({}, open(MEMORY_PATH, "w"))

    data = json.load(open(MEMORY_PATH))
    data[key] = value
    json.dump(data, open(MEMORY_PATH, "w"))

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        json.dump({}, open(MEMORY_PATH, "w"))
        return {}

    try:
        return json.load(open(MEMORY_PATH))
    except:
        # auto-fix corrupted file
        json.dump({}, open(MEMORY_PATH, "w"))
        return {}

