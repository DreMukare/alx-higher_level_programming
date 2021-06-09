#!/usr/bin/python3
""" square: class Square """
from models.rectangle import Rectangle

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
            self.id, self.__x, self.__y, self.__size)

    @property
    def size(self):
        """ getter for Square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for Square size """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ updates values for instances of Square """
        if args is not None:
            self.id = arg[0]
            self.__size = arg[1]
            self.__x = arg[2]
            self.__y = arg[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of Square instance """
        return {
            'id': self.id,
            'size': self.__size,
            'x': self.__x,
            'y': self.__y
            }
