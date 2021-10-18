#!/usr/bin/python3
"""
function that writes an
Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Text file in JSON
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
