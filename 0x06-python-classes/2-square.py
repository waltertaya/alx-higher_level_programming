#!/usr/bin/python3

'''Defines a class Square'''


class Square:
    '''class Square that defines a square by: (based on 1-square.py)'''
    
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
