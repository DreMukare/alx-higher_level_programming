#!/usr/bin/python3
def uppercase(str):
    i = 0
    lists = list(str)
    while i < len(lists):
        if lists[i].isalpha():
            up = ord(lists[i]) - 32
            lists[i] = chr(up)
        i += 1
    print(lists)
    str = ''.join(lists)
    print(str)
