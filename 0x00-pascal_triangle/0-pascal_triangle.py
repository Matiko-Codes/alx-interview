#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
     """Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n"""
     tri = []
     if n > 0:
         for k in range(1, n + 1):
             level = []
             C = 1
             for l in range(1, k + 1):
                 level.append(C)
                 C = C * (k - l) // l
                 tri.append(level)
                 return tri
