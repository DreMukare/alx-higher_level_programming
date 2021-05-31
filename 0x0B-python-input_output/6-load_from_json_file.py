#!/usr/bin/python3
import json
""" 6-load_from_json_file: def load_from_json_file """


def load_from_json_file(filename):
    """ creates an Object from a JSON file
        Args:
            filename: file to be read
    """
    with open(filename) as f:
        content = f.read()
    json.load(content) 
