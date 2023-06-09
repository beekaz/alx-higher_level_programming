#!/usr/bin/python3
"""
Rectangle class module
"""


class Rectangle:
    """
    An empty class Rectangle that defines a rectangle

    Args:
        width (int): int
        height (int): int

    Attributes:
        width (int): int
        height (int): int

    Raises:
        TypeError: not an integer
        ValueError: less than 0
    """

    def __init__(self, width=0, height=0):
        """ initializes a new rectangles"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """int: width of rectangle"""
        return self.__width

    @property
    def height(self):
        """int: height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args: value
           value (int): int
        Raises:
            TypeError: not int
            ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Arg:value
            value (int): int
            Raises:
                TypeError: not int
                ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
