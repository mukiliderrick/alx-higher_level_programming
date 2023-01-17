#!/usr/bin/python3
"""module for reading a file"""


def read_file(filename=""):
    """function that reads a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end='')
