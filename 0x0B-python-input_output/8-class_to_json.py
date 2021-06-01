#!/usr/bin/python3
""" 8-class_to_json: def class_to_json """


def class_to_json(obj):
    """
        serializes class instance
    """
    return obj.__dict__
