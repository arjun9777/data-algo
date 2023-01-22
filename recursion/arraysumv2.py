#! /usr/bin/env python3

def arraysum(listA: list, index=0)-> int:
    if len(listA) == 1:
        return listA[0]
    
    print(f"Calling for {index + 1}")
    return listA[0] + arraysum(listA[1:len(listA)], index + 1)

a = [56,89,48,2,59,78,45,38]
x = arraysum(a)
print(f"Array sum is : {x}")
