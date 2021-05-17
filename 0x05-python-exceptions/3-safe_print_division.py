#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
        print('Inside result: ', end='')
    except:
        print('None')
        return 'None'
    finally:
        print('{}'.format(a / b))
        return (a / b)
