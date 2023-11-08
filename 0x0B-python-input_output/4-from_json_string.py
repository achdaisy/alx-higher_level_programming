#!/usr/bin/python3
"""returns teh object representation of a json string"""

import json


def from_json_string(my_str):
    """returns the object representation of my_str."""
    return json.loads(my_str)
