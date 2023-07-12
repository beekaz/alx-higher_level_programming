#!/usr/bin/python3
"""
module
"""


def write_file(filename="", text=""):
    """
    write a string to text (UTF8) & return total of
    character written
    """
    with open(filename, 'w') as f:
        return f.write(text)
