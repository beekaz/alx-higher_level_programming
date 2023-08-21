#!/usr/bin/python3
"""
    Module containing the `is_kind_of_class` function.
"""


def is_kind_of_class(obj, a_class):
    """Check if `obj` is an instance of `a_class` or
    child class that inherits from it

    Args:
        obj: An object
        a_class: A class

    Return: True if `obj` is an instance a `a_class`, otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
