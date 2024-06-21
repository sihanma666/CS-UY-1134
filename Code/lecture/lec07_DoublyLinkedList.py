class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data;
            self.next = None;
            self.prev = None;
        def disconnect(self):
            self.data = None;
            self.next = None;
            self.prev = None;
    def __init__(self):
        self.head = DoublyLinkedList.Node(); #dummy node
        self.tail = DoublyLinkedList.Node(); #dummy node
        self.head.next = self.tail;
        self.tail.prev = self.head;
        self.size = 0;

    def __len__(self):
        return self.size;
    def is_empty(self):
        return len(self) == 0;
    def add_after(self, node, data):
        prev_node = node;
        next_node = node.next;
        new_node = DoublyLinkedList.Node(data);
        new_node.prev = prev_node;
        new_node.next = next_node;
        prev_node.next = new_node;
        next_node.prev = new_node;
        self.size+=1;
        return new_node;
    def add_first(self, data):
        return self.add_after(self.head,data);
    def add_last(self, data):
        return self.add_after(self.tail.prev,data);
    def add_before(self, node, data):
        return self.add_after(node.prev,data);
    def delete_node(self, node):
        prev_node = node.prev;
        next_node = node.next;
        prev_node.next = next_node;
        next_node.prev = prev_node;
        data = node.data;
        node.disconnect();
        self.size-=1;
        return data;
    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty");
        return self.delete_node(self.head.next);
    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty");
        return self.delete_node(self.tail.prev);
    def __iter__(self):
        cursor = self.head.next;
        while (cursor is not self.tail):
            yield cursor.data;
            cursor = cursor.next;
    def __repr__(self):
        return "["+ "<-->".join([str(item) for item in self])+"]";
    def clear(self):
        while not self.is_empty():
            self.delete_first();
    









        
