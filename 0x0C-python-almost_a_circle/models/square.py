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

    @property
    def size(self):
        """ getter for Square size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for Square size """
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of Square instance """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """ updates values for instances of Square """
        if args is not None:
            self.id = arg[0]
            self.size = arg[1]
            self.x = arg[2]
            self.y = arg[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of Square instance """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
