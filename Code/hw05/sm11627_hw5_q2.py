from DoublyLinkedList import DoublyLinkedList
class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()

        for i in num_str:
            self.data.add_last(int(i))

        curr = self.data.header.next
        breakout = False

        while (not breakout and curr is not None):
            if (curr.data == 0):
                currpoint = curr.next
                self.data.delete_node(curr)
                curr = currpoint
            else:
                breakout = True
        
        if (len(self.data) == 0):
            self.data.add_first(0)
    
    def __add__(self, other):
        temp = 0
        curr1 = self.data.trailer.prev
        curr2 = other.data.trailer.prev
        
        num = ""

        for i in range(max(len(self.data), len(other.data))):
            data1 = 0
            data2 = 0
            if (curr1.data is not None):
                data1 = curr1.data
            if (curr2.data is not None):
                data2 = curr2.data
            
            total = data1+data2+temp
            digit = total%10
            temp = total//10

            if (curr1.prev is not None): 
                curr1 = curr1.prev
            if (curr2.prev is not None):
                curr2 = curr2.prev

            num = str(digit) + num
        if (temp > 0):
            num = str(temp) + num
        
        return Integer(num)
    
    def __repr__(self):
        return "".join(str(i) for i in self.data)
    