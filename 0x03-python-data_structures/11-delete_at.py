#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    if idx < len(my_list):
        del my_list[idx]
    return my_list
