#!/usr/bin/python3
"""import add_0 function from the file add_0.py"""

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    c = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, c))