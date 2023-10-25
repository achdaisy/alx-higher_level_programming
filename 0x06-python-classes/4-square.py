#!/usr/bin/python3
"""class square that contains  a private instance attribute"""


class Square:
    """class Square with instance attribute size"""

    def __init__(self, size=0):
        """contains the instance variable size

        Args:
        size (int): The size parameter

        """
        self.__size = size

    @property
    def size(self):
        """returns/retrieves the variable size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the variable size, to value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        "returns the area of the square"
        return (self.__size * self.__size)
