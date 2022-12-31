#!/usr/bin/python3

"""this prgramme divides content of a matrix with a divisor
the matrix and divisor can aonly be eithe int or a float
    """

def matrix_divided(matrix, div):
        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    row_size = len(matrix[0])
    for i, row in enumerate(matrix):
        if not isinstance(i, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    
        for j, val in enumerate(row):
            new_matrix.append(round(val / div, 2))
    return (new_matrix)
        
