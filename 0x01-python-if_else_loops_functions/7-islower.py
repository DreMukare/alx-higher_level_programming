#!/usr/bin/python3
def islower(c):
    i = 97
    while i < 123:
        if ord(c) == i:
            return True
        i += 1
    return False
