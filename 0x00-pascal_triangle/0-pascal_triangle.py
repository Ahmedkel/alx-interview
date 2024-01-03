#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The size of the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the remaining rows of the triangle
    for i in range(1, n):
        row = [1]  # Start each row with
        # Compute the elements of the current row based on the previous row
        for j in range(1, i):
            # Each element is the sum of the
            # two elements above it in the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)  # End each row with 1

    return triangle
