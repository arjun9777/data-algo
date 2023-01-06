#! /usr/bin/env python3
#This program finds first duplicate and returns it

def findduplicate(listA: list) -> str:
    duplicate = {}
    for key, value in enumerate(listA):
        print(f"For loop key : {key} and value : {value}")    
        try:
            if duplicate[value]:
                return value
        except:
            duplicate[value] = True

a = ['a','b','c','d','c','e','f']

x = findduplicate(a)
print(f"Duplicate character is : {x}")


