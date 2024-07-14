from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(curr1, curr2):
        if (curr1.data is None and curr2.data is None):
            return DoublyLinkedList()
        elif (curr1.data is None):
            merge = merge_sublists(curr1, curr2.prev)
            merge.add_last(curr2.data)
        elif (curr2.data is None):
            merge = merge_sublists(curr1.prev, curr2)
            merge.add_last(curr1.data)
        else:
            if (curr1.data > curr2.data):
                merge = merge_sublists(curr1.prev, curr2)
                merge.add_last(curr1.data)
            else:
                merge = merge_sublists(curr1, curr2.prev)
                merge.add_last(curr2.data)
        
        return merge
    result = merge_sublists(srt_lnk_lst1.trailer.prev, srt_lnk_lst2.trailer.prev)
    return result
