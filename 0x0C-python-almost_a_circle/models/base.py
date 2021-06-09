#!/usr/bin/python3
""" base: class Base """
import json


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
        if (type(list_dictionaries) != list or
                not all(type(item) == dict for item in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs to a file """
        filename = cls.__name__ + '.json'
        list_of_dicts = []
        if list_objs is not None:
            for item in list_objs:
                list_of_dicts.append(cls.to_dictionary(item))
        jsonstr = cls.to_json_string(list_of_dicts)
        with open(filename, 'w') as f:
            f.write(jsonstr)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
