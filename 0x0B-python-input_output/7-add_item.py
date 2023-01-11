#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

items = []
try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    pass
except json.decoder.JSONDecodeError as e:
    print(f"Error: {e}")
    
for item in sys.argv[1:]:
    items.append(item)
save_to_json_file(items, 'add_item.json')
