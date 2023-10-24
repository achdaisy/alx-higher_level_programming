#!/usr/bin/python3
"""class square that contains  a private instance attribute"""


class Square:
    """class Square with instance attribute size"""

    def __init__(self, size):
        """contains the instance variable size

        Args:
        size (int): The size parameter

        """

        self.__size = size
