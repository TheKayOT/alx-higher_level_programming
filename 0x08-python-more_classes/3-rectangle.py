#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize values
        Args:
            width = width of rectangle
            height = height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retuns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a rectangle
        Args:
        width
        height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of a rectangle
        Args:
            width
            height
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """print # in form of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rec_gle = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_gle += '#'
            rec_gle += '\n'
        return rec_gle[:-1]
