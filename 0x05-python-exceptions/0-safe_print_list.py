#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # try:
    #     for i in range(x):
    #         print(my_list[i], end="")
    #     print()
    #     return i + 1
    # except IndexError:
    #     print()
    #     return i
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            break
    print()
    return i + 1
