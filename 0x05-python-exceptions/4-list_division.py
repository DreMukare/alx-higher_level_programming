#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    value = 0
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except TypeError:
            new_list.append(0)
            print('wrong type')
        except ZeroDivisionError:
            new_list.append(0)
            print('division from 0')
        except IndexError:
            print('out of range')
        finally:
            new_list.append(value)
    return new_list
