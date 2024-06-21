#1.
from ArrayQueue import *

def stack_sum(s):
    sum = 0
    if (s.is_empty() == True):
        return
    else:
        sum += s.pop()
        stack_sum(s)

    return sum

#2
class MeanStack:
    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):