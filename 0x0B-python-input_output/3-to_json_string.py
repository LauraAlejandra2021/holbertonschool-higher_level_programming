#!/usr/bin/python3
"""
function that
returns an object
in JSON
"""
import json


def to_json_string(my_obj):
    """ This function passes a dictionary to Json format """
    return json.dumps(my_obj)
