#!/usr/bin/python3
"""Checks if object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is exactly an instance.

    Args:
        obj (any): the onject to be checked.
        a_class (type): the class to compared obj with.
    Returns:
        if obj is exactly an instance - True.
        else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
