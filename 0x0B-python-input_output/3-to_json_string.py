#!/usr/bin/python3
"""module that returns JSON representation of an object"""

import json


def to_json_string(my_obj):
    """function that returns json representation"""
    return json.dumps(my_obj)