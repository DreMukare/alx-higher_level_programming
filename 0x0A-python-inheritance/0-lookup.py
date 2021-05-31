#!/usr/bin/python3
""" module contains: lookup """


def lookup(obj):
    """
        returns the list of available attributes
        and methods of obj
        Args:
            obj: object whose attributes and methods
                 are to be listed
        Return:
            list of attributes and methods of obj
    """
    return dir(obj)
