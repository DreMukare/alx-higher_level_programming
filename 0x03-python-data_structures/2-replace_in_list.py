#!/usr/bin/python3
def replace_int_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    return my_list[idx] = element
