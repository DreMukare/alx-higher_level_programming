#!/usr/bin/python3
""" 12-pascal_triangle: def pascal_triangle """


def pascal_triangle(n):
    """
        returns a list of lists of integers
        reps Pascal's triangle of n
        Args:
            n(int): to be repped
    """
    triangle = []
    inner_list  = []
    if not n <= 0:
        for i in range(n):
            innerlist.append(i + 1)
            triangle.append(inner_list)
    return triangle
