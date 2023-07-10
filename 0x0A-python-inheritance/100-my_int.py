#!/usr/bin/python3
"""
    Module containing the `MyInt` class
"""


class MyInt(int):
    """Inherits from the `int` class
    """
    def __eq__(self, other):
        """Override equality operator to call inequality operator

        Args:
            other (int): An int.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operaotr to call equality operator

        Args:
            other (int): An int.
        """
        return super().__eq__(other)
