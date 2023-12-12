#!/usr/bin/python3
''''program that imports the function def add(a, b):'''


def add(a, b):
    a = 1
    b = 2
    from add_0 import add
    sum = add(a, b)

    print("{} + {} = {}".format(a, b, sum))


if __name__ == "__main__":
    add(1, 2)
