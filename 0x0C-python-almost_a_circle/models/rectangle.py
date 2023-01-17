#!/usr/bin/python3
"""defines a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0,y=0,id=None):
       """Initialise a rectangle.
       Args:
            width of the rectangle.
            height of the rectangle.
            x: the x coordinate of the new rectangle.
            y: The y coordinate of the rectangle.
            id: Identity of the rectangle.
       """
       self.width = width
       self.height = height
       self.x = x
       self.y = y
       super().__init__(id)

    @property
    def width(self):
        """set/get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """sets the x coordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets the y cordinates"""
        return self.__y

    @y.setter
    def y(self,value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """str special method"""
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    # def update(self, *args, **kwargs):
    #     """update method"""
    #     if args is not None and len(args) is not 0:
    #         list_atr = ['id', 'width', 'height', 'x', 'y']
    #         for i in range(len(args)):
    #             setattr(self, list_atr[i], args[i])
    #     else:
    #         for key, value in kwargs.items():
    #             setattr(self, key, value)
    
    
        
