from collections import deque

class Dequecl:
    def __init__(self):
        self.data = deque()

    def empty(self):
        return len(self.data) == 0
    
    def insert_item(self, x):
        self.data.append(x)
    
    def read(self):
        if self.empty():
            return None
        return self.data[0]
    
    def remove_item(self):
        if self.empty():
            return None
        return self.data.popleft()
    
    def size(self):
        return len(self.data)

    def items(self):
        if self.empty():
            return None
        return self.data 


datadeque = Dequecl()

datadeque.insert_item(1)
datadeque.insert_item(2)
datadeque.insert_item(3)
print(f'Total items in queue : {datadeque.items()}')

print(f'Reading the item from queue : {datadeque.read()}')

datadeque.remove_item()

print(f'Reading after removing item from queue : {datadeque.read()}')