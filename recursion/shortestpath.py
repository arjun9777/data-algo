#! /usr/bin/env python3
from termcolor import colored

def unique_paths(rows, columns):
    print(colored(f"number of rows : {rows} and columns : {columns}", 'yellow'))
    if rows ==1 or columns ==1:
        return 1

    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)



a = 3
b = 7

x = unique_paths(a,b)
print(x)