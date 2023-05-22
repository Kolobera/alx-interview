#!/usr/bin/python3
"""Island Parameter Module"""


def island_perimeter(grid):
    m = len(grid[0])
    n = len(grid)
    perimeter = 0
    for i in range(1, m-1):
        for j in range (1, n-1):
            if grid[i][j] == 1:
                perimeter += 1
    return 2 * (perimeter + 1)
