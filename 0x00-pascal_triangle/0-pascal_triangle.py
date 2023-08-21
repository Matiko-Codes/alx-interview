#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
    # Returns an empty list if n <= 0
    if n <= 0:
        return []
    # Initializes an empty list to store the rows of the triangle
    triangle = []
    # Initializes a variable to store the current row of the triangle
    row = [1]
    # Iterates from 0 to n - 1
    for _ in range(n):
        # Adds the current row to the list of rows
        triangle.append(row)
        # Creates a new list to store the next row of the triangle
        next_row = []
        # Adds the first element of the next row
        next_row.append(1)
        # Iterates from 0 to len(row) - 2
        for i in range(len(row) - 1):
            # Adds an element to the next row based on the rule of Pascal's triangle
            next_row.append(row[i] + row[i + 1]
                    # Adds the last element of the next row
                    next_row.append(1)
                    # Updates the current row for the next iteration
                    row = next_row
                    # Returns the list of lists of integers representing the Pascal's triangle
                    return triangle
