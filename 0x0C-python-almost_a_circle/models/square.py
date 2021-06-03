#!/usr/bin/python3
""" square: class Square """
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """
        Attributes:
            size(int): size of square
            x(int): x coordinate
            y(int): y coordinate
            id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes values for all instances of Square """
        super.__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of Square """
        return '[Square] ({}) {}/{} - {}'.format(
            super.__init__(id), self.__x, self.__y, self.__size)
