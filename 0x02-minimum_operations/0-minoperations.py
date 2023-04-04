#!/usr/bin/python3
"""Minimum Operations
"""


def minOperations(n):
    """Minimum Operations
    """
    control_var = 1
    paste_control = [1]
    count = 0
    if n <= 1:
        return 0
    while (control_var != n):
        
        if n % control_var != 0:
            control_var += paste_control[-1]
            count += 1
        else:
            paste_control.append(control_var)
            control_var += paste_control[-1]
            count += 2
    return count
