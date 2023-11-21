#!/usr/bin/python3


'''class definition of a Square that defines a square by: (based on 2-square.py)'''

class Square:
    '''class definition of a Square that defines a square by: (based on 2-square.py)'''
    def __init__(self, size=0):
        '''Instantiation with optional size'''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

    def area(self):
        '''Public instance method that returns the current square area'''
        return self.__size ** 2
