#!/usr/bin/python3

if __name__ == "__main__":
    """program that imports all functions from the file calculator_1.py"""
    from calculator_1 import add, sub, mul, div
    import sys
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(int(sys.argv[1]), int(sys.argv[3]))))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub(int(sys.argv[1]), int(sys.argv[3]))))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul(int(sys.argv[1]), int(sys.argv[3]))))
        else:
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div(int(sys.argv[1]), int(sys.argv[3]))))
