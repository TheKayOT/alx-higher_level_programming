#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """Defines private instance attribute"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates the class"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 and self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle whose width and height are equal"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Prints the rectangle"""
        if self.width == 0 and self.height == 0:
            return ""
        new = []
        for i in range(self.height):
            for j in range(self.width):
                new.append(str(self.print_symbol))
            if i != self.height - 1:
                new.append("\n")
        return "".join(new)

    def __repr__(self):
        """Returns the rectangle stringly represented"""
        new = "Rectangle(" + str(self.width)
        new += ", " + str(self.height) + ")"
        return new

    def __del__(self):
        """Detects a rectangle being deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
