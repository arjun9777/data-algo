#! /usr/bin/env python3


def addupto10(listA):
    for key, value in enumerate(listA):
        print(f"Outer for loop key : {key} and value : {value}")
        for key2, value2 in enumerate(listA):
            print(f"************* Inner for loop key : {key2} and value : {value2}")
            if (key != key2 and value + value2 == 10):
                return True #This works as a break statement. If condition matches, then return true and breaks out of inner for loop
    return False

a = [2,3,4,5,8]

x= addupto10(a)
print(x)

