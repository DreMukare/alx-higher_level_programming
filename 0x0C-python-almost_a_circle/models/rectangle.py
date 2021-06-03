#!/usr/bin/python3
""" rectangle: class Rectangle """
Base = __import__('base').Base


class Rectangle(Base):
    """
        attributes:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int)
            y(int)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initializes width, height, id, x and y for all instances
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        # not sure about this bit
        super().__init__(id)

    @property
    def width(self):
        """ returns width """
        return self.__width
 
    @width.setter
    def width(self, value):
        """ setter function for width """
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        self.__y = value
