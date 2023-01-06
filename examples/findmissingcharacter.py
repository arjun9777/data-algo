#! /usr/bin/env python3

def findmissingcharacter(stringvalue: str) -> str:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dtringdict = {}
    for value in stringvalue:
        if value == " ":
            pass
        else:
            dtringdict[value] = True
    
    #print(dtringdict)
    
    for key, items in enumerate(alphabet):
        print(f"Second for loop key : {key} and value : {items}")
        try:
            if dtringdict[items]:
                pass
        except KeyError:
            return items

a = "the quick brown box jumps over a lazy dog"

x = findmissingcharacter(a)
print(f"Missing character in a string is : {x}")