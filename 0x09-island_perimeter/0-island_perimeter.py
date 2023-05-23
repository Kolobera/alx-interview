#!/usr/bin/python3
"""Island Parameter Module"""
from collections import Counter


def island_perimeter(grid):
    """Calculate perimeter of island"""
    m = len(grid[0])
    n = len(grid)
    perimeter = 0
    line_tracker = []
    column_tracker = []
    for i in range(1, n-1):
        for j in range (1, m-1):
            if grid[i][j] == 1:
                perimeter += 1
                line_tracker.append(i)
                column_tracker.append(j)
    if perimeter == 0:
        return 0
    line_tracker = dict(Counter(line_tracker))
    column_tracker = dict(Counter(column_tracker))
    adder = len([i for i in line_tracker.values() if i  > 1]) + len([i for i in column_tracker.values() if i  > 1]) -3
    return 2 * (perimeter + 1 - adder)
