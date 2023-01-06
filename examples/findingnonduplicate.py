#! /usr/bin/env python3

def findingnonduplicate(stringA : str) -> str:
    dictvalue = {}
    for key, value in enumerate(stringA):
        print(f"First for loop key : {key} and value : {value}")
        try:
            if dictvalue[value]:
                dictvalue[value] += 1
        except KeyError:
            dictvalue[value] = 1
    
    for key1, item in enumerate(dictvalue):
        print(f"------------Second for loop key : {key1} and value : {item}")
        if dictvalue[item] == 1:
            return item
 
a  = "minimum"

x = findingnonduplicate(a)
print(x)