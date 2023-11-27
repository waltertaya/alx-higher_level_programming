#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """__init__ constructor for Rectangle class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Returns: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): width of rectangle

        Returns: None

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): height of rectangle

        Returns: None

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >=0")

        self.__height = value
