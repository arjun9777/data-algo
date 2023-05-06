#! /usr/bin/env python3
from collections import deque
from termcolor import colored


class Stack:
    def __init__(self):
        self.items = deque()
    
    def empty(self) -> int:
        return len(self.items) == 0 
    
    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.empty():
            return None
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def peek(self):
        if self.empty():
            return None
        return self.items[-1]
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(colored(f"{stack.peek()}", "green"))

stack.pop()

print(colored(f"{stack.peek()}", "green"))
print(colored(f"Total size of stack : {stack.size()}", "yellow"))