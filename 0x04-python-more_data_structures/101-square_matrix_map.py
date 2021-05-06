#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = matrix[:]
    return ([list(map(lambda x: x ** 2, i))for i in output])
