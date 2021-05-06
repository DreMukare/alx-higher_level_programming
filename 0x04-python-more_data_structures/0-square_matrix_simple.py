#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None
    i = 0
    new_matrix = []
    while i < len(matrix):
        new_matrix.append(list(map(lambda x: x * x, matrix[i])))
        i += 1
    return new_matrix    
