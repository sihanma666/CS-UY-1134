from lec07_DoublyLinkedList import DoublyLinkedList


class ListQueue:
    def __init__(self):
        self.data = DoublyLinkedList();
    def __len__(self):
        return len(self.data);
    def is_empty(self):
        return (len(self.data)==0);
    def enqueue(self, item):
        self.data.add_last(item);
    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data.delete_first();
    def front(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data.head.next.data;
    def clear(self):
        self.data.clear();
