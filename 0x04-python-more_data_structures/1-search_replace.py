#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return None
    new_list = [replace if x == search else x for x in my_list]
    return new_list
