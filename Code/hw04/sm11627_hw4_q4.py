
from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.forwardS = ArrayStack()
        self.backwardS= ArrayStack()

    def __len__(self):
        return len(self.forwardS)+len(self.backwardS)

    def is_empty(self):
        return (self.forwardS.is_empty() and self.backwardS.is_empty())

    def enqueue(self, val):
        self.forwardS.push(val)
    
    def dequeue(self):
        if (self.backwardS.is_empty()):
            while (self.forwardS.is_empty() != True):
                self.backwardS.push(self.forwardS.pop())
        return self.backwardS.pop()

    def front(self):
        if (self.backwardS.is_empty()):
            while (self.forwardS.is_empty() != True):
                self.backwardS.push(self.forwardS.pop())
        return self.backwardS.top()

