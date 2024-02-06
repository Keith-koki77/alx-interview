#!/usr/bin/python3
"""
Function that returns the perimeter of the
island described in grid
"""


def island_perimeter(grid):
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for i, j in zip([0] + row, row + [0]):
            perimeter += int(i != j)
    return perimeter
