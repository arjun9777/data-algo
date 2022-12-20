#! /usr/bin/env python3

def greatestNumber(list_a):
    greatestNumbersofar = list_a[0]
    
    for i in list_a:
        if i > greatestNumbersofar:
            greatestNumbersofar = i
    
    return greatestNumbersofar

print(greatestNumber([5,6,15,8,16,1,512]))