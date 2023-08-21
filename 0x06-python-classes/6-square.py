#!/usr/bin/python3
"""
A module that Writes a class Square
"""


class Square:
    """
    This is a module that Write a class Square

    Attributes:
        size (int): Human readable string describing the exception.
        position (tuple): Tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        the __init__ method initializes a square instance

        Args:
            size (int): Description of `param1`.which defaults to 0
            position (tuple): Tuple which defaults to 0 too
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2
            or not isinstance(position[0], int) or
            not isinstance(position[1], int) or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        """
        Private instance attribute: size
        """
    def area(self):
        """

        Args:

        Returns:
            Area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        retrievs the size of the square

        Returns:
            int: Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        Args:
            value (int): value int
        Returns:
            Area
        Raises:
           Typeerro: if value is not an integer
           Valueerror: if value is less than )
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        prints the square with the character # using stdout
        if size is ), it prints an empty line
        the position is used to adjust the square's position

        Returns:
        """
        if self.__size == 0:
            print("")
        else:
            string_to_print = ""
            for i in range(self.position[1]):
                string_to_print += "\n"
            for x in range(self.size):
                for y in range(self.position[0]):
                    string_to_print += " "
                for z in range(self.size):
                    string_to_print += "#"
                string_to_print += "\n"
            print("{}".format(string_to_print), end='')

    @property
    def position(self):
        """
        Args:

        Returns:
            positon
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value (tuple): value tuple
        Returns:
            Area
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not
            isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
