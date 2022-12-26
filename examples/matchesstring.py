#! /usr/bin/env python3

def containsX(listA):
    for key, value in enumerate(listA):
        print(f"For loop key : {key} and value : {value}")
        if value.lower() == 'x':
            return True
    return False

a = ['a','b', 'X','Y','u', 'g']

x = containsX(a)
print(x)

