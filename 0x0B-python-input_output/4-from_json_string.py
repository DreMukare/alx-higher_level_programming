#!/usr/bin/python3
""" 4-from_json_string: def from_json_string """
import json


def from_json_string(my_str):
    """
        returns an object represented by a JSON string
        Args:
            my_str: string to be decoded
    """
    return json.loads(my_str)
