#!/usr/bin/python3
"""Validate UTF-8"""


def validUTF8(data):
    """Check if data is valid UTF-8"""
    n = len(data)
    i = 0
    while i < n:
        # Check the number of bytes in the current character
        num_bytes = 0
        if (data[i] & 0b10000000) == 0:
            num_bytes = 1
        elif (data[i] & 0b11100000) == 0b11000000:
            num_bytes = 2
        elif (data[i] & 0b11110000) == 0b11100000:
            num_bytes = 3
        elif (data[i] & 0b11111000) == 0b11110000:
            num_bytes = 4
        else:
            return False

        # Check if there are enough bytes left in the data
        if i + num_bytes > n:
            return False

        # Check if all following bytes start with '10'
        for j in range(1, num_bytes):
            if (data[i+j] & 0b11000000) != 0b10000000:
                return False

        # Move to the next character
        i += num_bytes

    return True
