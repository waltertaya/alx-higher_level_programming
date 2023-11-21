#!/usr/bin/python3

'''Defines a class Square'''


class Square:
    '''class Square that defines a square by: (based on 1-square.py)'''
    
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            try:
                if size < 0:
                    raise ValueError("size must be >= 0")
            except TypeError:
                raise TypeError("size must be an integer")
