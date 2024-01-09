#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list of lists where
    each sublist represents the keys in a box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    # Initialize a set to keep track of the boxes that have been unlocked
    unlocked = {0}

    # While there are still unlocked boxes
    while len(unlocked) != len(boxes):
        # Copy the current state of unlocked boxes
        old_unlocked = unlocked.copy()

        # Try to unlock new boxes
        for box in range(len(boxes)):
            if box in unlocked:
                for key in boxes[box]:
                    unlocked.add(key)

        # If no new boxes were unlocked, return False
        if old_unlocked == unlocked:
            return False

    # If all boxes are unlocked, return True
    return True
