#!/usr/bin/python3
def common_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return
    output = list(set_1 & set_2)
    return output
