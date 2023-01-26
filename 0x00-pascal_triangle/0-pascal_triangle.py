#!/usr/bin/python3
'''Module to return pascal triangle'''


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing the Pascal's triangle of n.
    If n <= 0, an empty list is returned.
    """
    if n <= 0:
        return []
    # create empty 2D list with n rows and i+1 columns for the first i rows
    triangle = [[1] * (i + 1) for i in range(n)]
    # loop through the rows
    for i in range(n):
        # loop through the columns of each row
        for j in range(1, i):
            # fill value of each element using formula for Pascal's triangle
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle