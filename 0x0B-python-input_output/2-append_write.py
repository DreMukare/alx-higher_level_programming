#!/usr/bin/python3
""" 2-append_write: def append_writre """


def append_write(filename="", text=""):
    """
        appends a string to end of a text file (UTF8)
        Return:
            no of characters added
    """
    with open(filename, 'a+') as f:
        f.write(text)
    return len(text)
