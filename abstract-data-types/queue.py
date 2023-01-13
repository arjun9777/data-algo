#! /usr/bin/env python3
from collections import deque


def printerqueue(filearray: list) -> str:
    myqueue = deque()

    for i in filearray:
        myqueue.append(i)
    print(f"Queue values : {myqueue}") 
    
    try:
        while (x:=myqueue.popleft()):
            print(x)
    except:
        pass
    return "Please check printer to collect your pages"


a = ["hello", "left", "to", "right"]
b = ["First Document" , "second Document", "Third Document"]

y = printerqueue(b)

print(f"Printing : {y}")
