#!/usr/bin/python3
"""returns the dictionary description with simple data structure."""


def class_to_json(obj):
    """function that returns the dictionary description of the object."""
    return obj.__dict__
