#! /usr/bin/env python3

a = [1,2,3,4, [5,6,7], [8], 9,10]

def print_values(b):
    for key,value in enumerate(b):
        if (type(value) is list):
            print_values(value)
        else:
            print(value)

print_values(a)


