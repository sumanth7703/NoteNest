import json

FILE_PATH = 'notes.json'

def read_notes():
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_notes(notes):
    with open(FILE_PATH, 'w') as f:
        json.dump(notes, f, indent=4)
