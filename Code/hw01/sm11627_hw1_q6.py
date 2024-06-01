def split_parity(lst):
    for i in range(len(lst)):
        if(lst[i] % 2 != 0):
            lst.insert(0,lst.pop(i))
    return lst
        
