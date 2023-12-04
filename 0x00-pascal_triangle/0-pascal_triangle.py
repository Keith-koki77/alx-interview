#!/usr/bin/python3
"""
Pascal's Triangle script
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascals triange
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        row.append(1)
        triangle.append(row)
    return triangle
