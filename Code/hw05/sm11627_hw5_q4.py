from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    copy = DoublyLinkedList()
    for i in lnk_lst:
        copy.add_last(i)

    return copy

def deep_copy_linked_list(lnk_lst):
    deepCopy = DoublyLinkedList()
    for i in lnk_lst:
        if isinstance(i, int):
            deepCopy.add_last(i)
        else:
            tempCopy = deep_copy_linked_list(i)
            deepCopy.add_last(tempCopy)
    
    return deepCopy