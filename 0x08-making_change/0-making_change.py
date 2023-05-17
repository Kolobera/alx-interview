#!/usr/bin/python3
"""Making change module"""


def makeChange(coins: list, total: int):
    """Finds minimal number of coins to add to total"""
    if total <= 0:
        return 0
    coins.sort()
    rest = total
    count = 0
    while rest > 0:
        if coins == []:
            return -1
        if coins[-1] > rest:
            coins.remove(coins[-1])
        else:
            rest -= coins[-1]
            count+=1
    return count
