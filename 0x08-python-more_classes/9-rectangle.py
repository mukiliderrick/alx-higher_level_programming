#!/usr/bin/python3
class Rectangle:
    """
    class that defines the rectangle
    
    number_of_instances (int): attribute that keeps track of instances
    print_symbol (any type): attribute that stores symbol
    """
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """initializes a rectangle instance
        args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        
    @property
    def width(self):
        """Retrives the width of the rectangle."""
        return self._width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
        
    @property
    def height(self):
        """retrives height of the rectangle"""
        return self._height
    
    @height.setter
    def height(self, value):
        """sets the height of the rectange"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    
    def area(self):
        """calculates the area of the rectangle
        
        Returns :
        int: Area of the rectangle
        """
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle
        
            Returns:
            int: Perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return(self.width + self.height) * 2
    
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """_summary_

        Args:
            rect_1 (_type_):  must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
            rect_2 (_type_): must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle

        Raises:
            TypeError: _description_
            TypeError: _description_

        Returns:
            rect_1 if both have the same area valuetype_: _description_
        """
        if  not isinstance (rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if  not isinstance (rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_2
    @classmethod
    def square(cls, size=0):
        """ that returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
    
    def __del__(self):
        """Deletes rectangle instance and a prints a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
