#!/usr/bin/python3
""" 4-inherits_from: inherits_from """


def inherits_from(obj, a_class):
    """
        returns True if obj is an instance
        of a class that inherited
        (directly or indirectly) from the
        specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
