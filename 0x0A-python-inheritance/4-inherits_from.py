#!/usr/bin/python3
"""Checks if is subclasss."""


def inherits_from(obj, a_class):
    """ returns True if the object is exactly an instance.

    Args:
        obj (any): the onject to be checked.
        a_class (type): the class to compared obj with.
    Returns:
        if obj is exactly an instance - True.
        else - False.
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
