#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''class rectangle'''
    
    def __init__(self, width=0, height=0):
        '''private instance attribute width and height'''
        self.width = width
        self.height = height
        
    @property
    def height(self):
        '''getter for height to retrieve height'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''Setter for height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        '''getter for width to retrieve width'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''Setter for width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
