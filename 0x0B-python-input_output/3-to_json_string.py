#!/usr/bin/python3
"""Returns thejson rep of an object"""


import json


def to_json_string(my_obj):
    """returns the json representation of an object"""
    return json.dumps(my_obj)