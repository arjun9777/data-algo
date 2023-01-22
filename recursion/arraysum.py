#! /usr/bin/env python3

def arraysum(listA: list, index = 0, sum = 0) -> int:
    if index < len(listA):
        print(f"Processing index : {index} and value : {listA[index]}")
        sum = sum + listA[index]
        print (f"---------------------sum is : {sum}")
        return arraysum(listA, index + 1, sum)
    return sum

a =  [56,89,48,2,59]

x = arraysum(a)
print(f"Sum of array : {a} is : {x}")


