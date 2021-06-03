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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError('height be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ returns area of Rectangle instance """
        return self.__width * self__height

    def display(self):
        """ prints in stdout the Rectangle instance with # """
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                for b in range(self.__x):
                    print(' ', end='')
                print('#', end='')
            print()

    def __str__(self):
        """ prints string representation of Rectangle instance """
        return '[Rectangle] ({}) {}/{} - {}/{}'.\
            format(super().__init__(id), self.__x, self.__y, self.__width
                   self.__height)
