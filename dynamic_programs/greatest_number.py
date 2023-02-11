#! /usr/bin/env python3

def maxnumber(listA:list) -> int:
    print(f"Recursion")
    if len(listA) == 1:
        return listA[0]

    if listA[0] > maxnumber(listA[1:]):
        return listA[0]
    else:
        return maxnumber(listA[1:])


a = [1,2,3,4]

x = maxnumber(a)
print(f"{x}")
