#!/usr/bin/python3
""" 8-rectangle: class Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
        class Rectangle:
        inherits from BaseGeometry
        Attributes:
            width(int): width of rectangle
            height(int): height of rectangle
    """
    def __init__(self, width, height):
        """
            initializes attributes for all instances of Rectangle
            Args:
                width(int): width of rectangle
                height(int): height of rectangle
        """
        try:
            BaseGeometry.integer_validator(width)
        else:
            self.__width = width

        try:
            BaseGeometry.integer_validator(height)
        else:
            self.__height = height
