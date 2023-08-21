#!/usr/bin/python3
"""
module that prints list of available attributes and methods of  an object
"""


def lookup(obj):
    """
    the function lookup  returns list of avaiable attributes and
    methods of an object

    Args:
    (obj):

    Returns: list
    """
    return dir(obj)
