#! /usr/bin/env python3

from termcolor import colored

def stringindexmatch(inputstring, indextofind) -> int:
    print(colored(f"Values of inputstring : {inputstring}", 'yellow'))

    if len(inputstring) == 0:
        return " "

    if inputstring[0] == indextofind:
        return inputstring[0]

    if (value:=stringindexmatch(inputstring[1:], indextofind)):
        return value 
    
x = "abcdefghijk"
t = 'g'
a = stringindexmatch(x,t) 
if a == " ":
    print(colored(f"value is not found", 'red'))
else:
    print(colored(f"Found matching character : {t!r} which is at index : {x.index(a)}", 'green'))

