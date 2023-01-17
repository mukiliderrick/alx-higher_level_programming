#!/usr/bin/python3
"""module for writing a file"""


def write_file(filename="", text=""):
    """function that write a text file"""
    with open(filename, "w", encoding='utf-8') as file:
        write_txt = file.write(text)
    return (write_txt)