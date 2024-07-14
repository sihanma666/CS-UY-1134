from DoublyLinkedList import DoublyLinkedList
class CompactString:
    def __init__(self, orig_str):
        orig_str = ""
        self.data = DoublyLinkedList()
        for i in orig_str:
            self.data.add_last((i,1))
        if (len(self.data) > 0):
            self.__compress()

    def __add__(self, other):
        val = CompactString()
        for i in self.data:
            val.data.add_last(i)
        for i in other.data:
            val.data.add_last(i)

        curr = val.data.header.next
        while (curr is not None 
               and curr.next is not None 
               and curr.next.data is not None):
            if (curr.data[0] == curr.next.data[0]):
                curr.data = (curr.data[0], curr.data[1] + curr.next.data[1])
                val.data.delete_node(curr.next)
            else:
                curr = curr.next
                
        return val
        
    def __lt__(self, other):
        selfCurr = self.data.header.next
        otherCurr = other.data.header.next

        if(self.data.is_empty() and not other.data.is_empty()):
            return True
        while (selfCurr.data is not None and otherCurr.data is not None):
            char1 = selfCurr.data[0]
            count1 = selfCurr.data[1]
            char2 = otherCurr.data[0]
            count2 = otherCurr.data[1]

            if (char1 != char2 or count1 != count2):
                if (char1 < char2):
                    return True
                elif (char2 > char1):
                    return False
                else:
                    if (selfCurr.next.data is not None):
                        nextChar1 = selfCurr.next.data[0]
                    else:
                        nextChar1 = None
                    
                    if (otherCurr.next.data is not None):
                        nextChar2 = otherCurr.next.data[0]
                    else:
                        nextChar2 = None

                    if (count1 < count2):
                        if (nextChar1 is None):
                            return True
                        elif (nextChar1 < char2):
                            return True
                        else: 
                            return False
                    elif (count2 < count1):
                        if (nextChar2 is None):
                            return False
                        elif (nextChar2 < char1):
                            return False
                        else:
                            return True
            selfCurr = selfCurr.next
            otherCurr = otherCurr.next
        
        return False
                    
    def __le__(self, other):
        if (self <= other):
            return True
        else:
            return False
    def __gt__(self, other):
        if (self <= other):
            return False
        else:
            return True
    def __ge__(self, other):
        if (self < other):
            return False
        else:
            return True
    def __repr__(self):
        str = ''
        for i in self.data:
            str += i[0] * i[1]

        return str