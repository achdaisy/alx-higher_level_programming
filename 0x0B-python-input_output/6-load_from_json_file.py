#!/usr/bin/python3
"""Creates an object from a json file."""

import json


def load_from_json_file(filename):
    """Create an object from a json file."""
    with open(filename) as file:
        return json.load(file)
