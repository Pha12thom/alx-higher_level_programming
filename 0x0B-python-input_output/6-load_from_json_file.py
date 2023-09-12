#!/usr/bin/python3
"""imposrt json module"""
import json


def load_from_json_file(filename):
    """create pythom object from json file"""
    with open(filename) as f:
        return json.load(f)
