#!/usr/bin/python3
"""
function that returns
a data structure
in JSON format
"""
import json


def from_json_string(my_str):
    """ function that returns a data structure in JSON format
    """
    return json.loads(my_str)
