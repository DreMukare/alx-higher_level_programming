#!/usr/bin/python3
""" base: class Base """


class Base:
    """
        class Base
        Attributes:
            __nb_objects(int): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            initializes all instances
        """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
