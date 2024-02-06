#!/usr/bin/python3
"""
Function that returns the perimeter of the
island described in grid
"""


def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                if x == 0 or grid[x - 1][y] == 0:
                    perimeter += 1

                if x == rows - 1 or grid[x + 1][y] == 0:
                    perimeter += 1

                if y == 0 or grid[x][y - 1] == 0:
                    perimeter += 1

                if y == cols - 1 or grid[x][y + 1] == 0:
                    perimeter += 1

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
