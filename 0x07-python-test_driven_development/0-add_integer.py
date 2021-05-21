#!/usr/bin/python3
""" adds two integers together """

def add_integer(a, b=98):
    """
        adds two integers together
        Args:
            a: first integer
            b: second integer
        Return:
            result of sum
    """
    res = 0
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    res = a + b
    return res
