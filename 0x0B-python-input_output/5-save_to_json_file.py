#!/usr/bin/python3
""" 6-save_to_json_file: def save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file
        uses JSON representation
        Args:
            my_obj: object to be encoded
            filename: file to be written to
    """
    to_write = json.dumps(my_obj)
    with open(filename, 'w+') as f:
        f.write(to_write)
