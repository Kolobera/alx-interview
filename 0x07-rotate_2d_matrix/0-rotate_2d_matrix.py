#!/usr/bin/python3
"""Rotate Matrix module"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    n = len(matrix[0])
    copy_m = [[matrix[i][j] for j in range(n)] for i in range (n)]
    for i in range(n):
        for j in range(n):
            matrix[j][n-1-i] = copy_m[i][j]
