#! /usr/bin/env python3
from collections import deque

def lint(text: str) -> str:
    mystack = deque()
    for key, value in enumerate(text):
        if (timo := openingbrace(value)):
            #print(f"It is opening brace {timo}")
            mystack.append(timo)
        elif (jimo := closingbrace(value)):
            #print(f"---------------------------It is closing brace : {jimo}")
            if mystack:
                popped_opening_brace =  mystack.pop()
                if ( y:= is_match_brace(jimo) == popped_opening_brace): #check condition and assign values to y for testing
                    pass
                else:
                    return f"there is a syntax error"
            else:
                return f"{jimo} corresponding opening brace missing"
    try:
        if (opening_brace := mystack.pop()):
            return f"{opening_brace!r} does not have closing brace"
    except:
        pass
        
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



#b = "( var x = { y: [1, 2, 3] } )"

b = "var x = { y: [1, 2, 3] })"
x = lint(b)
print(f"Let's check result : {x!r}")
