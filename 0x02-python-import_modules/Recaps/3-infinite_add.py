#!/usr/bin/python3
'''prints the result of the addition of all arguments'''
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sum = 0
        for i in sys.argv[1:]:
            sum += int(i)
        print("{}".format(sum))
    else:
        print("0")
