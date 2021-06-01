#!/usr/bin/python3
import json
""" 3-to_json_string: def to_json_string """


def to_json_string(my_obj):
    """
        returns JSON representation of an object
        Args:
            my_obj: object to be serialized
    """
    json_rep = json.dumps(my_obj)
    return json_rep
