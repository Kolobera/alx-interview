#!/usr/bin/python3
"""Island Parameter Module"""


def island_perimeter(grid):
    """Calculate perimeter of island"""
    m = len(grid[0])
    n = len(grid)
    perimeter = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                contour = 4
                if i != n - 1 and grid[i + 1][j] == 1:
                    contour -= 1
                if j != m - 1 and grid[i][j + 1] == 1:
                    contour -= 1
                if j != 0 and grid[i][j - 1] == 1:
                    contour -= 1
                if i != 0 and grid[i - 1][j] == 1:
                    contour -= 1
                perimeter += contour
    return perimeter
