#!/usr/bin/python3
""" The main code."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list of lists where
    each sublist represents the keys in a box.

    Returns:
    True if all unlocked, False otherwise.
    """
    box_set = set(boxes[0])

    i = 0
    while i < len(boxes[0]):
        n = boxes[0][i]
        if n < len(boxes):
            box_set.update(boxes[n])
        i += 1

    j = 1
    while j < len(boxes):
        if j in box_set:
            box_set.update(boxes[j])
        else:
            return False
        j += 1

    return True
