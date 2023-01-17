#!/usr/bin/python3
"""module that appends string at the end of a file"""


def append_write(filename="",text=""):
    """function that appends a character"""
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
