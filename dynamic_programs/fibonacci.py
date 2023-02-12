#! /usr/bin/env python3
from termcolor import colored

def fibonacci(n:int, memo: dict)->int:
    #print(colored(f"Function call for {n} and dictionary {memo}", "yellow"))
    if n == 0 or n == 1:
        return n

    if not memo.get(n):
        print(colored(f"Executing IF statement for value : {n}", "yellow"))
        memo[n] = fibonacci(n-2, memo) + fibonacci(n-1, memo)
        print(colored(f"Value for dictionary {memo}", "blue"))

    return memo[n]


a = 6
x = fibonacci(a, {})
print(colored(f"{x}", "green"))

