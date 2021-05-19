#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    output = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
        except (TypeError, ValueError):
            pass
        output += 1
    print()
    return output
