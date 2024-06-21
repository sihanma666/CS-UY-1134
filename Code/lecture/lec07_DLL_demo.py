from lec07_DoublyLinkedList import DoublyLinkedList
import random
from lec07_ListQueue import ListQueue

def max_in_linked_list(lst):
    if (len(lst)==0):
        raise Exception("List is empty");
    if (len(lst) ==1):
        return lst.head.next.data;
    else:
        #first_data = lst.head.next.data;
        first_data = lst.delete_first();
        rest_max = max_in_linked_list(lst);
        lst.add_first(first_data);
        return max(first_data, rest_max);

def main():
##    dll = DoublyLinkedList();
##    for i in range(10):
##        dll.add_first(random.randint(0,100));
##    print(dll);
##    print(max_in_linked_list(dll));
##    print(dll);

    q = ListQueue();
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    while (not q.is_empty()):
        print(q.dequeue());

        
if __name__=='__main__':
    main();
    
