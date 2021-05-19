#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
            value = 0
        except ZeroDivisionError:
            print('division by 0')
            value = 0
        except IndexError:
            print('out of range')
            value = 0
        finally:
            new_list.append(value)
    return new_list
