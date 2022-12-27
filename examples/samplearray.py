#! /usr/bin/env python3

def samplearray(listA: list) -> list:
    first = listA[0]
    meddle = listA[int(len(listA)/2)]
    last = listA[-1]

    return [f"First element : {first}", f"Middle element : {meddle}", f"Last element : {last}"]

a = [1,2,3,4,5,6,7,8,9,10]

x = samplearray(a)
print(x)

#Note : O(1) complexity