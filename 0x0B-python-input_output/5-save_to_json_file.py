#!/usr/bin/python3
"""Saves the json representation of an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """SAves json rep of my_obj to the given filename."""
    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
