#!/usr/bin/python3
"""modules for the class Base"""
import json
import csv
import os.path


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            