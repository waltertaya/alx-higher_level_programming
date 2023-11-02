#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all arguments."""
    from sys import argv

    total = 0

    for i in range(1, len(argv)):
        total += int(argv[i])

    print(total)
