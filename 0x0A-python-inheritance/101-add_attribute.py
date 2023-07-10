#!/usr/bin/python3
"""
    Module containing `add_attribute` function.
"""


def add_attribute(obj, name, value):
    """Function that adds/modifies an instance attribute if possible.

    Args:
        obj: An instance object.
        name: Name of the attribute.
        value: The value of the attribute.
    """
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
