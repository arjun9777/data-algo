#! /usr/bin/env python3


def issubset(array1: list, array2: list) -> bool:
    if len(array1) > len(array2):
        largerarray = array1
        smallerarray = array2
    else:
        largerarray = array2
        smallerarray = array1


    hashtableA = {}
    for key, value in enumerate(largerarray):
        hashtableA[value] = True
    print(f"Dictionary : {hashtableA}")
    for key1, item in enumerate(smallerarray):
        try:
            if hashtableA[item] == False:
                return False
        except KeyError:
            return False
    
    return True

a = ['a', 'b', 'c', 'd', 'e', 'f','h']
b = ['b','d','f','h']

x = issubset(a, b)
print(f"Is it subset? : {x}")