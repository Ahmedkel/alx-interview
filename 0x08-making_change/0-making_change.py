#!/usr/bin/python3
"""
Module to make change for
a given amount of money .
"""


def makeChange(coins, total):
    """
    Given a list of coins
    and a total amount of money
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
