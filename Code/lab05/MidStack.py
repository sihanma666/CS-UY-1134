from DoublyLinkedList import DoublyLinkedList

class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.midNode = self.data.header
        self.midPos = 0
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data)==0
    
    def push(self, e):
        self.data.add_last(e)
        
        newMid = (len(self.data)+1)//2
        while self.midNode < newMid:
            self.midNode = self.midNode.next
            self.midPos += 1
    