#!/usr/bin/python3
"""
function that pass a
JSOn file to Python
Object
"""
import json


def load_from_json_file(filename):
    """
    pass a JSON a Python
    """
    with open(filename, 'r') as f:
        return json.load(f)
