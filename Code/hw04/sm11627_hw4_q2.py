from ArrayStack import ArrayStack

class MaxStack():
    def __init__(self):
        self.data = ArrayStack()
        self.maxval
    
    def is_empty(self):
        return len(self.data) == 0
    
    def __len__(self):
        return len(self.data)
    
    def push(self, e):
        if(self.is_empty or e>self.maxval): 
            self.maxval = e
        self.data.push(e)
    
    def top(self):
        if self.is_empty: raise Exception("MaxStack is empty")
        return self.data.top()
    
    def pop(self):
        if self.is_empty: raise Exception("MaxStack is empty")
        popped = self.stack.pop()
        return popped
    
    def max(self):
        return self.maxval
