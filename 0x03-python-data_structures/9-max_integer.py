#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > max_val:
            max_val = i
        else:
            continue
    return max_val
