#! /usr/bin/env python3
from collections import deque

def lint(text: str):
    mystack = deque()
    for key, value in enumerate(text):
        if (timo := openingbrace(value)):
            #print(f"It is opening brace {timo}")
            mystack.append(timo)
        elif (jimo := closingbrace(value)):
            #print(f"---------------------------It is closing brace : {jimo}")
            popped_opening_brace =  mystack.pop()
            if popped_opening_brace == None:
                return f"Does not have openning braces"
            elif ( y:= is_match_brace(jimo) == popped_opening_brace): #check condition and assing values to y for testing
                pass
            else:
                return f"there is a syntax error"
    return "You do not have syntax error"

def is_match_brace(popped):
    matching_close = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    if matching_close[popped]:
        return matching_close[popped]

def openingbrace(j: str):
    if j in ["(","[", "{"]:
        return j

def closingbrace(c: str):
    if c in [")", "]","}"]:
        return c



a = "( var x = { y: [1, 2, 3] } )"

x = lint(a)
print(f"Let's check result : {x!r}")
