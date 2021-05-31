#!/usr/bin/python3
import json
""" 5-save_to_json_file: def save_to_json_file """


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file
        uses JSON representation
        Args:
            my_obj: object to be encoded
            filename: file to be written to
    """
    to_write = json.dumps(my_obj, sort_keus=True)
    with open(filename, 'w+') as f:
        f.write(to_write)
