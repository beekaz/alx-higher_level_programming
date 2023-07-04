#!/usr/bin/python3
""" Rclangle class module from 0-rectangle.py"""


class Rectangle:
    """
    an empty class Rectangle that defines  arectangle
    Args:
        width (int): 
        height (int):
    
    Attributes:
        width (int):
        height (int):
        
    Raises:
        TypeError: not an inter
        ValueError: less than 0
        
    """
    
    def __init__(self, width = 0, height = 0):
        if not isinstance(width, int):
            raise TypeError("width must be an interger")
        if  width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise ValueError("height  must be >= 0")
        self.__height = height
        self.__width = width
        
    @property
    def width(self):
        """int: width in  the rectsngle"""
        return self.__width
    
    @property
    def height (self):
        """int: height"""
        return self.__height
    
    @property
    def height(self, value):
        """
        Args:
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
            Args:
                value (int): int
                
            Raises:
                TypeError: not int
                ValueError: less than 0
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= o")
            self.__width = value
        
        def area(self):
            """
            Calculating Area
            
            Return:
            area (int)"""
            
            return self.__width * self.__height
        
        def Perimeter(self):
            """
            calacuting of perimeter
            
            Return:
            perimeter (int)
            """
            if self.__width == 0 or self.__height == 0:
                return 0
            
            return (self.__width + self.height) * 2