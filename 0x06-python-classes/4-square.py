#!/usr/bin/python3
""" module contains: class Square """


class Square:
    """
        Square: defines a square
        Attributes:
            size (int): size of square
        Method:
            __init__: Initializes size for all instances
    """

    def __init__(self, size=0):
        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Finds area of the square
            Return:
                area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ getter function to for private attribute size
            Return:
                size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function for private attribute size
            Args:
                value (int): value to be set
        """
        if not size.is_integer():
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
