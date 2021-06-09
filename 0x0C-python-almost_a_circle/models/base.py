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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        if (type(list_dictionaries) != list or not all(type(item) == dict
                    for item in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
