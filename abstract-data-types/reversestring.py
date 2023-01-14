#! /usr/bin/evn python3
from collections import deque

def reversestring(anystring:str) -> str:
    mydeque = deque()

    for key, value in enumerate(anystring):
        print(f"For loop key : {key} and value : {value}")
        mydeque.append(value)

    inverstring = str()
    try:
        while (popvalue := mydeque.pop()):
            print(f"--------------- while loop value popped from the stack: {popvalue}")
            inverstring += popvalue
    except:
        pass
    return inverstring

a = "abcde"
x = reversestring(a)
print(f"String in reverse order : {x!r}")
