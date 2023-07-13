#!/usr/bin/python3

"""
This module contains a function for generating Pascal's
Triangle up to a given number of rows.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A 2-dimensional list representing Pascal's Triangle
        up to the specified number of rows.
              Each inner list represents a row in the triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
