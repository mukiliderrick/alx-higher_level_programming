#!/usr/bin/bash
""" module that contains class square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """initialize instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str special method for square"""
        str_square ="[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)
        
        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value    

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self,list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key , value)

    def to_dictionary(self):
        """returns dictionary with attributes"""
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}
        
        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)
        
        return dict_res