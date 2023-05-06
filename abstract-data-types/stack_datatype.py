#! /usr/bin/env python3
from collections import deque
from termcolor import colored


class Stack:
    def __init__(self):
        self.data = deque()
    
    def empty(self) -> int:
        return len(self.data) == 0 
    
    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            return None
        return self.data.pop()
    
    def size(self):
        return len(self.data)

    def peek(self):
        if self.empty():
            return None
        return self.data[-1]
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(colored(f"{stack.peek()}", "green"))

stack.pop()

print(colored(f"{stack.peek()}", "green"))
print(colored(f"Total size of stack : {stack.size()}", "yellow"))