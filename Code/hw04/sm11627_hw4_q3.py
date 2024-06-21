from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.topS = ArrayDeque()
        self.bottomS = ArrayStack()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.topS)+len(self.bottomS)

    def push(self, e):
        self.topS.enqueue_first(e)

        midlen = len(self)-((len(self)+1)//2)

        while (len(self.topS) != midlen):
            if (len(self.topS) > midlen):
                self.bottomS.push(self.topS.dequeue_last())
            else:
                self.topS.enqueue_last(self.bottomS.pop())

    def top(self):
        if (self.is_empty()): 
            raise Exception("MidStack is empty")
        return self.topS.first()

    def pop(self):
        if (self.is_empty()): 
            raise Exception("MidStack is empty")
        if (self.topS.is_empty()):
            self.topS.enqueue_last(self.bottomS.pop())

        popped = self.topS.dequeue_first()
        
        midlen = len(self)-((len(self)+1)//2)

        while (len(self.topS) != midlen):
            if (len(self.topS) > midlen):
                self.bottomS.push(self.topS.dequeue_last())
            else:
                self.topS.enqueue_last(self.bottomS.pop())
                
        return popped

    def mid_push(self, e):
        self.bottomS.push(e)
        
        midlen = len(self)-((len(self)+1)//2)

        while (len(self.topS) != midlen):
            if (len(self.topS) > midlen):
                self.bottomS.push(self.topS.dequeue_last())
            else:
                self.topS.enqueue_last(self.bottomS.pop())
      
