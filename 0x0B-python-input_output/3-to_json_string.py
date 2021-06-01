#!/usr/bin/python3
import json
""" 3-to_json_string: def to_json_string """


def to_json_string(my_obj):
    """
        returns JSON representation of an object
        Args:
            my_obj: object to be serialized
    """
    return json.dumps(my_obj)
