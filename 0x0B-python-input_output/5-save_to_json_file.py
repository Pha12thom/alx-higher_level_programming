#!/usr/bin/python3
"""storimg json comtents to a file"""
import json


def save_to_json_file(my_obj, filename):
    """make file writable"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(json.dump(my_obj))
