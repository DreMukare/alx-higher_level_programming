#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return
    new_list = list(set(my_list))
    output = sum(new_list)
    return output