#!/usr/bin/python3
'''prints all the names defined by the compiled module'''

import hidden_4

my_list = dir(hidden_4)

for i in my_list:
    if i[0] != '_':
        print(i)
