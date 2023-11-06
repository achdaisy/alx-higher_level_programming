#!/usr/bin/python3
"""checks if an object is eactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance.

    Args:
        obj (any): the onject to be checked.
        a_class (type): the class to compared obj with.
    Returns:
        if obj is exactly an instance - True.
        else - False.
    """
    if type(obj) == a_class:
        return True
    return False
