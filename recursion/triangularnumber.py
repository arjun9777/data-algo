#! /usr/bin/env python3
from termcolor import colored

def triangular(n:int) -> int:
    #Accept int number, then calculate number in Triangular pattern
    print(colored(f"Input number to the triangular function : {n}", 'yellow'))
    if n == 0:
        return 0

    if n == 1:
        return 1
    else:
        return n + triangular(n - 1)

if (__name__ == "__main__"):
    a = 8
    x = triangular(int(a))
    print(colored(f"Input number {a}. Output for Triangular pattern is : {x}", 'green'))

    
