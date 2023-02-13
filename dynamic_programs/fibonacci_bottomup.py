#! /usr/bin/env python3
from termcolor import colored

def fibon(n:int) -> int:
    if n == 0:
        return 0
    
    a = 0 
    b = 1

    for i in range(1, n):
        print(colored(f"Working for index {i}", "yellow"))
        temp = a
        a = b 
        b = temp + a
        print(colored(f"---------------Value calculated : {b}", "blue"))
    
    return b

a = 10
x = fibon(a)
print(colored(f"Fibonacci value in sequence : {x}", "green"))