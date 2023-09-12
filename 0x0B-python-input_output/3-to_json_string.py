#!/usr/bin/python3
import json
"""changing texts to string format"""


def to_json_string(my_obj):
    """
    args(my_obj)
    presenting string im json format
    """
    return json.dumps(my_obj)
