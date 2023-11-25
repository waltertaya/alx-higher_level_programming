#!/usr/bin/python3
def add_integer(a, b=98):
    '''Add two values a and b which must be integers or floats'''
    '''Return integer value'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        return int(a) + int(b)
    elif isinstance(a, float) and isinstance(b, int):
        return int(a) + b
    elif isinstance(a, int) and isinstance(b, float):
        return a + int(b)
        