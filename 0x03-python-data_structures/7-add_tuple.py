#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    output = ()
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        output = (tuple_a[0} + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        output = ()
