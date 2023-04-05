#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    # Validate input
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Add a and b and return the result
    return a + b
