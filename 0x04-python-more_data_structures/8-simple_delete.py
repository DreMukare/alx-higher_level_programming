#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if len(key) == 0:
        return
    a_dictionary.pop(key)
    return a_dictionary
