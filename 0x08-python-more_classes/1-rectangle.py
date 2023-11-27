#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''class rectangle'''
    
    def __init__(self, width=0, height=0):
        '''private instance attribute width and height'''
        
        self.width = width
        self.height = height
        
    @property
    def width(self):
        '''getter for width to retrieve width'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''Setter for width'''
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        '''getter for width to retrieve width'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''Setter for width'''
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
