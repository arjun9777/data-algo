#! /usr/bin/env python3

def ispalindrome(listA: list) -> bool:
    leftIndex = 0
    rightIndex = len(listA) - 1

    while (leftIndex < len(listA)/2):
        if listA[leftIndex] != listA[rightIndex]:
            return False
    
        leftIndex +=1
        rightIndex -=1
    return True

a = ['r','a','c','e','c','a','r']
b = ['a', 'p', 'p','l','e']
x = ispalindrome(b)

print(f"Is it palindrome : {x}")

