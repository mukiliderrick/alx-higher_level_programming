#!/usr/bin/python3
""" 
    the programme prints a squeare with # the size should be an int
"""
def print_square(size):
    if not isinstance (size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print('#' * size)