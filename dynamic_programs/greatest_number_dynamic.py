#! /usr/bin/env python3
from termcolor import colored
 
y = 1
def max(listA):
    if len(listA) == 1:
        return listA[0]
    
    max_of_remainder = max(listA[1:])

    if listA[0] > max_of_remainder:
        print(colored(f"IF statement is returning : {listA[0]}", 'red'))
        return listA[0]
    else:
        print(colored(f"-------------------Else statement returning : {max_of_remainder}", 'yellow'))
        return max_of_remainder

a = [10,2,3,4,7,1,2,4,9]
x = max(a)

print(colored(f"Maximum value : {x}", 'green'))


