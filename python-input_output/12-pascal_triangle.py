#!/usr/bin/python3
"""module that representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    function that represents the Pascal’s triangle of n

    Args:
        n: number of iteration of the triangle

    Returns: (list)
        empty list if n <= 0
        Pascals triangle of n
    """

    triangle = []

    for i in range(n):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(triangle[i-1][j-1]+triangle[i-1][j])
        triangle.append(tmp)
    return triangle
