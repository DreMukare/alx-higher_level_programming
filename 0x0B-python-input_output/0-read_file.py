#!/usr/bin/python3
""" 0-read_file: def read_file """


def read_file(filename=""):
    """
        reads a text file (UTF-8) and prints to stdout
    """
    with open(filename) as f:
        for line in f:
            print(line, end='')
