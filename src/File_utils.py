import json
import os

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)y
