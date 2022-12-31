#! /usr/bin/env python3

def twoNumberProducts(listA: list) -> list:
    products = []
    for i in range(len(listA) - 1): #Do not need to iterate for the last element 
        print(f"Outer loop key : {i} and value : {listA[i]}")
        for j in range(i+1, len(listA)):
            print(f"------------------- Inner loop key : {j} and value : {listA[j]}")
            products.append(listA[i] * listA[j])

    return products


a  = [1,2,3,4,5]
x = twoNumberProducts(a)
print(f" Products of every combination of two numbers : \n {x}")
