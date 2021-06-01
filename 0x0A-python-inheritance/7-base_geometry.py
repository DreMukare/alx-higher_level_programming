#!/usr/bin/python3
""" 5-base_geometry: class BaseGeometry """


class BaseGeometry:
    """
        class BaseGeometry
        Methods:
            area: raise exception for now
    """
    def area(self):
        """
            raises exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            validates value
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
