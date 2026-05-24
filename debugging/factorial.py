#!/usr/bin/python3
"""
factorial.py

This script computes the factorial of a given positive integer.
Usage:
    ./factorial.py <number>
"""

import sys


def factorial(n):
    """
    Computes the factorial of a positive integer.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of n.
    """
    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result


# Convert command-line argument to integer
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)
