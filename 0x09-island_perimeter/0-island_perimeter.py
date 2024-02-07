#!/usr/bin/python3
"""
Function that returns the perimeter of the
island described in grid
"""


def island_perimeter(grid):
    """
    Returns perimeter of island described in grid
    """
    num = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):

            idx = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
            check = [1 if z[0] in range(row) and z[1] in range(col) else 0
                     for z in idx]

            if grid[x][y]:
                num += sum([1 if not r or not grid[z[0]][z[1]] else 0
                            for r, z in zip(check, idx)])

    return (num)
