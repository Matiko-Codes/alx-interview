#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
     """Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = []
    row = [1]
    for _ in range(n)
        triangle.append(row)
        next_row = []
        next_row.append(1)
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1]
                    next_row.append(1)
                    row = next_row
                    return triangle
