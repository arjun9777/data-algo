#! /usr/bin/env python3
def issubset(array1:list, array2:list):
    if len(array1) > len(array2):
        largerarray = array1
        smallerarray = array2
    else:
        largerarray = array2
        smallerarray = array1
    
    for key, value in enumerate(smallerarray):
        print(f"smaller array key : {key} and value : {value}")
        found = False
        for key1, item in enumerate(largerarray):
            print(f"----------------- Larger array key : {key1} and value : {item} ")
            if value == item:
                found = True
                break
    if found == False:
        return False
    return True

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = ['b','d','f']

x = issubset(a, b)
print(x)

