#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing the Pascal's triangle of n.
    '''
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    result = [[1], [1, 1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i-1][j-1] + result[i-1][j])
        row.append(1)
        result.append(row)
    return result

