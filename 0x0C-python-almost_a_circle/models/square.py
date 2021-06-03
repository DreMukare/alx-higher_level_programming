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
        super.__init__(width, height, x, y, id)

    def __str__(self):
        """ string representation of Square """
        return '[Square] ({}) {}/{} - {}'.format(
            super.__init__(id), self.__x, self.__y, self.__width)

    @property
    def size(self):
        """ getter for Square size """
        return self.__width

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
        if args and args is not None:
            super().__init__(id) = arg_1
            self.__size = arg_2
            self.__x = arg_3
            self.__y = arg_4
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of Square instance """
        return {
            'id': super().__init__(id),
            'size': self.__size,
            'x': self.__x,
            'y': self.__y
            }
