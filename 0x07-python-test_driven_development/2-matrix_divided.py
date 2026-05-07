#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    """
    
    # 1. Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Validation: Is the matrix valid?
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # We need to know the size of the first row to compare others to it
    # We check matrix[0] because we know the matrix isn't empty now
    if not isinstance(matrix[0], list):
        raise TypeError(msg)
    
    row_size = len(matrix[0])

    for row in matrix:
        # Check if the row is actually a list
        if not isinstance(row, list):
            raise TypeError(msg)

        # Check if the row size matches the first row
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check every single item in the row
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)

    # 4. The Calculation: Create a NEW matrix
    # We create a new list for the whole matrix
    new_matrix = []
    
    for row in matrix:
        new_row = []
        for item in row:
            # Divide and round to 2 decimal places
            result = round(item / div, 2)
            new_row.append(result)
        # Add the finished row to our new matrix
        new_matrix.append(new_row)

    return new_matrix