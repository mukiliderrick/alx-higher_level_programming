#!/usr/bin/python 3
"""
    contains one method that gets the sum of two values.
    Accepts either int ot float
"""
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)