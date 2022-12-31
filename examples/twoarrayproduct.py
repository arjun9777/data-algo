#! /usr/bin/env python3

def twoArrayProducts(listA : list, listB: list) -> list:
    products = []
    for key, value in enumerate(listA):
        print(f"Outer loop key : {key} and value : {value}")
        for key1, value1 in enumerate(listB):
            print(f"------------------ Inner loop key : {key1} and value : {value1}")
            products.append(value * value1)
    return products

a = [1, 2, 3]
b = [10,100,1000]

x = twoArrayProducts(a, b)
print(f"Product of first array each elements with second array each elements : \n {x}")