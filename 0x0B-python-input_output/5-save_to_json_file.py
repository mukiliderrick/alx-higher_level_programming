#!/usr/bin/python3
"""module that returns an object (Python data structure) represented by a JSON string:"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
