#!/usr/bin/python3
"""
script that adds all the
arguments to a python list
and then saves them to a file
"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.exists("add_item.json") is True:
    my_lyst1 = list(load_from_json_file("add_item.json"))

    for i in range(1, len(sys.argv)):
        my_lyst1.append(sys.argv[i])
    save_to_json_file(my_lyst1, "add_item.json")
    """
    a list the saved Json representation
    """
else:
    my_lyst1 = []
    save_to_json_file(my_lyst1, "add_item.json")
