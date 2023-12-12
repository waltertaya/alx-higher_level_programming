#!/usr/bin/python3
'''prints the number of and the list of its arguments.'''


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print("{} arguments".format(len(sys.argv) - 1))
        for i in sys.argv[1:]:
            print("{}: {}".format(sys.argv.index(i), i))
    else:
        print("0 arguments.")
