class Stack :
    def __init__(self, items):
        self.items = items
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("empty stack")
    def display(self):
        if not self.is_empty():
            return self.items
        raise IndexError("empty stack")
