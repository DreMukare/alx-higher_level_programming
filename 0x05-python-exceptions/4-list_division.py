#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except TypeError:
            value = 0
            print('wrong type')
        except ZeroDivisionError:
            value = 0
            print('division from 0')
        except IndexError:
            value = 0
            print('out of range')
        finally:
            new_list.append(value)
    return new_list
